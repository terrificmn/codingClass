# shared to other computers
이더넷과 이더넷으로 연결해서 Host 쪽의 Wi-Fi 로 연결을 할 수가 있는데  

일단 설정에서 Network -> Wired 에서 설정을 눌러서  
Ipv4 탭에서 Shared to other computers 를 눌러준다.   

만약 nmcli 커맨드로 하려면  
```
nmcli connection show
```

```
NAME                UUID                                  TYPE      DEVICE    >
Wired connection 1  b4921b2b-7d63-3033-b6fc-4128658972b5  ethernet  enp4s0    >
```

좀 더 자세히 보려면  
`nmcli connection show "Wired connection 1"` 이렇게 하면 자세하게 나오는데  
Ipv4 항목을 찾아본다.  

```
ipv4.method:                            auto
```
만약에 이게 auto 라면 shared 모드로 바꿔줘야 한다. 

```
sudo nmcli connection modify "Wired connection 1" ipv4.method shared
sudo nmcli connection down "Wired connection 1"
sudo nmcli connection up "Wired connection 1"
```

그러면 다시 이렇게 바뀐다. 
`nmcli connection show "Wired connection 1" | grep ipv4.method`
```
ipv4.method:                            shared
```


이제 랜 케이블을 다른 second 컴퓨터에 연결해준다.  

이렇게 되면 간단하게 터미널을 이용해서 ssh 로 접속이 가능해진다.  

먼저 ip를 찾기 위해서 
```
ip neighbor show
```

10.42.0 으로 시작하는 아이피를 찾으면 된다. 
```
10.42.0.218 dev enp4s0 lladdr 48:21:0b:25:c1:e6 DELAY 
```

이제 해당 ip로 ssh 접속을 하면 된다. 


## 인터넷 되게 하기
위의 작업 까지만 하면 internet share 는 안되지만 해당 second 컴퓨터에 접속하는 게 가능하다.  

host의 internet 를 연결해서 공유를 해주려면  

```
sudo sysctl -w net.ipv4.ip_forward=1
cat /proc/sys/net/ipv4/ip_forward
```
포워드를 해주고  1 이라고 나오면 oK

`ip route` 를 통해서 default route 를 찾아준다. 
```
default via 192.168.11.1 dev wlan0 proto dhcp src 192.168.11.51 metric 600 
10.42.0.0/24 dev enp4s0 proto kernel scope link src 10.42.0.1 metric 100 
```
wlan0 로 192.168.11.1 로 나가는 것을 알 수가 있다.

이제 2개의 커맨드로 해준다.
```
sudo iptables -A FORWARD -i enp4s0 -o wlan0 -s 10.42.0.0/24 -j ACCEPT
sudo iptables -A FORWARD -i wlan0 -o enp4s0 -d 10.42.0.0/24 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
```

> enp4s0 은 ethernet 카드 interface 이고, wlan0 는 wifi


second 컴퓨터에서 ping 8.8.8.8 을 해서 ping 이 되면 ok
