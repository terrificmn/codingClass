# FT-확인1-nmcli-wpa_supplicant
## nmcli
*deprecate*  
아래 내용은 참고로만 알아두자, 몇몇 커맨드는 확인할 때 유용할 수 있으므로 활용 참고   

**중요** 
FT-확인2-iwd(supplicant).md 파일을 주로 확인하자!!


wpa_cli 가 작동이 안 되는 경우  
```
sudo wpa_cli status 
```

 에러
```
Failed to connect to non-global ctrl_ifname: (nil)  error: No such file or directory
```

Fedora 에서는 NetworkManager 에서 D-bus 인터페이스로 wifi를 관리하는데  
wpa_cli 는 wap_supplicant 의 traditional control interface 임  


`nmcli`를 사용하자

```
nmcli general status
nmcli -f GENERAL,WIFI-PROPERTIES dev show wlo1
```

해당 wifi SSID가 FT를 지원하는지 확인  
```
sudo iw dev wlo1 scan | grep -A 20 "SSID: my_wifi" | grep -i "RSN\|WPA\|Authentication"

결과 ---
	RSN:	 * Version: 1
		 * Authentication suites: PSK FT/PSK
	RSN:	 * Version: 1
		 * Authentication suites: PSK FT/PSK
	RSN:	 * Version: 1
		 * Authentication suites: PSK FT/PSK
	RSN:	 * Version: 1
		 * Authentication suites: PSK FT/PSK
	RSN:	 * Version: 1
		 * Authentication suites: PSK FT/PSK
	RSN:	 * Version: 1
```
FT 를 지원

```
nmcli -f 802-11-wireless-security.key-mgmt,802-11-wireless-security.proto connection show "my_wifi"
```
결과  

```
802-11-wireless-security.key-mgmt:      wpa-psk
802-11-wireless-security.proto:         --
```

클라이언트에서는 wpa-psk 모드로 사용 중   
이는 정상적인 상황   
NetworkManager에서는 wpa_supplicant 를 사용하게 되는데   

sudo vi /etc/NetworkManager/system-connections/almesh.nmconnection
여기에서 nmconnection 파일 수정

```
[wifi-security]
key-mgmt=wpa-psk;ft-psk;
```
또는 강제로 ft-psk만 남긴다. 

이후 재시작
```
sudo nmcli connection reload
sudo nmcli connection up my_wifi
```
> my_wifi 대신에 wifi SSID 를 넣어주면 된다. 

이렇게 해도 실제 AP에서 FT가 지원이 되는 상황이라도 NetworkManager에서는 FT를 무시하게 된다.  

그래서 journaltcl 로 로그를 보게 되면  (-f 옵션 실시간으로 보기)

```
sudo journalctl -u wpa_supplicant -f
```
결과를 보게 되면 
```
Dec 19 10:51:33 myuser wpa_supplicant[1196]: wlo1: SME: Trying to authenticate with 8c:86:dd:b0:73:db (SSID='my_wifi' freq=5240 MHz)

Dec 19 10:51:34 myuser wpa_supplicant[1196]: wlo1: Trying to associate with 8c:86:dd:b0:73:db (SSID='my_wifi' freq=5240 MHz)

Dec 19 10:51:34 myuser wpa_supplicant[1196]: wlo1: Associated with 8c:86:dd:b0:73:db

Dec 19 10:51:34 myuser wpa_supplicant[1196]: wlo1: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0

Dec 19 10:51:34 myuser wpa_supplicant[1196]: wlo1: WPA: Key negotiation completed with 8c:86:dd:b0:73:db [PTK=CCMP GTK=CCMP]

Dec 19 10:51:34 myuser wpa_supplicant[1196]: wlo1: CTRL-EVENT-CONNECTED - Connection to 8c:86:dd:b0:73:db completed [id=0 id_str=] 
```
이 부분이 standard full handshake 로 하고 있는 로그이다.  
Fast Transition (FT) 관련된 로그가 발생하지 않는다.   

이와 비슷한 설정 바꾸는 것을 여러 차례 했지만, 계속 표준 방식만 따를 뿐이다.  

이유는 supplicant 인 wpa_supplicant 는 오래된 프로그램이어서  
802.11/r 관련 FT 를 무시하는 듯 하다.   

> wpa_supplicant 은 signal이 거의 없어질 때까지 기다린 후 disconect 가 되고   
새로운 AP 를 scan 하게 되는데 이후 4-way handshake 를 하게 된다. 그래서 packet loss 및 lag 발생  


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

