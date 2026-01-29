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

systemct enable iwd-disable-wlan1.service

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
