#! /usr/bin/python
import picamera
from os import listdir
from os.path import isfile, join
import random
import sys
import pygame
import datetime
from gpiozero import MotionSensor
from paramiko import SSHClient
from scp import SCPClient
import os


def get_file_name(search_path):
    onlyfiles = [f for f in listdir(search_path) if isfile(join(search_path, f))]
    print(onlyfiles)

    random_filename = random.choice(onlyfiles)
    print(random_filename)
    return random_filename


def play_sound():

    # If a file_path was passed in then use it
    if(sys.argv[1:]):
        print(sys.argv[1:])
        file_path = sys.argv[1]
    # Otherwise do not play sound
    else:
        return

    if not listdir(file_path):
        raise FileNotFoundError("Directory is empty")

    filename = get_file_name(file_path)

    pygame.mixer.init()
    pygame.mixer.music.load(file_path + '/' + filename)

    pygame.mixer.music.play()

    # Wait for the sound to finish playing
    while pygame.mixer.music.get_busy():
        continue


def take_snapshot(target_dir):
    my_date = datetime.datetime.now().strftime("%B %d %Y %-H %M %S")
    my_timestamp = datetime.datetime.now().strftime("%B-%d-%Y-%-H-%M-%S")
    print(my_date)
    file_name = target_dir + '/' + my_timestamp + '.png'
    camera = picamera.PiCamera()
    camera.resolution = (1280, 720)
    camera.rotation = 180
    camera.annotate_text = my_date
    camera.capture(file_name)
    camera.close()
    return file_name


def detect_motion():
    pir = MotionSensor(4,2,100,.3)
    pir.wait_for_motion()
    print("Motion Detected")
    return True

def copy_snapshot(file_name):
    passwd = (os.environ.get('PW'))
    dest_dir = '/media/orlando/XP/snapshots'
    source_file = file_name

    ssh = SSHClient()
    ssh.load_system_host_keys()
    try:
        ssh.connect('orlando-ubuntu',22,'orlando',passwd, None,None,5)
    except Exception as e:
        print("Could not scp " + str(e) )
        return
    
    scp = SCPClient(ssh.get_transport())
    scp.put(source_file, dest_dir, False, True)
    scp.close()
    ssh.close()
    os.remove(source_file)

    

