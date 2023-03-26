# wl-clipboard
처음에는 그냥 c++ 연동을 해서 clipboard에 복사를 하고 싶었지만..  
이런 저런 이유로 실패, 예전 라이브러리들은 X11 지원을 보통으로 하지만  

아예 프로그램을 설치를 해서 직접 라이브러리를 가져다가 쓰기보다는  
아예 cli 로 실행되는 프로그램을 설치 후 popen(), system() 같은 명령어로 간접적으로 실행하는 방법으로 생각을 바꿈   

> 이래저래 하면 라이브러리로 빌드하는게 되겠지만,, 시간도 많이 들고 얼핏보기에는  
> 뭔가 복잡해 보였다. 핑계 ㅋㅋ

## 의존성 설치
먼저 의존성 설치가 필요
Rocky linux 기준 
```
sudo dnf install wayland-devel
```

우분투는 확인해보지 않았으나, libwayland-dev 일 수도 있음

> 어쨋든 linux, BSD 시스템, Mac OS 및 GNU Hurd를 지원한다고 하니 꼭 필요한 dependency는  
wayland-client 라고 함

그리고 meson 설치, 빌드를 위해서 설치, 차세대 빌드시스템 이라고 한다  
어쨋든 이 프로그램은 meson과 ninja를 이용해서 빌드를 한다. 

```
sudo python3 -m pip install meson
```

[나머지 옵션 의존성 패키지도 있으나 필요할 시 깃허브확인-wl-clipboard](https://github.com/bugaevc/wl-clipboard)


## 빌드 후 설치
깃클론 후 이동
```
git clone https://github.com/bugaevc/wl-clipboard.git
cd wl-clipboard
```

빌드
```
meson build
cd build
ninja
```

설치
```
sudo ninja install
```

/usr/local/bin 등으로 설치가 된다. 


## meson 참고
wl-clipboard 유틸에서는 `meson build` 라는 명령어와 만들어진 meson.build 파일을 사용하는 듯 하다. 

[CMake는 가라! Meson과 함께하는 차세대 C++ 빌드 시스템 구축](https://int-i.github.io/cpp/2021-06-26/cpp-meson/)  

