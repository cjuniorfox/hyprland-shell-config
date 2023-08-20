%global srcname checkupdate
%define debug_package %{nil}

Name:           hyprland-shell-config
Version:        0.0.0
Release:        0%{?dist}
Summary:        Hyprland shell config scripts and installer
Url:            https://pagure.io/%{srcname}
# Sources can be obtained by
# git clone https://pagure.io/checkupdate
# cd checkupdate
# tito build --tgz
License:        GPLv3


BuildRequires: systemd-rpm-macros

BuildArch:      noarch
Requires:       beep
Requires:       amixer
Requires:	brightnessctl

Source0:        %{name}-%{version}.tar.gz

%description
Hyprland shell config scripts and installer

%prep
%autosetup

%build

%install
install -d $RPM_BUILD_ROOT%{_bindir}
install -m 755 changevolume %{buildroot}%{_bindir}
install -m 755 changebright %{buildroot}%{_bindir}
install -m 755 changekeybright %{buildroot}%{_bindir}

%files
%{_bindir}/changevolume
%{_bindir}/changebright
%{_bindir}/changekeybright

%post

%changelog
