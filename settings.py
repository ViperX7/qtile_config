"""
Settings
"""

from subprocess import check_output

# pylint: disable=C0103
MOD = "mod4"
TERMINAL = "kitty"
BROWSER = "firefox"
FILEMAN = "dolphin"
WALL_PATH = "Pictures/wallpapers/"

IS_DESKTOP = "base" in check_output("cat /etc/hostname".split(" ")).decode("latin")

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
