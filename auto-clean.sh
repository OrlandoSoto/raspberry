#! /bin/sh

cd /media/orlando/XP/snapshots
find . -type f -mtime +6 -name '*.png' -execdir rm -rf -- '{}' \;

cd /media/orlando/XP/videos/media
find . -type f -mtime +6 \( -name '*.mp4' -o -name '*.h264' \) -execdir rm -rf -- '{}' \;
find . -type f -mtime +6 -name '*.jpg' -execdir rm -rf -- '{}' \;

cd /media/orlando/XP/videos/Camera1
find . -type f -mtime +6 \( -name '*.mp4' -o -name '*.h264' \) -execdir rm -rf -- '{}' \;
find . -type f -mtime +6 -name '*.thumb' -execdir rm -rf -- '{}' \;
find /media/orlando/XP/ -empty -type d -delete
