"""
Qtile Config
"""

from subprocess import PIPE, Popen
from libqtile import hook

from os import listdir
from random import choice as rand_choice
from libqtile.config import Click, Drag, Key, Screen, ScratchPad
from libqtile.lazy import lazy

from settings import *
from q_scratchpads import spads, spad_keys
from q_groups import groups, group_keys
from bar import custom_bar
from layouts import layouts, floating_layout
from keymaps import keys

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
]


def run(cmd):
    otp = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=False)


@hook.subscribe.startup_once
def autostart():
    run(["deadd-notification-center"])
    run(["picom"])
    run(["nm-applet"])
    run("lxqt-policykit-agent")
