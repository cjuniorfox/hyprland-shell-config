%global srcname hyprland-shell-config
%define debug_package %{nil}

Name:           hyprland-shell-config
Version:        1.0.1
Release:        1%{?dist}
Summary:        Hyperland shell configuration files
Url:            https://pagure.io/%{srcname}
# Sources can be obtained by
# git clone https://pagure.io/hyprland-shell-config
# cd hyperland-shell-config
# tito build --tgz
License:        GPLv3

%define buildroot %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: checkupdate hyprland-keyboard-changer hyprland-shell-waybar rofi-shutdown-menu wol-changer

Source0:        %{name}-%{version}.tar.gz

%description
Hyprland Configuration Files for customizing system utilities.

%prep
# Nothing to prepare
%autosetup

%build
# Nothing to build

%install
mkdir -p %{buildroot}/etc/skel/.config
install -d hypr %{buildroot}/etc/skel/.config/hypr
install -d waybar %{buildroot}/etc/skel/.config/waybar
install -d rofi %{buildroot}/etc/skel/.config/rofi
touch %{buildroot}/etc/skel/.config/hypr/monitors.conf

%files
/etc/skel/.config/hypr
/etc/skel/.config/waybar
/etc/skel/.config/rofi

%changelog
* Fri May 24 2024 Junior_FOX <cjuniorfox@gmail.com>
- new package built with tito

