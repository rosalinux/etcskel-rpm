Summary:	Mandriva Linux default files for new users' home directories
Name:		etcskel
Version:	1.63
Release:	38
License:	Public Domain
Group:		System/Base
# get the source from our cvs repository (see
# http://cvs.mandriva.com)
Source0:	%{name}-%{version}.tar.xz
Source1:	etcskel.rpmlintrc
BuildArch:	noarch
Requires:	bash

%description
The etcskel package is part of the basic Mandriva system.

Etcskel provides the /etc/skel directory's files. These files are then placed
in every new user's home directory when new accounts are created.

%prep
%setup -q

%install
%makeinstall_std
mkdir -p %{buildroot}%{_sysconfdir}/skel/.cache
chmod 0755 %{buildroot}%{_sysconfdir}/skel/.cache

%files
%doc ChangeLog
%config(noreplace) %{_sysconfdir}/skel
