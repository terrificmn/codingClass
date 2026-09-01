# xstartup 없을 경우
우분투 20 버전에서는 실제 /etc/vnc/xstartup 파일이 없어도 실행하는데는 문제가 없었다.
그러나 우분투 22 에서는 위의 경로에 파일이 없을 경우 vncserver 작동이 실패한다.

> ubuntu 20.04 에서는 .vnc/이하의 xstartup 만으로도 잘 실행이 되었다.  
> /etc/vnc/xstartup 실제로는 이 파일은 없었고, /usr/bin/gnome-session 파일은 있다.  

먼저 의존성 패키지 설치,
```
sudo apt install ubuntu-gnome-desktop dbus-x11
```
> 단 dbus-launch 가 없다고 할 경우에는 dbus-x11 설치해야한다.

### 직접 만들어서 사용하기
ubuntu 22.04 버전, 커널 6.8.0-47-generic

먼저 /etc 이하에 vnc 디렉토리 및 파일을 만들어 준다.
```
sudo mkdir -p /etc/vnc
sudo vi /etc/vnc/xstartup
```

이후 xstartup 을 만들어 준다. 
```
#!/bin/sh

test x"$SHELL" = x"" && SHELL=/bin/bash
test x"$1"     = x"" && set -- default

unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS

vncconfig -iconic &
"$SHELL" -l << EOF
export XDG_SESSION_TYPE=x11
export GNOME_SHELL_SESSION_MODE=ubuntu
dbus-launch --exit-with-session gnome-session --session=ubuntu
EOF
vncserver -kill $DISPLAY
```

실행 권한을 만들어 준다.

```
sudo chmod +x /etc/vnc/xstartup
```

이후 기존 자신의 home/user 이하 디렉토리에 만들어주는데   
`vncserver` 입력하면 패스워드 설정 및 ~/.vnc 디렉토리를 만들어준다.   

나머지는 .vnc/ 이하에 xstartup 을 기존과 비슷하지만 실제 /etc 이하의 xstartup 을 실행하게 해준다.    

이동 및 입력
```
cd  ~/.vnc
touch xstartup
```

편집기로 열어서 내용을 넣어준다.
```
#!/bin/sh
[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
```

역시 실행 권한을 준다.
```
sudo chmod + ~/.vnc/xstartup 
```

> 나머지 uvncconfig -iconic 은 실제 xstartup 에서 이미 실행하게 되는 듯 하다.

~~하지만 우분투 22.04 같은 경우에는 wayland 를 사용해서 X11을 사용안해서~~  
~~vncserver가 작동을 안 한다.~~  

X11 을 사용하게 하면 된다. 
확인은 `echo $XDG_SESSION_TYPE`

> tigervnc는 wayland를 지원하지 않는다.

### permission 에러 발생 시
```
Can't exec "/home/myuser/.vnc/xstartup": Permission denied at /usr/share/perl5/TigerVNC/Wrapper.pm line 1237.
```
위에 처럼 실행 권한을 설정해준다.

## trouble shooting
vncserver 는 정상 작동하는데 클라이언트에서 접속이 안 될 경우  

```
vnc unable connect to socket: Connection timed out (110)  
```

firewall 이 작동할 경우에 사용할 수 있게 허용을 해줘야 한다.

ufw 확인하기
```
sudo ufw status
```

주롷 사용하는 포트 추가하기
```
sudo ufw allow 5902
```
결과
```
5902 (V6)   ALLOW  Anywhere(V6)
```

