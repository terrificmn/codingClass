# powertools 가능하게 하기

obs-stdio를 설치하려고 하면   
sudo dnf install obs-studio

```
conflicting requests
  - nothing provides libSDL2-2.0.so.0()(64bit) needed by ffmpeg-4.2.4-1.el8.x86_64
```
libSDL2-2.0은 아무리 yum 명령어를 쳐도 match 되는게 없다

이때 powertools를 사용가능하게 리포지터리 추가를 해주면
쉽게 다운받아지고 의존성 패키지도 해결해준다   

You can enable it with the following commands:

```
yum install dnf-plugins-core
yum config-manager --set-enabled powertools
```

화면 캡쳐 블랙일때 wayland에서 x11로 로그인 해준다
 
그러면 스크린 캡쳐가 잘 된다.
