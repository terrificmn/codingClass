# vnc other user display issue
VNC 를 사용할 경우에 (X server) 로그인 한 유저만(vnc session시작)  
X11 관련 퍼미션이 허용이 되는데, 그래서 해당 유저는 프로그램 등을 실행하는데 문제가 없지만, 

새로운 유저를 만들어서 할 경우에  
간편하게 `su username` 식으로 테스트를 진행할 수가 있는데   
터미널에서 꽤나 유용하게 깃 클론 등, ros 빌드 등 진행할 수가 있다.  

ros 패키지 등을 실행할 경우에 
```
This application failed to start because no Qt platform plugin could be initialized.  
Reinstalling the application may fix this problem. 
Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, 
vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, xcb.
```
이런 에러가 발생하면서 실행이 제대로 되지가 않는다. 

이렇게만 보면 apt install 등을 해야할 것 같지만, 의외로 해결책은 간단하다.   


rviz 를 실행해서 아래와 같은 에러이라면 더 확실하다
```
No protocol specified qt.qpa.xcb: could not connect to display :2.
```

이때는 처음에 말한 내용 처럼 X11 권한 문제이다. 

도커를 사용할 때에도 많이 사용하는 `xhost` 를 이용해서 to grant access 를 해주면 된다.  
> 새로운 유저에서 해주는 것이 아니라 원래 vnc를 실행했던 id 에서 사용할 user를 추가해주면 된다.  

```
xhost +SI:localuser:my-new-user
```

아예 local 유저들 모두 허용하려면 (less secure 하다고 함)
```
xhost +local:
```

이렇게 하면 해당 su 로 유저 로그인해서 사용할 경우에도 
프로그램 및 rviz 등이 잘 실행이 된다.

