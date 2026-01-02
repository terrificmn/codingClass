# FT-확인2-iwd(supplicant)
참고 자료   
| Tool |	Role |	 The "Analogy"	| Description |  
| -- | -- | -- | -- |
| NetworkManager |	The Manager |	The CEO	| The high-level tool that handles Wi-Fi, Ethernet, and VPNs. It doesn't actually "talk" to the Wi-Fi hardware; it gives orders to the Supplicant. |  
| wpa_supplicant | The Supplicant (Old) | The Veteran Worker |	The industry standard for 20 years. It’s very powerful but "heavy" and requires complex config files. It handles the actual WPA2/WPA3 handshakes. |
| iwd |	The Supplicant (New) | The Modern Specialist | Intel's modern replacement for wpa_supplicant. It is tiny, fast, and understands modern roaming (802.11r/k/v) natively without extra configuration. |
| wpa_cli / iwctl |	The Intercom |	The Phone |	These are just the "keyboards" you use to talk to the worker. wpa_cli talks to wpa_supplicant; iwctl talks to iwd. |



## 내 와이파이 device 확인하기 
가장 쉽게 확인할 수 있는 것은 `lsusb`	
```
Bus 001 Device 002: ID 8087:0026 Intel Corp. AX201 Bluetooth
```

드라이버 확인
```
nmcli -f GENERAL.DRIVER device show wlo1
```
장치 interface를 넣어준다. 

`nmcli device status` 로 device 이름을 확인할 수 있다. 

현재 내 laptop 은 
```
GENERAL.DRIVER:                         iwlwifi
```
라고 나오는데  
AX201 은 인텔에서 나온 칩셋에 드라이버도 괜찮다. Wi-Fi 6 및 802.11r 지원  

>wifi5 일 경우에도 FT가 지원은 된다고는 하나, 장치마다 안 될 수도 있다. (안되는 경우가 많은 듯) 


## iwd 설치 및 enable 시키기
tranditional supplicant 인 wpa_supplicant 대신에  
새로운 supplicant 인 iwd 를 설치  

```
sudo dnf install iwd
sudo systemctl enable --now iwd
```

> iwd , Intel에서 만든 Wireless Daemon 으로 modern roaming 에 더 적합하다.  


파일을 하나 만들어준다.  
```
sudo vi /etc/NetworkManager/conf.d/wifi_backend.conf
```

내용은 
```
[device]
wifi.backend=iwd
```

NetworkManager.service 재시작
```
sudo systemctl restart NetworkManager
```

wpa_cli 를 사용하는 대신에 *iwctl* 를 사용할 수 있다.  

```
iwctl
```

새로운 프롬프트가 열린다.  
`station list`  
여기에서 나오는 장치명(interface) 를 넣어준다. 

```
station wlo1 show
```

여기에서 Security 가 WPA2-Personal + FT 이면 FT fast Transition (FAST roaming) 이 작동  


로그 확인  journalctl 로 확인
```
journalctl -u iwd -f
```
이제 실제로 움직이면서 로그를 확인   

```
Dec 19 11:24:21 my_user iwd[42479]: event: state, old: connecting, new: connected
Dec 19 11:27:12 my_user iwd[42479]: event: roam-scan,
Dec 19 11:27:12 my_user iwd[42479]: event: roam-info, bss: 8c:86:dd:b0:74:15, signal: -51, load: 0/255
Dec 19 11:27:12 my_user iwd[42479]: event: state, old: connected, new: ft-roaming
Dec 19 11:27:13 my_user iwd[42479]: event: state, old: ft-roaming, new: connected 
```

`event: state, old: connected, new: ft-roaming` 이 부분이 중요  
AP가 지원하는 Fast Transition 으로 FT handshake 를 하는 로그  

여기까지 오면 잘 작동하는 것으로 확인할 수 있고  

추가로 `ping -i 0.5 1.1.1.1` 등으로 패킷 loss 등을 테스트 해볼 수가 있다. 

만약 로밍이 지원되지 않는 상황이라면 AP를 옮겨갈 때 무조건 disconnect를 먼저하기 때문에  
약 3~5초 정도 timeout 이 걸릴 수 밖에 없고,  
Request timed out 등이 발생할 수 있다.   

FT 지원이 되는 환경이라면 약간의 delay가 발생하고 packet loss 도 거의 발생하지 않는다.  

그리고 마지막으로 중요한 기존의 wpa_supplicant 를 disable 및 mask를 해준다.  

