# realtek RTL8852CU
Fenvi AXE5400  
lsusb 하기

ID 0bda:c832 이면 rtl8852cu 


의존성 
```
sudo dnf install make gcc bc \
  elfutils-libelf-devel \
  kernel-devel-$(uname -r) \
  kernel-headers-$(uname -r)
```

클론
```
git clone https://github.com/morrownr/rtl8852cu-20240510.git
cd rtl8852cu-20240510
```


컴파일이 완료되면 option 설정화면까지 나왔다면 성공  

Wifi가인식이 되지만 계속 flickering 현상이 있다. 꺼졌다가 켜졌다가..  
결국 원인은 옵션  

`sudo vi /etc/modprobe.d/8852cu.conf` 를 열어서  

```
blacklist rtw89_8852cu
blacklist rtw89_8852c
options 8852cu rtw_switch_usb_mode=1 rtw_power_mgnt=0 rtw_ips_mode=0
```
정도가 기본인데, 이렇게 하면 **실패**한다. 

확실한 것은 옵션에서  
```
options 8852cu rtw_switch_usb_mode=0 rtw_power_mgnt=0 rtw_ips_mode=0 rtw_drvextra_ips_mode=0 rtw_runtime_pm_enable=0
```

rtw_runtime_pm_enable=0: This is the most important one. It stops the "underflow" error you see in your logs.  
rtw_drvextra_ips_mode=0: Extra insurance against the radio sleeping.  

이후 
```
sudo dracut --force
```
또는 재부팅

그리고 가장 중요한 rtw_switch_usb_mode 는 0 기본으로 해준다. 
2를 해서 USB3 방식으로 사용할 수가 있는데, 또는 1,  이렇게 하면 계속 Wi-Fi가 꺼졌다 켜졌다가 한다.  
대신 0 기본 방식으로 하면 이 문제는 없어진다.  

또한 NetworkManager의 wpa_supplicant 를 사용하게 되면 이상하게도 와이파이 비번 인증이 안된다.  
> 이 또한 방법도 있겠지만 결국 해결책은 못찾음  

대신 iwd 를 설치하면 Wifi 비번 인증이 되는 것을 확인 했다. wifi backend 를 iwd 로 설정해서 사용하고  
wpa_supplicant 를 disable 해줘야 충돌이 없다. 아예 지워버렸다.    
> 한번 더 일부러 wpa_supplicant (iwd는 stop 시키고) 테스트를 했으나 비번을 계속 물어보며 인증이 성공하지 못하고 계속 실패한다.  

iwd로 하면 확실하게 접근이 된다. 


