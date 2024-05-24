%define name hyprland-config
%define version 1.0
%define release 1
%define buildroot %{_tmppath}/%{name}-%{version}-%{release}-root

Summary: Hyprland Configuration Files
Name: %{name}
Version: %{version}
Release: %{release}
License: MIT
Group: Applications/System
BuildArch: noarch

Requires: checkupdate hyprland-keyboard-changer hyprland-shell-waybar rofi-shutdown-menu wol-changer

%description
Hyprland Configuration Files for customizing system utilities.

%prep
# Nothing to prepare

%build
# Nothing to build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/skel/.config
cp -rvp hypr %{buildroot}/etc/skel/.config/hypr
cp -rvp waybar %{buildroot}/etc/skel/.config/waybar
cp -rvp rofi %{buildroot}/etc/skel/.config/rofi
touch %{buildroot}/etc/skel/.config/hypr/monitors.conf

%files
/etc/skel/.config/hypr
/etc/skel/.config/waybar
/etc/skel/.config/rofi

%changelog

