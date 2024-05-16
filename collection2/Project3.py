from pathlib import Path
import sys
from gpiozero import RGBLED
import time
import tkinter as tk
from tkinter import messagebox

RED_LED_PIN = 17      # define 3 pins for RGBLED
GREEN_LED_PIN = 27
BLUE_LED_PIN = 22
RGB_LED = RGBLED(red=RED_LED_PIN, GREEN_LED_PIN =GREEN_LED_PIN, blue=BLUE_LED_PIN, pwm=True)

CPUtemp = open /sys/class/thermal/thermal_zone0/temp

def setup():
    
def loop():

def destroy():

if __name__ == '__main__':   # Program entrance
    print ('Program is starting... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()