# fedora docker 정상 작동이 안 되는 경우
fedora 40 에서 정상 작동했지만 42 버전에서 docker service 자체가 실행이 안되는 경우

iptables-ntf 관련 파일을 심링크 다시 연결 해준다. 
```
sudo ln -s /usr/sbin/iptables-nft /usr/sbin/iptables
sudo ln -s /usr/sbin/ip6tables-nft /usr/sbin/ip6tables
```

> iptables-utils-1.8.11-6.fc42.x86_64.rpm  에서 관련 path가 변경되어서 그렇다고 함