#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kdenetwork-filesharing
Version  : 23.04.1
Release  : 53
URL      : https://download.kde.org/stable/release-service/23.04.1/src/kdenetwork-filesharing-23.04.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.1/src/kdenetwork-filesharing-23.04.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.1/src/kdenetwork-filesharing-23.04.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT
Requires: kdenetwork-filesharing-data = %{version}-%{release}
Requires: kdenetwork-filesharing-lib = %{version}-%{release}
Requires: kdenetwork-filesharing-license = %{version}-%{release}
Requires: kdenetwork-filesharing-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qcoro-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<!--
SPDX-License-Identifier: CC0-1.0
-->
# Requirements
- samba or windows server
- samba server needs to share off of a file system with POSIX ACLs enabled.
e.g. btrfs, or ext4 with acl enabled. also see https://help.ubuntu.com/community/FilePermissionsACLs

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
%setup -q -n kdenetwork-filesharing-23.04.1
cd %{_builddir}/kdenetwork-filesharing-23.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685570563
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1685570563
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing
cp %{_builddir}/kdenetwork-filesharing-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/3630f1ffcec0e075bf446b88c7b507b1287b571d || :
cp %{_builddir}/kdenetwork-filesharing-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kdenetwork-filesharing-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kdenetwork-filesharing-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kdenetwork-filesharing-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/kdenetwork-filesharing-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/fa05e58320cb7c64786b26396f4b992579a628bc || :
cp %{_builddir}/kdenetwork-filesharing-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/0b71159e19bef95069e18d17296291916e89b5cd || :
cp %{_builddir}/kdenetwork-filesharing-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kdenetwork-filesharing-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kdenetwork-filesharing-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kdenetwork-filesharing-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kdenetwork-filesharing-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/adadb67a9875aeeac285309f1eab6e47d9ee08a7 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kfileshare
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kauth/authhelper
/usr/lib64/libexec/kauth/authhelper

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/org.kde.filesharing.samba.service
/usr/share/dbus-1/system.d/org.kde.filesharing.samba.conf
/usr/share/metainfo/org.kde.kdenetwork-filesharing.metainfo.xml
/usr/share/polkit-1/actions/org.kde.filesharing.samba.policy

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt5/plugins/kf5/propertiesdialog/SambaAcl.so
/V3/usr/lib64/qt5/plugins/kf5/propertiesdialog/sambausershareplugin.so
/usr/lib64/qt5/plugins/kf5/propertiesdialog/SambaAcl.so
/usr/lib64/qt5/plugins/kf5/propertiesdialog/sambausershareplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdenetwork-filesharing/0b71159e19bef95069e18d17296291916e89b5cd
/usr/share/package-licenses/kdenetwork-filesharing/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kdenetwork-filesharing/3630f1ffcec0e075bf446b88c7b507b1287b571d
/usr/share/package-licenses/kdenetwork-filesharing/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kdenetwork-filesharing/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kdenetwork-filesharing/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kdenetwork-filesharing/adadb67a9875aeeac285309f1eab6e47d9ee08a7
/usr/share/package-licenses/kdenetwork-filesharing/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kdenetwork-filesharing/e712eadfab0d2357c0f50f599ef35ee0d87534cb
/usr/share/package-licenses/kdenetwork-filesharing/fa05e58320cb7c64786b26396f4b992579a628bc

%files locales -f kfileshare.lang
%defattr(-,root,root,-)

