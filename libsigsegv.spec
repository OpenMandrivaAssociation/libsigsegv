%define major 2
%define libname %mklibname sigsegv %{major}
%define develname %mklibname sigsegv -d
%define staticname %mklibname sigsegv -d -s

Summary:	Library for handling page faults in user mode
Name:		libsigsegv
Version:	2.10
Release:	%mkrel 4
License:	GPLv2+
Group:		System/Libraries
URL:		http://libsigsegv.sourceforge.net/
Source0:	http://ftp.gnu.org/gnu/libsigsegv/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a library for handling page faults in user mode. A page fault
occurs when a program tries to access to a region of memory that is
currently not available. Catching and handling a page fault is a useful
technique for implementing:
  - pageable virtual memory,
  - memory-mapped access to persistent databases,
  - generational garbage collectors,
  - stack overflow handlers,
  - distributed shared memory,

%package -n %{libname}
Summary:	Library for handling page faults in user mode
Group:		System/Libraries

%description -n %{libname}
This is a library for handling page faults in user mode. A page fault
occurs when a program tries to access to a region of memory that is
currently not available. Catching and handling a page fault is a useful
technique for implementing:
  - pageable virtual memory,
  - memory-mapped access to persistent databases,
  - generational garbage collectors,
  - stack overflow handlers,
  - distributed shared memory,

%package -n %{develname}
Summary:	Development libraries and header files for %{name} 
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname sigsegv 0 -d

%description -n	%{develname}
Libraries and header files for %{name} development.

%package -n %{staticname}
Summary:	Static development libraries for %{name}
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
Obsoletes:	%mklibname -d -s sigsegv 0

%description -n %{staticname}
Static development libraries for %{name} development.

%prep
%setup -q

%build
%configure2_5x \
    --libdir=/%{_lib} \
    --enable-shared \
    --enable-static
%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std

rm -f %{buildroot}/%{_lib}/*.la
rm -f %{buildroot}/%{_lib}/*.so

install -d %{buildroot}%{_libdir}
ln -s /%{_lib}/libsigsegv.so.%{major} %{buildroot}%{_libdir}/libsigsegv.so
mv %{buildroot}/%{_lib}/lib*.a %{buildroot}%{_libdir}/

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
/%{_lib}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_includedir}/*

%files -n %{staticname}
%{_libdir}/lib*.a


%changelog
* Sun Apr 17 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2.10-1mdv2011.0
+ Revision: 654571
- update to new version 2.10

* Sun Nov 28 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 2.9-1mdv2011.0
+ Revision: 602351
- update to new version 2.9

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 2.8-2mdv2010.1
+ Revision: 519776
- move the libraries to /%%{_lib}/

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 2.8-1mdv2010.1
+ Revision: 519533
- 2.8

* Sun Aug 09 2009 Frederik Himpe <fhimpe@mandriva.org> 2.7-1mdv2010.0
+ Revision: 412924
- Update to new version 2.7 (new major)

* Sun Jul 26 2009 Funda Wang <fwang@mandriva.org> 2.6-2mdv2010.0
+ Revision: 400115
- drop invalid provides

* Mon Aug 25 2008 Emmanuel Andry <eandry@mandriva.org> 2.6-1mdv2009.0
+ Revision: 275824
- ?\194New version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.5-3mdv2009.0
+ Revision: 223002
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Nov 26 2007 Funda Wang <fwang@mandriva.org> 2.5-2mdv2008.1
+ Revision: 112165
- fix requires of static devel package

* Mon Nov 12 2007 Funda Wang <fwang@mandriva.org> 2.5-1mdv2008.1
+ Revision: 108148
- New version 2.5

* Sat Oct 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.4-1mdv2008.1
+ Revision: 102659
- new version
- new license policy
- new devel library policy
- spec file clean


* Sat May 20 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.3-1mdk
- initial release

