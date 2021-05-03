# X11 로그인 시 선택하기

obs-studio 프로그램을 설치하고 나니, 화면 캡쳐기능이 안되고 검정화면만 나왔는데..
조금 알아보니~ X11 Xorg 로 선택을 해야지 캡쳐도 잘 된다고 한다.

x11 xOrg로 바꾸려면
로그인할 때 톱니바퀴 모양을 누르면 wayland와 x11 중에서 고를 수가 있다.
wayland standard, x11 standard, classic 이런식으로 있었던 거 같음

현재 어떤 걸로 되어 있는지 환경 변수 확인하기
```
echo $XDG_SESSION_TYPE
```

설정파일 주석해제해서 xorg 선택 가능하게 하기
```
sudo vi /etc/gdm/custom.conf
```
GDM 설정이라고 하는데 
```
# Uncoment the line below to force the login screen to use Xorg
#WaylandEnable=false

```

WaylandEnable 부분의 주석을 해제하면 강제로 Xorg로 로그인할 수 있게 한다고 함
하지만 주석을 해제하고 false로 설정하지 않아도 로그인 시에 톱니바퀴에서 
로그인 방식을 고를 수 있다.

아무튼 강제로 Wayland 사용을 안하려면 
그리고 바로아래
DefaultSession=gnome-xorg.desktop
내용을 추가해준다 

이제 reboot하면
이제 로그인 시 톱니바퀴에 wayland가 없어진다


아래는 Xorg(X11)과 Wayland의 차이점

Why still Xorg?

Even though Wayland eliminates most of the design flaws of the Xorg it has its own issues. In order to communicate with the display server the programs, which act as clients, running on the system must know how to communicate with it. Xorg being older than Wayland is more developed and has better extensibility. This is the reason why some applicatons or programs might not run when using Wayland. This is why redshift doesn't work in Wayland.

Wayland is not very stable when compared with Xorg, as it is relatively new. Ubuntu 18 LTS's primary concern was of stability. Even though the Wayland project has been up for almost ten years things are not 100% stable. All this resulted in making Xorg as default in Ubuntu 18, but Wayland is installed allowing users to switch if desired.


https://www.secjuice.com/wayland-vs-xorg/