FROM centos:centos6
MAINTAINER Leo Laksmana <beol@laksmana.com>

RUN yum -y install \
           expect \
           rpm-build

WORKDIR /etc/pki/rpm-gpg
COPY RPM-GPG-KEY-laksmana .
RUN rpm --import RPM-GPG-KEY-laksmana

RUN useradd -m -d /source -u 1000 rpmbuild

WORKDIR /source
USER rpmbuild
