#
%define snap 12075
Summary:	Maemo osso library
Name:		libosso
Version:	2.8
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://archive.ubuntu.com/ubuntu/pool/universe/libo/libosso/%{name}_%{version}-1ubuntu2.tar.gz
# Source0-md5:	674c72cdae220156882d9cc7ec2253dd
# Source0: https://stage.maemo.org/svn/maemo/projects/haf/trunk/libosso/
URL:		http://maemo.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	mce-devel
#BuildRequires:	python-devel
#BuildRequires:	xulrunner-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In-place editor library for the Maemo platform.

%package devel
Summary:	Header files for libosso
Group:		Development/Libraries

%description devel
Header files for libosso.

%package static
Summary:	Static libosso library
Summary(pl.UTF-8):	Statyczna biblioteka libosso
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liboss library.

%description static -l pl.UTF-8
Statyczna biblioteka libosso.

%prep
%setup -q

%build
%{__glib_gettextize}
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
%doc AUTHORS ChangeLog NEWS README

%files devel
%defattr(644,root,root,755)

%files static
%defattr(644,root,root,755)
