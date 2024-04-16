Summary:	HEVC decoder
Summary(pl.UTF-8):	Dekoder HEVC
Name:		openHEVC
Version:	2.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/OpenHEVC/openHEVC/tags
Source0:	https://github.com/OpenHEVC/openHEVC/archive/openhevc-%{version}/%{name}-openhevc-%{version}.tar.gz
# Source0-md5:	efc4e49ef9b0ba87ff6eb60d2ea3e1d8
Patch0:		%{name}-sysctl.patch
Patch1:		%{name}-asm.patch
Patch2:		%{name}-libdir.patch
URL:		https://github.com/OpenHEVC/openHEVC
BuildRequires:	SDL2-devel >= 2.0
BuildRequires:	cmake >= 2.8
BuildRequires:	yasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
openHEVC is a fork of Libav with only the files needed to decode HEVC
content, it was created for research purposes.

%description -l pl.UTF-8
openHEVC do odgałęzienie Libav zawierające tylko pliki potrzebne do
dekodowania treści HEVC, stworzone do celów badawczych.

%package devel
Summary:	Header files for openHEVC library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki openHEVC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for openHEVC library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki openHEVC.

%prep
%setup -q -n %{name}-openhevc-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
install -d build
cd build
%ifarch %{ix86}
CFLAGS="%{rpmcflags} -DX86_32"
%endif
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libLibOpenHevcWrapper.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/hevcdsp.h
%{_includedir}/hevcpred.h
%{_includedir}/openHevcWrapper.h
