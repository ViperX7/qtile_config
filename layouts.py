"""
layouts
"""
from libqtile import layout
from libqtile.config import Match
from libqtile.layout import Columns, Floating, Max, MonadTall, Zoomy

layouts = [
    layout.MonadThreeCol(
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=1,
        ratio=0.6,
    ),
    layout.Stack(num_stacks=3,
                 border_focus_stack=["#d75f5f", "#8f3d3d"],
                 border_width=1),
    Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=1),
    Max(),
    Zoomy(),
    # MonadTall(),
    Floating(),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
]

floating_layout = Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class="confirmreset"),  # gitk
    Match(wm_class="flet"),
    Match(wm_class="Flet"),
    Match(wm_class="winapps"),  # gitk
    Match(wm_class="makebranch"),  # gitk
    Match(wm_class="maketag"),  # gitk
    Match(wm_class="ssh-askpass"),  # ssh-askpass
    Match(title="branchdialog"),  # gitk
    Match(title="pinentry"),  # GPG key password entry
    Match(title="flameshot"),  # GPG key password entry
])
