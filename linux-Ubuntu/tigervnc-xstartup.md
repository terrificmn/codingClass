# xstartup 없을 경우

사실 /etc/vnc/xstartup이 없어도 실행이 잘 되어야 하는 듯 하다.   
ubuntu 20.04 에서는 .vnc/이하의 xstartup 만으로도 잘 실행이 되었다.  
> /etc/vnc/xstartup 실제로는 이 파일은 없었고, /usr/bin/gnome-session 파일은 있다.  


### 직접 만들어 주는 방법은 참고만...
```
mkdir -p /etc/vnc
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

이후 나머지는 .vnc/ 이하에 xstartup 을 만들어 주는데 똑같은 방식으로 하면 된다.  
단 dbus-launch 가 없다고 할 경우에는  
```
sudo apt install dbus-x11
```

하지만 우분투 22.04 같은 경우에는 wayland 를 사용해서 X11을 사용안해서  
vncserver가 작동을 안 한다.  

X11 서버로 작동해야지 가능한 듯 하다.   
> tigervnc는 wayland를 지원하지 않는다.




