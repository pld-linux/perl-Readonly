#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Readonly
Summary:	Readonly - Facility for creating read-only scalars, arrays, hashes.
#Summary(pl):	Readonly
Name:		perl-Readonly
Version:	0.07
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/authors/id/R/RO/ROODE/%{pdir}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
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

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
perl Makefile.PL
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
%{perl_sitelib}/*.pm
%{_mandir}/man3/*
