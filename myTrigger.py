import RPi.GPIO as gpi
import pygame as pg
from time import sleep


pg.mixer.init()
pg.mixer.music.load("") #file name here



gpi.setwarnings(False)
gpi.setmode(gpi.BCM)

gpi.setup(36, gpi.IN) #GPIO-16 INPUT-Button

gpi.setup(31, gpi.OUT) #GPIO-6 OUTPUT-Speaker

trigger= 0

while trigger==0:
    # evaluate if button is pressed
    if gpi.input(36):
        print("[INFO] button triggered")
        import object_detection
        from object_detection import desired_detect
        if desired_detect == True:
            gpi.output(31,True)
            sleep(3)
            gpi.output(31,False)
            pg.mixer.music.play() #play sound
            print('detected')

        else:
            print("No person detected")
        trigger = 1
