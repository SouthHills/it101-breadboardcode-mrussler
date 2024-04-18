from asyncore import loop
from gpiozero import LED as LEDClass, Button
from signal import pause
import time

LED = LEDClass(17)  # define ledPin
BUTTON = Button(18)  # define buttonPin
is_blinking = False

def changeLedState():
    global is_blinking
    is_blinking = not is_blinking
    
def loop():
    global LED, is_blinking
    if is_blinking == True:
        LED.on()
        print ("led on >>>")
        time.sleep(0.5)
        LED.off()
        print ("led off <<<")
        time.sleep(0.5)

def destroy():
    global LED, BUTTON
    # Release resources
    LED.close()
    BUTTON.close()

if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")
    try:
        # If the button gets pressed, call the function
        # This is an event
        BUTTON.when_pressed = changeLedState
        while True:
            loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

