# RHEL CentOS 계열의 firewalld
firewall에서는 미리 지정된 zone들이 있는데 미리 서비스들을 허용하고 있는지   
정의가 되어 있다.   

그 중 public으로 셋팅되어 있는 것 보기   
일단 default로 지정되어 있다.

```
sudo firewall-cmd --zone=public --list-all
```

```
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp3s0
  sources: 
  services: cockpit dhcpv6-client ssh
..생략
```
cockpit (system 방화벽과 관련)
ssh
dhcpv6-client 

> dhcpv6-client 허용되게 되어 있다고 한다(기본 룰), dhcpv4 와 다른게 작동한다고 함
IPv6 어드레스를 static으로 쓰고 있거나  
IPv6를 안쓰고 있다면 disable해도 됨


### remove-service 
```
sudo firewall-cmd --zone=public --remove-service=dhcpv6-client --permanent
```

### add-service
다시 추가하려면 `--add-service=` 로 사용하면 됨  

예를 들어서 https를 추가하려면 
```
sudo firewall-cmd --zone=public --add-service=https --permanent
```
그리고 reload를 하면 적용이 된다
```
sudo firewall-cmd --reload
```


> --permanent 플래그를 사용 유무에 따른 변화
--permanent를 사용 안하게 되면 현재 zone에 바로 적용이 된다.  
하지만 reload를 하거나 재부팅 시에는 적용이 안되게 된다.  
--permanent를 사용하면 현재 zone에는 바로 적용이 안됨  
하지만 reload나 재부팅 시 부터는 적용이 되게 됨


## 서비스 포트 번호 확인하기 /etc/services
서비스 되고 있는 것 포트번호 확인하기
```
grep ssh /etc/services
```

결과는 
```
ssh             22/tcp                          # The Secure Shell (SSH) Protocol
ssh             22/udp                          # The Secure Shell (SSH) Protocol
x11-ssh-offset  6010/tcp                        # SSH X11 forwarding offset
ssh             22/sctp                 # SSH
sshell          614/tcp                 # SSLshell
... 생략
```

위에서 보듯이 ssh서비스는 22/tcp 22/udp 포트를 사용하는 것을 알 수가 있다  
이를 참고해서 사용할 수 있다.


## 서버에서 셋팅 

웹서버 dmz 존으로 셋팅 예

Assign the dmz zone as the default zone to eth0. Of the default zones offered, dmz (demilitarized zone) is the most desirable to start with for this application because it allows only SSH and ICMP.

### default zone 바꾸기 --set-default-zone=, interface 추가하기
```
sudo firewall-cmd --set-default-zone=dmz
sudo firewall-cmd --zone=dmz --add-interface=eth0
```


### add-service 로 추가하기 --add-service=
Add permanent service rules for HTTP and HTTPS to the dmz zone:
```
sudo firewall-cmd --zone=dmz --add-service=http --permanent
sudo firewall-cmd --zone=dmz --add-service=https --permanent
```

Reload FirewallD so the rules take effect immediately:
```
sudo firewall-cmd --reload
```

If you now run firewall-cmd --zone=dmz --list-all, this should be the output:
```
sudo firewall-cmd --zone=dmz --list-all
```

결과
```
dmz (default)
  interfaces: eth0
  sources:
  services: http https ssh
  ports:
  masquerade: no
  forward-ports:
  icmp-blocks:
  rich rules:
```
This tells us that the dmz zone is our default which applies to the eth0 interface, all network sources and ports. Incoming HTTP (port 80), HTTPS (port 443) and SSH (port 22) traffic is allowed and since there are no restrictions on IP versioning, this will apply to both IPv4 and IPv6. Masquerading and port forwarding are not allowed. We have no ICMP blocks, so ICMP traffic is fully allowed, and no rich rules. All outgoing traffic is allowed.

```
sudo firewall-cmd --state
```
상태확인하기

현재 되는 것 보기
```
sudo firewall-cmd --get-active-zone
```

## 추가 port 추가해서 열기 --add-port=
예를 들어서 5000번 tcp를 이용하는 것을 추가하려면은 
```
sudo firewall-cmd --zone=public --add-port=5000/tcp
```
역시 지울 때는 --remove-port= 가 되겠다 


## permanent tag로 추가하거나 --runtime-to-permanent
```
sudo firewall-cmd --runtime-to-permanent 
```

