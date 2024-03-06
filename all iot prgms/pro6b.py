import time
import RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

import datetime
led=13
gpio.setup(led,gpio.OUT,initial=0)
gpio.setup(led,gpio.OUT)
from flask import Flask,render_template
app=Flask(__name__,template_folder='template')
@app.route('/')
def hello_world():
    return render_template('web2.html')
@app.route('/redledon')
def redledon():
    gpio.output(13,gpio.HIGH)
    now=datetime.datetime.now()
    timestring=now.strftime("%Y-%m-%d-%H-%M")
    templateData={
        'status':'ON',
        'time':timestring}
    return render_template('web2.html',**templateData)
@app.route('/redledoff')

def redledoff():
    gpio.output(13,gpio.LOW)
    now=datetime.datetime.now()
    timestring=now.strftime("%Y-%m-%d-%H-%M")
    templateData={
        'status':'OFF',
        'time':timestring}
    return render_template('web2.html',**templateData)
if __name__=='__main__':
    app.run(debug=True,port=4002,host='172.16.4.147')


    


