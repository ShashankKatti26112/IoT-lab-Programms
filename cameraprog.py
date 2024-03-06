from picamera import PiCamera
import time
import datetime

camera = PiCamera()
camera.resolution=(1920,1080)
camera.vflip=False

camera.start_preview()
time.sleep(10)

current_date=datetime.datetime.now().strftime('%d-%m-%y-%H:%M:%S')
camera.capture('/home/pi/Desktop/Manjunath_iot'+current_date+'.jpg')
camera.stop_preview()
print("done")