#!/bin/bash

cd ~/projects/covid-riau-tracker && /usr/bin/python overall-tracker.py >> overall.out
cd ~/projects/covid-riau-tracker && /usr/bin/python regional-tracker.py >> overall.out
cd ~/projects/covid-riau-tracker && /usr/bin/python rohul-tracker.py >> overall.out
