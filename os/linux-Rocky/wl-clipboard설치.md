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
sudo dnf install wayland-devel ninja-build pip g++
```

우분투는 확인해보지 않았으나, libwayland-dev 일 수도 있음.확인 : 우분투에서는 
```
sudo apt install libwayland-dev
```

> 어쨋든 linux, BSD 시스템, Mac OS 및 GNU Hurd를 지원한다고 하니 꼭 필요한 dependency는  
wayland-client 라고 함

그리고 meson 설치, 빌드를 위해서 설치, 차세대 빌드시스템 이라고 한다  
어쨋든 이 프로그램은 meson과 ninja를 이용해서 빌드를 한다. 

```
sudo python3 -m pip install meson
```

참고로 sudo 로 설치할 시에는 아래와 같은 워닝이 발생하지만   
```
  WARNING: The script meson is installed in '/usr/local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed meson-1.2.1
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
```
sudo로 설치를 안 하면 아래와 같은 에러 발생   
```
Traceback (most recent call last):
  File "/home/sgtraphael/.local/bin/meson", line 5, in <module>
    from mesonbuild.mesonmain import main
ModuleNotFoundError: No module named 'mesonbuild'
```

그래서 sudo로 설치를 해준다.   
이유는 일반 유저로 설치를 하면 home디렉토리에 설치가 되어서 root가 사용할 수가 없다.  
그래서 root 가 사용할 수 있게 설치를 하거나, 시스템 폴더에 설치를 해준다.(모든 유저 사용가능-sudo 사용시)   
그래서 '/usr/local/bin'에 설치가 되는 듯 하다..  

> 일반 유저로 meson을 설치하게 되면 ~/.local/bin 이하에 meson이 설치가 되어서   
심링크 또는 $PATH 등에 넣어서 사용할 수 있겠지만, 마지막에 /usr/ 이하 경로에 설치install 명령을 할 때 실패하게 되어서   
그냥 맘편하게 사용하려면 sudo로 설치해주자.


[나머지 옵션 의존성 패키지도 있으나 필요할 시 깃허브확인-wl-clipboard](https://github.com/bugaevc/wl-clipboard)


## 빌드 후 설치
깃클론 후 이동
```
git clone https://github.com/bugaevc/wl-clipboard.git
cd wl-clipboard
```

빌드
```
meson setup build
cd build
ninja
```

설치
```
sudo ninja install
```
또는 `sudo meson install` 

/usr/local/bin 등으로 설치가 된다. 


## meson 참고
wl-clipboard 유틸에서는 `meson build` 라는 명령어와 만들어진 meson.build 파일을 사용하는 듯 하다. 

[CMake는 가라! Meson과 함께하는 차세대 C++ 빌드 시스템 구축](https://int-i.github.io/cpp/2021-06-26/cpp-meson/)  



## 우분투 wayland가 안되는 경우  
그래픽 카드 혹은 시스템 설정 때문에 wayland가 막혀있을 경우가 있음   
그러면 설정에서 풀어줘야하는데, Nvidia의 그래픽 카드는 지원을 안하는 경우도 있다고 한다   

gdm설정-wayland.md 파일을 참고하자 

> wayland가 안되면 프로그램을 구동 시 `Failed to connect to a Wayland server` 라고 나온다   

