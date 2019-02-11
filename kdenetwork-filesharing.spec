#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kdenetwork-filesharing
Version  : 18.12.2
Release  : 2
URL      : https://download.kde.org/stable/applications/18.12.2/src/kdenetwork-filesharing-18.12.2.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.2/src/kdenetwork-filesharing-18.12.2.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.2/src/kdenetwork-filesharing-18.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.1
Requires: kdenetwork-filesharing-data = %{version}-%{release}
Requires: kdenetwork-filesharing-lib = %{version}-%{release}
Requires: kdenetwork-filesharing-license = %{version}-%{release}
Requires: kdenetwork-filesharing-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

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
%setup -q -n kdenetwork-filesharing-18.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549865106
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549865106
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing
cp COPYING %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/COPYING.DOC
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kdenetwork-filesharing/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kfileshare

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/sambausershareplugin.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/sambausershareplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdenetwork-filesharing/COPYING
/usr/share/package-licenses/kdenetwork-filesharing/COPYING.DOC
/usr/share/package-licenses/kdenetwork-filesharing/COPYING.LIB

%files locales -f kfileshare.lang
%defattr(-,root,root,-)

