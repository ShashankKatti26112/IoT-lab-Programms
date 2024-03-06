import time
import RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

relay1=38
gpio.setup(relay1,gpio.OUT,initial=0)
try:
    gpio.output(relay1,True)
    print("The relay is switched on")
    time.sleep(5)
    print("The relay is switched off")
    gpio.output(relay1,False)
except KeyboardInterrupt:
    gpio.cleanup()
    