> iwd 를 wifi backend 로 설정했지만 , Fedora에서의 기본 supplicant인 wpa_supplicant 가 작동할 수 있어서 NetworkManager 가 헤깔리지 않게 해준다. (중요)

이럴 경우 자동으로 접속할 때 wifi가 먹통이 될 수가 있고  로그에 
```
iwd[42479]: Unexpected connection related event -- is another supplicant running?
```
이런 로그가 발생할 수가 있다. 

```
sudo systemctl stop wpa_supplicant.service 
sudo systemctl disable wpa_supplicant.service
```

더 강력하게  mask 를 시켜줌
```
sudo systemctl mask wpa_supplicant.service 
```

최종 둘 중 하나만 작동하는지 확인
```
ps aux | grep -E "wpa_supplicant|iwd"
```

*/usr/libexec/iwd* 만 나오면 OK


wifi가 연결된 상태에서 Log out 및 log in을 해보거나  
system 을 suspend 했다가 다시 켰을 때   

wifi가 자동으로 바로 붙어야 한다!


## interface 하나 disable 시키기
iwctl 후 deivce list 로 확인하자   
주의 nmcli 로는 wlo1 이였는데, iwd에서는 wlan0 으로 나올 수도 있다.  

일단 NetworkManager는 wlan wlo 형식으로 만드는 듯 하다.   

그래서 그냥 /etc/NetworkManager/conf.d 이하에 만들어 놓은 것을 사용하는데   
기존에 nmcli 에서는 wlo1 로 인식했던 interface가 backend가 iwd 로 바뀌면서 이름이 wlan0 로 바뀌었고  
이를 그대로 적용하면 사용이 가능하다  

unmanaged 로 적용하기  

*/etc/NetworkManager/conf.d/에 disable-pcie-wifi.conf*  

```
[keyfile]
unmanaged-devices=interface-name:wlan0
```
> 중요한 것은 iwctl 로 device list로 확인하자 . wpa_supplicant 일 경우에는 wlo1   
`iw dev` 의 Interface  
물론 컴퓨터 마다 다르므로 원하는 커맨드로 확인  

> MediaTek pic-e 를 사용하는 경우에는 오히려 USB가 먼저 잡히는 경우가 생길 수 도 있어서  
꼭 pci-e 라고 해서 먼저 잡히는 것은 아니다. 

> 사실 Fedora 쪽에서는 Intel 것만 사용하면 되지만 **우분투 경우**를 참고하자   
우분투에서는 재부팅 후 usb 장치가 잘 작동 안하는 경우가 있다. 내부 pci-e 는 잘 작동해서   
내부 pci-e 로 wifi 가 연결이 되고 이후 usb 장치를 settings 에서 클릭을 해도  
와이파이 신호가 empty 로 나오는 모습이 보이고, 네트워크 상에 SSID가 보이지만 클릭해도 바뀌지 않는다.   
> Fatal 한 상황이다. 가끔 하나만 연결이 안되기도 하지만, 둘 다 안되는 상황도 발생한다. 

이 현상 때문에 race 현상일 것이라 추측했는데  
race 현상 보다는 iwd 와 NM 에서 다루는 방식이 달라서 에러가 발생
```
journalctl -u NetworkManager.service -b --no-pager
```
로 확인해보면 (문제가 발생한 직후, 일단 연결이 안되고 있을 경우에 )  

