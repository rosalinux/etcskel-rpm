Summary:	MandrivaLinux default files for new users' home directories
Name:		etcskel
Version:	1.63
Release:	%mkrel 20
License:	Public Domain
Group:		System/Base
# get the source from our cvs repository (see
# http://www.linuxmandrake.com/en/cvs.php3)
Source:		%{name}-%{version}.tar.bz2
Requires:	bash
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The etcskel package is part of the basic Mandriva system.

Etcskel provides the /etc/skel directory's files. These files are then placed
in every new user's home directory when new accounts are created.

%prep
%setup -q

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog
%config(noreplace) /etc/skel


