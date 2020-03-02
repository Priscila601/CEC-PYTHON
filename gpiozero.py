# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:26:30 2020

@author: CEC
"""

from gpiozero import LED, Button
from signal import pause

led = LED(18)
button = Button(25)

button.when_pressed = led.on
button.when_released = led.off

pause()