#!/bin/bash

cd ~/projects/covid-riau-tracker && /usr/bin/python overall-tracker.py >> overall.out
cd ~/projects/covid-riau-tracker && /usr/bin/python regional-tracker.py >> overall.out
cd ~/projects/covid-riau-tracker && /usr/bin/python rohul-tracker.py >> overall.out

sleep 5
cd ~/projects/covid-riau-tracker && /usr/bin/git add .
cd ~/projects/covid-riau-tracker && /usr/bin/git commit -m "Update Dataset"
HOME = /home/pi/.ssh/id_rsa 
/usr/bin/git push origin master
