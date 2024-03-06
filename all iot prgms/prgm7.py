import signal
import sys
import datetime
import RPi.GPIO as GPIO

button_gpio = 37
led_gpio = 13
last_led_state = 0
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
    
def button_pressed_callback(channel):
    global last_led_state
    GPIO.output(led_gpio, not last_led_state)
    last_led_state = not last_led_state
    print("LED", last_led_state)
    
from flask import Flask, render_template
app = Flask(__name__, template_folder='template')
@app.route('/')

def relaystatus():
    now = datetime.datetime.now()
    timestring = now.strftime("%H-%M-%d-%m-%y")
    tempdate = {
        'status':last_led_state,
        'time':timestring
        }
    return render_template("web2.html",**tempdate)

if __name__=="__main__":
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(button_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(led_gpio, GPIO.OUT)
    GPIO.add_event_detect(button_gpio, GPIO.FALLING, callback =button_pressed_callback,bouncetime=200)
app.run(debug = False, port=4001, host='172.16.4.147')
signal.signal(signal.INIT, signal_handler)
signal.pause()
                                                                                                                     