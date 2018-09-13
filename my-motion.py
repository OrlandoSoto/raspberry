#!/usr/bin/python

import picamera
import picamera.array
import time
import sys
from os import listdir
from os.path import isfile, join
import random
import pygame
import datetime
import utils 

threshold = 20    # How Much pixel changes
sensitivity = 100 # How many pixels change


def play_sound():

    # If a file_path was passed in then use it
    if(sys.argv[1:]):
        print(sys.argv[1:])
        file_path = sys.argv[1]
    # Otherwise use the deafult directory
    else:
        file_path = 'warn'

    if not listdir(file_path):
        raise FileNotFoundError("Directory is empty")

    filename = utils.get_file_name(file_path)

    pygame.mixer.init()
    pygame.mixer.music.load(file_path + '/' + filename)

    pygame.mixer.music.play()

    # Wait for the sound to finish playing
    while pygame.mixer.music.get_busy():
        continue
    
def takeMotionImage(width, height):
    with picamera.PiCamera() as camera:
        time.sleep(1)
        camera.resolution = (width, height)
        with picamera.array.PiRGBArray(camera) as stream:
            camera.exposure_mode = 'auto'
            camera.awb_mode = 'auto'
            camera.capture(stream, format='rgb')
            return stream.array

def scanMotion(width, height):
    motionFound = False
    data1 = takeMotionImage(width, height)
    while not motionFound:
        data2 = takeMotionImage(width, height)
        diffCount = 0;
        for w in range(0, width):
            for h in range(0, height):
                # get the diff of the pixel. Conversion to int
                # is required to avoid unsigned short overflow.
                diff = abs(int(data1[h][w][1]) - int(data2[h][w][1]))
                if  diff > threshold:
                    diffCount += 1
            if diffCount > sensitivity:
                break;
        if diffCount > sensitivity:
            motionFound = True
        else:
            data2 = data1
    return motionFound

def take_snapshot():
    my_date = datetime.datetime.now().strftime("%B %d %Y %-I %M %S %p")
    print(my_date)
    camera = picamera.PiCamera()
    camera.rotation = 180
    camera.annotate_text = my_date
    camera.capture('selfie.png')
    camera.close()

def motionDetection():
    print("Scanning for Motion threshold=%i sensitivity=%i"  % (threshold, sensitivity))
    while True:
        if scanMotion(640, 480):
            print("Motion detected")
            take_snapshot()
            play_sound()
            

if __name__ == '__main__':
    try:
        motionDetection()
    finally:
        print("Exiting Program")
