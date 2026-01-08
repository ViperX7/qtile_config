
# set display properly
# xrandr --output HDMI-1 --off
# sleep 5
xrandr --output DisplayPort-0 --mode 3440x1440 --rate 174 --primary
xrandr --output HDMI-A-0 --mode 2560x1440 --rate 170 --primary --right-of DisplayPort-0
sleep 1
xrandr --output  DisplayPort-0  --primary
