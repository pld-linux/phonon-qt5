%define		qt_ver		5.3.1

Summary:	Phonon: multimedia API for Qt5/KDE5
Summary(pl.UTF-8):	Phonon - biblioteka multimedialna dla Qt5/KDE5
Name:		phonon-qt5
Version:	4.11.1
Release:	4
License:	LGPL v2.1 or LGPL v3
Group:		X11/Libraries
Source0:	https://download.kde.org/Attic/phonon/%{version}/phonon-%{version}.tar.xz
# Source0-md5:	d3df5ba646e4b3f11623d998caa40e74
URL:		https://userbase.kde.org/Phonon
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5Designer-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5UiTools-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.5
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	kf5-extra-cmake-modules >= 5.60
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.21
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	qt5-linguist >= %{qt_ver}
BuildRequires:	qt5-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Obsoletes:	Qt5Declarative-plugin-phonon < 4.11.1
Conflicts:	phonon < 4.10.3-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Phonon is the multimedia API for Qt5/KDE5.

Phonon was originally created to allow KDE 5 to be independent of any
single multimedia framework such as GStreamer or Xine and to provide a
stable API for KDE5's lifetime. It was done to fix problems of
frameworks becoming unmaintained, API instability, and to create a
simple multimedia API.

%description -l pl.UTF-8
Phonon to biblioteka multimedialna dla Qt5/KDE5.

Pierwotnie powstała, aby pozwolić na niezależność KDE 5 od konkretnego
środowiska multimedialnego, takiego jak GStreamer czy Xine, oraz
zapewnić stabilne API na cały czas życia KDE5. Została stworzona w
celu wyeliminowania problemów z porzucaniem bibliotek i
niestabilnością ich API, a także w celu stworzenia prostego API
multimedialnego.

%package devel
Summary:	Header files for Phonon library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Phonon
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qt_ver}
Requires:	Qt5Gui-devel >= %{qt_ver}

%description devel
Header files for Phonon library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Phonon.

%package -n Qt5Designer-plugin-phonon
Summary:	Phonon plugin for Qt5 QtDesigner
Summary(pl.UTF-8):	Wtyczka Phonon dla Qt5 QtDesignera
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Designer >= %{qt_ver}

%description -n Qt5Designer-plugin-phonon
Phonon plugin for Qt5 QtDesigner.

%description -n Qt5Designer-plugin-phonon -l pl.UTF-8
Wtyczka Phonon dla Qt5 QtDesignera.

%prep
%setup -q -n phonon-%{version}

%build
install -d build
cd build
%cmake .. \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DPHONON_BUILD_DESIGNER_PLUGIN=ON
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/qt5/plugins/phonon4qt5_backend

# libphonon_qt.qm and phononsettings_qt.qm files
%find_lang libphonon_qt --with-qm --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libphonon_qt.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/phononsettings
%attr(755,root,root) %ghost %{_libdir}/libphonon4qt5.so.4
%attr(755,root,root) %{_libdir}/libphonon4qt5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libphonon4qt5experimental.so.4
%attr(755,root,root) %{_libdir}/libphonon4qt5experimental.so.*.*.*
%dir %{_libdir}/qt5/plugins/phonon4qt5_backend
%{_datadir}/phonon4qt5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libphonon4qt5.so
%attr(755,root,root) %{_libdir}/libphonon4qt5experimental.so
%{_includedir}/phonon4qt5
%{_pkgconfigdir}/phonon4qt5.pc
%{_libdir}/cmake/phonon4qt5
%{_libdir}/qt5/mkspecs/modules/qt_phonon4qt5.pri

%files -n Qt5Designer-plugin-phonon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/phononwidgets.so
