"""
BAR
"""
import os
from libqtile import bar
from libqtile.widget import (
    GroupBox,
    CurrentLayout,
    CurrentLayoutIcon,
    Prompt,
    WindowName,
    Chord,
    Battery,
    Net,
    CPU,
    Memory,
    Systray,
    Clock,
    PulseVolume,
    TextBox,
    TaskList,
    Notify,
    Sep,
)
from colors import theme, nord_fox

GREY = theme["bg"]
DARK_GREY = "#111111"
BLUE = "#007fdf"
DARK_BLUE = "#002a4a"
ORANGE = "#dd6600"
DARK_ORANGE = "#371900"


def init_widgets():
    """widgets initialiser"""
    widgets = [
        CurrentLayoutIcon(scale=0.6, padding=8),
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
        TextBox(
            text="◤", fontsize=45, padding=-1, foreground=DARK_GREY, background=GREY
        ),
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
            fontsize=45,
            padding=-2,
            foreground=nord_fox["green"],
            background=GREY,
        ),
        CPU(
            format="<span color='#452342'>  {freq_current}GHz {load_percent}%</span>",
            update_interval=2,
            background=nord_fox["green"],
        ),
        TextBox(
            text="◥",
            fontsize=45,
            padding=-2,
            foreground=nord_fox["orange"],
            background=nord_fox["green"],
        ),
        Memory(
            format="<span color='#114477'></span> {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}",
            update_interval=2,
            background=nord_fox["orange"],
        ),
        TextBox(
            text="◥",
            fontsize=45,
            padding=-1.5,
            foreground=nord_fox["pink"],
            background=nord_fox["orange"],
        ),
        Net(format="{down}   {up}", background=nord_fox["pink"]),
        TextBox(
            text="◥",
            fontsize=45,
            padding=-1.5,
            foreground=nord_fox["blue"],
            background=nord_fox["pink"],
        ),
        Systray(background=nord_fox["blue"]),
        TextBox(
            text="◤",
            fontsize=45,
            padding=-2,
            foreground=nord_fox["blue"],
            background=DARK_GREY,
        ),
        Notify(fmt=" 🔥 {} "),
        # PulseVolume(fmt=" {}", emoji=True, volume_app="pavucontrol"),
        TextBox(
            text="◤",
            fontsize=45,
            padding=-2,
            foreground=DARK_GREY,
            background=nord_fox["cyan"],
        ),
        # PulseVolume(volume_app="pavucontrol"),
        Clock(
            format="<span color='#222'> ⏱ %H:%M  %A %d-%m-%Y</span>  ",
            background=nord_fox["cyan"],
        ),
    ]
    if os.path.isdir("/sys/module/battery"):
        widgets.insert(
            -2,
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
        )
        widgets.insert(
            -2,
            Battery(
                fmt="<span color='#eee'>{}</span> ",
                format="{hour:d}:{min:02d}",
                update_interval=2,
                show_short_text=True,
                default_text="",
            ),
        )
    return widgets


widgets = init_widgets()
custom_bar = bar.Bar(
    widgets,
    16,
    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
    background=theme["bg"],
)
