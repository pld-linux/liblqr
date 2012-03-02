Summary:	LiquidRescale - easy to use C/C++ seam carving library
Summary(pl.UTF-8):	LiquidRescale - łatwa w użyciu biblioteka do skalowania przez wycinanie szwów
Name:		liblqr
Version:	0.4.1
Release:	1
License:	LGPL v3
Group:		Libraries
Source0:	http://liblqr.wikidot.com/local--files/en:download-page/%{name}-1-%{version}.tar.bz2
# Source0-md5:	0e24ed3c9fcdcb111062640764d7b87a
URL:		http://liblqr.wikidot.com/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
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
%setup -q -n %{name}-1-%{version}

%if "%{cc_version}" < "4.0"
%{__sed} -i -e 's,-fvisibility=\\"hidden\\",,' configure.ac
%endif

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/liblqr-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblqr-1.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblqr-1.so
%{_libdir}/liblqr-1.la
%{_includedir}/lqr-1
%{_pkgconfigdir}/lqr-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblqr-1.a
