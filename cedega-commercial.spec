Summary:	A commercial version of cedega WINE
Summary(pl):	Komercyjna wersja WINE w wersji cedega
Name:		cedega-commercial
Version:	4.0
Release:	1
Copyright:	 2000-2004 TransGaming Technologies Inc.
#License:	Check /usr/share/doc/cedega/copyright
Group:		Applications
Vendor:		TransGaming Technologies Inc.
Source0:	cedega_%{version}-1.i386.tgz
# NoSource0-md5:	438e04b5e065ae52c6a5c26fd8f5c95
URL:		http://www.transgaming.com
BuildRequires:	tar
Requires:       OpenGL
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         no_install_post_strip   1

%description
A modified  WINE version with DirectX 9 support.

%description -l pl
Rozszerzona wersja WINE z obs³ug± DirectX 9.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__tar} xfz %{SOURCE0} -C $RPM_BUILD_ROOT

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

# The licence
%{_defaultdocdir}/cedega
