#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kmail-account-wizard
Version  : 24.12.0
Release  : 113
URL      : https://download.kde.org/stable/release-service/24.12.0/src/kmail-account-wizard-24.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.0/src/kmail-account-wizard-24.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.0/src/kmail-account-wizard-24.12.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: kmail-account-wizard-bin = %{version}-%{release}
Requires: kmail-account-wizard-data = %{version}-%{release}
Requires: kmail-account-wizard-license = %{version}-%{release}
Requires: kmail-account-wizard-locales = %{version}-%{release}
Requires: gpgme-extras
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : gpgme-dev
BuildRequires : gpgme-extras
BuildRequires : kcontacts-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kimap-dev
BuildRequires : kimap-staticdev
BuildRequires : kldap-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kpimtextedit-dev
BuildRequires : ktexteditor-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : libkdepim-dev
BuildRequires : libkleo-dev
BuildRequires : pimcommon-dev
BuildRequires : qt6base-dev
BuildRequires : qtkeychain-dev
BuildRequires : qttools-dev
BuildRequires : shared-mime-info
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Analyzing Build Performance
For debug build time:
We need ClangBuildAnalyzer
git clone https://github.com/aras-p/ClangBuildAnalyzer
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=<path> ../
make install

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kmail-account-wizard-24.12.0
cd %{_builddir}/kmail-account-wizard-24.12.0
pushd ..
cp -a kmail-account-wizard-24.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735268431
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735268431
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmail-account-wizard
cp %{_builddir}/kmail-account-wizard-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kmail-account-wizard/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kmail-account-wizard-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kmail-account-wizard/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kmail-account-wizard-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kmail-account-wizard/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kmail-account-wizard-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmail-account-wizard/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kmail-account-wizard-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmail-account-wizard/20079e8f79713dce80ab09774505773c926afa2a || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang accountwizard
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/accountwizard
/usr/bin/accountwizard

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.accountwizard.desktop
/usr/share/metainfo/org.kde.accountwizard.appdata.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmail-account-wizard/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kmail-account-wizard/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kmail-account-wizard/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kmail-account-wizard/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kmail-account-wizard/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f accountwizard.lang
%defattr(-,root,root,-)

