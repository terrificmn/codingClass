# ubuntu 20.04  x11 | wayland 확인하기

```
echo $XDG_SESSION_TYPE
```
해보면 현재 디스플레이 상태를 알 수가 있다.  

그러면 우분투 같은 경우에는 기본 설정이 아예 주석처리가 되어 있는데 주석을 해제해주면 로그인시 고를 수 있게 된다  

`/etc/gdm3/custom.conf`를 확인해보자
```
sudo vi /etc/gdm3/custom.conf
```

주석처리된 부분을 `#WaylandEnable=false` 해제하고 true 바꿔준다
```
...생략...
WaylandEnable=true
```

이렇게 한 후 재부팅을 하거나 gdm3를 다시 시작한다
```
sudo systemctl restart gdm3
```

> 바로 로그아웃이 된다.  

이제 로그인을 하기 위해서 유저를 누르고 오른쪽 하단에서 톱니바퀴를 골라준다   

정확히는 
ubuntu **wayland** 이런식으로 나와야지 적용이 된것.. 

GNOME on Xorg  
ubuntu wayland   
요렇게 나와야지 wayland가 되는 것임

> 만약 ubuntu 라고만 나오면 wayland가 안될 확률이 높음;;;



## 단, Nvidia의 그래픽 카드에서 지원을 안하는 경우도 있다
wayland를 지원을 안 하고 있는 nvidia의 그래픽 같은 경우는  

/lib/udev/rules.d 의 61-gdm.rules 파일을 보면 아예 disable 한다고 되어 있다

```
sudo cat /lib/udev/rules.d/61-gdm.rules 
```

결과
```
# disable Wayland on Hi1710 chipsets
ATTR{vendor}=="0x19e5", ATTR{device}=="0x1711", RUN+="/usr/lib/gdm3/gdm-disable-wayland"
# disable Wayland when using the proprietary nvidia driver
DRIVER=="nvidia", RUN+="/usr/lib/gdm3/gdm-disable-wayland"
```

## 그래서 wayland가 안됨
그래서  /etc/gdm3/custom.conf을 수정해도 wayland가 안나왔던 것..   
강제로 wayland를 사용안하고 x11로 쓰게 되어 있던 것  

위의 disable하는 것을 주석처리했더니,, 마지막 3번째 줄 DRIVER부분... 

다시 gdm을 재시작하면 wayland가 나온다. 사용이 가능하지만~   
**듀얼 모니터가 안된다..** 그리고 뭔가 원활히 작동을 안하는 것 같다...   

그래서 **비추천** 아직까지는 어쩔 수 없는 듯 하다  


그래픽 카드가.. *GEFORCE RTX 3060* 임


## desktop 변경 하려면
공식 지원해주는 
```
sudo apt install ubuntu-gnome-desktop
```
또는 
```
sudo apt install vanilla-gnome-desktop 
```

원하는 desktop을 설치한 후에 (검색하면 더 많이 있음)


로그아웃을 한 다음에 다시 로그인을 할 때 톱니바퀴를 골라서 해당 desktop으로 들어가 주면 된다   
xor가 붙은 것은 x11,