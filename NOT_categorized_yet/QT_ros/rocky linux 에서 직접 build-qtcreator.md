qtcreator-ros를 빌드를 설치하기 위한 dependencies 이지만..

## dependencies 설치
```
sudo dnf install mesa-libGL-devel ninja-build yaml-cpp-devel utf8proc-devel 
```

Rocky Linux 9.0 이상에서 설치할 경우

```
sudo dnf install mesa-libGL-devel yaml-cpp-devel
sudo dnf --enablerepo=crb install ninja-build
sudo dnf --enablerepo=crb install utf8proc-devel
sudo dnf install libxkbcommon-devel
sudo dnf install cmake g++
sudo dnf install vulkan-loader-devel
sudo dnf install python3-pip
python3 -m pip install pyyaml requests py7zr
```

Fedora 40 기준, 
```
sudo dnf install mesa-libGL-devel ninja-build utf8proc-devel vulkan-loader-devel libxkbcommon-devel
```
> 거의 처음 인스톨 후 다른 것들이 설치가 안되어 있는 경우  
로 설치 가능했음, (다른 enablerepo 할 필요없었음)  

단, 파이썬 몇개의 라이브러리는 필요  
```
python3 -m pip install pyyaml requests py7zr tqdm-loggable
```
이 정도면 py 실행이 되어 다운로드가 된다. 


### 잠깐! Fedora 42
기존 설치한 Qt 6.7.0 버전이 잘 동작을 안함   
이상 증상 :
```Qt policy QTP0001 is not set: ':/qt/qml/' is the default resource prefix for QML modules
```
물론 6.7 부터는 내 패키지에서 qt/qml/ qml 파일을 넣어서 사용할 수가 있으나,   
기본 설정을 안사용해도 무방하다. 그래서 별 문제가 발생을 안 했으나,   위의 워닝 부터 시작해서   
```
multiple definition of QtPrivate::IsFloatType_v<_Float16>
```
에러 발생.. 이것은 기존에 설치되어 있는 qt 버전에서 (이후 페도라 42로 업글)하면서 이상해진것 일 수도 있다.

*암튼* 그래서 Fedora dnf 로 받아서 사용할 수 있으니 dnf로 받아서 사용하자!

> 참고로 위의 dependenceis 는 딱히 설치할 필요는 없는 듯 함.. 필요시 설치

qt6 및 quick (Full QML/Quick Setup)
```
sudo dnf install qt6-qtbase-devel qt6-qtdeclarative-devel qt6-qtquickcontrols2-devel
```

qt-creator IDE
```
sudo dnf install qt-creator
```

qt6 는 `/usr/lib64/cmake/Qt6`

qtcreator 설치는 `/usr/bin/qtcreator`

CMakeLists.txt 에서는 
```
find_package(Qt6 REQUIRED COMPONENTS Core Quick Widgets)
```
이 정도로 사용할 수 있다.

___  
___  
## ONLY 참고 
## 이제 깃클론 (흠.. 이제 참고만 하자)
추후 편의를 위해 qtc-sdk 가 생기므로 하나로 모으는게 좋을 듯 하다. 깃허브 클론할 디렉토리를 넣어준다.
```
mkdir ~/qtcsdk
```

클론
```
cd ~/qtcsdk
git clone https://github.com/ros-industrial/ros_qtc_plugin.git -b devel
```

devel 브랜치에 따라서 빌드가 잘 안되는 경우도 발생하는 듯 하다.  
일단 로그 참고   
> commit 8e81cefcd3a8c2cab038b8a8821bc233d29869a3 (HEAD -> devel, tag: 11.0, origin/devel, origin/HEAD, origin/11.0)
Author: Christian Rauch <Rauch.Christian@gmx.de>
Date:   Sat Jun 10 23:25:13 2023 +0200
그래서 이미 준비된 압축파일을 그냥 받아서 실행하는게 더 쉬울 수도 있다.  
압축파일을 ftp 참고  


생성된 ros_qtc_plugin 이동 후 setup.py를 실행하면  
```
cd ros_qtc_plugin
./setup.py
```

