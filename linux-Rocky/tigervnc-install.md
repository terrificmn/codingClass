# tiger vnc 설치
먼저 tigervnc server / vncviewer 등을 설치할 수가 있다.

## vncviewer
먼저 클라이언트만 필요한 경우에는

```
sudo dnf install tigervnc
```

실행은 터미널에서 `vncviewer` 로 하면 된다. 윈도우가 열리면 주소 등을 입력 후 사용   
또는 `vncviewer 192.168.100.100:5901`, ssh터널링 사용시 `vncviewer localhost:5901` 등으로 사용한다.


### realvnc viewer
realvnc viewer가 필요한 경우에는 realvnc 사이트에서 rpm 파일을 다운 받은 후 설치   
```
sudo rpm -ivh VNC-Viewer-7.버전...rpm
```

> tigervnc server로 서비스할 경우 뷰어를 real vnc로 사용할 경우 문제는 없으나  
탭이나 화면 전환을 할 때 느리게 전환되는 현상이 있음.   


## vncserver
현재는 딱히 rocky linux나 fedora에서 vnc server를 실행할 일이 없어서 설치는 안했지만...

> 거의 서버는 ubuntu에서 사용하다보니.. 클라이언트만 사용 중

설치는 이렇게
```
sudo dnf install tigervnc-server
```

dnf에서 패키를 못 찾는다면 
```
sudo dnf install epel-release
```
이후 다시 설치 진행


## vncserver 설정
~/.vnc 이하 디렉토리에 xstartup 파일을 만들고   
이 방법도 결국은 gnome-session 을 사용하는 듯 하다.  
``` 
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
exec /etc/vnc/xstartup &
vncconfig -iconic &
dbus-launch --exit-with-session /usr/bin/gnome-session --systemd --session=ubuntu &
```

중요한 점은 DBUS_SESSION_BUS_ADDRESS 을 unset을 해야하는 것이고   
dbus-launch 커맨드가 비슷하게 다 작동한다. 차이점을 찾아볼려고 했지만 일단, gnome-session 을
```
dbus-launch --exit-with-session gnome-session &

또는
dbus-launch --exit-with-session gnome-session --session=ubuntu &
```

> 다같이 작동하는 이유는 /usr/bin/gnome-session 실행 파일이 있기 때문  


