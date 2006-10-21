#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	UNIVERSAL
%define		pnam	isa
Summary:	UNIVERSAL::isa - Hack around module authors using UNIVERSAL::isa as a function
Summary(pl):	UNIVERSAL::isa - poprawianie autorów modu³ów u¿ywaj±cych UNIVERSAL::isa jako funkcji
Name:		perl-UNIVERSAL-isa
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	835c9aa89e18521767c9c13b6c9f50d3
URL:		http://search.cpan.org/dist/UNIVERSAL-isa/
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

%description -l pl
Przy ka¿dym u¿yciu UNIVERSAL/isa jako funkcji kotek u¿ywaj±cy
Test::MockObject umiera. Normalnie kotki by³yby bezbronne, ale je¶li
u¿ywaj± UNIVERSAL::isa (czyli tego modu³u), kotki mog± ¿yæ d³ugo i
szczê¶liwie.

Ten modu³ zastêpuje UNIVERSAL::isa wersj± sprawdzaj±c±, czy je¶li jest
wywo³ywana jako funkcja na obiekcie przykrywaj±cym isa, isa bêdzie
wywo³ana na tych obiektach jako metoda.

We wszystkich innych przypadkach prawdziwa UNIVERSAL::isa bêdzie
wywo³ana bezpo¶rednio.

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
