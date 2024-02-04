# kenrel update
wifi adapter 관련해서 드라이버 인식하려다가 결국은 커널 업데이트 하게 되었음.  
리눅스에서 in-kernel 드라이버로 사용할 수 있다고 하는데  
전혀 인식이 안된다.   

- Fenvi FU-AX1800  
- wifi 6 및 듀얼 밴드 2.4G/5Ghz 
- Mediatek 의 mt7921au 칩셋 사용

필요한 드라이버는 7921au 인데 몇몇 방법으로 시도했지만 wifi usb 인식 실패   

그래서 결국은 커널 업데이트를 하게 되었는데 Rocky Linux는 현재 5.14 버전

`uname -r` 또는 `uname -srm` 하면 된다
5.14.0-362.18.1.el9_3.x86_64   
Linux 5.14.0-362.18.1.el9_3.x86_64 x86_64

참고로 `lsusb` 했을 경우에
```
Bus 005 Device 002: ID 046d:c52f Logitech, Inc. Unifying Receiver
Bus 005 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 002: ID 0e8d:7961 MediaTek Inc. Wireless_Device
```

이렇게 나오는데 MediaTek의 7961 드라이버가 필요함을 알 수 있다.   
> 7961 - 7921au 드라이버 


## elrepo 로 커널 업그레이드
[elrepo 사이트](http://elrepo.org/tiki/kernel-ml)  
일단 공식 커널로는 최신 버전이므로, elrepo를 이용해서 elrepo 패키지를 추가한다.

```
sudo dnf install https://www.elrepo.org/elrepo-release-9.el9.elrepo.noarch.rpm
```

확인
```
yum repolist epel
```

결과
```
repo id          repo name                                               status
epel             Extra Packages for Enterprise Linux 9 - x86_64          enabled
```

이제 관련 커널을 설치를 한다.
```
sudo yum --enablerepo=elrepo* install kernel-ml
```
이렇게 하면 kernel-ml, ml-core, ml-modules 등이 설치된다.

이후 *reboot* 해준다. 다시 `uname -r` 확인해보면
```
6.7.2-1.el9.elrepo.x86_64
```

이제 wifi 인식하면 잘 된다.


#### 참고 
https://github.com/morrownr/USB-WiFi/blob/main/home/How_to_Install_Firmware_for_Mediatek_based_USB_WiFi_adapters.md

인스톨 방법.. 하지만 실패함

3개의 파일을 다운받은 후에  /lib/firmware/mediatek 넣어주는 방식

usb 어댑터 호환 목록

https://github.com/morrownr/USB-WiFi/blob/main/home/USB_WiFi_Adapters_that_are_supported_with_Linux_in-kernel_drivers.md
