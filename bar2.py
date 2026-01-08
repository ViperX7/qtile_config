"""
BAR
"""
import os

from colors import catppuccin, theme
from libqtile import bar, lazy, qtile
from libqtile.widget import (CPU, Battery, BatteryIcon, Chord, Clock,
                             CurrentLayout, GroupBox, Image,
                             Memory, Net, Notify, Prompt, Sep, Spacer, Systray,
                             TaskList, TextBox, Volume, WindowName)
from settings import IS_DESKTOP


def search():
    qtile.cmd_spawn("rofi -show drun")


def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")


FONT_SIZE = 12
ICON_SIZE = 16

BAR = bar.Bar(
    [
        TextBox(
            text="\ue0b6",
            background="#00000000",
            foreground="#282738",
            padding=0,
            fontsize=24,
        ),
        Image(
            filename="~/.config/qtile/Assets/launch_Icon.png",
            margin=2,
            background="#282738",
            mouse_callbacks={"Button1": power},
        ),
        Image(filename="~/.config/qtile/Assets/6.png", ),
        GroupBox(
            fontsize=FONT_SIZE,
            borderwidth=3,
            highlight_method="block",
            active="#CAA9E0",
            block_highlight_text_color="#91B1F0",
            highlight_color="#4B427E",
            inactive="#282738",
            foreground="#4B427E",
            background="#353446",
            this_current_screen_border="#353446",
            this_screen_border="#353446",
            other_current_screen_border="#353446",
            other_screen_border="#353446",
            urgent_border="#353446",
            rounded=True,
            disable_drag=True,
        ),
        Spacer(
            length=8,
            background="#353446",
        ),
        Image(filename="~/.config/qtile/Assets/1.png", ),
        Image(filename="~/.config/qtile/Assets/layout.png",
              background="#353446"),
        CurrentLayout(
            background="#353446",
            foreground="#CAA9E0",
            fmt="{}",
            font="JetBrains Mono Bold",
            fontsize=FONT_SIZE,
            # mode="both"
        ),
        Image(filename="~/.config/qtile/Assets/5.png", ),
        Image(
            filename="~/.config/qtile/Assets/search.png",
            margin=2,
            background="#282738",
            mouse_callbacks={"Button1": search},
        ),
        TextBox(
            fmt="Search",
            background="#282738",
            font="JetBrains Mono Bold",
            fontsize=FONT_SIZE,
            foreground="#CAA9E0",
            mouse_callbacks={"Button1": search},
        ),
        Image(filename="~/.config/qtile/Assets/4.png", ),
        WindowName(
            background="#353446",
            format="{name}",
            font="JetBrains Mono Bold",
            foreground="#CAA9E0",
            empty_group_string="Desktop",
            fontsize=FONT_SIZE,
        ),
        Image(filename="~/.config/qtile/Assets/3.png", ),
        TextBox(
            text=" ",
            background="#282738",
        ),
        # Image(
        #     filename="~/.config/qtile/Assets/6.png",
        #     background="#353446",
        # ),
        # Image(filename="~/.config/qtile/Assets/Drop1.png", ),
        Net(
            format=" {up}   {down} ",
            # background="#353446",
            background="#282738",
            foreground="#CAA9E0",
            font="JetBrains Mono Bold",
            prefix="k",
        ),
        Image(filename="~/.config/qtile/Assets/6.png", ),
        TextBox(
            " ",
            fontsize=ICON_SIZE,
            background="#353446",
            foreground="#CAA9E0",
            padding=4,
        ),
        CPU(
            format=
            "{freq_current}GHz {load_percent}%",
            update_interval=2,
            background="#353446",
            foreground="#CAA9E0",
        ),
        Image(filename="~/.config/qtile/Assets/2.png", ),
        # Spacer(
        #   # length=8,
        #   # background='#353446',
        # ),
        Image(
            filename="~/.config/qtile/Assets/Misc/ram.png",
            background="#353446",
        ),
        Spacer(
            length=2,
            background="#353446",
        ),
        Memory(
            background="#353446",
            # format="{MemUsed: .0f}{mm}",
            format="{MemPercent: .0f}%",
            foreground="#CAA9E0",
            font="JetBrains Mono Bold",
            fontsize=FONT_SIZE,
            update_interval=5,
        ),
        Image(filename='~/.config/qtile/Assets/Drop2.png', ),
        Image(filename="~/.config/qtile/Assets/2.png", ),
        Spacer(
            length=8,
            background="#353446",
        ),
        Systray(
            background='#353446',
            fontsize=2,
        ),

        # BatteryIcon(
        #     theme_path="~/.config/qtile/Assets/Battery/",
        #     background="#353446",
        #     scale=1,
        # ),
        # Battery(
        #     font="JetBrains Mono Bold",
        #     background="#353446",
        #     foreground="#CAA9E0",
        #     format="{percent:2.0%}",
        #     fontsize=13,
        # ),
        Image(filename="~/.config/qtile/Assets/2.png", ),
        Spacer(
            length=8,
            background="#353446",
        ),
        # Battery(format=' {percent:2.0%}',
        # font="JetBrains Mono ExtraBold",
        # fontsize=12,
        # padding=10,
        # background='#353446',
        # ),
        # Memory(format='{MemUsed: .0f}{mm}',
        # font="JetBrains Mono Bold",
        # fontsize=12,
        # padding=10,
        # background='#4B4D66',
        # ),
        Volume(
            font="JetBrainsMono Nerd Font",
            theme_path="~/.config/qtile/Assets/Volume/",
            emoji=True,
            fontsize=ICON_SIZE,
            background="#353446",
        ),
        Spacer(
            length=-5,
            background="#353446",
        ),
        Volume(
            font="JetBrains Mono Bold",
            background="#353446",
            foreground="#CAA9E0",
            fontsize=FONT_SIZE,
        ),
        Image(
            filename="~/.config/qtile/Assets/5.png",
            background="#353446",
        ),
        Clock(
            format="%I:%M %p",
            background="#282738",
            foreground="#CAA9E0",
            font="JetBrains Mono Bold",
            fontsize=FONT_SIZE,
        ),
        TextBox(
            "",
            fontsize=ICON_SIZE,
            background="#282738",
            foreground="#CAA9E0",
            padding=4,
        ),
        Clock(
            format=" %a %b %d",
            background="#282738",
            foreground="#CAA9E0",
            font="JetBrains Mono Bold",
            fontsize=FONT_SIZE,
        ),
        TextBox(
            text="\ue0b4",
            background="#00000000",
            foreground="#282738",
            padding=0,
            fontsize=24,
        ),
    ],
    20,
    border_color="#282738",
    border_width=[0, 0, 0, 0],
    margin=[0, 16, 0, 16],
)