```
12월 30 12:15:59 my_robot systemd[1]: Starting Network Manager...
12월 30 12:15:59 my_robot NetworkManager[602]: <info>  [1767064559.3486] NetworkManager (version 1.36.6) is starting... (for the first time)
... 생략 ...

12월 30 12:16:01 my_robot NetworkManager[602]: <info>  [1767064561.1024] manager: (wlan1): new 802.11 Wi-Fi device (/org/freedesktop/NetworkManager/Devices/6)
12월 30 12:16:01 my_robot NetworkManager[602]: <info>  [1767064561.1029] rfkill2: found Wi-Fi radio killswitch (at /sys/devices/pci0000:00/0000:00:14.0/usb4/4-3/4-3.1/4-3.1.4/4-3.1.4:1.0/ieee80211/phy1/rfkill2) (driver mt7921u)
12월 30 12:16:01 my_robot NetworkManager[602]: <info>  [1767064561.7001] manager: (wlx90de80f9769d): new 802.11 Wi-Fi device (/org/freedesktop/NetworkManager/Devices/7)
12월 30 12:16:01 my_robot NetworkManager[602]: <error> [1767064561.7050] iwd-manager[0x56f6f2165170]: if_nametoindex failed for Name wlan1 for Device at /net/connman/iwd/1/6: 19
12월 30 12:16:01 my_robot NetworkManager[602]: <info>  [1767064561.7055] device (wlx90de80f9769d): state change: unmanaged -> unavailable (reason 'managed', sys-iface-state: 'external')
12월 30 12:16:02 my_robot NetworkManager[602]: <info>  [1767064562.1936] agent-manager: agent[503e3dfe4b867007,:1.45/org.gnome.Shell.NetworkAgent/1000]: agent registered
12월 30 12:16:05 my_robot NetworkManager[602]: <info>  [1767064565.6720] manager: startup complete
 name="my_wifi" pid=3017 uid=1000 result="fail" reason="Connection 'my_wifi' is not available on device wlx90de80f9769d because device is not available"
12월 30 12:19:40 my_robot NetworkManager[602]: <info>  [1767064780.4579] audit: op="connection-activate" uuid="7a5278e8-0ddc-47b6-a10d-97d6695f2991" name="my_wifi" pid=3017 uid=1000 result="fail" reason="Connection 'my_wifi' is not available on device wlx90de80f9769d because device is not available"
12월 30 12:20:18 my_robot NetworkManager[602]: <info>  [1767064818.2505] audit: op="connection-activate" uuid="7a5278e8-0ddc-47b6-a10d-97d6695f2991" name="my_wifi" pid=3017 uid=1000 result="fail" reason="Connection 'my_wifi' is not available on device wlx90de80f9769d because device is not available"
12월 30 12:20:19 my_robot NetworkManager[602]: <info>  [1767064819.3754] audit: op="connection-activate" uuid="7a5278e8-0ddc-47b6-a10d-97d6695f2991" name="my_wifi" pid=3017 uid=1000 result="fail" reason="Connection 'my_wifi' is not available on device wlx90de80f9769d because device is not available"
```

처음에 부팅을 하고나서 usb 장치를 발견하고 if_nametoindex 에러가 발생한다. wlan1 에 대한 index를  
확인하는게 실패   

이후 wlx90de80f9769d interface 는 unmanaged -> unavailable 로 변경이 되게 되면서   
wifi 연결 자체가 실패하게 된다.  
reason="Connection 'my_wifi' is not available on device wlx90de80f9769d because device is not available  

이유는 iwd 에서 wlanxx 로 시작하는 인터페이스를 사용하려고 하는데  
NM 에서 interface를 요청하는지 iwd에 문의 하면 wlanxx 를 사용하려고 하고   
실제로 interface가  wlx90de80f9769d 로 되어 있어서  
if_nametoindex 가 실패하게 된다.  그래서 NM 에서 
usb장치 mt7921u를  인터페이스 이름으로 사용하는데 강제로 unmanaged -> unavailable  변경 되어서   

고로 GUI setting 하는 부분에서 네트워크는 보이나 실제로는 unavailable 이어서 
클릭해도 연결이 되지 않는 현상  

또한 `iwctl station wlxxxx show` 해보면
```
State connected  
No IP addresses is DHCP client configured?
```
unavailable 이기 때문에 ip도 받지를 못한다.


> 페도라에서도 엠티 시그널로 나오지는 않지만, 비슷하게 usb 장치로 테스트 할 경우 먹통이 되는 현상이 있다.  
같은 증상으로 보인다.   


그래서 iwd이 원하는 wlaxx 형태로 udevrule 을 변경해준다.  

```
sudo vi /etc/udev/rules.d/70-usb-wifi-wlan.rules
```

Mac address 확인한 후 수정해준다. NAME 은 iwd에 원하는 장치로 변경해준다. 
```
SUBSYSTEM=="net", ACTION=="add", ATTR{address}=="30:de:90:f9:76:2d", NAME="wlan1"
```
> 현재는 wlan0 는 pci-e slot 에 연결되어 있는 것으로 되어 있다.  
Mac addres도 확인하자  
또한 인텔 wifi는 usb 보다 빨리 잡혀서 wlan0 이 되나, MediaTek 같은 경우에는 오히려 USB가 먼저 잡히는 경우가 생김  
그래서 USB를 아예 wlanUSB 처럼 특정 문자열로 바꾸는 것도 좋다   
NAME="wlanUSB"  

udevadm 을 적용해준다.  
```
sudo udevadm control --reload
sudo udevadm trigger
```

(재부팅) 확인 시 

```
ip link
```

wlan0, wlan1 로 나와야 한다.  

또는, iwctl 후
```
device list
```


