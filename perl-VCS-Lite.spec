%define upstream_name	 VCS-Lite
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Minimal upstream_version control system
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/I/IV/IVORW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Algorithm::Diff)
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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{_bindir}/*
%{perl_vendorlib}/VCS
%{_mandir}/*/*


%changelog
* Thu Aug 20 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 418634
- update to 0.09
- update to 0.08
- update to 0.08
- update to 0.08
- update to 0.08

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 401919
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.08-4mdv2009.0
+ Revision: 242148
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.08-2mdv2008.0
+ Revision: 23602
- rebuild


* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdk
- New release 0.08
- spec cleanup

* Sat Nov 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.07-2mdk
- Fix BuildRequires

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.07-1mdk
- First mandriva release ( needed by WWW-Mediawiki-Client )

