from gpiozero import PWMLED

LED = PWMLED(17)
LED1 = PWMLED(18)

import subprocess

def is_internet_connected():
    try:
    # Run the ping command with a timeout of 2 seconds and count 1 packet
        subprocess.check_output(['ping', '-c', '1', '-W', '2', 'www.google.com'])
        return True
    except subprocess.CalledProcessError:
        return False      
    
def destroy():
    global LED, LED1
    LED.close()
    LED1.close()
    
if __name__ == '__main__':
    print ('Program is starting ... ')
    print(f"Using pin {LED.pin}")
    try:
        while True:
            if is_internet_connected():
                LED1.on()
            else:
                LED1.off()
                LED.on()
    except KeyboardInterrupt:
        destroy()