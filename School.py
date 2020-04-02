#!/usr/bin/python3

## Pi-Alarm
## Create separate of these .py files for different messages
## Open crontab file by running this in Terminal "crontab -e"
##
## Examples of what to add to the crontab file
##   0 8 * * 1,2,3,4,5 DISPLAY=:0 /usr/bin/python3 /home/pi/pi-alarm/WakeUp.py
## This will execute the WakeUp.py script every Monday-Friday at 8AM
##
## Install Python 3: sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y
## Install GUIZero:  sudo pip3 install guizero
## About GUIZero:    https://lawsie.github.io/guizero/window/
## Install MPG123:   sudo apt-get install mpg123
## About MPG123:     https://www.mpg123.org/

from guizero import App, Text
import subprocess, os

# Function to Close the Window
def closewindow():
    app.destroy()

# Play a sound file
# Options [-q = quiet] [-f = scalefactor for volume control default(max): 32768 (0-32768)]
playsound = os.popen('mpg123 -q -f 25000 /home/pi/pi-alarm/School-bell-sound-effect.mp3', 'w')

# Display GUI window
app = App(title="PiAlarm", bg = "green", height=200, width=500)
Alarm = Text(app, text="", size=40, font="Arial", color="black")
Alarm = Text(app, text="Time for SCHOOL!", size=40, font="Arial", color="white")
app.after(200000, closewindow) # Time in milliseconds to wait before closing window
app.display()
