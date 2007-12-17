%define module	VCS-Lite
%define name	perl-%{module}
%define version 0.08
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Minimal version control system
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/I/IV/IVORW/%{module}-%{version}.tar.gz
URL:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
Buildrequires: perl-devel
%endif
Buildrequires: perl-Algorithm-Diff
BuildArch:	noarch

%description
This module provides the functions normally associated 
with a version control system, but without needing or 
implementing a version control system. Applications 
include wikis, document management systems and configuration 
management.

It makes use of the module Algorithm::Diff. It provides the 
facility for basic diffing, patching and merging.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{perl_vendorlib}/VCS
%{_mandir}/*/*

