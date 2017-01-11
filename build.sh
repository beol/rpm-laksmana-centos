#!/bin/env bash

set -ev

BASE_DIR=$(dirname $0)

mkdir -p $BASE_DIR/rpmbuild/BUILD/laksmana-centos-repo
cp -p $BASE_DIR/{RPM-GPG-KEY-laksmana,laksmana-centos.repo} $BASE_DIR/rpmbuild/BUILD/laksmana-centos-repo/

rpmbuild -bb $BASE_DIR/laksmana-centos-repo.spec

for file in $(find ${BASE_DIR}/rpmbuild/RPMS -type f -name "*.rpm"); do
    expect $BASE_DIR/rpm-sign.exp $file
    rpm --checksig $file
done
