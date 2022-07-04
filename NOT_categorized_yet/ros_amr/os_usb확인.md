omo_r1_bringup 패키지의 제공되는 scripts 에서 udev_rules를 정의할 수 있는데  

먼저 usb 장치를 확인  


udevadm info /dev/ttyUSB0


DEVPATH=/devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1:1.0/ttyUSB0/tty/ttyUSB0  
DEVNAME=/dev/ttyUSB0  
E: ID_VENDOR_ID=10c4  
E: ID_MODEL_ID=ea60  

대표적으로 알 수 있는 정보들, 만약 회사가 같으면 DEVPATH의 usb1/1-1/ 부분의 차이점 봐야한다     
만약 usb1 살펴보면 DEVPATH의 usb1/1-3 으로 다르다

E: DEVPATH=/devices/pci0000:00/0000:00:14.0/usb1/1-3/1-3:1.0/ttyUSB1/tty/ttyUSB1
E: DEVNAME=/dev/ttyUSB1
E: ID_VENDOR_ID=10c4
E: ID_MODEL_ID=ea60


또는  
dmesg | grep ttyUSB*   
도 확인가능


스크립트에서는   
```sh
echo "YD LiDAR (USB Serial) : /dev/ttyUSBx to /dev/ydlidar :"
if [ -f "/etc/udev/rules.d/ydlidar.rules" ]; then
    echo "ydlidar.rules file already exist."
else
    echo 'SUBSYSTEM=="tty", KERNELS=="1-1", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", MODE:="0666", GROUP:="dialout",  SYMLINK+="ydlidar"' >/etc/udev/rules.d/97-ydlidar.rules

    echo 'ydlidar.rules created'
fi
```

KERNELS, ATTRS, MODE, GROUP, SYMLINK로 설정을 하게 된다  

확인해보면 심볼릭 링크로 잘 연결이 되어 있다
```
ls -l /dev/ydlidar 
lrwxrwxrwx 1 root root 7 Jul  4 19:28 /dev/ydlidar -> ttyUSB0
```