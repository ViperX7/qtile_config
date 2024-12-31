
# set display properly
# xrandr --output HDMI-1 --off
# sleep 5
xrandr --output HDMI-1 --mode 1920x1080 --rate 60 --right-of DP-1
xrandr --output DP-1 --mode 2560x1440 --rate 170 --primary
sleep 1
xrandr --output  DP-1  --primary
