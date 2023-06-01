#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kmail-account-wizard
Version  : 23.04.1
Release  : 63
URL      : https://download.kde.org/stable/release-service/23.04.1/src/kmail-account-wizard-23.04.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.1/src/kmail-account-wizard-23.04.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.1/src/kmail-account-wizard-23.04.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 LGPL-2.0
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
BuildRequires : ktextaddons-dev
BuildRequires : ktexteditor-dev
BuildRequires : kwallet-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : libkdepim-dev
BuildRequires : libkleo-dev
BuildRequires : pimcommon-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtkeychain-dev
BuildRequires : qttools-dev
BuildRequires : shared-mime-info
BuildRequires : syntax-highlighting-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Revert-GIT_SILENT-time-to-increase-version.patch

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
%setup -q -n kmail-account-wizard-23.04.1
cd %{_builddir}/kmail-account-wizard-23.04.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685587458
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
export SOURCE_DATE_EPOCH=1685587458
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmail-account-wizard
cp %{_builddir}/kmail-account-wizard-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kmail-account-wizard/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kmail-account-wizard-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kmail-account-wizard/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kmail-account-wizard-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kmail-account-wizard/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kmail-account-wizard-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmail-account-wizard/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kmail-account-wizard-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmail-account-wizard/20079e8f79713dce80ab09774505773c926afa2a || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang accountwizard
%find_lang accountwizard_tine20
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/accountwizard
/V3/usr/bin/ispdb
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
/V3/usr/lib64/qt5/plugins/accountwizard_plugin.so
/usr/lib64/qt5/plugins/accountwizard_plugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmail-account-wizard/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kmail-account-wizard/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kmail-account-wizard/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kmail-account-wizard/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kmail-account-wizard/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f accountwizard.lang -f accountwizard_tine20.lang
%defattr(-,root,root,-)

