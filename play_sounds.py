#! /usr/bin/env python
from os import listdir
from os.path import isfile, join 
import random
import pygame

file_path = 'warn/'

def get_file_name():
    onlyfiles = [f for f in listdir(file_path) if isfile(join(file_path, f))]
    print(onlyfiles)

    random_filename = random.choice(onlyfiles)
    print(random_filename)
    return random_filename

if not listdir(file_path) :
    raise FileNotFoundError("Directory is empty")

filename = get_file_name()

pygame.mixer.init()
pygame.mixer.music.load(file_path + filename)

pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
    continue

