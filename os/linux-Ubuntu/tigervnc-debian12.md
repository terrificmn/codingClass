## tigervnc debian 12 설치

공통
```
sudo apt update
sudo apt install tigervnc-standalone-server tigervnc-common dbus-x11
```

```
sudo apt update
sudo apt install xfce4 xfce4-goodies
```
> xface 가 아니다,, 왜 자꾸 xface4라고 타이핑 했는지;;

또는 xface desktop install (minimal)
```
sudo apt install xfce4-session xfce4-panel xfwm4 xfdesktop4 xfce4-terminal
```

xstartup settings
```
#!/bin/sh
# Uncomment the following two lines for normal desktop:
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS

# Start D-Bus
eval `dbus-launch --sh-syntax --exit-with-session`

# Set background
xsetroot -solid grey

# Start XFCE4
exec startxfce4
```

## 데스크탑 버전인 kde plasma
xstartup for kde plasma 
```
sudo apt install kde-plasma-desktop plasma-workspace-wayland dbus-x11
```
아무래도 무겁다.
```
#!/bin/sh
# Uncomment the following two lines for normal desktop:
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS

# Start D-Bus
eval `dbus-launch --sh-syntax --exit-with-session`

# Set up environment
export XKL_XMODMAP_DISABLE=1
export QT_QPA_PLATFORM=xcb

# Start KDE Plasma session
#exec startplasma-x11
```
그래도 잘 되기는 하는데, 사용은 잘 되지만, 확실히 무겁고 느리다.

