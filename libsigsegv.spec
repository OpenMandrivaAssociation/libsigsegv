%define name libsigsegv
%define version 2.5
%define release %mkrel 1

%define major 0
%define libname %mklibname sigsegv %{major}
%define develname %mklibname sigsegv -d
%define staticname %mklibname sigsegv -d -s

Summary:	Library for handling page faults in user mode
Name:		%{name}
Version:	%{version}
Release:	%{release}
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
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname sigsegv 0 -d

%description -n	%{develname}
Libraries and header files for %{name} development.

%package -n %{staticname}
Summary:	Static development libraries for %{name}
Group:		Development/C
Requires:	%{libname}-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n %{staticname}
Static development libraries for %{name} development.

%prep
%setup -q

%build
%configure2_5x \
	--enable-shared \
	--enable-static

%make

%check
make check

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_includedir}/*

%files -n %{staticname}
%{_libdir}/lib*.a
