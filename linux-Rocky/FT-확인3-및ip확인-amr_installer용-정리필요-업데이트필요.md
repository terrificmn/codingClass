[iwd]# device wlan1 set-property Powered off
[iwd]# device list
                                    Devices                                    
--------------------------------------------------------------------------------
  Name                Address             Powered   Adapter   Mode      
--------------------------------------------------------------------------------
  wlanUSB             90:de:80:92:24:45   on        phy0      station   
  wlan1               84:9e:56:41:7a:2b   off       phy1      station   




sudo vi /etc/systemd/system/iwd-disable-wlan1.service

[Unit]
Description=Disable PCIe WiFi
After=iwd.service

[Service]
Type=oneshot
ExecStart=/usr/bin/iwctl device wlan1 set-property Powered off

[Install]
WantedBy=multi-user.target




/etc/iwd/main.conf
[General]
# iwd is capable of performing network configuration on its own, including
# DHCPv4 based address configuration.  By default this behavior is
# disabled, and an external service such as NetworkManager, systemd-network
# or dhcpclient is required.  Uncomment the following line if you want iwd
# to manage network interface configuration.
#
EnableNetworkConfiguration=true
#
# iwd can randomize your WiFi card's MAC address for additional privacy.  By
# default, this behavior is disabled and the MAC address assigned by the
# kernel driver is used.  The address will be stable when connecting
# to a saved network profile, so as to not interfere with any MAC filtering
# rules that exist on the network.
# If a randomized MAC address is desired, uncomment the setting line below:
#
#AddressRandomization=network
ink quality.
#
#RoamThreshold=-75
RoamThreshold5G=-76
#DisableRoaming=true
#
[Network]
# If EnableNetworkConfiguration=true is set, iwd forwards DNS information to
# the system resolving service.  The currently supported services are:
# - systemd-resolved ["systemd"]
# - openresolv / resolvconf ["resolvconf"]
#
# If not set, the value "systemd" is used by default.  Uncomment the value
# below if you are using openresolv:
#
#NameResolvingService=resolvconf
 via SLAAC is currently not supported (DHCPv6 only).
#
#EnableIPv6=true
EnableIPv6=false
[Scan]
DisablePeriodicScan=true



/etc/NetworkManager/conf.d/
99-no-wifi-nm.conf

[main]
plugins=keyfile

[keyfile]
unmanaged-devices=interface-name:wlan*


모든 wlan으로 시작되는 것을 unmanaged-상태로 만듬, usb 포함


default-wifi-powersave-on.conf 

[connection]
wifi.powersave = 2



/etc/NetworkManager/conf.d$ cat wifi_backend.conf 
[device]
wifi.backend=none

여기에서 중요 기존에 iwd 로 backend 를 지정했던 것과는 다르게 none으로 백엔드를 지정하지 않고 
wpa_supplicant 도 disabled 된 상태라면 
NM에서 wifi 자체를 연결 시도를 하지 않는다.  


/etc/systemd/system이하에 oneshot 으로 시작 프로그램 등록

/etc/systemd/system/iwd-disable-wlan1.service
```
[Unit]
Description=Disable PCIe WiFi
After=iwd.service
Requires=iwd.service

[Service]
Type=oneshot
#ExecStart=/usr/bin/iwctl device wlan1 set-property Powered off
ExecStart=/bin/sh -c '\
  for i in $(seq 1 20); do \
    /usr/bin/iwctl device list | grep -q "^ *wlan1" && break; \
    sleep 0.5; \
  done; \
  /usr/bin/iwctl device wlan1 set-property Powered off \
'


[Install]
WantedBy=multi-user.target
```

업데이트 0 또는 1도 확인할 수 있게 변경.. 가끔 wlan0 이 되기도 했다가 wlan1 되기도 하는 현상 발생,  

```
[Unit]
Description=Disable PCIe WiFi
After=iwd.service
Requires=iwd.service

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/bin/bash -c '\
  device=
  for ((i=0;i<360;i++)) do \ ####  여기에서 (( )) 는 지원되지 않음. 한줄로 표현할 경우
    device=$(/usr/bin/iwctl device list | grep -oE "^ *wlan[01]") \
    if [ -n "$device" ]; then \
      echo "Found $device" \
      break \
    fi \
    echo "Not found" \
    sleep 0.5 \
  done; \
  /usr/bin/iwctl device $device set-property Powered off '

[Install]
WantedBy=multi-user.target
```


