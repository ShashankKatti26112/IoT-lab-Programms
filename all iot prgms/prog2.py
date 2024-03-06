import time 
import RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
led1=15
led2=13
switch1=37
switch2=35
gpio.setup(led1,gpio.OUT,initial=0)
gpio.setup(led2,gpio.OUT,initial=0)
gpio.setup(switch1,gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(switch2,gpio.IN,pull_up_down=gpio.PUD_UP)
while True:
    if gpio.input(switch1)==1:
        gpio.output(led1,0)
    else:
        gpio.output(led1,1)
    if gpio.input(switch2)==1:
        gpio.output(led2,0)
    else:
        gpio.output(led2,1)