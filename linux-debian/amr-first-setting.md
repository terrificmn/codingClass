# radxa 5b+ 셋팅
## wifi
와이파이가 자동으로 연결되지 않는 현상.  
KDE 월렛 기능이 문제인 듯 한데, 셋팅을 제대로 해야할 듯 하지만, 어쨋든 비활성화로 한 다음에 
접속된 와아파이 SSID 를 삭제한 후에 다시 접속하면 비번 입력,   
이후 자동으로 접속이 잘 된다. 

## ssh
openssh-server 를 설치한 후에  
enable을 시켜야지 자동으로 시작됨에 유의

```
sudo apt install openssh-server
```

```
systemctl enable ssh.service
systemctl start ssh.service
```

## vnc
vnc는 ubuntu 22 만큼 까다롭지 않고 그냥 설치만 해주면 잘 작동한다  

기존 설치하듯이 apt로 설치  
```
sudo apt install tigervnc-standalone-server tigervnc-common
sudo apt install dbus-x11
sudo apt install xfce4 xfce4-goodies
```
> xfce4 는 데스크탑 환경, 가볍고 괜찮다.

설치 후 `vncserver` 실행하여 암호 설정해주고  

~/.vnc/ 이하에 xstartup 파일을 만들어 준다.  
```
vi ~/.vnc/xstartup
```

이하 내용, xfce4 사용할 경우 (추천)
```sh
#!/bin/sh
# Uncomment the following two lines for normal desktop:
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS

# Start D-Bus
eval `dbus-launch --sh-syntax --exit-with-session`

# Set up environment
export XKL_XMODMAP_DISABLE=1

# Set background
xsetroot -solid grey

# Start XFCE4
exec startxfce4
```

plasma 데스크탑 환경 사용할 경우 (조금 느림)   
데스크탑 설치  
```
sudo apt install kde-plasma-desktop plasma-workspace-wayland dbus-x11
```

이하 xstartup
```sh
# Uncomment the following two lines for normal desktop:
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS

# Start D-Bus
eval `dbus-launch --sh-syntax --exit-with-session`

# Set up environment
export XKL_XMODMAP_DISABLE=1
export QT_QPA_PLATFORM=xcb

# Start KDE Plasma session
exec startplasma-x11
```
여기까지만 해주면 잘 작동

> 기존에 설치되어 있는 KDE plasma 는 실제 모니터로 연결했을 경우 사용하면 좋고  
vnc 에서는 desktop 관련은 xfce4 가 가벼운 듯 (추천) 하다. 물론 KDE plasma로도 가능함  


## docker 
docker는 amr-64 에도 잘 지원되므로, 일단 docker 사이트에서 debian 버전으로 설치해주면 된다.  

이후  
```
sudo usermod -aG docker $USER
sudo usermod -aG adm $USER
```

> adm 은 journal files 접근 관련해서 아래와 같은 워닝 발생  
`docker Warning: some journal files were not opened due to insufficient permissions.`

서버로 활용하니 `systemctl enable docker` 해준다  


