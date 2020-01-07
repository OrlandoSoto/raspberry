#!/bin/sh
while inotifywait -qq /var/lib/motioneye/carport --recursive --event CREATE; do
    date >> /home/pi/test.txt
    /home/pi/raspberry/play_sounds.py /home/pi/raspberry/warn
done

