#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Readonly
Summary:	Readonly - facility for creating read-only scalars, arrays, hashes
Summary(pl):	Readonly - udogodnienie do tworzenia zmiennych tylko do odczytu
Name:		perl-Readonly
Version:	1.02
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/R/RO/ROODE/%{pdir}-%{version}.tar.gz
# Source0-md5:	c5da5b0da4a1d6fdbefb15385e9d1baf
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test-Harness
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This is a facility for creating non-modifiable variables.  This is
useful for configuration files, headers, etc.  It can also be useful as
a development and debugging tool, for catching updates to variables that
should not be changed.

%description -l pl
Readonly umo¿liwia tworzenie niemodyfikowalnych zmiennych.  Jest to
u¿yteczne w plikach konfiguracyjnych, nag³ówkach, itp.  Mo¿e byæ tak¿e
przydatne jako narzêdzie do rozwijania programów i wyszukiwania b³êdów,
wy³apuj±c próby zapisu do zmiennych, które nie powinny byæ zmieniane.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
