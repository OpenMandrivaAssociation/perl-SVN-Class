%define upstream_name    SVN-Class
%define upstream_version 0.17
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.17
Release:	1

Summary:	Represents the repository of a Subversion workspace
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SVN/SVN-Class-0.17.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Data::Dump)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IPC::Cmd)
BuildRequires:	perl(IPC::Run)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Path::Class::File::Stat)
BuildRequires:	perl(Rose::Object)
BuildRequires:	perl(Rose::URI)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::ParseWords)
BuildArch:	noarch

%description
SVN::Class extends Path::Class to allow for basic Subversion workspace
management. SVN::Class::File and SVN::Class::Dir are subclasses of
Path::Class::File::Stat and Path::Class::Dir respectively.

SVN::Class does not use the SVN::Core Subversion SWIG bindings. Instead,
the 'svn' binary tool is used for all interactions, using IPC::Cmd. This
design decision was made for maximum portability and to eliminate non-CPAN
dependencies.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%if %{?_with_test:1}%{!?_with_test:0}
%make test
%endif

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.160.0-2mdv2011.0
+ Revision: 657831
- rebuild for updated spec-helper

* Tue Oct 26 2010 Buchan Milne <bgmilne@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 589497
- import perl-SVN-Class


