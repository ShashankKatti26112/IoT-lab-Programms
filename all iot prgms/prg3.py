import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

led1=15

gpio.setup(led1,gpio.OUT,initial=0)

file1=open('light.txt','r')
line= file1.readlines()
setOn=str(line[0].split('=')[1])
starthr=setOn.split(':') [0]
startmin=setOn.split(':') [1]
setOff=str(line[1].split('=')[1])
stophr=setOff.split(':') [0]
stopmin=setOff.split(':') [1]

while(True):
    time1=time.ctime(time.time())
    ptime=time1.split()[3]
    phr=ptime.split(':')[0]
    pmin=ptime.split(':')[1]
    if(phr==starthr and pmin==startmin):
        gpio.output(led1,True)
        print("LED on")
    elif(phr==stophr and pmin==stopmin):
        gpio.output(led1,False)
        print("LED off")