#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Lingua-Translit
Version  : 0.28
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/A/AL/ALINKE/Lingua-Translit-0.28.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AL/ALINKE/Lingua-Translit-0.28.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblingua-translit-perl/liblingua-translit-perl_0.28-1.debian.tar.xz
Summary  : transliterates text between writing systems
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Lingua-Translit-bin = %{version}-%{release}
Requires: perl-Lingua-Translit-license = %{version}-%{release}
Requires: perl-Lingua-Translit-man = %{version}-%{release}
Requires: perl-Lingua-Translit-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Perl Module Lingua::Translit
----------------------------
ABOUT
Lingua::Translit can be used to convert text from one writing system to
another, based on national or international transliteration tables.
Where possible a reverse transliteration is supported.

%package bin
Summary: bin components for the perl-Lingua-Translit package.
Group: Binaries
Requires: perl-Lingua-Translit-license = %{version}-%{release}

%description bin
bin components for the perl-Lingua-Translit package.


%package dev
Summary: dev components for the perl-Lingua-Translit package.
Group: Development
Requires: perl-Lingua-Translit-bin = %{version}-%{release}
Provides: perl-Lingua-Translit-devel = %{version}-%{release}
Requires: perl-Lingua-Translit = %{version}-%{release}

%description dev
dev components for the perl-Lingua-Translit package.


%package license
Summary: license components for the perl-Lingua-Translit package.
Group: Default

%description license
license components for the perl-Lingua-Translit package.


%package man
Summary: man components for the perl-Lingua-Translit package.
Group: Default

%description man
man components for the perl-Lingua-Translit package.


%package perl
Summary: perl components for the perl-Lingua-Translit package.
Group: Default
Requires: perl-Lingua-Translit = %{version}-%{release}

%description perl
perl components for the perl-Lingua-Translit package.


%prep
%setup -q -n Lingua-Translit-0.28
cd %{_builddir}
tar xf %{_sourcedir}/liblingua-translit-perl_0.28-1.debian.tar.xz
cd %{_builddir}/Lingua-Translit-0.28
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Lingua-Translit-0.28/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Lingua-Translit
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Lingua-Translit/5b393c2adae1e322316aff4db87c45cd20027db7
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/translit

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Lingua::Translit.3
/usr/share/man/man3/Lingua::Translit::Tables.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Lingua-Translit/5b393c2adae1e322316aff4db87c45cd20027db7

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/translit.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
