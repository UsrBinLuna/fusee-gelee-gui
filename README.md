
# Fusée-Gelée GUI
A mod of the [Nintendo Homebrew Server's](https://github.com/nh-server/fusee-interfacee-tk) Fusée-Interfacée with a more modern UI. 

## Differences from NH-Server's fusée-interfacée-tk
- Revamped UI, made with [CTk](https://github.com/TomSchimansky/CustomTkinter)
- Saves last used payload to not have to navigate through your files
- Removed SD-Card mounting

## Disclaimer
* As always, use at your own discretion. I take no reponsibility for any damages caused to your device.
* I'm assuming you understand how the exploit is done and the setup needed, this README is to help you run this specific app.
* Although Fusée is able to exploit any Tegra X1 device, this app is designed to work with Nintendo Switches only.
* The Fusée Launcher script included in this project is slightly modified to be used as a module.

## Running this app
### Requirements
* Have latest [python 3](https://www.python.org/downloads/) and [pyusb](https://github.com/pyusb/pyusb) installed.
* __On Linux__ have libusb1 installed (you probably already have).
* __On Windows__ have libusbK installed. [Get it here](https://sourceforge.net/projects/libusbk/files/libusbK-release/)
* Clone this repo
* Get required modules via `pip install -r requirements.txt`
* Run `app.py`

## Using Fusée-Gelée GUI
The app is very simple, it should be very intuitive to use:

* Click the `Select Payload` button to browse your files and select the desired payload.
* Connect your Switch in RCM mode to the computer. The progress bar will stop and fill up when the device is detected.
* When the `Send Payload` button activates, click it to send the selected payload.


## Credits
- The [Nintendo Homebrew Server](https://github.com/nh-server) / [Fusée-Interfacée-Tk](https://github.com/nh-server/fusee-interfacee-tk)
- [Kate Temkin](https://github.com/ktemkin) / [Fusée Launcher](https://github.com/Cease-and-DeSwitch/fusee-launcher)
- [Rajkosto](https://github.com/rajkosto) / [memloader](https://github.com/rajkosto/memloader), Mounting Tool
- [falquinho](https://github.com/rajkosto) / [Fusée Launcher Interfacée](https://github.com/falquinho/fusee-interfacee-tk), Original Author