import subprocess
import time
from gpiozero import Button
from signal import pause

BUTTON1 = Button(23)
BUTTON2 = Button(24)
toggle1 = True
toggle2 = True
firefox_process = 0
chrome_process = 0

def loop1():
    global BUTTON1, toggle1, firefox_process
    if toggle1 == True:
        firefox_process = subprocess.Popen(["firefox"])
    else:
        firefox_process.terminate()
    toggle1 = not toggle1

def loop2():
    global BUTTON2, toggle2, chrome_process
    if toggle2 == True:
        chrome_process = subprocess.Popen(["chromium-browser"])
    else:
        chrome_process.terminate()
    toggle2 = not toggle2
            
def destroy():
    global BUTTON1, BUTTON2
    BUTTON1.close()
    BUTTON2.close()

if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")
    try:
        BUTTON1.when_pressed = loop1
        BUTTON2.when_pressed = loop2
        pause()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()