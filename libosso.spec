Summary:	OSSO Application Framework for Maemo
Summary(pl.UTF-8):	Szkielet aplikacji OSSO dla Maemo
Name:		libosso
Version:	1.20
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://repository.maemo.org/pool/bora/free/source/%{name}_%{version}-1.tar.gz
# Source0-md5:	6bb3f309371d398d321e52c9e52ca605
Patch0:		%{name}-opt.patch
URL:		http://maemo.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.22
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	libtool
BuildRequires:	outo >= 0.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D-Bus-related functionality for Maemo applications.

%description -l pl.UTF-8
Funkcjonalność związana z D-Bus dla aplikacji Maemo.

%package devel
Summary:	Header files for libosso
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libosso
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.22
Requires:	glib2-devel >= 1:2.4.0

%description devel
Header files for libosso.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libosso.

%package static
Summary:	Static libosso library
Summary(pl.UTF-8):	Statyczna biblioteka libosso
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libosso library.

%description static -l pl.UTF-8
Statyczna biblioteka libosso.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/dbus-launch-systembus.sh
%attr(755,root,root) %{_bindir}/dbus-launch.sh
%attr(755,root,root) %{_bindir}/osso-date
%attr(755,root,root) %{_libdir}/libosso.so.*.*.*
%{_sysconfdir}/dbus-1/system.d/libosso.conf
%dir %{_sysconfdir}/libosso
%{_sysconfdir}/libosso/sessionbus-libosso.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libosso.so
%{_libdir}/libosso.la
%{_includedir}/libosso.h
%{_includedir}/log-functions.h
%{_includedir}/osso-log.h
%{_includedir}/osso-mem.h
%{_pkgconfigdir}/libosso.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libosso.a