```
[Unit]
Description=Disable PCIe WiFi
After=iwd.service
Requires=iwd.service

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/bin/bash -c '
  device=
  i=0
  while [ $i -lt 360 ]; do
    device=$(/usr/bin/iwctl device list | grep -oE "wlan[01]")
    if [ -n "$device" ]; then
      echo "Found $device"
      break
    fi
    echo "Not found"
    sleep 0.5
    i=$((i+1))
  done
  /usr/bin/iwctl device $device set-property Powered off
'

[Install]
WantedBy=multi-user.target

```



 3월 05 14:22:47 robot-14 systemd[1]: Starting Disable PCIe WiFi...
 3월 05 14:22:47 robot-14 bash[10317]: /bin/bash: -c: line 1: syntax error near unexpected token `do'
 3월 05 14:22:47 robot-14 bash[10317]: /bin/bash: -c: line 1: `   device=    i=0    while [ $i -lt 360 ]; do      device=$(/usr/bin/iw>
 3월 05 14:22:47 robot-14 systemd[1]: iwd-disable-wlan1.service: Main process exited, code=exited, status=2/INVALIDARGUMENT
 3월 05 14:22:47 robot-14 systemd[1]: iwd-disable-wlan1.service: Failed with result 'exit-code'.
 3월 05 14:22:47 robot-14 systemd[1]: Failed to start Disable PCIe WiFi.
~

결국은 파일을 하나 새로 만듬;;


```
[Unit]
Description=Disable PCIe WiFi
After=iwd.service
BindsTo=iwd.service

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/etc/amr-rc/wlan_power_off

[Install]
WantedBy=iwd.service
```
sudo vi /etc/systemd/system/iwd-disable-wlan1.service 

> ExeStart 를 script 파일 연결해준다.  
그냥 /bin/bash -c '.....'  등으로 하려고 했으나, escaping 하는게 잘 안 먹혀서 불편하다. 

vi /etc/amr-rc/wlan_power_off 만들어 준다.
```
#!/bin/bash
sleep 5s
device=
i=0
for ((i=0;i<360;i++)) do
  device=$(/usr/bin/iwctl device list | grep -oE "wlan[01]")
  if [ -n "$device" ]; then
    echo "Found $device"
    /usr/bin/iwctl device $device set-property Powered off
    break
  fi
  echo "Not found" 
  sleep 0.5
  i=$((i+1))
done;
```

systemctl daemon-reload
sudo systemctl enable iwd-disable-wlan1.service 

> 쉘 스크립트 변경이 있을 경우에는 daemon-reload 를 꼭 해주자, 바로 할 경우 반영이 안 될 수가 있다. 

status 를 확인해보면 조금 스크립트에 sleep 5초 정도를 먼저 해주고 시작해주는게 좋을 듯 하다. 

```
● iwd-disable-wlan1.service - Disable PCIe WiFi
     Loaded: loaded (/etc/systemd/system/iwd-disable-wlan1.service; enabled; vendor preset: enabled)
     Active: active (exited) since Thu 2026-03-05 14:50:04 KST; 16s ago
    Process: 11322 ExecStart=/etc/amr-rc/wlan_power_off (code=exited, status=0/SUCCESS)
   Main PID: 11322 (code=exited, status=0/SUCCESS)
        CPU: 7ms

 3월 05 14:49:58 robot-15 systemd[1]: Starting Disable PCIe WiFi...
 3월 05 14:50:03 robot-15 wlan_power_off[11322]: Found wlan0

```

> 잘 인식한 케이스, 
 3월 05 14:47:10 robot-15 systemd[1]: Starting Disable PCIe WiFi...
 3월 05 14:47:11 robot-15 wlan_power_off[11007]: Found wlan1
 3월 05 14:47:11 robot-15 wlan_power_off[11016]: Device wlan1 not found.
 3월 05 14:47:11 robot-15 systemd[1]: Finished Disable PCIe WiFi.
이런 경우가 생기기도 함, 찾았다가 다시 못 찾는 케이스 wlan1로 잡혔다가 wlan0 으로 변경 된 듯 하다. 
이런 경우에는 wlan0 으로 on 되어 있는 상태로 확인된다 (iwctl device list)





이유는 NM이 간섭을 안하더라도 대신에 iwd 에서는 pci-e , usb 를 모두 연결 시켜준다.  

자동 연결이 잘 되지만 둘다 연결됨  

그래서 아예 연결을 해제 시켜주는 시작 프로그램을 등록해준다. 

iwctl device list 를 했을 때



[iwd]# device list
                                    Devices                                    
--------------------------------------------------------------------------------
  Name                Address             Powered   Adapter   Mode      
--------------------------------------------------------------------------------
  wlan1               84:9e:56:41:7a:2b   off       phy1      station   
  wlanUSB             90:de:80:92:24:45   on        phy0      station   


off 로 나와야 하낟. 

그리고 수동으로 시켜줄 때에는 
iwctl device wlan1 set-property Powered off 

로 해준다. 


이렇게 하면 한 개만 실행이 되게 된다. 

# station wlanUSB show
                                Station: wlanUSB                               
--------------------------------------------------------------------------------
  Settable  Property            Value                                          
--------------------------------------------------------------------------------
            Scanning            no
            State               connected
            Connected network   almesh                                         
            IPv4 address        192.168.11.107                                 
            ConnectedBss        8c:86:dd:b0:74:15   
            Frequency           5200                
            Security            WPA2-Personal + FT  
            RSSI                -63                  dBm
            AverageRSSI         -63               




wifi 확인 방법
iwctl을 사용하거나 
iwctl device list

wctl device list
                                    Devices                                    
--------------------------------------------------------------------------------
  Name                  Address               Powered     Adapter     Mode      
--------------------------------------------------------------------------------
  wlan0                 d4:e9:8a:d5:7a:00     on          phy0        station     

 iwctl station wlan0 show
                                 Station: wlan0                                
--------------------------------------------------------------------------------
  Settable  Property              Value                                          
--------------------------------------------------------------------------------
            Scanning              no                                               
            State                 connected                                        
            Connected network     SK_3776_2.4G                                     
            IPv4 address          192.168.45.152                                   
            ConnectedBss          28:4e:e9:23:37:79                                
            Frequency             2422                                             
            Channel               3                                                
            Security              WPA2-Personal                                    
            RSSI                  -58 dBm                                          
            AverageRSSI           -51 dBm                                          
            RxMode                802.11ax                                         
            RxMCS                 3                                                
            TxMode                802.11ax                                         
            TxMCS                 8                                                
            TxBitrate             103200 Kbit/s                                    
            RxBitrate             68800 Kbit/s                                     

[sgtfedmsi@sgtfedmsi ~]$ 


여기에서 connected 로 확인할 수도 있을 듯..

또는 쉽게 ip addr 이용


ip addr show wlan0
5: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether d4:e9:8a:d5:7a:00 brd ff:ff:ff:ff:ff:ff
    altname wlo1
    altname wlp0s20f3
    altname wlxd4e98ad57a00
    inet 192.168.45.152/24 scope global dynamic noprefixroute wlan0
       valid_lft 19473sec preferred_lft 19473sec
    inet6 fe80::d6e9:8aff:fed5:7a00/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever

ip route | grep default

ip route | grep default
default via 192.168.45.1 dev wlan0 proto dhcp src 192.168.45.152 metric 305 

json
ip -j addr show wlan0 | jq -r '.[0].addr_info[] | select(.family == "inet") | .local'
ip만 딱 나옴

또는 awk사용
ip addr show wlan0 | grep "inet " | awk '{print $2}' | cut -d/ -f1
ip만 나옴


mac address
json
ip -j link show wlan0 | jq -r '.[0].address'

awk
ip link show wlan0 | grep "link/ether" | awk '{print $2}'




### remote 로 ssh 접속이 안될 경우

s]$ ssh amrrobot@192.168.11.115
ssh: connect to host 192.168.11.115 port 22: No route to host


