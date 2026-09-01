# auto login 

Settings 에 보면 Users 부분에서 auto login을 가능하게 설정해 줄 수가 있는데 (Unlock 후)  

Automatic Login 만 설정해주면 됨


## disable 하기
반대로 settings 에서 위의 방법 반대로 설정해주면 되나,   
user가 안나오는 경우.. (다른 유저를 추가하고 sudoers에 추가했더니, 기존 유저가 안나옴- 정확하지는 않다)   

터미널을 열어서 `/etc/gdm3/custom.conf` 파일을 열어 수정한다   

```
# Enabling automatic login
#  AutomaticLoginEnable = true
#  AutomaticLogin = user1
```

위의 부분에서 false 로 바꿔준다.   
(원래 기본적으로 주석처리 되어 있으나, 한번 auto login이 되면 true 로 바뀌어 있게 된다)


추가로 WaylandEnable 시키는 방법..  
```
# Uncomment the line below to force the login screen to use Xorg
WaylandEnable=true
```
대신 설명대로 주석처리를 풀면 Wayland 을 사용할 수가 있다..   

> 주석처리를 해제하면 강제로 로그인 화면에서 Xorg 화면을 선택할 수 있게 해주는 것 같다   
로그인 화면에서 GNOME on Xorg 와 Ubuntu : 2개 중에서 고를 수 있게 되는데   
어쨋든 둘 다 X11 이다


reboot 하거나, command the line below.
```
sudo systemctl restart gdm3 
```

## 참고 wayland 인지 확인
```
echo $XDG_SESSION_TYPE
```

wayland 라고 나온다. X11 이면 x11 사용하는 것

WaylandEnable 이라고 해서 wayland는 아닌 듯 하다  

