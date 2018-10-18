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

snapshots_directory = 'snapshots'

def main():
    print("Scanning for Motion")
    while True:
        if utils.detect_motion():
            print("Motion detected")
            utils.take_snapshot(snapshots_directory)
            utils.play_sound()
            time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    finally:
        print("Exiting Program")
