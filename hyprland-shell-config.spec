%global srcname hyprland-shell-config
%define debug_package %{nil}

Name:           hyprland-shell-config
Version:        1.0.12
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
Requires: hyprland-keyboard-changer, hyprland-shell-waybar, rofi-shutdown-menu

Source0: %{name}-%{version}.tar.gz

%description
Hyprland Configuration Files for customizing system utilities.

%prep
# Nothing to prepare
%autosetup

%build
# Nothing to build

%install
mkdir -p %{buildroot}/etc/skel/.config/{hypr,waybar,rofi}
cp -rp hypr/* %{buildroot}/etc/skel/.config/hypr/
cp -rp waybar/* %{buildroot}/etc/skel/.config/waybar/
cp -rp rofi/* %{buildroot}/etc/skel/.config/rofi/
touch %{buildroot}/etc/skel/.config/hypr/monitors.conf

%files
/etc/skel/.config/hypr
/etc/skel/.config/waybar
/etc/skel/.config/rofi

%changelog
* Wed Oct 02 2024 Junior <cjuniorfox@gmail.com> 1.0.12-1
- removal of the requirement for Hyprland (cjuniorfox@gmail.com)

* Wed Oct 02 2024 Junior <cjuniorfox@gmail.com> 1.0.11-1
- replace swaylock to hyprlock (cjuniorfox@gmail.com)

* Wed Jul 24 2024 Junior <cjuniorfox@gmail.com> 1.0.10-1
- Added the ability to alt+tab windows (cjuniorfox@gmail.com)

* Tue Jul 09 2024 Junior <cjuniorfox@gmail.com> 1.0.9-1
- chore: fixed changelog spec file (cjuniorfox@gmail.com)
- chore: created a readme file (cjuniorfox@gmail.com)
- chore: update the dependencies. Removed checkupdate as a requirement
  (cjuniorfox@gmail.com)
- chore: removed unused scripts (cjuniorfox@gmail.com)

* Thu Jul 04 2024 Junior <cjuniorfox@gmail.com> 1.0.8-1
- chore: pavucontrol as float (cjuniorfox@gmail.com)

* Thu Jun 27 2024 Junior <cjuniorfox@gmail.com> 1.0.7-1
- bugfix: error at waypaper class namimg (cjuniorfox@gmail.com)

* Thu Jun 27 2024 Junior <cjuniorfox@gmail.com> 1.0.6-1
- chore: replaced azote related stuff to waypaper (cjuniorfox@gmail.com)

* Thu Jun 27 2024 Junior <cjuniorfox@gmail.com> 1.0.5-1
- removed the master is new master (cjuniorfox@gmail.com)

* Fri May 24 2024 Junior_FOX <cjuniorfox@gmail.com> 1.0.4-1
- fix copying (cjuniorfox@gmail.com)

* Fri May 24 2024 Junior_FOX <cjuniorfox@gmail.com> 1.0.3-1
- 

* Fri May 24 2024 Junior_FOX <cjuniorfox@gmail.com> 1.0.2-1
- added changelog (cjuniorfox@gmail.com)

* Fri May 24 2024 Junior_FOX <cjuniorfox@gmail.com>
- new package built with tito
