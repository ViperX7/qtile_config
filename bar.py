"""
BAR
"""
import os
import libqtile

from colors import catppuccin, theme
from libqtile import bar, lazy
from libqtile.widget import (CPU, Battery, Chord, Clock, CurrentLayout,
                              GroupBox, Memory, Net, Notify,
                             Prompt, Sep, Systray, TaskList, TextBox,Chord,
                             WindowName)
from settings import IS_DESKTOP

GREY = theme["base"]
DARK_GREY = "#111111"
BLUE = "#007fdf"
DARK_BLUE = "#002a4a"
ORANGE = "#dd6600"
DARK_ORANGE = "#371900"
BAR_CUT_OUT_SIZE = 38 if IS_DESKTOP else 45


def init_widgets():
    """widgets initialiser"""

    widgets = []
    left_widget_group = [
        CurrentLayout(scale=0.6, padding=8, mode="icon"),
        Chord(),
        GroupBox(
            fontsize=10,
            padding=4,
            borderwidth=1,
            urgent_border=DARK_BLUE,
            disable_drag=True,
            highlight_method="block",
            this_screen_border=DARK_BLUE,
            other_screen_border=DARK_ORANGE,
            this_current_screen_border=BLUE,
            other_current_screen_border=ORANGE,
        ),
        # GlobalMenu(background="red")
    ]

    clock = [
        Clock(
            format="%I:%M %p",
            background="#282738",
            foreground="#CAA9E0",
            font="JetBrains Mono Bold",
            fontsize=12,
        ),
        TextBox(
            "",
            fontsize=18,
            background="#282738",
            foreground="#CAA9E0",
            padding=4,
        ),
        Clock(
            format=" %a %b %d",
            background="#282738",
            foreground="#CAA9E0",
            font="JetBrains Mono Bold",
            fontsize=12,
        ),
    ]


    battery = [
        # TextBox(
        #     text="◤",
        #     fontsize=BAR_CUT_OUT_SIZE,
        #     padding=-2,
        #     foreground=DARK_GREY,
        #     background=catppuccin["sapphire"],
        # ),
        Battery(
            format=" {char} {percent:2.0%} ",
            charge_char="⚡",
            discharge_char="🔋",
            full_char="⚡",
            unknown_char="⚡",
            empty_char="⁉️ ",
            update_interval=2,
            show_short_text=False,
            default_text="",
            notify_below=50,
        ),
        Battery(
                fmt="<span color='#eee'>{}</span> ",
                format="{hour:d}:{min:02d}",
                update_interval=2,
                show_short_text=True,
                default_text="",
            ),
    ]

    post_tray_widgets = [
        CPU(
            format=
            "<span color='#452342'>  {freq_current}GHz {load_percent}%</span>",
            update_interval=2,
            background=catppuccin["green"],
        ),
        TextBox(
            text="◥",
            fontsize=BAR_CUT_OUT_SIZE,
            padding=-2,
            foreground=catppuccin["peach"],
            background=catppuccin["green"],
        ),
        Memory(
            format=
            "<span color='#114477'></span> {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}",
            update_interval=2,
            background=catppuccin["peach"],
            foreground=catppuccin["base"],
        ),
        TextBox(
            text="◥",
            fontsize=BAR_CUT_OUT_SIZE,
            padding=-1.5,
            foreground=catppuccin["pink"],
            background=catppuccin["peach"],
        ),
        Net(
            format=" {up}  {down} ",
            background=catppuccin["pink"],
            foreground=catppuccin["base"],
        )
    ]

    widgets += left_widget_group
    widgets += [
        TextBox(text="◤",
                fontsize=BAR_CUT_OUT_SIZE,
                padding=-1,
                foreground=DARK_GREY,
                background=GREY),
        WindowName(
            borderwidth=0,
            highlight_method="block",
            background=GREY,
            border=DARK_GREY,
            urgent_border=DARK_BLUE,
            markup_floating="<i>{}</i>",
            markup_minimized="<s>{}</s>",
        ),
        TextBox(
            text="◥",
            fontsize=BAR_CUT_OUT_SIZE,
            padding=-2,
            foreground=catppuccin["green"],
            background=GREY,
        ),]

    widgets += post_tray_widgets

    widgets += [

        TextBox(
            text="◥",
            fontsize=BAR_CUT_OUT_SIZE,
            padding=-1.5,
            foreground=catppuccin["blue"],
            background=catppuccin["pink"],
        ),
        # Systray(background=catppuccin["blue"]),
        TextBox(
            text="◤",
            fontsize=BAR_CUT_OUT_SIZE,
            padding=-2,
            foreground=catppuccin["blue"],
            background=DARK_GREY,
        ),
        # Notify(fmt=" 🔥 {} "),
        # PulseVolume(fmt=" {}", emoji=True, volume_app="pavucontrol"),
        # PulseVolume(volume_app="pavucontrol"),
    ]
    # widgets+= [Bluetooth()]
    widgets += battery if os.path.isdir("/sys/module/battery") and not IS_DESKTOP else []
    widgets += clock


    return widgets


custom_bar = bar.Bar(
    init_widgets(),
    16,
    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
    background=theme["base"],
)
