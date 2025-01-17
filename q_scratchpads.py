"""
Scratchpads
"""
# pyright: basic

import os
import subprocess

from libqtile.config import DropDown, Key, KeyChord, Match
from libqtile.lazy import lazy
from settings import FILEMAN, MOD, TERMINAL


def scratchgen(name, spawn, h, w, x=None, y=None, autohide=False, res="", opacity=1):
    # center everything by default
    if x is None:
        x = x if x else (1 - w) / 2
    if y is None:
        y = y if y else (1 - h) / 2
    y = y - 0.015
    if res:
        spad = DropDown(
            name,
            spawn,
            match=Match(wm_class=res),
            width=w,
            height=h,
            x=x,
            y=y,
            opacity=opacity,
            on_focus_lost_hide=autohide,
        )
    else:
        spad = DropDown(
            name,
            spawn,
            width=w,
            height=h,
            x=x,
            y=y,
            opacity=opacity,
            on_focus_lost_hide=autohide,
        )
    return spad


DROPTERM = "/bin/bash .config/qtile/scripts/drop_down.sh"
NOTES = "/bin/bash .config/qtile/scripts/notes.sh"
POMO = "pomotroid --no-sandbox"
MTERM = "/bin/bash .config/qtile/scripts/master_term.sh"

APP_PATH = os.path.expanduser("~/.local/share/applications/")
file = [file for file in os.listdir(APP_PATH) if "brave" in file]
TEAMS = None
if file:
    target = file[0]
    target = os.path.join(APP_PATH, target)
    TEAMS = (
        subprocess.check_output(f'cat {target}|grep "Exec="|grep -oE "/.*"', shell=True)
        .decode("latin")
        .strip()
    )

AIBOARD = "python projects/interact/main.py"

spads = [
    scratchgen("term", DROPTERM, 0.4, 0.9, None, 0, True, "termdrop"),
    scratchgen("fman", FILEMAN, 0.9, 0.84, res="dolphin"),
    scratchgen("passman", "keepassxc", 0.8, 0.6, res="keepassxc"),
    scratchgen("mailclient", "thunderbird", 0.8, 0.6, res="thunderbird"),
    scratchgen("discord", "discord", 0.9, 0.84, res="discord"),
    scratchgen("scratch_term", MTERM, 0.9, 0.84, res="Vterm"),
    scratchgen("aidboard", AIBOARD, 0.9, 0.84, res="flet"),
    scratchgen("notes", NOTES, 0.9, 0.55, 0.44, None, res="kittynotes"),
    scratchgen(
        "videoplayer",
        "mpv --player-operation-mode=pseudo-gui",
        0.9,
        0.84,
        None,
        None,
        res="mpv",
    ),
    scratchgen("tgram", "telegram-desktop", 0.8, 0.6, res="telegram-desktop"),
    (
        scratchgen("teams", TEAMS, 0.8, 0.6, res="crx_cifhbcnohmdccbgoicgdjpfamggdegmo")
        if TEAMS
        else None
    ),
    scratchgen("weston", "weston", 0.98, 0.25, x=0.75, y=0.015, res="weston-1"),
    scratchgen("pomo", POMO, 0.4, 0.2),
    scratchgen(
        "sprod",
        "Applications/superProductivity-7.11.5.AppImage",
        0.9,
        0.84,
        res="superproductivity",
    ),
    scratchgen("openrgb", "openrgb", 0.5, 0.3, 0.656, 0.015, autohide=True),
    scratchgen("mixer", "pavucontrol", 0.5, 0.3, 0.7, 0.015, autohide=True),
    scratchgen("btooth", "blueman-manager", 0.5, 0.3, 0.7, 0.015, autohide=True),
    scratchgen("network", "nm-connection-editor", 0.5, 0.3, 0.7, 0.015, autohide=True),

]

spad_keys = [
    Key([], "F12", lazy.group["scratchpad"].dropdown_toggle("term")),
    Key(["control"], "semicolon", lazy.group["scratchpad"].dropdown_toggle("scratch_term")),
    Key([MOD], "h", lazy.group["scratchpad"].dropdown_toggle("scratch_term")),
    Key([MOD], "r", lazy.group["scratchpad"].dropdown_toggle("scratch_term")),
    # Key(["control"], 48, lazy.group["scratchpad"].dropdown_toggle("scratch_term")),
    Key([MOD], "F3", lazy.group["scratchpad"].dropdown_toggle("teams")),
    Key([MOD], "d", lazy.group["scratchpad"].dropdown_toggle("discord")),
    Key([MOD], "e", lazy.group["scratchpad"].dropdown_toggle("fman")),
    Key([MOD], "m", lazy.group["scratchpad"].dropdown_toggle("mailclient")),
    Key([MOD], "n", lazy.group["scratchpad"].dropdown_toggle("notes")),
    Key([MOD], "p", lazy.group["scratchpad"].dropdown_toggle("passman")),
    # Key([MOD], "r", lazy.group["scratchpad"].dropdown_toggle("videoplayer")),
    Key([MOD], "t", lazy.group["scratchpad"].dropdown_toggle("tgram")),
    # Key([MOD], "i", lazy.group["scratchpad"].dropdown_toggle("pomo")),
    Key([MOD], "0", lazy.group["scratchpad"].dropdown_toggle("sprod")),
    # Key([MOD], "u", lazy.group["scratchpad"].dropdown_toggle("weston")),
    KeyChord(
        [],
        "F10",
        [
            Key([], "b", lazy.group["scratchpad"].dropdown_toggle("btooth")),
            Key([], "n", lazy.group["scratchpad"].dropdown_toggle("network")),
            Key([], "o", lazy.group["scratchpad"].dropdown_toggle("mixer")),
            Key([], "r", lazy.group["scratchpad"].dropdown_toggle("openrgb")),
        ],
        # mode=True,
        name="Utils [B N O R]",
    ),
    Key([MOD], "i", lazy.group["scratchpad"].dropdown_toggle("aidboard")),
]
# spads = []
# spad_keys = []

# lazy.group["scratchpad"].dropdown_toggle("network"),
