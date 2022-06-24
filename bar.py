"""
BAR
"""
from libqtile import bar, widget
from colors import theme

custom_bar = bar.Bar(
    [
        widget.GroupBox(),
        widget.CurrentLayout(),
        widget.Prompt(),
        widget.WindowName(),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.Battery(
            charge_char="⚡",
            discharge_char=" ",
            full_char=" ",
            notify_below=25,
            # background=theme["green"],
        ),
        widget.Net(
            interface="wlp0s20f3", format="{down} ↓↑{up}", background=theme["red"]
        ),
        widget.CPU(),
        widget.Systray(),
        widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
    ],
    16,
    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
    background=theme["bg"],
)
