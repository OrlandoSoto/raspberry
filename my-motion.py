#!/usr/bin/python
import time
import utils
from gpiozero import MotionSensor

snapshots_dir = 'snapshots'

def main():
    print("Scanning for Motion")
    pir = MotionSensor(4,2,100,.9)
    while (True):
        if(pir.wait_for_motion()):
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
