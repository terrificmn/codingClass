# openmediavalut 트러블 슈팅 무선랜이 안될 때
당황스럽게도 모든 설치가 순조롭게 진행되고 마무리로 재부팅이 되었을 때   
무선랜이 사라지는 현상이 나타났다. ifconfig를 해도 무선랜이 wlan0 가 잡히지를 않는다.  

검색을 했더니 이런 경우가 많지는 않는것 같지만.. 다시 무선랜이 가능하게 패키지를 설치를 해야하는데    
이때 유선랜을 연결해서 한다고 한다고 했지만..     

더 당황스러운것은 유선랜을 연결했는데도...eth0 마저 ip를 잡지못하고     
lo만 나온다. 루프백 127.0.0.1 자기자신만 나오고 있었다..    

조금 지난 기억이라서;; 조금 정확하지는 않지만..    
99-default.link를 지워줘야 했다.    

```shell
sudo rm /etc/systemd/network/99-default.link
sudo netplan apply
sudo omv-salt deploy run systemd-networkd
```
그러면 유선랜 eth0가 살아나면서 ip를 받아온다. 

정확하게는 기억이 가물가물하지만.. 세번째 명령어는 안된거 같기도 한데..
어쨋든 다시 인터넷이 된다

먼저 update를 해줘야한다
```
sudo apt update
```
이제 업그레이드를 진행해준다
```
sudo apt list --upgradable
sudo apt upgrade
```

이제 rpi-update를 해준다
```
$sudo apt install rpi-update
```

rpi-update가 된 후에 다시 update & upgrage를 다시 해줘서 추가로 업데이트가 될 수 있게 한다
```
sudo apt update
sudo apt upgrade
```

이제 라즈베리파이의 펌웨어 업데이트를 한다
raspberry pi 3 B+ 모델에 해당한다고 함
```
sudo rpi-update ef7621d91cb58ccc856c3c17ddda28685edd23f3
```

펌웨어 업데이트를 한 후에 최신 Wifi 드라이버를 설치해준다
```
wget https://archive.raspberrypi.org/debian/pool/main/f/firmware-nonfree/firmware-brcm80211_20161130-3+rpt3_all.deb
```
그리고 dpkg를 이용해서 설치 (다운은 위에서 wget으로 받은 디렉토리에 있음)
```
dpkg -i firmware-brcm80211_20161130-3+rpt3_all.deb
```

이제 nmtui를 누르면 cli모드에서 유선/무선을 선택할 수 있는데 
무선을 선택하고 SSID 및 비번을 눌러서 연결이 되는지 확인하면 된다
```
nmtui connect
```

라즈베리파이 바탕화면에서도 잘 된다.  
단, 원래 처음 기본값으로 되어 있던 화면과는 구성이 좀 다르다..    
뭐 어쩔 수 없지.. 일단 인터넷만 잘 된다면...  

여기도 약간 헛깔리지만.. 여기까지 했는데도 nmtui connect가 안된다면
```
sudo apt install network-manager network-manager-gnome
```

<br>

참고사이트

https://pcmac.biz/openmediavault-wifi-setup-raspberrypi-3b-plus/