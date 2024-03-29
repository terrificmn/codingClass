# udevadm | dmesg 로 장치 확인하기

usb 장치를 연결해서 심볼릭 링크로 만들어서 udevrule에 추가할 수가 있다 

무선조종장치, GPS, motor driver, lidar sensor등.. 각종 센서류를 등록할 수가 있다 

무선조종을 연결할 때 serial 패키지를 이용한다면  (md robot에서)
```
sudo apt install ros-noetic-serial
```

먼저 무선 장치를 usb로 연결한 후   
```
dmesg | grep ttyUSB*
```
로 몇 번 장치인지 확인한다 

> USB를 연결했다가 다시 빼면 disconnected 되었다는 식으로 나오는데 어떤 /dev/ttyUSBn 으로 잡혔는지 알 수 있다 

장치가 확인이 되었으면  (예를 들어 3번 이면)
```
udevadm info /dev/ttyUSB3
```
로 장치의 자세한 정보를 본다  

VENDER_ID, ID, PATH 등이 중요하다.  
usb 허브에 물려있다면 1-1.1, 1-1.3 이런식으로 나오므로 참고한다   

> 만약 usb관련 칩의 vender_id, id_product 의 경우에 같은 제품이 아니라면 다 다르게 나오므로  
 kernels를 지정할 필요가 없다. 오히려 지정을 안하면 특정 커널 (usb포트번호)에 매칭되는게 아니므로 유연하게 지정이 되게 된다. (usb을 뺏다가 다른 위치로 옮겼을 경우)  
물론 vender_id, id_product 가 겹치는 같은 경우라면 kernels를 지정을 해주면 된다


이제 udev_rules를 만들기 위해서 script파일을 이용   
아래 내용은 gps usb를 인식할 때 했던 것인데 거의 echo 부분은 출력되는 부분이므로 알맞게 바꾸고   
else 부분에서의 echo는 udevadm 명령어로 확인했던 내용으로 수정해서 넣어준다  

좀 더 쉽게 하려면 변수를 따로 만들어서 거기에서만 바꾸고 echo 부분은 아예 수정 안되게 하는 식으로 하는게 좋을 듯 하다... 추후 작업 예정...

GPS 관련 shell script 예)
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


