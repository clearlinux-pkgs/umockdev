#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : umockdev
Version  : 0.17.12
Release  : 2
URL      : https://github.com/martinpitt/umockdev/releases/download/0.17.12/umockdev-0.17.12.tar.xz
Source0  : https://github.com/martinpitt/umockdev/releases/download/0.17.12/umockdev-0.17.12.tar.xz
Summary  : Mock hardware devices
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: umockdev-bin = %{version}-%{release}
Requires: umockdev-data = %{version}-%{release}
Requires: umockdev-lib = %{version}-%{release}
Requires: umockdev-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : glib-dev
BuildRequires : gobject-introspection-dev
BuildRequires : libgudev-dev
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(libpcap)
BuildRequires : pkgconfig(libudev)
BuildRequires : vala

%description
With this program and libraries you can easily create mock udev objects.
This is useful for writing tests for software which talks to
hardware devices.

%package bin
Summary: bin components for the umockdev package.
Group: Binaries
Requires: umockdev-data = %{version}-%{release}
Requires: umockdev-license = %{version}-%{release}

%description bin
bin components for the umockdev package.


%package data
Summary: data components for the umockdev package.
Group: Data

%description data
data components for the umockdev package.


%package dev
Summary: dev components for the umockdev package.
Group: Development
Requires: umockdev-lib = %{version}-%{release}
Requires: umockdev-bin = %{version}-%{release}
Requires: umockdev-data = %{version}-%{release}
Provides: umockdev-devel = %{version}-%{release}
Requires: umockdev = %{version}-%{release}

%description dev
dev components for the umockdev package.


%package lib
Summary: lib components for the umockdev package.
Group: Libraries
Requires: umockdev-data = %{version}-%{release}
Requires: umockdev-license = %{version}-%{release}

%description lib
lib components for the umockdev package.


%package license
Summary: license components for the umockdev package.
Group: Default

%description license
license components for the umockdev package.


%prep
%setup -q -n umockdev-0.17.12
cd %{_builddir}/umockdev-0.17.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652995677
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/umockdev
cp %{_builddir}/umockdev-0.17.12/COPYING %{buildroot}/usr/share/package-licenses/umockdev/01a6b4bf79aca9b556822601186afab86e8c4fbf
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/umockdev-record
/usr/bin/umockdev-run
/usr/bin/umockdev-wrapper

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/UMockdev-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/umockdev-1.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/umockdev-1.0/umockdev.h
/usr/lib64/libumockdev-preload.so
/usr/lib64/libumockdev.so
/usr/lib64/pkgconfig/umockdev-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libumockdev-preload.so.0
/usr/lib64/libumockdev-preload.so.0.0.0
/usr/lib64/libumockdev.so.0
/usr/lib64/libumockdev.so.0.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/umockdev/01a6b4bf79aca9b556822601186afab86e8c4fbf
