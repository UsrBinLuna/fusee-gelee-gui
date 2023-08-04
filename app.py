import sys
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
import customtkinter as ctk
import fusee_launcher as fusee
import mock_arguments

# ctk colors
ctk.set_appearance_mode("System") # set theme (System, Light, Dark)
ctk.set_default_color_theme("blue") # set default color theme (blue, dark-blue, green)


class App(ctk.CTk):

    def __init__(self, master=None):
        ctk.CTk.__init__(self, master)
        self.title('Fusée Gelée GUI')
        self.iconbitmap('icon.ico')
        self.grid()
        self.geometry("330x200")
        self.build_widgets()

        self.payload_path = ''
        self.device_found = False
        self.lbl_length   = 22
        self.usb_backend  = fusee.HaxBackend.create_appropriate_backend()

        root = self.winfo_toplevel()
        root.update()
        root.resizable(0, 0)

        self.do_update()



    def build_widgets(self):

        self.progress = ctk.CTkProgressBar(self, mode='indeterminate', height=12)
        self.progress.grid(row=0, columnspan=2, sticky=tk.W+tk.E, pady=12, padx=12)
        self.progress.start()

        self.lbl_look = ctk.CTkLabel(self, text="Looking for Device...")
        self.lbl_look.grid(row=1, column=0, columnspan=2, pady=8)

        self.btn_open = ctk.CTkButton(self, text="Select Payload", command=self.btn_open_pressed, corner_radius=12, fg_color=("#d9d9d9", "#454545"), hover_color=("#b5b5b5", "#4f4f4f"))
        self.btn_open.grid(row=2, column=0, padx=8)

        # last-payload
        self.btn_last_payload = ctk.CTkButton(self, text="Load last used payload", command=self.load_last_payload, corner_radius=12, fg_color=("#d9d9d9", "#454545"), hover_color=("#b5b5b5", "#4f4f4f"))
        self.btn_last_payload.grid(row=3, column=0, padx=8, pady=8)

        self.lbl_file = ctk.CTkLabel(self, text="No Payload Selected.    ", justify=tk.LEFT)
        self.lbl_file.grid(row=2, column=1, padx=8)

        self.btn_send = ctk.CTkButton(self, text="Send Payload", command=self.btn_send_pressed, corner_radius=12, fg_color=("#d9d9d9", "#454545"), hover_color=("#b5b5b5", "#4f4f4f"), state="disabled")
        self.btn_send.grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E, pady=8, padx=8)
        


    def do_update(self):
        device = self.usb_backend.find_device(0x0955, 0x7321)
        if device and not self.device_found:
            self.device_found = True
            self.lbl_look.configure(text='Device ready!')
            self.progress.stop()
            self.progress.grid_remove()
            self.progress.configure(mode='determinate')
            #self.progress.step(999)

        elif not device and self.device_found:
            self.device_found = False
            self.progress.grid()
            self.lbl_look.configure(text='Looking for device...')
            self.progress.configure(mode='indeterminate')
            self.progress.start()

        self.validate_form()
        self.after(333, self.do_update)



    def btn_open_pressed(self):
        path = askopenfilename(filetypes=[('Binary', '*.bin')], title='Select Payload')
        if path:
            excess = len(path)-self.lbl_length
            self.payload_path = path
            self.lbl_file.configure(text='..'+path[max(0, excess):], text_color=("#000000", "#d9d9d9"))

            # save payload for later
            with open('last_payload', 'w') as file:
                file.write(path)

            # log payload for debugging
            print(path)

        self.validate_form()
    
    def load_last_payload(self):
        
        if os.path.exists('last_payload'):
            with open('last_payload') as file:
                savepath = file.readlines()
                path = savepath[0]
                
                # log payload path for debugging
                print(path)
                print(savepath)
                excess = len(path)-self.lbl_length
                self.payload_path = path
                self.lbl_file.configure(text='..'+path[max(0, excess):], text_color=("#000000", "#d9d9d9"))
        else:
            self.lbl_file.configure(text='File not found!', text_color=("#FF0000", "#FF7070"))


        




    def btn_send_pressed(self):
        args = mock_arguments.MockArguments()
        args.payload   = self.payload_path
        args.relocator = self.build_relocator_path()
        fusee.do_hax(args)

    def validate_form(self):
        if self.payload_path and self.device_found:
            self.btn_send.configure(state="enabled")
        else:
            self.btn_send.configure(state="disabled")


    def build_mountusb_path(self):
        try:
            path = sys._MEIPASS
        except Exception:
            path = os.path.abspath('.')

        return os.path.join(path, 'memloader.bin')

    def build_relocator_path(self):
        try:
            path = sys._MEIPASS
        except Exception:
            path = os.path.abspath('.')

        return os.path.join(path, 'intermezzo.bin')



my_app = App()
my_app.mainloop()