실제로 remote 115는 인터넷 연결은 끊긴 상태는 아님, 잘 연결 되어 있음 
iwd 에서도 Scanning no, State connected 로 확인이 가능

다만, ip addr을 해보면 brd (broadcasting) 이 지정되어 있지 않다.  
```
Remote Pc: inet 192.168.11.115/24 scope global dynamic noprefixroute wlanUSB 
```

brd 가 빠져 있음

이것 때문에 다른 컴퓨터에서 remote로 접속하려고 하면 No route to host 라고 접속이 불가능

이유는 대충 다른 랜카드를 사용하고 있으므로 충돌이 날 가능성이 있다. 

메뉴얼로 brd를 지정해주면 바로 접속이 가능해 진다.
```
sudo ip addr flush dev wlanUSB
sudo ip addr add 192.168.11.115/24 brd 192.168.11.255 dev wlanUSB
sudo ip link set wlanUSB up
```


완전 매뉴얼로만 하고 있으므로 NetworkManager 사용안함으로 인해서  
systemd networkd 서비스를 사용하므로 따로 지정해준다.  

/etc/systemd/network/이하에 파일을 만듬

10-wlanUSB.network
```
[Match]
Name=wlanUSB

[Network]
Address=192.168.11.115/24
# Forces the broadcast address that was missing
Broadcast=192.168.11.255
Gateway=192.168.11.1
DNS=8.8.8.8
IPv6AcceptRA=no
IgnoreCarrierLoss=yes

[Route]
# Lower number = Higher priority
Metric=10
```


