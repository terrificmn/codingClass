## 우분투 dd로 설치 usb 굽기

먼저 usb를 연결한 후  
```
$lsblk -p
```
로 usb장치를 확인해준다. 중요 /dev/sd(X) 파티션(숫자) 제외한다   

위에서는 라즈베리파이에서 해서 /dev/sda로 잡혔고, 데스크탑이라면 아마도 /dev/sda는 하드디스크 일 것이므로    
usb장치를 잘 결정해준다. 

주의!!! 장치 디렉토리를 잘 못 지정해주면 다른 하디디스크 등의 내용이 지워질 수 있으므로    
조심할 것! (더블체크 할 것)   

lsblk 한 것에서 저장 장치로 of=부분은 자신에게 맞게 수정한다
```
sudo dd if=./ubuntu-20.04.2.0-desktop-amd64.iso of=/dev/sda bs=1M status=progress
```

> status=progress를 넣어야 진행 상황을 알 수 있다.



## 만약 실패하거나 잘 안되는 경우에는  

Etcher 프로그램을 사용하자 (balenaEtcher) - GUI 상태에서 사용
