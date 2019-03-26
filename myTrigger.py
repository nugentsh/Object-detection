import RPi.GPIO as gpi
import pygame as pg
from time import sleep

pg.mixer.init()
pg.mixer.music.load("") #file name here

gpi.setwarnings(False)
gpi.setmode(gpi.BCM)

# set pins, GPIO-16 INPUT-Button, GPIO-6 OUTPUT-Speaker
gpi.setup(36, gpi.IN) 
gpi.setup(31, gpi.OUT) 

trigger= 0

while trigger==0:
    # evaluate if button is pressed
    if gpi.input(36):
        print("[INFO] button triggered")
        
        # run the object detection program and import detection confirmation
        import object_detection
        from object_detection import desired_detect
        
        # evaluate if person detected and play sound
        if desired_detect == True:
            gpi.output(31,True)
            sleep(3)
            gpi.output(31,False)
            pg.mixer.music.play()
            print('Person detected')

        else:
            print("No person detected")
        trigger = 1
