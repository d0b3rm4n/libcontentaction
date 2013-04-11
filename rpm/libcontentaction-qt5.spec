# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       libcontentaction-qt5

# >> macros
# << macros

Summary:    Library for associating content with actions
Version:    0.1.74
Release:    1
Group:      System/Desktop
License:    LGPLv2.1
URL:        https://github.com/nemomobile/libcontentaction
Source0:    libcontentaction-%{version}.tar.bz2
Source1:    %{name}.rpmlintrc
Source100:  libcontentaction-qt5.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(mlite5)
BuildRequires:  pkgconfig(mlocale5)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5SystemInfo)
BuildRequires:  python

%description
libcontentaction is a library for associating content with actions.


%package devel
Summary:    Development files for libcontentaction
Group:      Development/System
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains development files for building applications using
libcontentaction library.


%package tests
Summary:    Tests for libcontentaction
Group:      System/X11
Requires:   %{name} = %{version}-%{release}
Requires:   dbus-python
Requires:   pygobject2
Requires:   python
Requires:   tracker-utils

%description tests
This package contains the tests for libcontentaction library.



%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/lca-tool5
%{_datadir}/contentaction5/highlight1.xml
%{_datadir}/contentaction5/tracker1.xml
%{_libdir}/libcontentaction5.so.*
%exclude %{_datadir}/applications/defaults.list
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_includedir}/contentaction5/contentaction.h
%{_includedir}/contentaction5/contentinfo.h
%{_libdir}/libcontentaction5.so
%{_libdir}/pkgconfig/contentaction5.pc
# >> files devel
# << files devel

%files tests
%defattr(-,root,root,-)
/opt/tests/libcontentaction5/*
# >> files tests
# << files tests
