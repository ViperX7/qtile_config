"""
Qtile Config
"""
from os import listdir
from random import choice as rand_choice
from subprocess import PIPE, Popen

from bar import custom_bar
from bar2 import BAR as custom_bar_new
from keymaps import keys
from libqtile import hook
from libqtile.config import ScratchPad, Screen
from q_groups import group_keys, groups
from q_scratchpads import spad_keys, spads
from layouts import layouts, floating_layout
from settings import (AUTO_START_ALWAYS, AUTO_START_ONCE, IS_DESKTOP, MOD,
                      WALL_PATH, auto_fullscreen)

MOD_S = [MOD, "shift"]
MOD_C = [MOD, "control"]
# pyright: basic
# Append scratchpad with dropdowns to groups
groups.append(ScratchPad("scratchpad", spads))
keys.extend(spad_keys)  # extend keys list with keybinding for scratchpad
keys.extend(group_keys)

widget_defaults = {
    "font": "FiraCode Nerd Font",
    "fontsize": 12,
    "padding": 3,
    "background": "#111111",
}
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=custom_bar,
        wallpaper=WALL_PATH + rand_choice(listdir(WALL_PATH)),
        wallpaper_mode="fill",
    ),
    Screen(
        # top=custom_bar_new,
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

    # _ = (
    #     run(
    #         "xrandr --output DP-1 --mode 2560x1440 --rate 170 --primary --left-of HDMI-1",
    #         shell=True,
    #     )
    #     if IS_DESKTOP
    #     else None
    # )

    _ = [run(prog) for prog in AUTO_START_ONCE["daemon"]]
    _ = [run(prog, shell=True) for prog in AUTO_START_ONCE["cmd"]]


@hook.subscribe.startup
def autostart_everytime():
    """
    starts programs every restart
    """

    _ = [run(prog) for prog in AUTO_START_ALWAYS["daemon"]]
    _ = [run(prog, shell=True) for prog in AUTO_START_ALWAYS["cmd"]]
