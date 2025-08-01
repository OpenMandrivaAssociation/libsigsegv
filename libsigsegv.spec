%define major 2
%define libname %mklibname sigsegv %{major}
%define devname %mklibname sigsegv -d

Summary:	Library for handling page faults in user mode
Name:		libsigsegv
Version:	2.15
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		https://libsigsegv.sourceforge.net/
Source0:	http://ftp.gnu.org/gnu/libsigsegv/%{name}-%{version}.tar.gz
Patch1:		SIGSTKSZ-adjust.patch
Patch2:		no-stackhandler-on-s390.patch
Patch4:		libsigsegv-2.10-musl.patch

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

%package -n %{devname}
Summary:	Development libraries and header files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Libraries and header files for %{name} development.

%prep
%autosetup -p1
autoreconf -fiv

%build
%configure \
	--enable-shared \
	--disable-static

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libsigsegv.so.%{major}*

%files -n %{devname}
%doc AUTHORS NEWS README
%{_libdir}/lib*.so
%{_includedir}/*
