Summary: Create deltas between rpms
Name: deltarpm
Version: 3.6
Release: 1
License: BSD
Group: Applications/System
Vendor:		VMware, Inc.
Distribution: Photon
URL: http://www.novell.com/products/linuxpackages/professional/deltarpm.html
Source0: ftp://ftp.suse.com/pub/projects/deltarpm/deltarpm-%{version}.tar.bz2
BuildRequires: rpm-devel >= 4.2
BuildRequires: bzip2-devel
Requires: perl
BuildRequires: xz-devel
BuildRequires: popt-devel
BuildRequires: python2
%description
A deltarpm contains the difference between an old
and a new version of a rpm, which makes it possible
to recreate the new rpm from the deltarpm and the old
one. You don't have to have a copy of the old rpm,
deltarpms can also work with installed rpms.

%prep
%setup

%build
%{__make} %{?_smp_mflags} prefix="%{_prefix}" mandir="%{_mandir}"
%{__make} %{?_smp_mflags} prefix="%{_prefix}" mandir="%{_mandir}" python

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}" mandir="%{_mandir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE.BSD README
%doc %{_mandir}/man8/applydeltaiso.8*
%doc %{_mandir}/man8/applydeltarpm.8*
%doc %{_mandir}/man8/combinedeltarpm.8*
%doc %{_mandir}/man8/drpmsync.8*
%doc %{_mandir}/man8/makedeltaiso.8*
%doc %{_mandir}/man8/makedeltarpm.8*
%doc %{_mandir}/man8/fragiso.8*
%{_bindir}/applydeltaiso
%{_bindir}/applydeltarpm
%{_bindir}/combinedeltarpm
%{_bindir}/drpmsync
%{_bindir}/makedeltaiso
%{_bindir}/makedeltarpm
%{_bindir}/rpmdumpheader
%{_bindir}/fragiso

%changelog
* Fri Mar 09 2007 Dag Wieers <dag@wieers.com> - 3.3-2
- Fixed group.

* Sat Dec 03 2005 Dries Verachtert <dries@ulyssis.org> - 3.3-1
- Initial package.
