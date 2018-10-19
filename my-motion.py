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

snapshots_dir = 'snapshots'

def main():
    print("Scanning for Motion")
    while True:
        if utils.detect_motion():
            print("Motion detected")
            snapshot_file = utils.take_snapshot(snapshots_dir)
            utils.play_sound()
            utils.copy_snapshot(snapshot_file)
            time.sleep(5)


if __name__ == '__main__':
    try:
        main()
    finally:
        print("Exiting Program")
