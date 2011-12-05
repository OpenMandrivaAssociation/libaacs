%define major	0
%define libname	%mklibname aacs %major
%define devname %mklibname aacs -d

Summary:	implementation of the libaacs standard
Name:		libaacs
Version:	0.3.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.videolan.org
Source:		ftp://ftp.videolan.org/pub/videolan/libaacs/0.3.0/%{name}-%{version}.tar.bz2

BuildRequires:	libgcrypt-devel

%description
The doom9 researchers and the libaacs developers would like to present the first official release
of their library of the implementation of the libaacs standard.

%package -n %{libname}
Summary:	implementation of the libaacs standard
Group:		System/Libraries

%description -n %{libname}
The doom9 researchers and the libaacs developers would like to present the first official release 
of their library of the implementation of the libaacs standard.

%package -n %{devname}
Summary:	libaacs development files
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	aacs-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}


%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std
rm %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
