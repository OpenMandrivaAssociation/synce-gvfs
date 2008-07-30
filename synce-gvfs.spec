%define svn		0
%define rel		1
%if %svn
%define release		%mkrel 0.%svn.%rel
%define distname	%name-%svn.tar.lzma
%define	dirname		gvfs
%else
%define release		%mkrel %rel
%define distname	%name-%version.tar.gz
%define dirname		%name-%version
%endif

Name:		synce-gvfs
Summary:	SynCE tray icon for GNOME
Version:	0.1
Release:	%{release}
License:	MIT
Source0:	http://downloads.sourceforge.net/synce/%{distname}
URL:		http://synce.sourceforge.net/
Group:		Communications
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libsynce-devel
BuildRequires:	librapi-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libgvfs-devel
Requires:	gvfs

%description
Synce-gvfs is part of the SynCE project. GVFS is the GNOME virtual file
system - an infrastructure for accessing various things as if they were
simply a local filesystem. This GVFS backend lets you access the
contents of Windows Mobile-based mobile devices via GVFS - just browse
to synce:/// in Nautilus or any other GVFS-compliant application.

%prep
%setup -q -n %{dirname}

%build
%if %svn
./autogen.sh
%endif
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog 
%{_libdir}/gvfsd-*
%{_datadir}/gvfs/mounts/synce.mount
%{_iconsdir}/gnome/*/apps/*.png

