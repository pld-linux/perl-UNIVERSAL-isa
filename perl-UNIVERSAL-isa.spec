#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	UNIVERSAL
%define		pnam	isa
Summary:	UNIVERSAL::isa - Hack around module authors using UNIVERSAL::isa as a function
Summary(pl.UTF-8):	UNIVERSAL::isa - poprawianie autorów modułów używających UNIVERSAL::isa jako funkcji
Name:		perl-UNIVERSAL-isa
Version:	1.03
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/UNIVERSAL/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0643f2e04cd0b5739fc0908af291c609
URL:		http://search.cpan.org/dist/UNIVERSAL-isa/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Whenever you use UNIVERSAL/isa as a function, a kitten using
Test::MockObject dies. Normally, the kittens would be helpless, but if
they use UNIVERSAL::isa (the module whose docs you are reading), the
kittens can live long and prosper.

This module replaces UNIVERSAL::isa with a version that makes sure
that if it's called as a function on objects which override isa, isa
will be called on those objects as a method.

In all other cases the real UNIVERSAL::isa is just called directly.

%description -l pl.UTF-8
Przy każdym użyciu UNIVERSAL/isa jako funkcji kotek używający
Test::MockObject umiera. Normalnie kotki byłyby bezbronne, ale jeśli
używają UNIVERSAL::isa (czyli tego modułu), kotki mogą żyć długo i
szczęśliwie.

Ten moduł zastępuje UNIVERSAL::isa wersją sprawdzającą, czy jeśli jest
wywoływana jako funkcja na obiekcie przykrywającym isa, isa będzie
wywołana na tych obiektach jako metoda.

We wszystkich innych przypadkach prawdziwa UNIVERSAL::isa będzie
wywołana bezpośrednio.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/UNIVERSAL/*.pm
%{_mandir}/man3/*
