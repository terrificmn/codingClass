
sudo dnf -y install dnf-plugins-core
sudo dnf upgrade


EPEL 리포 등록
sudo dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm


PowerTools enable 리포지터리
```
sudo dnf config-manager --set-enabled powertools
```

확인하기
```
sudo dnf repolist
```


