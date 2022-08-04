아직 제대로 정리 안됨;; 실행 안됨

 vnc서버 먼저 설치
sudo apt install xserver-xorg-core
sudo apt install tigervnc-standalone-server tigervnc-xorg-extension tigervnc-viewer

여기 다시 참고해서 도전하기!

https://www.tecmint.com/install-and-configure-vnc-server-on-ubuntu/


해상도 정해서 vnc서버 실행
```
 vncserver -depth 24 -geometry 1680x1050
```
 vncserver -kill :*


문제
r1d2@omo:~$ ssh sgtubunamr@192.168.10.27 -L 5901:127.0.0.1:5901
ssh: connect to host 192.168.10.27 port 22: Connection refused

openssh가 설치가 안되어 있을 수가 있다  


뷰어 일단 이거는 보류
sudo apt install tigervnc-viewer



x서버에서 마우스 키보드 안 될 때 
sudo apt install xserver-xorg-input-all

그런데 어떻게 입력? ssh로 접속하거나~ wayland로 들어간다  
