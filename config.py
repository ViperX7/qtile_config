"""
Qtile Config
"""
from os import listdir
from random import choice as rand_choice
from subprocess import PIPE, Popen

from bar import custom_bar
from keymaps import keys
from libqtile import hook
from libqtile.config import ScratchPad, Screen
from q_groups import group_keys, groups
from q_scratchpads import spad_keys, spads
from settings import *

MOD_S = [MOD, "shift"]
MOD_C = [MOD, "control"]

# Append scratchpad with dropdowns to groups
groups.append(ScratchPad("scratchpad", spads))
keys.extend(spad_keys)  # extend keys list with keybinding for scratchpad
keys.extend(group_keys)

widget_defaults = {
    "font": "FiraCode Nerd Font",
    "fontsize": 12,
    "padding": 3,
    "background": "#111111"
}
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
    _ = run(
        "xrandr --output DP-1 --mode 2560x1440 --rate 144 --primary --right-of HDMI-1",
        shell=True) if IS_DESKTOP else None
    run(["picom"])
    run(["nm-applet"])
    run("syncthing", shell=True)
    run("sh projects/capsmap.sh", shell=True)
    run("xfce4-power-manager --daemon")
    run(["deadd-notification-center"])
