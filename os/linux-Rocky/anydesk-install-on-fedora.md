# anydesk installation on Fedora
anydesk 에서 공식 홈에서는 Centos 8 등으로만 배포하므로 새로 repo 등록 후 다운 받는게 좋다

```
sudo tee /etc/yum.repos.d/AnyDesk-Fedora.repo <<EOF
[anydesk]
name=AnyDesk Fedora - stable
baseurl=http://rpm.anydesk.com/centos/x86_64/
gpgcheck=0
repo_gpgcheck=0
gpgkey=https://keys.anydesk.com/repos/RPM-GPG-KEY
EOF
```

> 위는 EOF 가 나올 때까지 파일의 라인을 추가해서 만들어주게 된다


리포지터리가 등록이 되었다면

```
sudo dnf makecache
sudo dnf install redhat-lsb-core anydesk
```

fedora 38 기준으로 잘 설치 된다.