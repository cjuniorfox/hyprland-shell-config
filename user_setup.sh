#!/usr/bin/bash

# Check if the configuration folders exist, if not, copy the files
if [ ! -d ~/.config/hypr ]; then
    cp -rvp hypr ~/.config/hypr
fi

if [ ! -d ~/.config/waybar ]; then
    cp -rvp waybar ~/.config/waybar
fi

if [ ! -d ~/.config/rofi ]; then
    cp -rvp rofi ~/.config/rofi
fi

# Create a file if it doesn't exist
touch ~/.config/hypr/monitors.conf

