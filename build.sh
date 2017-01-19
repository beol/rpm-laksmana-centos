#!/bin/env bash

set -ev

BASE_DIR=$(dirname $0)

cd $BASE_DIR

mkdir -p rpmbuild/SOURCES
cp -p laksmana-centos.repo RPM-GPG-KEY-laksmana rpmbuild/SOURCES

rpmbuild -bb laksmana-centos-repo.spec

[[ -n "${GPG_PASSPHRASE}" ]] && find ./rpmbuild/RPMS -type f -name "*.rpm" | xargs -I{} sh -c "./rpm-sign.exp {} && rpm --checksig {}"
