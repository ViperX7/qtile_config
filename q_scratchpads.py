"""
Scratchpads
"""

from libqtile.config import DropDown, Key, Match
from libqtile.lazy import lazy
from settings import TERMINAL, FILEMAN, MOD


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


DROPTERM = TERMINAL + " --class termdrop"
spads = [
    scratchgen("term", DROPTERM, 0.4, 0.9, None, 0, True, "termdrop"),
    scratchgen("fman", FILEMAN, 0.9, 0.84, res="dolphin"),
    scratchgen("passman", "keepassxc", 0.8, 0.6, res="keepassxc"),
    scratchgen("discord", "discord", 0.9, 0.84, res="discord"),
    scratchgen("tgram", "telegram-desktop", 0.8, 0.6, res="telegram-desktop"),
    scratchgen("weston", "weston", 0.98, 0.25, x=0.75, y=0.015, res="weston-1"),
    scratchgen("mixer", "pavucontrol", 0.5, 0.3, 0.7, 0.015, autohide=True),
    # DropDown('pomo', 'pomotroid', x=0.4, y=0.2, opacity=1),
]

spad_keys = [
    Key([], "F12", lazy.group["scratchpad"].dropdown_toggle("term")),
    Key([MOD], "e", lazy.group["scratchpad"].dropdown_toggle("fman")),
    Key([MOD], "p", lazy.group["scratchpad"].dropdown_toggle("passman")),
    Key([MOD], "d", lazy.group["scratchpad"].dropdown_toggle("discord")),
    Key([MOD], "t", lazy.group["scratchpad"].dropdown_toggle("tgram")),
    Key([MOD], "u", lazy.group["scratchpad"].dropdown_toggle("weston")),
    Key([MOD], "o", lazy.group["scratchpad"].dropdown_toggle("mixer")),
]
