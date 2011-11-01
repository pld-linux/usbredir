Summary:	USB network redirection protocol libraries
Name:		usbredir
Version:	0.3.1
Release:	1
License:	LGPL v2+
Group:		Libraries
URL:		http://cgit.freedesktop.org/~jwrdegoede/usbredir/
Source0:	http://people.fedoraproject.org/~jwrdegoede/%{name}-%{version}.tar.bz2
# Source0-md5:	17486f1662c65caab805487252274dc6
BuildRequires:	libusb-devel >= 1.0.9
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

%package devel
Summary:	Development files for usbredir
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains libraries and header files for developing
applications that use usbredir.

%package server
Summary:	Simple USB-host TCP server
License:	GPL v2+
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description server
A simple USB-host TCP server, using libusbredirhost.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="$RPM_OPT_FLAGS" \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{_libdir}/libusbredir*.so.*

%files devel
%defattr(644,root,root,755)
%doc usb-redirection-protocol.txt
%{_includedir}/usbredir*.h
%{_libdir}/libusbredir*.so
%{_pkgconfigdir}/libusbredir*.pc

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/usbredirserver
