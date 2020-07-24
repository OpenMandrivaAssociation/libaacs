%define major	0
%define libname	%mklibname aacs %major
%define libname	%mklibname aacs %major
%define devnamest %mklibname aacs -d -s
%define devname %mklibname aacs -d

Summary:	implementation of the libaacs standard
Name:		libaacs
Version:	0.11.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.videolan.org
Source0:	http://download.videolan.org/pub/videolan/libaacs/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	libgcrypt-devel
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	flex

%description
The doom9 researchers and the libaacs 
developers would like to present the 
first official release
of their library of the implementation
of the libaacs standard.

%package -n %{libname}
Summary:	implementation of the libaacs standard
Group:		System/Libraries

%description -n %{libname}
The doom9 researchers and the libaacs 
developers would like to present the 
first official release 
of their library of the implementation
of the libaacs standard.

%package -n %{devname}
Summary:	libaacs development files
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	aacs-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}

%package -n %{devnamest}
Summary:	libaacs development static lib
Group:		Development/C
Provides:	%{name}-devel-static = %{version}-%{release}
Provides:	aacs-devel-static = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	aacs-devel = %{version}-%{release}

%description -n %{devnamest}
Development static lib for %{name}

%prep
%setup -q
%autopatch -p1

%build
%configure --enable-static
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*
%{_bindir}/aacs_info

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n %{devnamest}
%{_libdir}/*.a
