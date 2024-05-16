from pathlib import Path
import sys
from gpiozero import PWMLED

HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import *
USING_GRAVITECH_ADC = False

LED1 = PWMLED(6)
LED2 = PWMLED(13)
LED3 = PWMLED(19)
LED4 = PWMLED(26)
ADC = ADCDevice()

def setup():
    global ADC
    if(ADC.detectI2C(0x48) and USING_GRAVITECH_ADC): 
        ADC = GravitechADC()
    elif(ADC.detectI2C(0x48)):
        ADC = PCF8591()
    elif(ADC.detectI2C(0x4b)):
        ADC = ADS7830()
    else:
        print("No correct I2C address found, \n"
            "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
            "Program Exit. \n")
        exit(-1)

def loop():
    global LED1, LED2, LED3, LED4
    while True:
        value = ADC.analogRead(0)
        percentage = (value / 255) * 100
        print(value)
        print(percentage)
        
        if percentage < 25:
            LED4.off()
            LED3.off()
            LED2.off()
            LED1.off()
        elif percentage >= 25 and percentage < 50:
            LED4.on()
            LED3.off()
            LED2.off()
            LED1.off()
        elif percentage >= 50 and percentage < 75:
            LED4.on()
            LED3.on()
            LED2.off()
            LED1.off()
        elif percentage >= 75 and percentage < 95:
            LED4.on()
            LED3.on()
            LED2.on()
            LED1.off()
        else:
            LED4.on()
            LED3.on()
            LED2.on()
            LED1.on()

def destroy():
    global LED1, LED2, LED3, LED4, ADC
    LED1.close()
    LED2.close()
    LED3.close()
    LED4.close()
    ADC.close()
    
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()