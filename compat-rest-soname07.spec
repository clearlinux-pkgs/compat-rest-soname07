#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-rest-soname07
Version  : 0.8.1
Release  : 23
URL      : https://download.gnome.org/sources/rest/0.8/rest-0.8.1.tar.xz
Source0  : https://download.gnome.org/sources/rest/0.8/rest-0.8.1.tar.xz
Summary  : RESTful web api query library
Group    : Development/Tools
License  : LGPL-2.1
Requires: compat-rest-soname07-data = %{version}-%{release}
Requires: compat-rest-soname07-lib = %{version}-%{release}
Requires: compat-rest-soname07-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : ca-certs
BuildRequires : docbook-xml
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libsoup-gnome-2.4)
BuildRequires : pkgconfig(libxml-2.0)

%description
librest
=======
This library has been designed to make it easier to access web services that
claim to be "RESTful". A reasonable definition of what this means can be found
on Wikipedia [1]. However a reasonable description is that a RESTful service
should have urls that represent remote objects which methods can then be
called on.

%package data
Summary: data components for the compat-rest-soname07 package.
Group: Data

%description data
data components for the compat-rest-soname07 package.


%package dev
Summary: dev components for the compat-rest-soname07 package.
Group: Development
Requires: compat-rest-soname07-lib = %{version}-%{release}
Requires: compat-rest-soname07-data = %{version}-%{release}
Provides: compat-rest-soname07-devel = %{version}-%{release}
Requires: compat-rest-soname07 = %{version}-%{release}

%description dev
dev components for the compat-rest-soname07 package.


%package doc
Summary: doc components for the compat-rest-soname07 package.
Group: Documentation

%description doc
doc components for the compat-rest-soname07 package.


%package lib
Summary: lib components for the compat-rest-soname07 package.
Group: Libraries
Requires: compat-rest-soname07-data = %{version}-%{release}
Requires: compat-rest-soname07-license = %{version}-%{release}

%description lib
lib components for the compat-rest-soname07 package.


%package license
Summary: license components for the compat-rest-soname07 package.
Group: Default

%description license
license components for the compat-rest-soname07 package.


%prep
%setup -q -n rest-0.8.1
cd %{_builddir}/rest-0.8.1
pushd ..
cp -a rest-0.8.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656099115
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --with-ca-certificates=/var/cache/ca-certs/compat/ca-roots.pem
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --with-ca-certificates=/var/cache/ca-certs/compat/ca-roots.pem
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1656099115
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-rest-soname07
cp %{_builddir}/rest-0.8.1/COPYING %{buildroot}/usr/share/package-licenses/compat-rest-soname07/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Rest-0.7.typelib
/usr/lib64/girepository-1.0/RestExtras-0.7.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/rest-0.7/rest-extras/flickr-proxy-call.h
/usr/include/rest-0.7/rest-extras/flickr-proxy.h
/usr/include/rest-0.7/rest-extras/lastfm-proxy-call.h
/usr/include/rest-0.7/rest-extras/lastfm-proxy.h
/usr/include/rest-0.7/rest-extras/youtube-proxy.h
/usr/include/rest-0.7/rest/oauth-proxy-call.h
/usr/include/rest-0.7/rest/oauth-proxy.h
/usr/include/rest-0.7/rest/oauth2-proxy-call.h
/usr/include/rest-0.7/rest/oauth2-proxy.h
/usr/include/rest-0.7/rest/rest-enum-types.h
/usr/include/rest-0.7/rest/rest-param.h
/usr/include/rest-0.7/rest/rest-params.h
/usr/include/rest-0.7/rest/rest-proxy-auth.h
/usr/include/rest-0.7/rest/rest-proxy-call.h
/usr/include/rest-0.7/rest/rest-proxy.h
/usr/include/rest-0.7/rest/rest-xml-node.h
/usr/include/rest-0.7/rest/rest-xml-parser.h
/usr/lib64/librest-0.7.so
/usr/lib64/librest-extras-0.7.so
/usr/lib64/pkgconfig/rest-0.7.pc
/usr/lib64/pkgconfig/rest-extras-0.7.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/rest-0.7/FlickrProxy.html
/usr/share/gtk-doc/html/rest-0.7/FlickrProxyCall.html
/usr/share/gtk-doc/html/rest-0.7/LastfmProxy.html
/usr/share/gtk-doc/html/rest-0.7/LastfmProxyCall.html
/usr/share/gtk-doc/html/rest-0.7/OAuth2Proxy.html
/usr/share/gtk-doc/html/rest-0.7/OAuth2ProxyCall.html
/usr/share/gtk-doc/html/rest-0.7/OAuthProxy.html
/usr/share/gtk-doc/html/rest-0.7/OAuthProxyCall.html
/usr/share/gtk-doc/html/rest-0.7/RestProxy.html
/usr/share/gtk-doc/html/rest-0.7/RestProxyCall.html
/usr/share/gtk-doc/html/rest-0.7/RestXmlParser.html
/usr/share/gtk-doc/html/rest-0.7/ch01.html
/usr/share/gtk-doc/html/rest-0.7/ch02.html
/usr/share/gtk-doc/html/rest-0.7/ch03.html
/usr/share/gtk-doc/html/rest-0.7/ch04.html
/usr/share/gtk-doc/html/rest-0.7/ch05.html
/usr/share/gtk-doc/html/rest-0.7/home.png
/usr/share/gtk-doc/html/rest-0.7/index.html
/usr/share/gtk-doc/html/rest-0.7/ix01.html
/usr/share/gtk-doc/html/rest-0.7/left-insensitive.png
/usr/share/gtk-doc/html/rest-0.7/left.png
/usr/share/gtk-doc/html/rest-0.7/rest-0.7.devhelp2
/usr/share/gtk-doc/html/rest-0.7/rest-RestParam.html
/usr/share/gtk-doc/html/rest-0.7/rest-RestParams.html
/usr/share/gtk-doc/html/rest-0.7/right-insensitive.png
/usr/share/gtk-doc/html/rest-0.7/right.png
/usr/share/gtk-doc/html/rest-0.7/style.css
/usr/share/gtk-doc/html/rest-0.7/up-insensitive.png
/usr/share/gtk-doc/html/rest-0.7/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/librest-0.7.so
/usr/lib64/glibc-hwcaps/x86-64-v3/librest-0.7.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/librest-0.7.so.0.0.0
/usr/lib64/glibc-hwcaps/x86-64-v3/librest-extras-0.7.so
/usr/lib64/glibc-hwcaps/x86-64-v3/librest-extras-0.7.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/librest-extras-0.7.so.0.0.0
/usr/lib64/librest-0.7.so.0
/usr/lib64/librest-0.7.so.0.0.0
/usr/lib64/librest-extras-0.7.so.0
/usr/lib64/librest-extras-0.7.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-rest-soname07/9a1929f4700d2407c70b507b3b2aaf6226a9543c
