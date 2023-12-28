"""
Keybindings
"""
from subprocess import check_output

from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy
from settings import (BROWSER, LAUNCHER_CMD, MOD, NOTIFICATION_CENTER_CMD,
                      SCREEN_LOCK_CMD, TERMINAL)

MOD_S = [MOD, "shift"]
MOD_C = [MOD, "control"]
ALT = ["mod1"]


def is_kero_connected():
    """
    returns true if specific keyboard is connected
    """
    return b"Kreo" in check_output("lsusb")


VOL_CMD = "pactl set-sink-volume @DEFAULT_SINK@"
VOL_UP_CMD = f'{VOL_CMD} {"-" if is_kero_connected() else "+"}5%'
VOL_DOWN_CMD = f'{VOL_CMD} {"+" if is_kero_connected() else "-"}5%'

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([MOD], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD], "j", lazy.layout.down(), desc="Move focus down"),
    Key([MOD], "k", lazy.layout.up(), desc="Move focus up"),
    Key(["mod1"], "Tab", lazy.layout.next(), desc="Focus next window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(MOD_S, "h", lazy.layout.shuffle_left(), desc="window to ->"),
    Key(MOD_S, "l", lazy.layout.shuffle_right(), desc="window to <-"),
    Key(MOD_S, "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key(MOD_S, "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([MOD], "equal",lazy.screen.next_group(skip_empty=False) , desc="Move window up"),
    Key([MOD], "minus",lazy.screen.prev_group(skip_empty=False) , desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(MOD_C, "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(MOD_C, "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key(MOD_C, "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key(MOD_C, "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([MOD], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(MOD_S, "Return", lazy.layout.toggle_split(), desc="lock window"),
    # Toggle between different layouts as defined below
    Key([MOD], "space", lazy.next_layout(), desc="next layouts"),
    Key(MOD_C, "space", lazy.prev_layout(), desc="prev layouts"),
    # Misc
    Key([MOD], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(MOD_C, "r", lazy.reload_config(), desc="Reload the config"),
    Key(MOD_C, "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([MOD], "f", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen"),
    Key(MOD_C, "f", lazy.window.toggle_floating(), desc="Toggle Floating"),
    # Applaunch
    Key([MOD], "Return", lazy.spawn(TERMINAL), desc="Launch terminal"),
    Key([MOD], "b", lazy.spawn(BROWSER), desc=f"Launch {BROWSER}"),
    Key([MOD], "HOME", lazy.spawn("firefox --private-window")),
    Key([MOD], "c", lazy.spawn(SCREEN_LOCK_CMD), desc="Lock Screen"),
    Key(ALT, "space", lazy.spawn(LAUNCHER_CMD), desc="Show Launcher"),
    # Media Keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn(VOL_UP_CMD)),
    Key([], "XF86AudioLowerVolume", lazy.spawn(VOL_DOWN_CMD)),
    Key([], "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioMicMute", lazy.spawn("amixer set Capture toggle")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([MOD], "semicolon", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    # Brightness control
    # Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5%")),
    # Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10%")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 10")),
    Key([], "XF86PowerOff", lazy.spawn("/bin/systemctl suspend")),
    Key([], "Print", lazy.spawn("flameshot gui")),
    Key([MOD], "Print", lazy.spawn("flameshot full")),
    # Key(MOD_S, "s", lazy.spawn("flameshot gui")),
    Key([MOD], "s", lazy.spawn("sh .config/qtile/scripts/screen_read.sh")),

    # Notification Center
    Key([MOD], "y", lazy.spawn(NOTIFICATION_CENTER_CMD)),
    Key([MOD], "v", lazy.spawn("sh .config/qtile/scripts/multi_monitor.sh")),

    # Move focus to screens
    Key([MOD], "F1", lazy.to_screen(0), desc="Move focus to screen 0"),
    Key([MOD], "F2", lazy.to_screen(1), desc="Move focus to screen 1"),
    Key([MOD], "F3", lazy.to_screen(2), desc="Move focus to screen 2"),
]

# Drag floating layouts.
mouse = [
    Drag(
        [MOD],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag([MOD],
         "Button3",
         lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]
