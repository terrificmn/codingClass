자신의 네트워크이름 탭으로 완성
```
$ sudo vi /etc/sysconfig/network-scripts/ifcfg-eth0
```

DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
PEERDNS=no

여기에서 REERDNS=no 는 /etc/resolv.conf에 저장하지 않는다. 그래서 직접 DNS를 추가해줘야함


스태틱 DNS 설정
```
sudo vi /etc/resolv.conf 
```

nameserver 8.8.8.8
nameserver 8.8.4.4




## 또는 직접 입력하기
```
$ sudo vi /etc/sysconfig/network-scripts/ifcfg-eth0
```

```
DNS1=8.8.8.8
DNS2=8.8.4.4
```
추가한다
만약 PEERDNS=no 가 있다면 지워주자


위의 파일에 DNS1, DNS2를 입력하면 /etc/reslov.conf에 자동으로 추가가 되는데   
인터페이스가 작동중일 때 추가됨 (아마도 network를 껏다가 다시 켬?)

