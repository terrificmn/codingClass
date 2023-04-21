# SDL 설치

설치하려고 할 때 아래와 같은 방식으로 안될 경우 
```
The following packages have unmet dependencies:
 libsdl2-dev : Depends: libdbus-1-dev but it is not going to be installed
               Depends: libegl1-mesa-dev but it is not going to be installed
               Depends: libgles2-mesa-dev but it is not going to be installed
               Depends: libibus-1.0-dev but it is not going to be installed
               Depends: libudev-dev but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
```


슈퍼키(윈도키)를 누르고 "Software & Updates"를 검색   
창이 열리면 Updates 탭을 클릭   
Subscribed to:를 Custom 이나 Security updates only 으로 되어 있다면   
과감하게(?) **All updates**로 선택을 해주고 Close를 눌러준다   

```
sudo apt update
sudo apt install libsdl2-dev
```
설치가 된다   

설치 후에 다시 Softwar & Updates 프로그램을 띄우고   
다시 Updates 탭으로 가서 Revert를 눌러준다   


## ROcky 
`sudo dnf install SDL2-devel` 



## include SDL
#include "SDL.h" 하고 빌드를 하면   
SDL.h no such file or directory found 라고 나온다   

libsdl2-dev가 잘 설치가 되었다면 SDL.h 가 아닌  
```c
#include <SDL2/SDL.h>
```
로 인쿠르드 해주면 빌드가 잘 된다 

컴파일러 linker에는 `-lSDL2main` 와 `-lSDL2`를 넣어준다 ()


추가로 설치할 것들 우분투 기준
```
apt-get install libsdl2-image-dev  
apt-get install libsdl2-mixer-dev  
apt-get install libsdl2-ttf-dev  
```

헤더 
```c
#include <SDL2/SDL_image.h>
#include <SDL2/SDL_ttf.h>
#include <SDL2/SDL_mixer.h>  
```

compiler linker에는   
각각 `-lSDL2_image`, `-lSDL2_ttf`, `-lSDL2_mixer`   



## code::block 에서 linker 셋팅
Projcect가 열려있는 상태에서 Project를 누르고 Project settings 탭 (첫번째)   
아래에서 Project build options을 클릭 -> Linker settings 를 눌러준다   

오른쪽에 Other linker options 에 
```
-lSDL2
```
라고 추가해준 후에 OK 버튼을 클릭해준다   

> vscode나, gcc+로 컴파일 할 때에도 -lSDL2 라고 해주면 될 듯 하다   

