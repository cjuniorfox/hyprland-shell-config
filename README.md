# Hyprland Shell Config

Hyprland Configuration Files for customizing system utilities.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Files](#files)
- [License](#license)

## Overview

This package provides configuration files for customizing system utilities in Hyprland. It includes configurations for:
- Hyprland
- Waybar
- Rofi

## Installation

To install the `hyprland-shell-config` package, you can use the following commands:

```bash
# Clone the repository
git clone https://pagure.io/hyprland-shell-config

# Change to the repository directory
cd hyprland-shell-config

# Build the package
tito build --tgz

# Install the package
sudo rpm -i hyprland-shell-config-1.0.8-1.noarch.rpm
```

## Usage

After installation, the configuration files will be copied to the appropriate directories. If the configuration folders do not exist, they will be created.

```bash
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
```

## Requirements

This package requires the following dependencies:

- waybar
- hyprland
- rofi
- hyprland-keyboard-changer
- hyprland-shell-waybar
- rofi-shutdown-menu

## Files

The following configuration files are included in this package:

- ```/etc/skel/.config/hypr```
- ```/etc/skel/.config/waybar```
- ```/etc/skel/.config/rofi```

## License

This project is licensed under the GPLv3 License.
