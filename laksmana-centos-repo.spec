Name: laksmana-centos-repo
Version: 6
Release: 1
Summary: Laksmana CentOS RPM Repository
License: GPLv2
Group: System Environment/Base
BuildArch: noarch

%description
This package contains packages for Laksmana CentOS 6 RPM repository configuration
and GPG key.

%prep
exit 0

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp -p %{_builddir}/%{name}/laksmana-centos.repo ${RPM_BUILD_ROOT}%{_sysconfdir}/yum.repos.d/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/
cp -p %{_builddir}/%{name}/RPM-GPG-KEY-laksmana ${RPM_BUILD_ROOT}%{_sysconfdir}/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sysconfdir}/yum.repos.d/laksmana-centos.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-laksmana
