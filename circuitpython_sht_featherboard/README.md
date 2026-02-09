# Notes on the Precision Hygrometer/Thermometer used in this build

![WIP](../img/hygrometer_thermometer/IMG_8027.mov)

Nothing really fancy or special in this, all of it derived from tutorials:

The star of the show, an SHT45:
- https://docs.circuitpython.org/projects/sht4x/en/latest/
Adafruit ESP32-S3 Reverse TFT Feather
- https://learn.adafruit.com/esp32-s3-reverse-tft-feather/overview
DisplayIO:
- https://learn.adafruit.com/circuitpython-display-support-using-displayio/text
Fonts:
- https://learn.adafruit.com/custom-fonts-for-pyportal-circuitpython-display/conversion
UART Serial:
- https://learn.adafruit.com/circuitpython-essentials/circuitpython-uart-serial

## Hardware I used to light this up:
- [Adafruit ESP32-S3 Reverse TFT Feather](https://learn.adafruit.com/esp32-s3-reverse-tft-feather)
- [Sensirion SHT45 Temperature & Humidity Sensors](https://learn.adafruit.com/adafruit-sht40-temperature-humidity-sensor)

## Rogh steps to lighting this up yourself (mileage varies, many ways to do this):

1) Flash the Featherboard with current CircuitPython
2) Plug the SHT45 board in via built-in i2c (my code does not use the GPIO, it's used for UART/serial instead)
3) from this directory, run `make all`, or,
4) Copy `./main.py`, `./lib/` and `./font/` onto the CIRCUITPY volume and wait for it to complete.

Your board should light up showing the RH/Temp on screen, and pumping output via GPIO serial headers.

# Happy hacking!