이제 다운로드되는데 시간이 조금 걸림  (공식 사이트 다운로드 사이트가 조금 느린편;;)   
[qt official_releases 버전을 여기에서 다운 받을 수 있다](https://download.qt.io/official_releases/qtcreator/11.0/11.0.0/installer_source/)   

/tmp/qtc_sdk 에 다운 받은 것들이 압축이 풀린다. 이때 컴퓨터를 껏다가 키면 /tmp에서 저장된 것이 지워질 수 있으니 주의  

이제 현재 경로인 ros_qtc_plugin 에서 아래 실행   
> 단 버전 다운받은 것이 다를 경우 아래 명령어 중 경로나 버전이 다를 수 있다.  
setup.py 실행 후에 마지막에 나오는 프린트 되는 결과 확인하기   
```
cmake -B build -GNinja -DCMAKE_BUILD_TYPE=Debug -DCMAKE_PREFIX_PATH="/tmp/qtc_sdk/Tools/QtCreator;/tmp/qtc_sdk/6.4.0/gcc_64"
	cmake --build build --target package
```

호환성 문제로 여러번 빌드하다보면 
```
CMake Error at /tmp/qtc_sdk/Tools/QtCreator/lib/cmake/QtCreator/QtCreatorAPI.cmake:444 (add_library):
  The install of the ROSProjectManager target requires changing an RPATH from
  the build tree, but this is not supported with the Ninja generator unless
  on an ELF-based or XCOFF-based platform.  The
  CMAKE_BUILD_WITH_INSTALL_RPATH variable may be set to avoid this relinking
  step.
```

그래서 여기에 build 디렉토리를 들어가서 안의 파일들을 다 지워준다  

그리고 다시 위의 cmake 명령어를 실행하면 빌드가 잘 된다  

최종적으로 아래처럼 나오면 성공!
```
CPack: - Install project: ROSProjectManager []
CPack: Create package
CPack: - package: /home/sgtocta/ros_qtc_plugin/build/ROSProjectManager-9.1-Linux-x86_64.zip generated.
```

> sdk를 통해서 (/tmp생성) ros플러그인을 만들어준다.   
빌드가 끝나고 만들어진 ROSProjectManager-9.1-Linux-x86_64.zip 파일을 플러그인으로 추가할 수 있게 된다    

(onSep17,2023에는 ROSProjectManager-11 로 업데이트 된 모양 )  
이제 /tmp에 생성된 skd를 전체를 이동시켜준다  

```
cd /tmp
mv qtc-sdk/ ~/qtcsdk/
```

qtcreator는 qtc_sdk/Tools/Qtcreator/bin 에 있음

> PATH 환경 변수를 등록하거나 심볼릭링크를 /usr/bin/ 에 만들어 주면 편하게 사용할 수가 있다

이런식으로 한다 
```
sudo ln -s ~/qtc_sdk/Tools/QtCreator/bin/qtcreator /usr/bin/
```

## qt6  not found
```
CMake Error at /usr/share/cmake/Modules/CMakeFindDependencyMacro.cmake:76 (find_package):
  Found package configuration file:

    /tmp/qtc-sdk/6.8.0/gcc_64/lib/cmake/Qt6/Qt6Config.cmake

  but it set Qt6_FOUND to FALSE so package "Qt6" is considered to be NOT
  FOUND.  Reason given by package:
```

빌드할 경우에 qt6를 못찾는 경우  
`/tmp/qtc-sdk/6.8.0/gcc_64/lib/cmake/Qt6/Qt6Config.cmake`  경로를 찾아서   
파일을 열어보면 vi 등으로 연 다음에 검색

```
if(Qt6_FIND_REQUIRED_${module})
            set(Qt6_FOUND False)
```
로 되어 있는데 *False* 로 바꿔준 후에 다시 cmake 를 진행하면 잘 찾아진다  




## Ros plugin 등록
Qt creator를 실행을 해서  Help -> About Plugins -> Install Plugin 을 해서 zip파일 통째로 선택해주면 된다 import를 해준다  

New Project를 했을 때 Other Project에서 ROS Workspace를 볼 수가 있다 

완료가 되면 Qt Creator9.0 에 Qt는 6.4 버전이다  

> Sep24,2023 이미 Qt creator는 11.0 버전으로 업데이트 됨   


## 의존성 패키지 
~~Could NOT find XKB  XKB 위치를 찾지 못하고, (설치는 되어 있는 듯)~~     
~~Could NOT find WrapVulkanHeaders~~

등의 문제가 있지만 위의 (의존성 프로그램들) 설치하는 것에 해결됨.    


___

아래 내용은 그냥 참고만 하고 구지 필요 없을 듯 하다.   
dnf 말고 snap 패키지 버전으로 설치하는 하는 방법이 있다.  단, snap버전도 약간의 버그가 있는 듯 하다.  
그래서 조금 시간은 걸리지만 빌드 버전을 추천!

> 일단, ubuntu, rocky , fedora 빌드는 모두 문제 없다. (문제는 다운로드 속도가 너무 느림;;;)    


## dnf 로 설치를 하고 그냥 사용하면 이상 5.15 버전 정도도 호환이 잘 안된다 
조금 번거로워도 위의 빌드 버전 사용하자   

dnf 버전이 조금 낮기 때문에 qtcreator 4 버전이다. (Rocky linux 8.5기준)

```
sudo dnf install qtcreator
```

> rocky linux 8.5 에서는 qt4 버전인가? qtcreator가 4 ? 였는데  
다행히 rocky linux 9.0 이상에서는 dnf 패키지로 했을 때 qt 5.15 정도에  
qt-creator는 7.0 버전 설치되는 듯 하다  
 
 qt 6이상에서 작성한 것은 사용이 안될 수도 있어서 qt5 버전을 사용할 것이면 
 dnf로 설치해도 되지만 호환성이 걱정되서 빌드 버전으로 설치함 (호환성 생각하면 하위 버전이어야겠지만...)   
 따로 우분투에서 사용하고 있는 것은 참고로 qt creator 버전은 8.0.1, QT는 6.3.1 버전이어서   
 Rocky Linux에서도 빌드로 설치를 함
 
> snap버전은 파일 경로를 설정거나 할 때 에러가 발생하며 제대로 실행이 안된다  
> 이것은 ubuntu 에서 snap으로 설치할 때에도 같은 현상..;;;





