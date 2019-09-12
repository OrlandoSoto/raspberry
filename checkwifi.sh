FILE="/tmp/one.txt"
ping -c4 192.168.1.1 > /dev/null

if [ $? != 0 ] 
then
  echo $(date) >> $FILE
  echo "No network connection, restarting wlan0" >> $FILE
fi