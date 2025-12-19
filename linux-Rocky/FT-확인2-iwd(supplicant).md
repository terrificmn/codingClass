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

