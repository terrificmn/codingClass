# dhcp 사용해서 고정 시키기

먼저 /etc/dhcpcd.conf 파일을 수정해준다
interface eth0 은 유선 랜
interface wlan0 은 무선 랜
원하는 ip를 static 써주고 ip를 적어준다. 

파일을 열자~
```
$sudo vim /etc/dhcpcd.conf
```

example로 이미 주석처리 되어 있는데.. 참고해서 적어주면 된다
```
# Example static IP configuration:#
interface wlan0
static ip_address=192.168.0.17/24
static routers=192.168.0.1
static domain_name_servers=8.8.8.8
#
#interface eth0
#static ip_address=192.168.35.248/24
#static routers=192.168.35.1                          
#static domain_name_servers=8.8.8.8    
```
저장을 하고 빠져나온다 

networking 데몬을 disable하고 dhcpcd를 enable 해준다
사실 두 놈다 잘 실행되고 있지만...

```
sudo systemctl disable networking
sudo systemctl enable dhcpcd
```

이제 리부팅을 해보면 고정으로 ip가 할당 될 것이다.

--참고---
networking은 /etc/network/interfaces 파일에 수정했을 때 
systemctl restart networking 을 하면 위의 파일을 기반으로 재설정해준다.
현재 라즈베리 OS에서는 /etc/dhcpcd.conf파일을 기본 데몬으로 사용 중이라고 한다.


