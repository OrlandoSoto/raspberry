#! /usr/bin/env python
from os import listdir
from os.path import isfile, join
import random
import sys
import pygame

file_path = ''


def get_file_name(search_path):
    onlyfiles = [f for f in listdir(search_path) if isfile(join(search_path, f))]
    print(onlyfiles)

    random_filename = random.choice(onlyfiles)
    print(random_filename)
    return random_filename


def main():

    # If a file_path was passed in then use it
    if(sys.argv[1:]):
        print(sys.argv[1:])
        file_path = sys.argv[1]
    # Otherwise use the deafult directory
    else:
        file_path = 'warn'

    if not listdir(file_path):
        raise FileNotFoundError("Directory is empty")

    filename = get_file_name(file_path)

    pygame.mixer.init()
    pygame.mixer.music.load(file_path + '/' + filename)

    pygame.mixer.music.play()

    # Wait for the sound to finish playing
    while pygame.mixer.music.get_busy():
        continue


if __name__ == "__main__":
    main()
