# PiAlarm
 Simple, Python3, Alarm Clock and Alerting Script

## Description: 
   Create as may separate PiAlarm python scripts as you want alerts, then schedule them in crontab.
   Instructions and examples are resonably well documented in the example School.py alarm file.
   In the standard configuration, when an alarm script is ran, it starts playing the music file
   with no player GUI visible.  It then triggers a GUI window to appear on the screen and display
   the message you program in the script.  After the window close delay that you set, the GUI window
   will automatically close.
   
   This was created as a fun way to keep our daughter on a schedule, while school was closed for COVID-19.
   
<p align="center">
<img width="834" height=auto src="Pi-Alarm-examples.jpg" alt="Examples of PiAlarm Windows">
</p>

##   My requirements for this were:
* Must only use Python scripts and crontabs
* Must have minimal dependancies
* Must pop a customizable alert on the screen and play a sound
* Must be a good introduction to expose beginners to python and crontab usage
   
##   Primary options in the python files:
*  Sound file to play or comment out if you don't want sound
*  Sound file volume control
*  GUI window size control
*  GUI window and text color control
*  GUI window text font control
*  GUI window time before it closes or comment out to manually close them
*  All of these options had to be independantly adjustable for each alarm

## Dependancies: 
`Python3`, `GUIZero`, `MPG123`

### Install Python 3:
`sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y`

### Install GUIZero:
`sudo pip3 install guizero`

About GUIZero:    https://lawsie.github.io/guizero/window/

### Install MPG123:
`sudo apt-get install mpg123`

About MPG123:     https://www.mpg123.org/

   I fought with many different sound apps and finally found that `MPG123` was the only one that accomplished what I needed

## Clone Pi-Alarm Git to your computer
```sh
git clone https://github.com/pi-alarm/pi-alarm.git
cd pi-alarm
```
### Pi-Alarm Usage
Create separate copies of the .py script files for different messages (make copies of School.py example and edit them)

Open crontab file by running this in Terminal `crontab -e`

Examples of what to add to the crontab file. This will execute the School.py script every Monday-Friday at 8AM

`  0 8 * * 1,2,3,4,5 DISPLAY=:0 /usr/bin/python3 /home/pi/PiAlarm/School.py`

### Testing your alerts
```sh
cd pi-alarm
python3 School.py
```
