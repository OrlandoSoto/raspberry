#! /bin/sh

cd /media/orlando/XP/snapshots
find -type f -mtime +6 -name '*.png' -execdir rm -rf -- '{}' \;

cd /media/orlando/XP/videos
find -type f -mtime +6 -name '*.mpg' -execdir rm -rf -- '{}' \;