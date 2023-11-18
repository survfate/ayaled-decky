# AYALED Decky
Fork of the ayaled plugin from https://github.com/honjow/ayaled (Original by https://github.com/Gawah/ayaled). This plugin enable control of the RGB LED on Ayaneo devices

## Fork updates
- This is primarily intended to work with ChimeraOS.
- Make the default language English.
- Add more supported devices to the list of the base code

## Supported devices
- AYANEO AIR
- AYANEO AIR 1S
- AYANEO AIR Pro
- AYANEO 2
- AYANEO 2S
- AYANEO GEEK
- AYANEO GEEK 1S

## Installation instructions (Manual)

1. Install [decky-loader](https://github.com/SteamDeckHomebrew/decky-loader)
2. Download [Releases](https://github.com/survfate/ayaled-decky/releases) ayaled-decky.tar.gz
3. Run `chmod -R 777 ${HOME}/homebrew/plugins`
4. Extract the plugin content to /home/gamer/homebrew/plugins/
5. Reload decky-loader with `sudo systemctl restart plugin_loader.service`

## Installation instructions (Script)
```
curl -L https://github.com/survfate/ayaled-decky/main/install.sh | sh
```