# brltty 문제
/dev/ttyUSB* 처럼 usb 장치를 연결하면 0,1,2.. 식으로 나와야하는데   
잠깐 나왔다가 사라진다던가 없어지는 경우가 있다.   

`sudo dmesg` 했을 경우에 또는 `sudo dmesg | tail -10`
```
/dev/ttyUSB0 device connects then is forced to disconnect by another device
```
이 경우에 


brltty 서비스가 작동 중일 경우에 blind people 을 위한 accessibility 서비스라고 한다.  
서비스를 작동을 중지 시켜주면 다시 잘 작동하는 듯 하다.

```
sudo systemctl stop brltty-udev.service
sudo systemctl mask brltty-udev.service
sudo systemctl stop brltty.service
sudo systemctl disable brltty.service
```

제거는 할 때에는 
```
sudo apt remove brltty
```

