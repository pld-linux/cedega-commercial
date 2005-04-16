Summary:	A commercial version of cedega WINE
Summary(pl):	Komercyjna wersja WINE w wersji cedega
Name:		cedega-commercial
Version:	4.3.1
Release:	1
License:	Check /usr/share/doc/cedega/copyright
Group:		Applications
Vendor:		TransGaming Technologies Inc.
Source0:	cedega_%{version}-1.i386.tgz
URL:		http://www.transgaming.com
BuildRequires:	sed >= 4.0
BuildRequires:	tar
Requires:	OpenGL
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%description
A modified WINE version with DirectX 9 support.

%description -l pl
Rozszerzona wersja WINE z obs³ug± DirectX 9.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__tar} xfz %{SOURCE0} -C $RPM_BUILD_ROOT

# cedega is a bash script
%{__sed} -i -e 's,#!/bin/sh,#!/bin/bash,' $RPM_BUILD_ROOT%{_bindir}/cedega

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# The symlink
%attr(755,root,root) %{_bindir}/cedega
%dir %{_libdir}/transgaming_cedega/
%{_libdir}/transgaming_cedega/*.*

# The windows C drive and Program files
%{_libdir}/transgaming_cedega/.transgaming/

# The implementation
%dir %{_libdir}/transgaming_cedega/winex/
%dir %{_libdir}/transgaming_cedega/winex/bin
%dir %{_libdir}/transgaming_cedega/winex/*lib
%attr(755,root,root) %{_libdir}/transgaming_cedega/winex/bin/*
%attr(755,root,root) %{_libdir}/transgaming_cedega/winex/*lib/*.so*
%{_libdir}/transgaming_cedega/winex/*lib/*.a
%{_mandir}/man1/cedega.1*
# The licence
%{_defaultdocdir}/cedega
