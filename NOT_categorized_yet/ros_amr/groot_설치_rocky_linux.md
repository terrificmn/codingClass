# groot 설치 (BehaviorTree) Rocky_Linux 용
Groot은 GUI 툴  
BehaviorTree의 Sequence등을 눈으로 볼 수 있게 만들 수 있다. 

BehaviorTree, Qt5 (tested with version 5.5.1), including the SVG module. 필요


## BT 먼저 설치
BehaviorTree 없다면 먼저 설치해준다
```
git clone https://github.com/BehaviorTree/BehaviorTree.CPP
cd BehaviorTree.CPP
mkdir build; cd build
cmake ..
make
sudo make install
```


## Groot 설치
#### ROS 에 설치
만약 리눅스용이 아닌 ROS에서 package 형태로 설치하려면 아래 방법을 사용하지 않고  
ROS 설치 시 다른점은 git에서 submodule update를 하지 않고   
깃 클론만 한 뒤에 rosdep으로 의존성 패키지 설치한 후에 cakin_make 를 해주게 된다 
```
cd catkin_ws/src
git clone https://github.com/BehaviorTree/Groot.git
cd ..
rosdep install --from-paths src --ignore-src
catkin_make  
```


### Groot 설치 - Rocky linux에 설치 (ros 아님)
의존성 패키지 설치
```
sudo dnf install qt5-qtbase-private-devel boost qt5-qtsvg-devel zeromq-devel
```

참고로 우분투라면 
```
sudo apt install qtbase5-dev libqt5svg5-dev libzmq3-dev libdw-dev
```
 
클론 후 build 디렉토리 만들고 cmake 를 해준다 
```
git clone https://github.com/BehaviorTree/Groot.git
cd Groot
git submodule update --init --recursive
mkdir build; cd build
cmake ..
make
```


## cmake 시 아래 에러 발생은
1. Qt5 발견되지 않게 설정된 경우
```
 Found package configuration file:

    /usr/lib64/cmake/Qt5/Qt5Config.cmake

  but it set Qt5_FOUND to FALSE so package "Qt5" is considered to be NOT
  FOUND.  Reason given by package:

```
에디터로 파일을 열어서 Qt5_FOUND 를 찾아보면  
set(Qt5_FOUND False) 에서 True로 바꿔준다 
```
if (NOT Qt5_FIND_COMPONENTS)
     set(Qt5_NOT_FOUND_MESSAGE "The Qt5 package requires at least one component")
     set(Qt5_FOUND True)
     return()
endif()
```
2개가 있으므로 찾아서 바꿀 것


2. 그리고  BehaviorTreeV3가 없다고 한다 
```
 "BehaviorTreeV3", but CMake did not find one.

  Could not find a package configuration file provided by "BehaviorTreeV3"
  with any of the following names:

    BehaviorTreeV3Config.cmake
    behaviortreev3-config.cmake
```

find_package(BehaviorTreeV3)의 BehaviorTreeV3는 예전 버전(?)명인듯하다   
이번에는 상위 디렉토리로 이동해서 CMakeLists.txt를 열어준다  
```
cd ..
vi CMakeLists.txt
```

그리고 BehaviorTreeV3 검색해서 BehaviorTreeV3를 behaviortree_cpp_v3 바꿔준다  
```
find_package(behaviortree_cpp_v3)
```
아래 if문은 바꿀 필요까지는 없을 듯



3. make 빌드 중에 zmq.hpp 파일을 못 찾는다고 나온다..아놔 zmq-devl 도 설치를 했는데 뭔가 경로를 못찾는듯
```
bt_editor/sidepanel_monitor.h:5:10: fatal error: zmq.hpp: No such file or directory
 #include <zmq.hpp>
```

다행히 3rd파티 파일들이 잘 준비되어있다. 그래서 파일을 열어 상대경로로 바꿔준다 ㅋ

깃 클론한 Groot 디렉토리 안에 bt_editor / sidepanel_monitor.h 를 열어준다
그리고 아래 처럼
```
// #include <zmq.hpp>
#include "../depend/BehaviorTree.CPP/3rdparty/cppzmq/zmq.hpp"
```
바꾼 후 저장 다시 make


이제 빌드 완료가 되면  build 디렉토리 안에 Groot 실행파일이 생긴다  
```
./Groot
```

로 실행하면 됨


## 심볼릭 링크 만들기
원하는 곳에 심볼릭 링크를 만들어서 편하게 사용하면 됨  아니면 복사를 해서 사용
현재 Groot 디렉토리에 있다면. (pwd 커맨드를 이용할 수 있다)   
원하는 곳에 심볼릭을 만들어준다
```
ln -s `pwd`/build/Groot $HOME/mygroot/groot
```
실행파일 Groot을 내 위치에 groot 심볼릭 링크로 만들어 준다   

아니면 /usr/bin/ 같은 곳에 심볼릭을 만들어주면 어디에서나 groot이라고 치면 실행 된다 

```
sudo ln -s $HOME/Groot/build/Groot /usr/bin/groot
```


### PATH에 추가하기
또는  복사 없이  
환경변수 path에 Groot 디렉토리를 추가하는 방법도 있다 
```
export PATH=$PATH:$HOME/Groot
```
이제 터미널 어디에서라도 Groot이라고 치면 위의 경로도 찾아서 실행해준다