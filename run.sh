#!/bin/bash
cd /home/pi/WRO_FE2021
sudo echo STARTING PROGRAMM >> ./log.txt
sudo -E python3 ./main.py >> ./log.txt 2>> ./log.txt
