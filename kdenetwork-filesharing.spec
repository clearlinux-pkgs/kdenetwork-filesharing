#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kdenetwork-filesharing
Version  : 20.08.3
Release  : 24
URL      : https://download.kde.org/stable/release-service/20.08.3/src/kdenetwork-filesharing-20.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.08.3/src/kdenetwork-filesharing-20.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.08.3/src/kdenetwork-filesharing-20.08.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.1
Requires: kdenetwork-filesharing-data = %{version}-%{release}
Requires: kdenetwork-filesharing-lib = %{version}-%{release}
Requires: kdenetwork-filesharing-license = %{version}-%{release}
Requires: kdenetwork-filesharing-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data

%description
No detailed description available

%package data
Summary: data components for the kdenetwork-filesharing package.
Group: Data

%description data
data components for the kdenetwork-filesharing package.


%package lib
Summary: lib components for the kdenetwork-filesharing package.
Group: Libraries
Requires: kdenetwork-filesharing-data = %{version}-%{release}
Requires: kdenetwork-filesharing-license = %{version}-%{release}

%description lib
lib components for the kdenetwork-filesharing package.


%package license
Summary: license components for the kdenetwork-filesharing package.
Group: Default

%description license
license components for the kdenetwork-filesharing package.


%package locales
Summary: locales components for the kdenetwork-filesharing package.
Group: Default

%description locales
locales components for the kdenetwork-filesharing package.


%prep
%setup -q -n kdenetwork-filesharing-20.08.3
cd %{_builddir}/kdenetwork-filesharing-20.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604600217
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1604600217
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing
cp %{_builddir}/kdenetwork-filesharing-20.08.3/COPYING %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/3860f7708aae6a8ddfe8483263b2a5f29b83c975
cp %{_builddir}/kdenetwork-filesharing-20.08.3/COPYING.DOC %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
cp %{_builddir}/kdenetwork-filesharing-20.08.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd
%find_lang kfileshare

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/sambausershareplugin.desktop
/usr/share/metainfo/org.kde.kdenetwork-filesharing.metainfo.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/sambausershareplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdenetwork-filesharing/3860f7708aae6a8ddfe8483263b2a5f29b83c975
/usr/share/package-licenses/kdenetwork-filesharing/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/kdenetwork-filesharing/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f kfileshare.lang
%defattr(-,root,root,-)

