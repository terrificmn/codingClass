[유투브 참고 https://www.youtube.com/watch?v=BLrHTHUjPuw](https://www.youtube.com/watch?v=BLrHTHUjPuw)

arduino IDE인 스케치를 설치해도 되고  IDE 2.0 Linux Zip file 64 bits 버전으로 받으면 됨
[arduino다운로드](https://www.arduino.cc/en/software)  

또는 vscode에서 Extensions 에서 PlatformIO IDE 검색 후 설치 사용한다.   
- vscode를 사용하면 자동완성 등에서 편하다. 
- 업로드 가능
- serial 모니터도 가능하나 read only 이다. (sketch IDE에서는 보내는 것도 됨)

새로운 프로젝트를 만들게 되면 (하단의 home 아이콘을 누르면 실행 됨 - PlatformIO 가 실행됨)      
Board 종류를 선택 후 예: arduino uno,  프로젝트 생성하면   

/home/유저명/Documents/PlatformIO/Projects/   
이하에 생성이 된다   

이제 확장자 platformio.ini 파일이 생기는데 여기에 port등을 설정 할 수 있다   

예:
```
[env:uno]
platform = atmelavr
board = uno
framework = arduino

; monitor_speed = A connection speed (baud rate) which “uploader” tool uses when sending firmware to board.
; monitor_port
; upload_port = /dev/ttyUSB0 If upload_port isn’t specified, then PlatformIO will try to detect it automatically.
```


___

업로드를 할 때   
/dev/ttyUSB0 이 퍼미션 에러가 발생할 경우   
udev rule을 설정해준다  

[udev-rules 설정](https://docs.platformio.org/en/latest/core/installation/udev-rules.html)

여기에 설치가 됨  
/etc/udev/rules.d/



업로드시 stk500_recv(): programmer is not responding 발생할 경우

USB 선 연결 해제 후 아두이노 reset버튼을 눌러 리셋후 다시 연결 후 사용




스케치에서 library를 install하게 되면 

~/Documents/libraries 디렉토리에 저장이 된다  



일단 
```
sudo usermod -aG dialout $USER
```

유저를 dialout 그룹에 포함시켜준다   

> 로그아웃 해야함




