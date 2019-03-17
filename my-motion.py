#!/usr/bin/python
import time
import utils
from gpiozero import MotionSensor
import datetime

snapshots_dir = 'snapshots'

def main():
    print("Scanning for Motion")
    pir = MotionSensor(4)
    while (True):
        if(pir.wait_for_motion()):
            print("Motion detected")
            #snapshot_file = utils.take_snapshot(snapshots_dir)
            my_date = datetime.datetime.now().strftime("%B %d %Y %-H %M %S")
            print(my_date)
            utils.play_sound()
            #utils.copy_snapshot(snapshot_file)
            time.sleep(10)


if __name__ == '__main__':
    try:
        main()
    finally:
        print("Exiting Program")
