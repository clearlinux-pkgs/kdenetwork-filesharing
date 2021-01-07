#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kdenetwork-filesharing
Version  : 20.12.1
Release  : 26
URL      : https://download.kde.org/stable/release-service/20.12.1/src/kdenetwork-filesharing-20.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.12.1/src/kdenetwork-filesharing-20.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.12.1/src/kdenetwork-filesharing-20.12.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
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
%setup -q -n kdenetwork-filesharing-20.12.1
cd %{_builddir}/kdenetwork-filesharing-20.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610052053
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
export SOURCE_DATE_EPOCH=1610052053
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing
cp %{_builddir}/kdenetwork-filesharing-20.12.1/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/kdenetwork-filesharing-20.12.1/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/kdenetwork-filesharing-20.12.1/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/kdenetwork-filesharing-20.12.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kdenetwork-filesharing-20.12.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/7d9831e05094ce723947d729c2a46a09d6e90275
pushd clr-build
%make_install
popd
%find_lang kfileshare

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kauth/authhelper

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/org.kde.filesharing.samba.service
/usr/share/dbus-1/system.d/org.kde.filesharing.samba.conf
/usr/share/kservices5/sambausershareplugin.desktop
/usr/share/metainfo/org.kde.kdenetwork-filesharing.metainfo.xml
/usr/share/polkit-1/actions/org.kde.filesharing.samba.policy

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/sambausershareplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdenetwork-filesharing/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kdenetwork-filesharing/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kdenetwork-filesharing/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kdenetwork-filesharing/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kfileshare.lang
%defattr(-,root,root,-)

