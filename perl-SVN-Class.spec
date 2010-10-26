%define upstream_name    SVN-Class
%define upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Represents the repository of a Subversion workspace
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/SVN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Data::Dump)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IPC::Cmd)
BuildRequires: perl(IPC::Run)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Path::Class::File::Stat)
BuildRequires: perl(Rose::Object)
BuildRequires: perl(Rose::URI)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::ParseWords)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%if %{?_with_test:1}%{!?_with_test:0}
#export SVN_CLASS_TMP_DIR=/tmp/%{name}-%{version}-test
%make test
#rm -Rf $SVN_CLASS_TMP_DIR
%endif

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


