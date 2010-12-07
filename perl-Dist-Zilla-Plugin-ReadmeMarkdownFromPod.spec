%define upstream_name    Dist-Zilla-Plugin-ReadmeMarkdownFromPod
%define upstream_version 0.100700

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Automatically convert POD to a README.mkdn for Dist::Zilla
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Dist::Zilla::File::InMemory)
BuildRequires: perl(Dist::Zilla::Role::InstallTool)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Autobox)
BuildRequires: perl(Pod::Markdown)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Generate a README.mkdn from 'main_module' by the Pod::Markdown manpage

The code is mostly a copy-paste of the Dist::Zilla::Plugin::ReadmeFromPod
manpage

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README META.yml LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*


