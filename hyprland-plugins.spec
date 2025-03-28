%global __provides_exclude_from ^(%{_libdir}/hyprland/.*\\.so)$

%global _disable_ld_no_undefined %nil
%global plugins borders-plus-plus csgo-vulkan-fix hyprbars hyprexpo hyprtrails hyprwinwrap xtra-dispatchers

Name:		hyprland-plugins
Version:	0.48.0
Release:	1
Group:		System/Libraries
Summary:	Official plugins for Hyprland
License:	BSD-3-Clause
URL:		https://github.com/hyprwm/hyprland-plugins
Source:		%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig(hyprland)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprgraphics)
BuildRequires:	pkgconfig(aquamarine)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pangocairo)
Requires:       hyprland

%description
%{summary}.

%prep
%autosetup -n hyprland-plugins-%{version} -p1

%build
export CXXFLAGS="%{optflags} -I%{_includedir}/hyprland/"
for plugin in %{plugins}
do
pushd $plugin
%meson --libdir=%{_libdir}/hyprland
%meson_build
popd
done


%install
for plugin in %{plugins}
do
pushd $plugin
%meson_install
popd
done

%files
%{_libdir}/hyprland/*.so
