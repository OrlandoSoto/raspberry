#! /bin/sh
DAYS=14
DIRECTORY=/media/orlando/camera

echo $DAYS
cd $DIRECTORY
find . -type f -mtime $DAYS -name '*.thumb' -execdir rm -rf -- '{}' \;
find . -type f -mtime $DAYS -name '*.png' -execdir rm -rf -- '{}' \;


find . -type f -mtime $DAYS \( -name '*.mp4' -o -name '*.h264' \) -execdir rm -rf -- '{}' \;
find . -type f -mtime $DAYS \( -name '*.jpg' -o -name '*.thumbs' \) -execdir rm -rf -- '{}' \;

# Delete empty directories
find $DIRECTORY -empty -type d -delete
