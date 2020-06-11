#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kmail-account-wizard
Version  : 20.04.2
Release  : 24
URL      : https://download.kde.org/stable/release-service/20.04.2/src/kmail-account-wizard-20.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.04.2/src/kmail-account-wizard-20.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.04.2/src/kmail-account-wizard-20.04.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.1
Requires: kmail-account-wizard-bin = %{version}-%{release}
Requires: kmail-account-wizard-data = %{version}-%{release}
Requires: kmail-account-wizard-lib = %{version}-%{release}
Requires: kmail-account-wizard-license = %{version}-%{release}
Requires: kmail-account-wizard-locales = %{version}-%{release}
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : extra-cmake-modules-data
BuildRequires : gpgme-dev
BuildRequires : kcmutils-dev
BuildRequires : kcodecs-dev
BuildRequires : kconfig-dev
BuildRequires : kcontacts-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kdoctools-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kimap-dev
BuildRequires : kimap-staticdev
BuildRequires : kldap-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : knewstuff-dev
BuildRequires : knotifications-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kpimtextedit-dev
BuildRequires : kross-dev
BuildRequires : kservice-dev
BuildRequires : ktexteditor-dev
BuildRequires : kwallet-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : libkdepim-dev
BuildRequires : libkleo-dev
BuildRequires : pimcommon-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qttools-dev
BuildRequires : shared-mime-info

%description
No detailed description available

%package bin
Summary: bin components for the kmail-account-wizard package.
Group: Binaries
Requires: kmail-account-wizard-data = %{version}-%{release}
Requires: kmail-account-wizard-license = %{version}-%{release}

%description bin
bin components for the kmail-account-wizard package.


%package data
Summary: data components for the kmail-account-wizard package.
Group: Data

%description data
data components for the kmail-account-wizard package.


%package lib
Summary: lib components for the kmail-account-wizard package.
Group: Libraries
Requires: kmail-account-wizard-data = %{version}-%{release}
Requires: kmail-account-wizard-license = %{version}-%{release}

%description lib
lib components for the kmail-account-wizard package.


%package license
Summary: license components for the kmail-account-wizard package.
Group: Default

%description license
license components for the kmail-account-wizard package.


%package locales
Summary: locales components for the kmail-account-wizard package.
Group: Default

%description locales
locales components for the kmail-account-wizard package.


%prep
%setup -q -n kmail-account-wizard-20.04.2
cd %{_builddir}/kmail-account-wizard-20.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591898615
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
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1591898615
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmail-account-wizard
cp %{_builddir}/kmail-account-wizard-20.04.2/COPYING %{buildroot}/usr/share/package-licenses/kmail-account-wizard/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/kmail-account-wizard-20.04.2/COPYING.DOC %{buildroot}/usr/share/package-licenses/kmail-account-wizard/1bd373e4851a93027ba70064bd7dbdc6827147e1
cp %{_builddir}/kmail-account-wizard-20.04.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/kmail-account-wizard/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd
%find_lang accountwizard
%find_lang accountwizard_tine20

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/accountwizard
/usr/bin/ispdb

%files data
%defattr(-,root,root,-)
/usr/share/akonadi/accountwizard/tine20/tine20wizard.desktop
/usr/share/akonadi/accountwizard/tine20/tine20wizard.es
/usr/share/akonadi/accountwizard/tine20/tine20wizard.ui
/usr/share/applications/org.kde.accountwizard.desktop
/usr/share/knsrcfiles/accountwizard.knsrc
/usr/share/mime-packages/accountwizard-mime.xml
/usr/share/qlogging-categories5/accountwizard.categories
/usr/share/qlogging-categories5/accountwizard.renamecategories

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/accountwizard_plugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmail-account-wizard/1bd373e4851a93027ba70064bd7dbdc6827147e1
/usr/share/package-licenses/kmail-account-wizard/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/kmail-account-wizard/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files locales -f accountwizard.lang -f accountwizard_tine20.lang
%defattr(-,root,root,-)

