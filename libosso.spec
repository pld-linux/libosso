#
# Condional build:
%bcond_without	tests	# unit tests

Summary:	OSSO Application Framework for Maemo
Summary(pl.UTF-8):	Szkielet aplikacji OSSO dla Maemo
Name:		libosso
Version:	2.35
Release:	1
License:	LGPL v2.1
Group:		Libraries
#Source0Download: https://github.com/maemo-leste/libosso/releases
Source0:	https://github.com/maemo-leste/libosso/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0c4c8313b824580777ed07d951c0ecbd
Patch0:		%{name}-opt.patch
URL:		http://maemo.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gcc >= 5:3.2
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	libtool
BuildRequires:	mce-devel >= 1.5
#BuildRequires:	osso-af-settings >= 0.8.6-3 just for dbus services dir detection
%{?with_tests:BuildRequires:	outo >= 0.1.1}
BuildRequires:	pkgconfig
Requires:	dbus-glib >= 0.61
Requires:	glib2 >= 1:2.4.0
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
Requires:	dbus-glib-devel >= 0.61
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
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with tests}
# don't package them
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/outo
%{__rm}	$RPM_BUILD_ROOT%{_datadir}/dbus-1/services/com.nokia.unit_test*.service
%endif

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libosso.la

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
%attr(755,root,root) %ghost %{_libdir}/libosso.so.1
%{_sysconfdir}/dbus-1/system.d/libosso.conf
%dir %{_sysconfdir}/libosso
%{_sysconfdir}/libosso/sessionbus-libosso.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libosso.so
%{_includedir}/libosso.h
%{_includedir}/log-functions.h
%{_includedir}/muali.h
%{_includedir}/osso-fpu.h
%{_includedir}/osso-log.h
%{_includedir}/osso-mem.h
%{_pkgconfigdir}/libosso.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libosso.a
