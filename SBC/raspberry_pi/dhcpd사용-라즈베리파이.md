# 라즈베리파이 dhcp 사용해서 ip 고정

먼저 /etc/dhcpcd.conf 파일을 수정해준다  
interface eth0 은 유선 랜  
interface wlan0 은 무선 랜  

파일을 열자~
```shell
$sudo vim /etc/dhcpcd.conf
```

example로 이미 주석처리 되어 있는데.. 참고해서 적어주면 된다
```conf
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
저장을 하고 빠져나온다.  

일단 무선랜을 사용할 것이라 interface eth0 부분은 주석을 처리했고     
wlan0 부분을 주석해제해서 static으로 나와있는 부분에 위처럼 ip를 적어준다

참고로 ip는 
```shell
$ifconfig
```
게이트 웨이는 
```shell
route
```
를 해서 찾을 수 있다.

<br>

이제  
networking 데몬을 disable하고 dhcpcd를 enable 해준다


```
sudo systemctl disable networking
sudo systemctl enable dhcpcd
```

이제 리부팅을 해보면 고정으로 ip가 할당 될 것이다.

--참고---  
networking은 /etc/network/interfaces 파일에 수정했을 때   
```
$systemctl restart networking 
```
을 하면 위의 파일을 기반으로 재설정해준다.  

현재 라즈베리 OS에서는 /etc/dhcpcd.conf파일을 기본 데몬으로 사용 중이라고 한다.
