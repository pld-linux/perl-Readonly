#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Readonly
Summary:	Readonly - facility for creating read-only scalars, arrays, hashes
Summary(pl):	Readonly - udogodnienie do tworzenia zmiennych tylko do odczytu
Name:		perl-Readonly
Version:	1.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/R/RO/ROODE/%{pdir}-%{version}.tar.gz
# Source0-md5:	0acef3a995ac9ecf575f66a726d638f4
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
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

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
