Summary:	Recent Notifications Applet
Name:		recent-notifications
Version:	0.5.4
Release:	0.1
License:	GPL v3
Group:		X11/Applications
Source0:	https://launchpad.net/recent-notifications/gnome3/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	a51daff631aa9ea71a0f5e47195991d3
URL:		https://launchpad.net/recent-notifications
BuildRequires:	pkgconfig(libpanel-applet) >= 3.1.91
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.713
BuildRequires:	vala >= 2:0.18
Requires:	python-dbus
Requires:	python-gnomeapplet
Requires:	python-gtk2
Requires:	python-pygobject
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Recent Notifications is a GNOME applet that collects recent messages
sent with libnotify to a notification daemon, such as notify-osd.

%prep
%setup -q

%{__sed} -i -e '/LIBPANELAPPLET_NAME/ s/libpanelapplet-4.0/libpanel-applet/' configure.ac
%{__sed} -i -e '/AM_INIT_AUTOMAKE/ s/-Werror//' configure.ac

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--libexecdir=%{_libdir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
