%define svn		0
%define rel		1
%if %svn
%define release		%mkrel 0.%svn.%rel
%define distname	%name-%svn.tar.lzma
%define	dirname		synce-gvfs
%else
%define release		%mkrel %rel
%define distname	%name-%version.tar.gz
%define dirname		%name-%version
%endif

Name:		synce-gvfs
Summary:	Access Windows Mobile device filesystems via GVFS
Version:	0.2.2
Release:	%{release}
License:	MIT
Source0:	http://downloads.sourceforge.net/synce/%{distname}
# synce-gvfs just copies a lot of source straight from gvfs; to build
# and work with gvfs 0.9x we have to re-copy these files from gvfs
# source tree (see also the patch) - AdamW 2008/09
#Source1:	gvfs-0.99.6.tar.bz2
#Patch0:		synce-gvfs-0.1.1-gvfs1.patch
#Patch1:		synce-gvfs-0.1.1-autogen.patch
URL:		http://synce.sourceforge.net/
Group:		Communications
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libsynce-devel
BuildRequires:	librapi-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libgvfs-devel
BuildRequires:	intltool
%if svn
BuildRequires:	gnome-common
%endif
Requires:	gvfs

%description
Synce-gvfs is part of the SynCE project. GVFS is the GNOME virtual file
system - an infrastructure for accessing various things as if they were
simply a local filesystem. This GVFS backend lets you access the
contents of Windows Mobile-based mobile devices via GVFS - just browse
to synce:/// in Nautilus or any other GVFS-compliant application.

%prep
%setup -q -n %{dirname}
#%patch0 -p1 -b .gvfs1
#%patch1 -p1 -b .autogen

%build
#pushd make-dist
#sed -i -e 's,GVFS_SRC_DIR,%{_builddir}/gvfs-0.99.6,g' make-dist.sh
#sh ./make-dist.sh
#popd

%if %svn
./autogen.sh
%endif
%configure2_5x --disable-mime-update
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_mime_database
%endif

%if %mdkversion < 200900
%postun
%clean_mime_database
%endif

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog 
%{_libdir}/gvfsd-*
%{_datadir}/gvfs/mounts/synce.mount
%{_iconsdir}/gnome/*/apps/*.png
%{_datadir}/mime/packages/synce-gvfs.xml



