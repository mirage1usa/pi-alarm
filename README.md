# PiAlarm
 Simple, Python3, Alarm Clock and Alerting Script

Description: 
   Create as may separate PiAlarm python scripts as you want alerts, then schedule them in crontab.
   Instructions and examples are resonably well documented in the example School.py alarm file.
   This was created as a fun way to keep our daughter on a schedule, while school was closed for COVID-19.
   
   My requirements for this were:
      1. Must only use Python scripts and crontabs
	  2. Must have minimal dependancies
	  3. Must pop a customizable alert on the screen and play a sound
	  4. Must be a good introduction to expose beginners to python and crontab usage
	  
   I fought with many different sound apps and finally found that MPG123 was the only one that accomplished what I needed
   
   Primary options in the python files:
      1. sound file to play or comment out if you don't want sound
	  2. sound file volume
	  3. GUI window size
      4. GUI window and text color
      5. GUI window text font
      6. GUI window time before it closes or comment out to manually close them

Dependancies: Python3, GUIZero, MPG123

Create separate of these .py files for different messages
Open crontab file by running this in Terminal "crontab -e"

Examples of what to add to the crontab file. This will execute the School.py script every Monday-Friday at 8AM
  0 8 * * 1,2,3,4,5 DISPLAY=:0 /usr/bin/python3 /home/pi/PiAlarm/School.py

Install Python 3: sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y

Install GUIZero:  sudo pip3 install guizero
   About GUIZero:    https://lawsie.github.io/guizero/window/

Install MPG123:   sudo apt-get install mpg123
   About MPG123:     https://www.mpg123.org/