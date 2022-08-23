#!/bin/bash
notify-send "Setting Up multi monitor"
xrandr --auto 
xrandr --output HDMI-1-0 --auto --mode 1920x1080 --left-of eDP1
xrandr --output HDMI-A-0 --auto --mode 1920x1080 --left-of eDP
