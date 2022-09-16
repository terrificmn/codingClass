먼저 무선 장치를 usb로 연결한 후   
```
dmesg | grep ttyUSB*
```
로 몇 번 장치인지 확인한다 

장치가 확인이 되었으면  (예를 들어 3번 이면)
udevadm info /dev/ttyUSB3
로 장치의 자세한 정보를 본다  
VENDER_ID, ID, PATH 등이 중요하다.  
usb 허브에 물려있다면 1-1.1, 1-1.3 이런식으로 나오므로 참고한다   

이제 udev_rules를 만들기 위해서 script파일을 이용   
아래 내용은 gps usb를 인식할 때 했던 것인데 거의 echo 부분은 출력되는 부분이므로 알맞게 바꾸고   
else 부분에서의 echo는 udevadm 명령어로 확인했던 내용으로 수정해서 넣어준다  

좀 더 쉽게 하려면 변수를 따로 만들어서 거기에서만 바꾸고 echo 부분은 아예 수정 안되게 하는 식으로 하는게 좋을 듯 하다... 추후 작업 예정...

```shell
#!/bin/bash

echo ""
echo "This script copies gps udev rules to /etc/udev/rules.d/"
echo ""

echo "ublox Gps (USB Serial from -) : /dev/ttyUSBx to /dev/ttyGps :"
if [ -f "/etc/udev/rules.d/98-gps.rules" ]; then
    echo "98-gps.rules file already exist."
else
    echo 'SUBSYSTEM=="tty", KERNELS=="1-1.4", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", MODE:="0666", GROUP:="dialout", SYMLINK+="ttyMdGps"' > /etc/udev/rules.d/98-md-gps.rules

    echo '98-gps.rules created'
fi

echo ""
echo "Reload rules"
echo ""
sudo udevadm control --reload-rules
sudo udevadm trigger

```

이런 스크립트 내용임


이제 런치파일에서 rosserial_python 패키지를 이용하는데  
rosserial 노드를 이용해서 장치 번호를 넣어주는데 위에서 만든 심볼릭링크를 사용하게 된다 

런치파일 예
```xml
<node pkg="rosserial_python" type="serial_node.py" name="rosserial" output="screen">
	<param name="port" value="/dev/ttyMdRc"/>
	<param name="baud" value="57600"/>
</node>
```


