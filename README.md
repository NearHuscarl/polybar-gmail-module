# Polybar Gmail Module
Custom module for [polybar](https://github.com/jaagr/polybar) that count unread mails from gmail

## Dependency:
* google-api-python-client
* [font awesome](https://github.com/FortAwesome/Font-Awesome)

## Installation
```
cd ~/.config/polybar
git clone https://github.com/NearHuscarl/polybar-gmail-module
mv polybar-gmail-module gmail
~/.config/polybar/gmail/gmail.py
```

## Add to polybar

```
[module/gmail]
type = custom/script
interval = 600

exec = $HOME/.config/polybar/gmail/gmail.py
click-left = xdg-open https://mail.google.com
```
![default color](https://raw.githubusercontent.com/NearHuscarl/polybar-gmail-module/master/screenshot/default.png)

```
[module/gmail]
type = custom/script
interval = 600

exec = $HOME/.config/polybar/gmail/gmail.py --icon-color=#00ff00 --text-color=#ff00ff
click-left = xdg-open https://mail.google.com
```
![custom color](https://raw.githubusercontent.com/NearHuscarl/polybar-gmail-module/master/screenshot/custom.png)

## Parameters
```
Display gmail unread count on polybar

optional arguments:
  -h, --help            show this help message and exit
  -pe [PREFIX_ERROR], --prefix-error [PREFIX_ERROR]
                        prefix when an error occurs
  -p [PREFIX], --prefix [PREFIX]
                        module prefix, preferably an icon
  -ec [ICON_ERROR_COLOR], --icon-error-color [ICON_ERROR_COLOR]
                        foreground color for error icon
  -ic [ICON_COLOR], --icon-color [ICON_COLOR]
                        foreground color for mail icon
  -tc [TEXT_COLOR], --text-color [TEXT_COLOR]
                        foreground color for text
```
