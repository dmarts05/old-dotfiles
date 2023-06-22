import os
import subprocess

from colors import colors
from screens import screens

from libqtile.config import (
    # KeyChord,
    Key,
    # Screen,
    Group,
    Drag,
    Click,
    # ScratchPad,
    # DropDown,
    Match,
)
from libqtile import extension
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
# from libqtile import qtile
# from typing import List  # noqa: F401
from custom.bsp import Bsp as CustomBsp
from custom.bsp import Bsp as CustomBspMargins
from custom.zoomy import Zoomy as CustomZoomy
# from custom.stack import Stack as CustomStack
# from custom.windowname import WindowName as CustomWindowName

mod = "mod4"
terminal = "alacritty"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.spawn("shutdown now")),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "space", lazy.spawn("./.config/rofi/launchers/colorful/launcher.sh")),

    # Power Menu
    ([mod], "x", lazy.spawn("./.config/rofi/powermenu/powermenu.sh")),

    # Browser
    ([mod], "b", lazy.spawn("brave")),

    # File Explorer
    ([mod], "e", lazy.spawn("thunar")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 4600")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "s", lazy.spawn("flameshot gui")),

    # Visual Studio Code
    ([mod], "v", lazy.spawn("code")),

    # Discord
    ([mod], "d", lazy.spawn("discord")),

    # Spotify
    ([mod], "m", lazy.spawn("env LD_PRELOAD=/usr/lib/spotify-adblock.so spotify %U")),

    # ------------ Hardware Configs ------------

    # Audio
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
    ([], "XF86AudioPlay", lazy.spawn(
        "playerctl play-pause"
    )),
    ([], "XF86AudioNext", lazy.spawn(
        "playerctl next"
    )),
    ([], "XF86AudioPrev", lazy.spawn(
        "playerctl previous"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]

# Command to find out wm_class of window: xprop | grep WM_CLASS
workspaces = [
    {
        "name": "1",
        "key": "1",
        "label": "",
        "layout": "monadtall",
        "matches": [
            Match(wm_class=""),
        ],
        "spawn": [],
    },
    {
        "name": "2",
        "key": "2",
        "label": "",
        "layout": "monadtall",
        "matches": [
            Match(wm_class=""),
        ],
        "spawn": [],
    },
    {
        "name": "3",
        "key": "3",
        "label": "",
        "layout": "monadtall",
        "matches": [
            Match(wm_class=""),
        ],
        "spawn": [],
    },
    {
        "name": "4",
        "key": "4",
        "label": "",
        "layout": "monadtall",
        "matches": [
            Match(wm_class=""),
        ],
        "spawn": [],
    },
    {
        "name": "5",
        "key": "5",
        "label": "",
        "layout": "monadtall",
        "matches": [
            Match(wm_class=""),
        ],
        "spawn": [],
    },
    {
        "name": "6",
        "key": "6",
        "label": "",
        "layout": "monadtall",
        "matches": [
            Match(wm_class=""),
        ],
        "spawn": [],
    },
    {
        "name": "7",
        "key": "7",
        "label": "",
        "layout": "monadtall",
        "matches": [
            Match(wm_class=""),
        ],
        "spawn": [],
    },
    {
        "name": "8",
        "key": "8",
        "label": "",
        "layout": "monadtall",
        "matches": [
            Match(wm_class=""),
        ],
        "spawn": [],
    },
    {
        "name": "9",
        "key": "9",
        "label": "",
        "layout": "monadtall",
        "matches": [
            Match(wm_class=""),
        ],
        "spawn": [],
    },
]

groups = []
for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    groups.append(
        Group(
            workspace["name"],
            matches=matches,
            layout=workspace["layout"],
            spawn=workspace["spawn"],
            label=workspace["label"],
        )
    )
    keys.append(
        Key(
            [mod],
            workspace["key"],
            lazy.group[workspace["name"]].toscreen(),
            desc="Focus certain workspace",
        )
    )
    keys.append(
        Key(
            [mod, "shift"],
            workspace["key"],
            lazy.window.togroup(workspace["name"]),
            desc="Move focused window to another workspace",
        )
    )

layout_theme = {
    "border_width": 3,
    "margin": 5,
    "border_focus": "88c0d0",
    "border_normal": "3b4252",
    "font": "Ubuntu Mono Nerd Font",
    "grow_amount": 4,
}

layout_theme_margins = {
    "name": "bsp-margins",
    "border_width": 3,
    "margin": [150, 300, 150, 300],
    "border_focus": "88c0d0",
    "border_normal": "3b4252",
    "font": "Ubuntu Mono Nerd Font",
    "grow_amount": 4,
}

layout_audio = {
    "name": "monadwide-audio",
    "border_width": 3,
    "margin": 100,
    "border_focus": "88c0d0",
    "border_normal": "3b4252",
    "font": "Ubuntu Mono Nerd Font",
    "ratio": 0.65,
    "new_client_position": "after_current",
}

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=colors[8][0],
    border_normal=colors[2][0],
    border_width=3
)

layouts = [
    # layout.MonadWide(**layout_audio),
    # layout.Bsp(**layout_theme, fair=False),
    # CustomBsp(**layout_theme, fair=False),
    # layout.Columns(
    #    **layout_theme,
    #    border_on_single=True,
    #    num_columns=3,
    #    # border_focus_stack=colors[2],
    #    # border_normal_stack=colors[2],
    #    split=False,
    # ),
    layout.MonadTall(**layout_theme),
    layout.MonadTall(**layout_theme, align=1),
    layout.RatioTile(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme, columns=3),
    CustomZoomy(**layout_theme),
    # layout.Slice(**layout_theme),
    # layout.TreeTab(
    #    **layout_theme,
    #    active_bg=colors[14],
    #    active_fg=colors[1],
    #    bg_color=colors[0],
    #    fontsize=16,
    #    inactive_bg=colors[0],
    #    inactive_fg=colors[1],
    #    sections=["TreeTab", "TreeTab2"],
    #    section_fontsize=18,
    #    section_fg=colors[1],
    # ),
    # layout.Max(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.Floating(**layout_theme),
    # CustomBspMargins(**layout_theme_margins),
]

# Setup bar

widget_defaults = dict(
    font="JetBrainsMono Nerd Font Mono Medium", fontsize=18, padding=3, background=colors[0]
)
extension_defaults = widget_defaults.copy()


# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click(
        [mod, "shift"], "Button2", lazy.window.bring_to_front()
    ),
    Click(
        [mod], "Button2", lazy.window.toggle_floating()
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = "floating_only"
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "urgent"


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
