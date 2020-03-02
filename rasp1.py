# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:19:45 2020

@author: CEC
"""

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)


while True:
    if GPIO.input(25):
        GPIO.output(18, False)
    else:
        GPIO.output(18, True)
    