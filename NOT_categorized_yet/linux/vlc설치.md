RHEL/CentOS 8

Use RPM Fusion for EL8. Available for x86_64, aarch64 and ppc64le

This repository uses EPEL

The vlc-3.0x branch will be provided for EL8
Install rpmfusion-free-release-8.noarch.rpm for EL8.

에서 VLC 설치하기

```
sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
sudo yum install https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm
sudo yum install vlc
```

Importing GPG key 0x158B3811:
 Userid     : "RPM Fusion free repository for EL (8) <rpmfusion-buildsys@lists.rpmfusion.org>"
Is this ok [y/N]: 

나올때 y로 등록해주면 된다
