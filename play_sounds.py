#! /usr/bin/python
import os
from os import listdir
from os.path import isfile, join
import random
import sys
import time
import subprocess
import psutil

file_path = ''


def get_file_name(search_path):
    onlyfiles = [f for f in listdir(search_path) if isfile(join(search_path, f))]
    print(onlyfiles)

    random_filename = random.choice(onlyfiles)
    print(random_filename)
    return search_path + '/' + random_filename


def main():

    # If a file_path was passed in then use it
    if(sys.argv[1:]):
        print(sys.argv[1:])
        file_path = sys.argv[1]
    # Otherwise use the default directory
    else:
        file_path = 'warn'

    if not listdir(file_path):
        raise FileNotFoundError("Directory is empty")

    filename = get_file_name(file_path)
    print filename

    if checkIfProcessRunning('/usr/bin/aplay'):
        print('Yes a aplay process was running')
        return
    else:
        print('No aplay process was running')
        subprocess.Popen(['/usr/bin/aplay', filename])
        sys.exit(0)

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


if __name__ == "__main__":
    main()
