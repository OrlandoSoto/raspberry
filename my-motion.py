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

threshold = 64     # How Much pixel changes
sensitivity = 3000  # How many pixels change
snapshots_directory = 'snapshots'


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
        diffCount = 0
        for w in range(0, width):
            for h in range(0, height):
                # get the diff of the pixel. Conversion to int
                # is required to avoid unsigned short overflow.
                diff = abs(int(data1[h][w][1]) - int(data2[h][w][1]))
                if diff > threshold:
                    diffCount += 1
            if diffCount > sensitivity:
                break
        if diffCount > sensitivity:
            motionFound = True
        else:
            data2 = data1
    return motionFound


def main():
    print("Scanning for Motion threshold=%i sensitivity=%i" % (threshold, sensitivity))
    while True:
        if utils.detect_motion():
        #if scanMotion(640, 480):
            print("Motion detected")
            utils.take_snapshot(snapshots_directory)
            utils.play_sound()


if __name__ == '__main__':
    try:
        main()
    finally:
        print("Exiting Program")
