# omo_r1 패키지를 설치할 때 USB확인
omo_r1_bringup 패키지의 제공되는 scripts 에서 udev_rules를 정의할 수 있는데  

먼저 usb 장치를 확인해보면 udevadm 명령어를 사용할 수 있다
```
udevadm info /dev/ttyUSB0
```

또는 dmesg 명령어 사용  
```
dmesg | grep ttyUSB*   
```
도 확인가능

아래는 그 중 몇몇 정보임
```
DEVPATH=/devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1:1.0/ttyUSB0/tty/ttyUSB0  
DEVNAME=/dev/ttyUSB0  
ID_VENDOR_ID=10c4  
ID_MODEL_ID=ea60  
```

대표적으로 알 수 있는 정보들, 만약 usb 회사가 같으면 ID_VENDOR_ID, ID_MODEL_ID가 같으므로  
DEVPATH의 usb1/1-1/ 부분의 차이점을 봐야한다     
만약 usb1 살펴보면 DEVPATH의 usb1/1-3 으로 다르다

```
E: DEVPATH=/devices/pci0000:00/0000:00:14.0/usb1/1-3/1-3:1.0/ttyUSB1/tty/ttyUSB1
E: DEVNAME=/dev/ttyUSB1
E: ID_VENDOR_ID=10c4
E: ID_MODEL_ID=ea60
```

위 2개를 비교를 해보면 나머지는 같고 DEVNAME는 장치가 다르지만 구별해내기 어렵다  
그러나 DEVPATH는 다른 것을 알 수 있다.  

이제 usb 가 파악이 되었다면 omo_r1 패키지에서 제공하는 스크립트를 보자

**주의** 만약 1-1 이 같은 usb가 겹친다면 위에 처럼 1-1 과 1-3 으로 다를 수도 있지만  
1-1, 1-1 과 같이 나오게 된다면 그 다음줄까지 봐서 바꾸면 된다  

ttyUSB1을 확인했을 경우와 
```
DEVPATH=/devices/pci0000:00/0000:00:15.0/usb1/1-1/1-1.4/1-1.4:1.0/ttyUSB1/tty/ttyUSB1
```
ttyUSB2를 확인했을 경우  
```
DEVPATH=/devices/pci0000:00/0000:00:15.0/usb1/1-1/1-1.2/1-1.2:1.0/ttyUSB2/tty/ttyUSB2
```
1-1로 같다. 이럴 때에는 1-1.4와 1-1.2 처럼 뒤에 것으로 비교해주면 됨   
KERNELS 설정도 1-1.4 처럼 해주면 된다



## udev rule 설정하기
편리하게 스크립트에서는 해당 장치를 symlink로 특정 이름을 지정해서 만들어 줄 수가 있다  
위에서 찾은 정보를 매칭해서 수정해주자 (KERNELS, ATTRS의 idVendor, idProduct 등..)

> omo_r1_bringup 패키지에서 scripts를 살펴보자

```sh
...생략
...
echo "This script copies md udev rules to /etc/udev/rules.d/"
echo ""

echo "Motor Driver (USB Serial from -) : /dev/ttyUSBx to /dev/mdMotor :"
if [ -f "/etc/udev/rules.d/98-md.rules" ]; then
    echo "98-md.rules file already exist."
else
    echo 'SUBSYSTEM=="tty", KERNELS=="1-1.4", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", MODE:="0666", GROUP:="dialout", SYMLINK+="mdMotor"' > /etc/udev/rules.d/98-md.rules

    echo '98-md.rules created'
fi

echo ""
echo "Reload rules"
echo ""

```

확인해보면 심볼릭 링크로 잘 연결이 되어 있다. 만들어진 /dev/mdMotor 보면  
```
ls -l /dev/mdMotor 
lrwxrwxrwx 1 root root 7  7월 11 17:26 /dev/mdMotor -> ttyUSB1
```
