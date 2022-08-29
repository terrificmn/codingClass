# BehaviorTree BT
[BehaviorTree 튜토리얼 https://www.behaviortree.dev/](https://www.behaviortree.dev/)

ros에서 multithread가 되기는 하나  
서브스크라이브를 받는 상태가 아니면 각 함수들은 계속 loop에 걸려서 다른 것에 영향을 끼치는 것 같다   
그래서 현재 BT를 공부 중!


## 소스 빌드 및 설치
dependencies 관련 설치
```
sudo apt-get install libzmq3-dev libboost-dev
```
> 이미 설치 되어 있음. 그리고 나머지 의존성 패키지는 3rdparty 디렉토리에 포함되어있음

깃 클론 부터
```
git clone https://github.com/BehaviorTree/BehaviorTree.CPP.git
```

이동 후 build 디렉토리 만들고 cmake 하기
```
cd BehaviorTree.CPP
mkdir build && cd build
cmake ..
```

이후 make로 빌드하기, make install 설치 까지 진행
```
make
sudo make install
```

/usr/local/include
/usr/locl/lib
등등에 설치가 됨  


## CMakelists.txt 
```c
cmake_minimum_required(VERSION 3.5)

project(hello_BT)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
find_package(behaviortree_cpp_v3)

add_executable(${PROJECT_NAME} "hello_BT.cpp")
target_link_libraries(${PROJECT_NAME} BT::behaviortree_cpp_v3)
```
이런식으로 사용하면 된다 

package.xml에는 추가 안해도 상관없다 


다행히 빌드 및 vscode내에서 include는 문제가 없다   
하지만 cakin build를 하면  
```
  Could not find a package configuration file provided by
  "behaviortree_cpp_v3" with any of the following names:

    behaviortree_cpp_v3Config.cmake
    behaviortree_cpp_v3-config.cmake
```

또 찾아보자 



## 트러블슈팅
트러블슈팅 md파일 참고



