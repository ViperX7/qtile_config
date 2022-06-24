"""
Groups
"""

from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy
from settings import TERMINAL, MOD

groups = [
    Group("1", None, False, TERMINAL, "column", label="१"),
    Group("2", [Match(wm_class="firefox")], False, [], "max", label="२"),
    Group("3", None, False, [], "column", label="३"),
    Group("4", None, False, [], "column", label="४"),
    Group("5", None, False, [], "column", label="५"),
    Group("6", None, False, [], "column", label="६"),
    Group("7", None, False, [], "column", label="७"),
    Group("8", None, False, [], "column", label="८"),
    Group("9", None, False, [], "column", label="९"),
]

group_keys = []
for i in groups:
    nm = i.name
    # mod1 + letter of group = switch to group
    gpk = [
        Key([MOD], nm, lazy.group[nm].toscreen(), desc=f"Switch to group {nm}"),
        Key(
            [MOD, "shift"],
            nm,
            lazy.window.togroup(nm),
            desc=f"move focused window to group {nm}",
        ),
    ]
    group_keys.extend(gpk)
