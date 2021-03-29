#! /usr/bin/python
import psutil
import sys

processName = ''

def main():

    # If a process name was passed in then use it
    if(sys.argv[1:]):
        print(sys.argv[1:])
        processName = sys.argv[1]
    # Otherwise exit
    else:
        return

    if checkIfProcessRunning(processName):
        print('Yes ' + processName + ' process was running')
        return
    else:
        print('No ' + processName + ' process was running')


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains
    the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


if __name__ == "__main__":
    main()
