%define	name	libsigsegv
%define	version	2.3
%define	release	%mkrel 1

%define	major	0
%define	libname	%mklibname sigsegv %{major}

Summary:	Library for handling page faults in user mode
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		http://libsigsegv.sourceforge.net/
Source0:	http://ftp.gnu.org/gnu/libsigsegv/%{name}-%{version}.tar.gz
Group:		System/Libraries
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

%package -n	%{libname}
Summary:	Library for handling page faults in user mode
Group:		System/Libraries

%description -n	%{libname}
This is a library for handling page faults in user mode. A page fault
occurs when a program tries to access to a region of memory that is
currently not available. Catching and handling a page fault is a useful
technique for implementing:
  - pageable virtual memory,
  - memory-mapped access to persistent databases,
  - generational garbage collectors,
  - stack overflow handlers,
  - distributed shared memory,

%package -n	%{libname}-devel
Summary:	Development libraries and header files for %{name} 
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libname}-devel
Libraries and header files for %{name} development.

%package -n     %{libname}-static-devel
Summary:        Static development libraries for %{name}
Group:          Development/C
Requires:       %{libname}-devel = %{version}
Provides:       %{name}-static-devel = %{version}-%{release}

%description -n %{libname}-static-devel
Static development libraries for %{name} development.


%prep
%setup -q

%build
%configure	--enable-shared \
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
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_includedir}/*

%files -n %{libname}-static-devel
%{_libdir}/lib*.a

