Name:		become
Version:	0.1
Release:	5
URL:		http://www.bindshell.net/tools/become
Source:		http://www.bindshell.net/tools/become/become.tgz
Summary:	Utility to changes the effective, or real, user and group id
License:	BSD
Group:		System/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description
The become utility changes the current effective, or real, user and
group identity to those specified on the command line. The default shell
(/bin/sh) is then executed.
UID and GID are specified numercially and do not have to be currently
defined on the system.

%prep
%setup -q -n %{name}

%build
%{make}
lzma become.8

%install
%{__rm} -Rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_sbindir} %{buildroot}%{_mandir}/man8
%{__install} -c become %{buildroot}%{_sbindir}
%{__install} -c -m 644 become.8.lzma %{buildroot}%{_mandir}/man8

%files
%doc LICENSE
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8.*



%changelog
* Tue Sep 01 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.1-4mdv2010.0
+ Revision: 424029
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1-3mdv2009.0
+ Revision: 243210
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1-1mdv2008.1
+ Revision: 167826
- fix no-buildroot-tag

* Fri Aug 17 2007 Nicolas Vigier <nvigier@mandriva.com> 0.1-1mdv2008.0
+ Revision: 65018
- Import become