### 테스트 확인 필요
/etc/iwd/main.conf 는 사용할 필요가 없다. 주석처리된 상태로 둔다.   
```sh
[General]
#EnableNetworkConfiguration=true
```
> 이 기능은 iwd가 network 설정도 자체로 하는 것인데 DHCPv4 등 .. (주석해제하면 기능을 사용)  

또한 systemd iwd 기본 설정으로 둔다. 
(바꿨다면, 변경하는 것은 edit 은 최소로 network-pre.target 은 사용하지 않아도 된다.)  
타이밍 (race 컨디션)은 이제 해결 됨  


### 중요 key points
1. udevrul 변경  
2. wifi.backend=iwd  
3. (disable) pci-e (for TEST)


*/etc/udev/rules.d* 이하에 *70-usb-wifi-wlan.rules* 을 만들고 아래 처럼 만들어준다. 
```sh
SUBSYSTEM=="net", ACTION=="add", ATTR{address}=="70:de:70:f9:76:2d", NAME="wlan1"
```

*/etc/NetworkManager/conf.d* 이하에 *disable-pcie-wifi.conf* 파일을 만든다.     
```sh
[keyfile]
unmanaged-devices=interface-name:wlan0
```

*/etc/NetworkManager/conf.d* 이하에 *wifi_backend.conf* 파일을 만든다.   
```
[device]
wifi.backend=iwd
```

optional 배터리 powersave 확인  
*/etc/NetworkManager/conf.d* 이하에 *default-wifi-powersave-on.conf* 파일을 만든다.  
```
[connection]
wifi.powersave = 3
```

### USB VS PIC-e
일단 
iwctl station wlna0 or wlan1 show 를 해서 

```
Scanning              no                                               
State                 connected                                        
Connected network     my_wifi                                           
IPv4 address          192.168.11.57                                    
ConnectedBss          8c:86:dd:b0:71:68                                
Frequency             2437                                             
Channel               6                                                
Security              WPA2-Personal + FT                               
RSSI                  -57 dBm                                          
AverageRSSI           -58 dBm                                          
RxMode                802.11n                                          
RxMCS                 13                                               
TxMode                802.11n                                          
TxMCS                 15                                               
TxBitrate             144400 Kbit/s                                    
RxBitrate             104000 Kbit/s     
```
802.11n 을 사용한다면 좀 더 낮은 버전  
802.11ax 가 더 좋다.   
802.11n 을 사용하더라도 roaming 잘 되면 크게 나쁘지 않은 것 같다.  
> 11n 은 현재 노트북 (Fedora)    

RSSI 는 신호세기   
RSSI scale (realistic)  
RSSI (dBm)	Quality	Meaning  
−30 to −50	Excellent	Near AP  
−50 to −60	Very good	Strong  
−60 to −67	Good	Reliable  
−67 to −75	Marginal	Still usable  
−75 to −80	Poor	Unstable  
< −80	Bad	Drops likely  


Intel 은 일단 roaming이 잘 된다. ConnectedBss sms individual AP 인데,  
로밍할 때 주소가 바로 바뀐다.  

> 로밍 조건 (다 맞아야 함)  
1. Another AP with same SSID is visible  
2.That AP’s signal is meaningfully better  
3.Current RSSI drops below the roam threshold  
4.Roaming cost < staying cost (client-side decision)  


로봇의  
Mediatek USB 는 ConnectedBss AP가 잘 안 바뀐다.  
로봇의 PCI-e AX201 는 802.11ax 를 사용하고 로밍도 자주 한다.   

2개를 더 비교를 해봐야겠지만  
loss 는 USB가 더 적고 로밍은 잘 안함.   
Intel 은 loss 가 좀 더 많다. 로밍은 더 자주 적극적으로 하게 된다.    

둘 다 많이 사용해보고 원하는 것으로 변경 해야할 듯 하다.   
Intel 것을 사용하려면 disable-pcie-wifi.conf 를 삭제하고 iwd restart 를 해주면 된다.   

## ubuntu 에서 iwctl 에러
iwctl 를 했을 떄
```
Rejected send message, 2 matched rules; type="method_call", sender=":1.412" (uid=1000 pid=6572 comm="iwctl " label="unconfined") interface="org.freedesktop.DBus.ObjectManager" member="GetManagedObjects" error name="(unset)" requested_reply="0" destination="net.connman.iwd" (uid=0 pid=613 comm="/usr/libexec/iwd " label="unconfined")
Failed to retrieve IWD dbus objects, quitting...

```
sudo 를 사용하거나 

현재 유저를 netdev 그룹을 추가(포함) 시켜준다. 

```
sudo usermod -aG netdev $USER
```
이렇게 하면 sudo 가 필요 없다.


