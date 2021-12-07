Summary:	USB network redirection protocol libraries
Summary(pl.UTF-8):	Biblioteki protokołu przekierowania USB przez sieć
Name:		usbredir
Version:	0.12.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://www.spice-space.org/download/usbredir/%{name}-%{version}.tar.xz
# Source0-md5:	dc7e2867a123c151573cb5f2dae4874e
URL:		https://www.spice-space.org/usbredir.html
BuildRequires:	glib2-devel >= 1:2.44
BuildRequires:	libusb-devel >= 1.0.19
BuildRequires:	meson >= 0.53
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.44
Requires:	libusb >= 1.0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
usbredir is a protocol for redirection USB traffic from a single USB
device, to a different (virtual) machine then the one to which the USB
device is attached. This package contains a number of libraries to
help implementing support for usbredir:

usbredirparser: A library containing the parser for the usbredir
protocol

usbredirhost: A library implementing the usb-host side of a usbredir
connection. All that an application wishing to implement an usb-host
needs to do is:
- Provide a libusb device handle for the device
- Provide write and read callbacks for the actual transport of
  usbredir data
- Monitor for usbredir and libusb read/write events and call their
  handlers

%description -l pl.UTF-8
usbredir to protokół pozwalający przekierować ruch USB z pojedynczego
urządzenia USB na inną (wirtualną) maszynę, a następnie na taką, do
której urządzenie USB jest podłączone. Ten pakiet zawiera biblioteki
pomagające przy implementacji usbredir:

usbredirparser - biblioteka zawierająca analizator protokołu usbredir

usbredirhost - biblioteka implementująca stronę hosta USB połączenia
usbredir. Wszystko, co musi zrobić aplikacja chcąca implementować
host USB, to:
- zapewnienie uchwytu libusb dla urządzenia USB
- zapewnienie wywołań zapisu i odczytu dla transportu danych usbredir
- monitorowanie zdarzeń odczytu/zapisu usbredir oraz libusb i
  wywoływanie ich procedur obsługi.

%package devel
Summary:	Development files for usbredir
Summary(pl.UTF-8):	Pliki programistyczne usbredir
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libusb-devel >= 1.0.19

%description devel
This package contains the header files for developing applications
that use usbredir.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących usbredir.

%package static
Summary:	Static usbredir libraries
Summary(pl.UTF-8):	Statyczne biblioteki usbredir
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static usbredir libraries.

%description static -l pl.UTF-8
Statyczne biblioteki usbredir.

%package server
Summary:	Simple USB-host TCP server
Summary(pl.UTF-8):	Prosty serwer TCP hosta USB
License:	GPL v2+
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description server
A simple USB-host TCP server, using libusbredirhost.

%description server -l pl.UTF-8
Prosty serwer TCP hosta USB wykorzystujący libusbredirhost.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog.md README.md TODO
%attr(755,root,root) %{_bindir}/usbredirect
%attr(755,root,root) %{_libdir}/libusbredirhost.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libusbredirhost.so.1
%attr(755,root,root) %{_libdir}/libusbredirparser.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libusbredirparser.so.1
%{_mandir}/man1/usbredirect.1*

%files devel
%defattr(644,root,root,755)
%doc docs/*.md
%attr(755,root,root) %{_libdir}/libusbredirhost.so
%attr(755,root,root) %{_libdir}/libusbredirparser.so
%{_includedir}/usbredirfilter.h
%{_includedir}/usbredirhost.h
%{_includedir}/usbredirparser.h
%{_includedir}/usbredirproto.h
%{_pkgconfigdir}/libusbredirhost.pc
%{_pkgconfigdir}/libusbredirparser-0.5.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libusbredirhost.a
%{_libdir}/libusbredirparser.a

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/usbredirserver
%{_mandir}/man1/usbredirserver.1*
