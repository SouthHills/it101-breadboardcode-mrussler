from gpiozero import RGBLED, Button
import time
import random
from signal import pause

LED = RGBLED(red=17, green=18, blue=27, active_high=True)
BUTTON = Button(24)
toggle = True
COLORS = ((1,0,0), (0,1,0), (0,1,1))

def set_color(r, g, t):
    LED.color = (1 - r, 1 - g, 1 - t)
    
def stop_game():
    global toggle
    toggle = False
    print(toggle)
    if LED.color == (1,0,1):
        for _ in range(5):
            set_color(0,0,0)
            time.sleep(0.5)
            set_color(0,1,0)
            time.sleep(0.5)
    else:
        for _ in range(5):
            set_color(0,0,0)
            time.sleep(0.5)
            set_color(1,0,0)
            time.sleep(0.5)

def cycle():
    global COLORS
    while toggle:
        color = random.choice(COLORS)
        set_color(color[0], color[1], color[2])
        time.sleep(0.5)
        
def destroy():
    global LED, BUTTON
    LED.close()
    BUTTON.close()
    
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        BUTTON.when_pressed = stop_game
        cycle()
        pause()
    except KeyboardInterrupt:
        destroy()