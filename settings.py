"""
Settings
"""
import os
from subprocess import check_output

# pylint: disable=C0103
MOD = "mod4"
TERMINAL = "kitty"
BROWSER = "firefox"
FILEMAN = "dolphin"
WALL_PATH = os.path.expanduser("~/Pictures/wallpapers/")

IS_DESKTOP = b"base" in check_output("hostname")

SCREEN_LOCK_CMD = ".config/qtile/scripts/lock.sh"
LAUNCHER_CMD = ".config/rofi/launchers/misc/launcher.sh"
NOTIFICATION_CENTER_CMD = "sh .config/qtile/scripts/notification_toggle.sh"

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True  # Allow windows to automatically minimize
wmname = "LG3D"  # Helps with Java stuff
# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# Things that start when you login with qtile
AUTO_START_ONCE = {
    "daemon": [
        "picom",
        "nm-applet",
        "lxqt-policykit-agent",
        # "syncthing",
        "deadd-notification-center",
        "kdeconnect-indicator",
        # "sunshine",
    ],
    "cmd": [
        "tmux start-server",
        "tmux new-session -d",
        "xfce4-power-manager --daemon",
        "xfce4-power-manager",
        # "barrier",
        # "cd ~/blog/; mkdocs serve",
    ],
}

# things that run every time qtile is started/restarted
AUTO_START_ALWAYS = {
    "daemon": [],
    "cmd": [
        "sh projects/capsmap.sh",
        "sh .config/qtile/scripts/desktop_autostart.sh" if IS_DESKTOP else "ls"
    ],
}