또는 위의 명령어들을 (추가했던) 다시 한번 실행시켜준다. 
```
sudo firewall-cmd --zone=public --add-port=5000/tcp --permanent
```




## docker 사용 시 nestat, nmap 으로 확인
[참고한 사이트 docker and firewalls](https://degreesofzero.com/article/docker-and-firewalls.html)

Are you running a firewall like ufw with docker? You might be surprised to learn that your firewall is probably not doing anything to block unwanted internet traffic from reaching your docker services. Docker modifies iptables rules to completely bypass or ignore the rules set by ufw. In this article, I will explain how to check if the services running on your server are exposed and how to protect them.

도커를 실행했을 때의 외부로 노출되어 있는 포트를 확인할 수 있다.   
처음에는 firewall에서 차단하겠지라고 생각했지만 몇번 firewalld 를 건드렸지만  
허용되어 있는 것은 ssh 일 뿐인데도 접속이 잘 되었다.   

게다가 로컬 집 기준으로는 firewall 에서는 http, https를 허용하고 있지 않는데도 불구하고 도커 컨테이너로 연결된 포트들은 open이 되어 있다~  

몇가지 테스트를 해본 결과 도커 컨테이너에는 iptables 를 직접 변경할 수 있게 되어 있는 듯하다.   
그래서 RHEL 계열의 firewalld 우분투 계열의 ufw 의 설정에도 불구하고 외부에서 직접 접근이 가능한걸로 확인이 됨

그래서 netstat 명령어를 사용하면 아래처럼 확인이 가능
```
 sudo netstat -tlpn
```
```
tcp        0      0 0.0.0.0:8010            0.0.0.0:*               LISTEN      91691/docker-proxy  
tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN      91055/docker-proxy  
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1340/sshd           
tcp6       0      0 :::8010                 :::*                    LISTEN      91697/docker-proxy  
tcp6       0      0 :::3306                 :::*                    LISTEN      91070/docker-proxy  
```
이런식으로 나온다. 

> 여기에서 0.0.0. 으로 되어 있는 것에 주목할 필요가 있다.   
127.0.0.1" is the loopback address. Services bound to the loopback address are not accessible remotely.      
"0.0.0.0" means all interfaces. Services bound to this address are accessible remotely unless a firewall is blocking those requests.


nmap 이라는 포트 확인하는 프로그램 (무시무시한 프로그램인 듯;;)

```
sudo dnf install nmap
```

-p포트 지정해서 찾을 수 있다. nmap -p 0-65535 ip주소
```
nmap -p 0-65535 220.120.210.241
```
를 해봤더니 

```
PORT     STATE SERVICE
22/tcp   open  ssh
111/tcp  open  rpcbind
3306/tcp open  mysql
8010/tcp open  xmpp
8828/tcp open  unknown
8829/tcp open  unknown
9889/tcp open  gt-proxy
```
이렇게 열려 있음

firewall에서는 상관없이 docker에서의 컨테이너가 오픈되어 있는 것   
mysql 3306도 열려 있다. 

예를 들어서 도커의 컨테이너를 3000으로 연결해서 열면   
docker run -p 3000:3000   
host 0.0.0.0 에 docker컨테이너가 연결이 된다.   
그러면 외부에서도 접근이 가능하게 되는 것

이것을 고치는 것을 아주 간단하다고 함   
바로 127.0.01:3000:3000 이런식으로 바꿔주는 것이다   

docker 데몬에 --iptables=false 을 하라는 조언도 보이지만 아주 좋지 않는 방법이라고 한다.     
왜냐하면 그렇게 하게 되면 도커 컨테이너에 들어오는 것도 막지만 외부로 나가는 것도 막기 때문에 도커가 사용 불가능이 된다   


firewalld에서는 적용이 안 되지만, 도커에서 설정을 변경해서   
외부에서의 접근을 차단할 수가 있다.

도커 설정을 변경 후 다시 nmap을 nmap -p 0-65535 220.120.210.241 조회해보면

```
PORT     STATE SERVICE
22/tcp   open  ssh
111/tcp  open  rpcbind
8010/tcp open  xmpp
8828/tcp open  unknown
8829/tcp open  unknown
```
mysql과 phpmyadmin 포트가 사라진 것을 알 수 있다 






