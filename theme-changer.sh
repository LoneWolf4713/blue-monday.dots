#!/bin/bash
echo "HUMME BUALAYA KYA"

swaybg -o \* -i $1 -m fill &
wal -i $1

pywalfox update

python ~/github/pywal_cava/wal_cava.py -c ~/.config/cava/config -i ~/.cache/wal/colors.json -G 8

oomox-cli ~/.cache/wal/colors-oomox -o oomoxTheme

gsettings set org.gnome.desktop.interface gtk-theme oomoxTheme

python ~/projects/theme.py

killall waybar
nohup waybar & 
disown

rm ~/.config/spicetify/Themes/customTheme/color.ini
cp -r ~/.cache/wal/colors-spicetify.ini ~/.config/spicetify/Themes/customTheme/color.ini
