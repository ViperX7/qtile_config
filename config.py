"""
Qtile Config
"""
from os import listdir
from random import choice as rand_choice
from subprocess import PIPE
from subprocess import Popen

from libqtile import hook
from libqtile.config import ScratchPad
from libqtile.config import Screen

from bar import custom_bar
from keymaps import keys
from layouts import floating_layout
from layouts import layouts
from q_groups import group_keys
from q_groups import groups
from q_scratchpads import spad_keys
from q_scratchpads import spads
from settings import *

MOD_S = [MOD, "shift"]
MOD_C = [MOD, "control"]

# Append scratchpad with dropdowns to groups
groups.append(ScratchPad("scratchpad", spads))
keys.extend(spad_keys)  # extend keys list with keybinding for scratchpad
keys.extend(group_keys)

widget_defaults = dict(
    font="FiraCode Nerd Font", fontsize=12, padding=3, background="#111111"
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=custom_bar,
        wallpaper=WALL_PATH + rand_choice(listdir(WALL_PATH)),
        wallpaper_mode="fill",
    ),
    Screen(
        wallpaper=WALL_PATH + rand_choice(listdir(WALL_PATH)),
        wallpaper_mode="fill",
    ),
]


def run(cmd, shell=False):
    """
    Start a program in background

    Args:
        cmd (str): command to execute in background
    """
    Popen(cmd, stdout=PIPE, stderr=PIPE, shell=shell)


@hook.subscribe.startup_once
def autostart():
    """
    Start stuff automatically
    """
    run("lxqt-policykit-agent")
    run("xrandr --output DP-1 --mode 2560x1440 --rate 144 --primary --right-of HDMI-1",
        shell=True) if IS_DESKTOP else None
    run(["picom"])
    run(["nm-applet"])
    run("syncthing", shell=True)
    run("sh projects/capsmap.sh", shell=True)
    run("xfce4-power-manager --daemon")
    run(["deadd-notification-center"])
