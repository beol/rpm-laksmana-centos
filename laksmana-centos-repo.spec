Name: laksmana-centos-repo
Version: 6
Release: 1
Summary: Laksmana CentOS 6 RPM Repository
License: MIT
Group: System Environment/Base
Source0: laksmana-centos.repo
Source1: RPM-GPG-KEY-laksmana
BuildRoot:	%{_tmppath}/%{_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
This package contains Laksmana CentOS 6 RPM yum repository configuration
and GPG key.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
install -m 644 %{SOURCE0} ${RPM_BUILD_ROOT}%{_sysconfdir}/yum.repos.d/

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/
install -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sysconfdir}/yum.repos.d/laksmana-centos.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-laksmana
