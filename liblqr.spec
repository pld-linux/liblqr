Summary:	LiquidRescale - easy to use C/C++ seam carving library
Summary(pl.UTF-8):	LiquidRescale - łatwa w użyciu biblioteka do skalowania przez wycinanie szwów
Name:		liblqr
Version:	0.4.3
Release:	1
License:	LGPL v3
Group:		Libraries
#Source0Download: https://github.com/carlobaldassi/liblqr/tags
Source0:	https://github.com/carlobaldassi/liblqr/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c460fe171d2e5449559365b89c709a5e
Patch0:		%{name}-am.patch
URL:		http://liblqr.wikidot.com/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake >= 1:1.11
BuildRequires:	gcc >= 6:4
BuildRequires:	glib2-devel >= 1:2.8.0
BuildRequires:	libtool >= 2:2.0
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The LiquidRescale (lqr) library provides a C/C++ API for performing
non-uniform resizing of images by the seam-carving technique.

%description -l pl.UTF-8
Biblioteka LiquidRescale (lqr) udostępnia API C/C++ do wykonywania
niejednostajnego skalowania obrazów techniką wycinania szwów (seam
carving).

%package devel
Summary:	Header files for lqr library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki lqr
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.8.0

%description devel
Header files for lqr library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki lqr.

%package static
Summary:	Static lqr library
Summary(pl.UTF-8):	Statyczna biblioteka lqr
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static lqr library.

%description static -l pl.UTF-8
Statyczna biblioteka lqr.

%prep
%setup -q -n %{name}-%{version}
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblqr-1.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/liblqr-1.so.*.*.*
%ghost %{_libdir}/liblqr-1.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/liblqr-1.so
%{_includedir}/lqr-1
%{_pkgconfigdir}/lqr-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblqr-1.a
