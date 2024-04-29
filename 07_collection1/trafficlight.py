from gpiozero import RGBLED
import time

LED = RGBLED(red = 17, green = 18, blue = 27, active_high = True)

def color_set(r, g, y):
    LED.color = (1 - r, 1 - g, 1 - y)
    
def cycle():
    while True:
        color_set(1, 0, 0)
        print("All red")
        time.sleep(5)
        color_set(0, 1, 0)
        print("All green")
        time.sleep(7)
        color_set(1, 1, 0)
        print("All yellow")
        time.sleep(2)        

def destroy():
    LED.close()
    
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        cycle()
    except KeyboardInterrupt:
        destroy()