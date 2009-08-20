%define upstream_name	 VCS-Lite
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Minimal upstream_version control system
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/I/IV/IVORW/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires: perl-devel
%endif
Buildrequires: perl-Algorithm-Diff
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides the functions normally associated 
with a version control system, but without needing or 
implementing a version control system. Applications 
include wikis, document management systems and configuration 
management.

It makes use of the module Algorithm::Diff. It provides the 
facility for basic diffing, patching and merging.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
