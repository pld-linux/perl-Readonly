#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Readonly
Summary:	Readonly - facility for creating read-only scalars, arrays, hashes
Summary(pl.UTF-8):	Readonly - udogodnienie do tworzenia zmiennych tylko do odczytu
Name:		perl-Readonly
Version:	2.05
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SA/SANKO/%{pdir}-%{version}.tar.gz
# Source0-md5:	acae851d7d55c509f5f00a8849597e54
URL:		http://search.cpan.org/dist/Readonly/
BuildRequires:	perl-Module-Build-Tiny >= 0.035
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test-Harness
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a facility for creating non-modifiable variables. This is
useful for configuration files, headers, etc. It can also be useful as
a development and debugging tool, for catching updates to variables
that should not be changed.

%description -l pl.UTF-8
Readonly umożliwia tworzenie niemodyfikowalnych zmiennych.  Jest to
użyteczne w plikach konfiguracyjnych, nagłówkach, itp.  Może być także
przydatne jako narzędzie do rozwijania programów i wyszukiwania
błędów, wyłapując próby zapisu do zmiennych, które nie powinny być
zmieniane.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Build.PL

./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	--destdir=$RPM_BUILD_ROOT \
	--installdirs=vendor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorlib}/Readonly.pm
%{_mandir}/man3/Readonly.3pm*
