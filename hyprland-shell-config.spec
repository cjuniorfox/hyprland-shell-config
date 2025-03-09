%global srcname hyprland-shell-config
%define debug_package %{nil}

Name:           hyprland-shell-config
Version:        1.0.25
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
* Sun Mar 09 2025 Junior_FOX <cjuniorfox@gmail.com> 1.0.25-1
- Automatic commit of package [hyprland-shell-config] release [1.0.24-1].
  (cjuniorfox@gmail.com)
- fixed screen brightness down (cjuniorfox@gmail.com)
- Automatic commit of package [hyprland-shell-config] release [1.0.24-1].
  (cjuniorfox@gmail.com)
- fixed window rules (cjuniorfox@gmail.com)

* Sun Mar 09 2025 Junior_FOX <cjuniorfox@gmail.com> 1.0.24-1
- fixed screen brightness down (cjuniorfox@gmail.com)
- Automatic commit of package [hyprland-shell-config] release [1.0.22-1].
  (cjuniorfox@gmail.com)
- fixed smartgaps accordgly with the following commit: https://github.com/hyprw
  m/Hyprland/commit/dca75db127fedc58fc85ae0e6e47162e3d5d16f9
  (cjuniorfox@gmail.com)

* Wed Dec 18 2024 Junior_FOX <cjuniorfox@gmail.com> 1.0.22-1
- fixed smartgaps accordgly with the following commit: https://github.com/hyprw

* Tue Nov 12 2024 Junior <cjuniorfox@gmail.com> 1.0.21-1
- split rules and resolved shadows (cjuniorfox@gmail.com)
- lxqt polkit as float (cjuniorfox@gmail.com)

* Wed Dec 11 2024 Junior <cjuniorfox@gmail.com> 1.0.23-1
- added bibata theme cursor to the default file (cjuniorfox@gmail.com)

* Sun Dec 08 2024 Junior <cjuniorfox@gmail.com> 1.0.22-1
- fixed volume down not working (cjuniorfox@gmail.com)

* Sun Nov 03 2024 Junior <cjuniorfox@gmail.com> 1.0.20-1
- replaced gnome polkit by lxqt polkit (cjuniorfox@gmail.com)

* Thu Oct 17 2024 Junior <cjuniorfox@gmail.com> 1.0.19-1
- cleanup and fix icons on top bar (cjuniorfox@gmail.com)

* Mon Oct 14 2024 Junior <cjuniorfox@gmail.com> 1.0.18-1
- dwindle, added no gaps when only one window (cjuniorfox@gmail.com)

* Sun Oct 13 2024 Junior <cjuniorfox@gmail.com> 1.0.17-1
- 

* Sun Oct 13 2024 Junior <cjuniorfox@gmail.com> 1.0.16-1
- removed dwindle config (cjuniorfox@gmail.com)

* Thu Oct 10 2024 Junior <cjuniorfox@gmail.com> 1.0.15-1
- templates updated (cjuniorfox@gmail.com)

* Wed Oct 02 2024 Junior <cjuniorfox@gmail.com> 1.0.14-1
- Replaced swayidle to hypridle (cjuniorfox@gmail.com)

* Wed Oct 02 2024 Junior <cjuniorfox@gmail.com> 1.0.13-1
- changed screenlock (cjuniorfox@gmail.com)

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
