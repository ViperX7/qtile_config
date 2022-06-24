"""
Qtile Config
"""


from os import listdir
from random import choice as rand_choice
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Key, Match, Screen, ScratchPad
from libqtile.lazy import lazy
from colors import onedark as theme
from settings import TERMINAL,BROWSER,MOD,WALL_PATH
from q_scratchpads import spads, spad_keys
from q_groups import groups, group_keys


MOD_S = [MOD,"shift"]
MOD_C = [MOD,"control"]

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
    Key(MOD_S,"Return",lazy.layout.toggle_split(),desc="Toggle split/unsplit"),
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
    Key([MOD], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]



# Append scratchpad with dropdowns to groups
groups.append(ScratchPad('scratchpad', spads))
keys.extend(spad_keys) # extend keys list with keybinding for scratchpad
keys.extend(group_keys)

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=1),
    layout.Max(),
    layout.MonadTall(),
    layout.Zoomy(),
    layout.Floating(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
]

widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
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
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
            ],
            16,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            background = theme["bg"],
        ),
        wallpaper = WALL_PATH + rand_choice(listdir(WALL_PATH)),
        wallpaper_mode = "fill",
    ),
]

# Drag floating layouts.
mouse = [
    Drag([MOD], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([MOD], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
