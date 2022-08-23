"""
Keybindings
"""

from libqtile.config import Key, Click, Drag
from libqtile.lazy import lazy
from settings import MOD, TERMINAL, BROWSER

MOD_S = [MOD, "shift"]
MOD_C = [MOD, "control"]

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
    Key(MOD_S, "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key(MOD_S, "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key(MOD_S, "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key(MOD_S, "k", lazy.layout.shuffle_up(), desc="Move window up"),
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
    Key(MOD_S, "Return", lazy.layout.toggle_split(), desc="Toggle split/unsplit"),
    # Toggle between different layouts as defined below
    Key([MOD], "space", lazy.next_layout(), desc="Toggle between layouts"),
    # Misc
    Key([MOD], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(MOD_C, "r", lazy.reload_config(), desc="Reload the config"),
    Key(MOD_C, "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([MOD], "f", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen"),
    Key(MOD_C, "f", lazy.window.toggle_floating(), desc="Toggle Floating"),
    # Applaunch
    Key([MOD], "Return", lazy.spawn(TERMINAL), desc="Launch terminal"),
    Key([MOD], "b", lazy.spawn(BROWSER), desc=f"Launch {BROWSER}"),
    Key([MOD], "c", lazy.spawn(".config/qtile/scripts/lock.sh"), desc="Lock Screen"),
    Key(
        ["mod1"],
        "space",
        lazy.spawn(".config/rofi/launchers/misc/launcher.sh"),
        desc="Spawn a command using a prompt widget",
    ),
    # Media Keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    # Brightness control
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10%")),
    Key([], "Print", lazy.spawn("flameshot gui")),
    Key([MOD], "Print", lazy.spawn("flameshot full")),
    # Notification Center
    Key([MOD], "y", lazy.spawn("sh .config/qtile/scripts/notification_toggle.sh")),
    Key([MOD], "v", lazy.spawn("sh .config/qtile/scripts/multi_monitor.sh")),
]

# Drag floating layouts.
mouse = [
    Drag(
        [MOD],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [MOD], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]
