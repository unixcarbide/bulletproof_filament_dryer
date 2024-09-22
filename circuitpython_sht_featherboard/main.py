# SPDX-FileCopyrightText: 2026 unixcarbide@blackhole.lol
#
# SPDX-License-Identifier: BSD-1-Clause
# -*- coding: utf-8 -*

import board
import displayio
import terminalio
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label

import time
import adafruit_sht4x
import gc

import busio
import digitalio

## Hardware Setup ##
#
display = board.DISPLAY
display.rotation = 90
#
try:
    i2c = board.I2C()  # uses board.SCL and board.SDA
    # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
    sht = adafruit_sht4x.SHT4x(i2c)
    print("Found SHT4x with serial number", hex(sht.serial_number))
    
    sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
    # Can also set the mode to enable heater
    # sht.mode = adafruit_sht4x.Mode.LOWHEAT_100MS
    print("Current mode is: ", adafruit_sht4x.Mode.string[sht.mode])
    sensor_err = False
except:
    print("Error setting up SHT4x sensor.")
    sensor_err = True
#
##  STUB: serial/uart setup
#
try:
    uartbaud = 9600
    # For most CircuitPython boards:
    led = digitalio.DigitalInOut(board.LED)
    # For QT Py M0:
    # led = digitalio.DigitalInOut(board.SCK)
    led.direction = digitalio.Direction.OUTPUT
    uart = busio.UART(board.TX, board.RX, baudrate=uartbaud)
    print("Set up UART serial commication.")
    print("Serial communication at %a baud." % uartbaud)
except:
    print("Error setting up uart serial.")
    uart_err = True
#
####################


def tempcolor(temp=0.0):
    '''
    Given a temperature float in C, return a hexadecimal color value.
    Start blue, transition orange, end red, then yellow freak out.
    https://www.colorhexa.com/e7ff00
    '''
    ti = int(temp)

    if temp <= 0:
        return 0x50eff5
    # starting blue,
    elif temp <= 18:
        return 0x0ee3ea
    elif temp <= 21:
        return 0x150eea
    elif temp <= 23:
        return 0x2b1bd4
    elif temp <= 26:
        return 0x4029bf
    elif temp <= 29:
        return 0x5537aa
    elif temp <= 31:
        return 0x6a4595
    elif temp <= 34:
        return 0x805280
    elif temp <= 37:
        return 0x95606a
    elif temp <= 39:
        return 0xaa6e55
    elif temp <= 42:
        return 0xbf7c40
    elif temp <= 45:
        return 0xd48a2b
    elif temp <= 47:
        return 0xea9715
    elif temp <= 50:
        return 0xffa500
    # transition orange,
    elif temp <= 53:
        return 0xff9700
    elif temp <= 56:
        return 0xff8a00
    elif temp <= 58:
        return 0xff7c00
    elif temp <= 61:
        return 0xff6e00
    elif temp <= 64:
        return 0xff6000
    elif temp <= 66:
        return 0xff5200
    elif temp <= 69:
        return 0xff4500
    elif temp <= 72:
        return 0xff3700
    elif temp <= 74:
        return 0xff2900
    elif temp <= 77:
        return 0xff1b00
    elif temp <= 80:
        return 0xff0e00
    elif temp <= 82:
        return 0xff0000
    # end in the red,
    elif temp <= 85:
        return 0xe7ff00
    else:
        return 0x8c8c8c


# Static Vars
DEBUG = "1"
# https://learn.adafruit.com/custom-fonts-for-pyportal-circuitpython-display/conversion
smallfont = bitmap_font.load_font("/font/NimbusSanL-Bol-16.bdf")
largefont = bitmap_font.load_font("/font/NimbusSanL-Bol-38.bdf")
massivefont = bitmap_font.load_font("/font/NimbusSanL-Bol-120.bdf")
magenta = 0xFF0080
meddark = 0x404040
medgrey = 0x666666
lightgrey = 0x8c8c8c
white = 0xFFFFFF


while True:
    try:
        temperature, relative_humidity = sht.measurements
    except:
        temperature, relative_humidity = 0.0, 99.0
        sensor_err = True

    # Write out to serial,
    try:
        msg_data = "%0.6f %0.6f" % (relative_humidity, temperature)
        uart.write(msg_data.encode('utf-8'))
    except:
        msg_data = b'ERR: UART!'
        serial_error =True


    # Write out to display,
    temphex = tempcolor(temperature)
    text_group = displayio.Group()

    if DEBUG:
        memfree = str(int(gc.mem_free() / 1024)) + " Mb"
        textmem = label.Label(terminalio.FONT, text=memfree, color=meddark)
        textmem.x = 2
        textmem.y = 230
        text_group.append(textmem)

        uptime = str(int(time.monotonic()))
        textup = label.Label(terminalio.FONT, text=uptime, color=meddark)
        textup.x = 2
        textup.y = 4
        text_group.append(textup)

        serial_message = str(msg_data)
        textup = label.Label(terminalio.FONT, text=serial_message, color=meddark)
        textup.x = 2
        textup.y = 14
        text_group.append(textup)

    rh_big=("%0.0f" % relative_humidity)
    bigRH = label.Label(massivefont, text=rh_big, color=magenta)
    bigRH.x = 0
    bigRH.y = 56
    text_group.append(bigRH)

    rh_title=("relative humidity")
    titleRH = label.Label(smallfont, text=rh_title, color=medgrey)
    titleRH.x = 2
    titleRH.y = 123
    text_group.append(titleRH)

    rh_string=("%0.02f%%" % relative_humidity)
    textRH = label.Label(largefont, text=rh_string, color=magenta)
    textRH.x = 2
    textRH.y = 146
    text_group.append(textRH)

    temp_title=("temperature")
    titleTemp = label.Label(smallfont, text=temp_title, color=medgrey)
    titleTemp.x = 2
    titleTemp.y = 174
    text_group.append(titleTemp)

    temp_txt=("%0.2fC" % temperature)
    temp_disp = label.Label(largefont, text=temp_txt, color=temphex)
    temp_disp.x = 2
    temp_disp.y = 197
    text_group.append(temp_disp)

    if sensor_err:
        error_msg = "ERR: sensor not found."
        ohsht = label.Label(terminalio.FONT, text=error_msg, color=white)
        ohsht.x = 2
        ohsht.y = 50 
        text_group.append(ohsht)


    display.root_group = text_group
    time.sleep(.9)
