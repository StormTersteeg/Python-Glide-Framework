# Python Glide

![Alt text](https://one.dontdalon.com/screenshot.png)<br>
Python Glide is a template/framework/setup used to compile HTML, CSS & Javascript into a native app.
<br>(by using [pywebview](https://pywebview.flowrl.com/) and [pyinstaller](https://www.pyinstaller.org/))<br><br>

### Apps written using Glide
- [Media Pin](https://github.com/StormTersteeg/media-pin)
- [Counter Pin](https://github.com/StormTersteeg/counter-pin)
- [Cam Auto Brightness](https://github.com/StormTersteeg/cam-auto-brightness)
- [NS Disruption Alert](https://github.com/StormTersteeg/NS-Disruption-Alert)
- [PingKit](https://github.com/StormTersteeg/pingkit)
- [Timer](https://github.com/StormTersteeg/timer)
- [Tabbed Notes](https://github.com/StormTersteeg/tabbed-notes)

### Dependencies
- Python 3
- [pywebview](https://pywebview.flowrl.com/)
- [pyinstaller](https://www.pyinstaller.org/)
- Windows

### Features
- Compile any HTML, CSS and Javascript into a native app.
- Connect your HTML UI to the Python backend with Javascript (by editing `resources/wrapper.py`)
<br><br>

### Includes:
| Resource            | Type |  |
|----------------------------|--------|-----------------------------------------------------------------|
| Bootstrap 4.1.1            | CSS/JS | https://getbootstrap.com/docs/4.1/getting-started/introduction/ |
| JQuery 3.5.1               | JS     | https://jquery.com/                                             |
| Daemonite's Material 4.1.1 | CSS    | https://daemonite.github.io/material/                           |
| Material Icons             | Font   | https://fonts.google.com/icons?selected=Material+Icons          |
| Popper 1.14.3              | JS     | https://popper.js.org/                                          |
| Roboto                     | Font   | https://fonts.google.com/specimen/Roboto                        |

<br>
<hr>
<br>

## How to use?
Phase 1 (repeat until app is done)
- Write HTML in `resources/index.html`
- Write CSS in `resources/assets/custom/custom.css`
- Write JS in `resources/assets/custom/custom.js`<br>
(or add more sources of code in `settings.py`)
- Tweak the `settings.py` to your liking
- Build your code into a `.pyw` by running `build.py` <br><br>

Phase 2
- Compile the `.pyw` into a `.exe` by running `compile.cmd`
- Find your `.exe` in `bin/dist/`

<br>

## Advanced
Resources contains `wrapper.pyw`, this is the pywebview preset file that is used to wrap your HTML. You can add custom functions to the Javascript API, see this: https://pywebview.flowrl.com/examples/js_api.html. This wrapper also already contains all the existing events that you can use.<br><br>
DONT remove `#!FLAG-HTML` from the wrapper, as it is used by the builder to identify where to inject the HTML.
