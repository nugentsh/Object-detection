from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/myproject/image.jpg')
camera.stop_preview()

sleep(2)
camera.stop_preview()