참고 ensp 카드를 위한 , 파일명 20-wired.network
```
[Match]
Name=enp3s0 # or en* This matches most ethernet names like eth0 or enp3s0

[Link]
# ignore wait-online
RequiredForOnline=no

[Network]
#DHCP=yes
Address=192.168.137.2/24
#Gateway=192.168.1.1
DNS=1.1.1.1
DNS=8.8.8.8
```

> eno1 로 할경우도 있고, enp3s0 으로 할 경우도 있다, device interface를 확인해야할 듯 하다.  
> 일단 Gateway는 지정 안하고 사용 , windows와 사용이 잘 된다. 


```
sudo systemctl enable systemd-networkd
sudo systemctl restart systemd-networkd
```

일단 재부팅을 해도 크게 문제가 없다.  

lo 확실히 보장하기,   
*00-lo.network* 파일을 만들어 준다. (/etc/systemd/network/이하)  

```
[Match]
Name=lo

[Route]
Destination=224.0.0.0/4
Scope=link
```

> Destiantion은 저렇게 정의된 주소  



ip addr 
```
7: wlanUSB: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 00:1f:05:66:a8:e0 brd ff:ff:ff:ff:ff:ff
    inet 192.168.11.115/24 brd 192.168.11.255 scope global dynamic wlanUSB
       valid_lft 42306sec preferred_lft 42306sec
    inet6 fe80::21f:5ff:fe66:a8e0/64 scope link 
       valid_lft forever preferred_lft forever
```


iwd 설정 중에  /etc/iwd/main.conf  
*EnableNetworkConfiguration=false*

false 로 사용하자  

> 일단 iwd 에서 true 로 지정해서 사용할 수 있지만,  크게 문제는 안되지만,  
간혹 systemd-networkd 와 충돌이 날 경우가 있다, 이럴 경우에 ssh 로 외부에서 접속이 안되는 현상이 발생하는 듯 하다. (관련이 있어 보인다. )   
접속은 안되지만, 통신 자체에 문제는 없는 듯 하다.wifi  
 
어차피, ip를 고정으로 사용하는 경우이므로 온전하게 systemd-networkd 에 ip 관련해서 맞겨 버리고,   
**wifi 관련해서 iwd 에서 사용할 수 있게 해주자**  

```
[General]
## let systemd-networkd handle the IP, iwd for only Wi-Fi
EnableNetworkConfiguration=false
RoamThreshold=-62
RoamThreshold5G=-64

[Network]
NameResolvingService=systemd

[Blacklist]
phy=phy1
```