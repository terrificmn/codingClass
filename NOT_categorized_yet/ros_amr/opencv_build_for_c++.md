opencv 설치 방법은 우분투 경우에는 apt install python3-opencv 도 있고   

```
sudo apt install libopencv-dev python3-opencv
```

python3의 패키지 매니저 pip을 이용해서 설치할 수도 있다. 


이번에는 직접 소스 코드 깃허브 다운 받은 후에 빌드를 해 본다 

먼저 깃허브 클론
```
git clone https://github.com/opencv/opencv.git
```

opencv 디렉토리로 이동 후 build 만들기
```
cd opencv
mkdir build
```

cmake를 이용해서 build script를 생성
```
cmake ../
```

그리고 build (소스파일을 make명령으로 빌드)
```
make -j4
```
역시 빌드 부분은 CPU가 많이 사용되고 시간이 꽤 걸린다  

빌드가 완료되면 install을 해주자  
```
sudo make install 
```

/usr/local/lib 등에 설치를 해준다  


이제 cpp 파일에 
```
#include <opencv2/opencv.hpp>
```
를 넣어주고 

CMakelists.txt 파일에는 find_package()에 OpenCV를 넣어준다   
그리고 include_directories()를 해서 라이브러리를 인쿠르드 시켜준다  
target_link_libraries()까지.. 모두 find_package를 해서 OpenCV_LIBS를 사용할 수 있다  

하면 되야 하지만... 멜로딕 도커 버전기준으로 안되고 있다;;

빌드 시 에러 메세지
```
  Could not find a package configuration file provided by "OpenCV" with any
  of the following names:

    OpenCVConfig.cmake
    opencv-config.cmake
```

구글링을 많이 해봤지만, opencv 자체는 빌드, 설치 시에 문제가 없었으므로 경로를 잘 못 찾고 있는 듯하다


## 해결
이럴 수가 에러 메세지에 힌트가 있었다. 늘 힌트를 주고 있는데 구글링 하면서 오래 돌아가는 것 같다 ㅠㅠ
```
 Could not find a package configuration file provided by "OpenCV" with any
  of the following names:

    OpenCVConfig.cmake
    opencv-config.cmake

Add the installation prefix of "OpenCV" to CMAKE_PREFIX_PATH or set
  "OpenCV_DIR" to a directory containing one of the above files.  If "OpenCV"
  provides a separate development package or SDK, be sure it has been
  installed.
```
못찾는다고 하니 먼저 OpenCVConfig.cmake 파일을 찾아보자. 

```
find / -name OpenCVConfig.cmake
```

그러면
```
/usr/local/lib/cmake/opencv4/OpenCVConfig.cmake
/usr/share/OpenCV/OpenCVConfig.cmake
```
2개의 dir을 찾음. 이 cmake 파일에는 버전 부터해서 여러 정보가 담겨 있다  

vi나 에디터로 열어보면 첫 번째로 나온 경로가 설치한 opencv4라는 것을 알 수 있다 

이제 CMakeLists.txt를 열어서 위의 에러 메세지에서 OpenCV_DIR을 설정하라고 했으니 set() 이용해서 지정한다 

이제 빌드를 할 때 경로등을 알 수 있으므로 target_link_libraries에서 OpenCV_LIBS 을 제대로 읽게 됨  

ROS 기준으로 아래 처럼 해주면 됨 (melodic)
```c
cmake_minimum_required(VERSION 3.0.2)
project(my_cam)

set(OpenCV_DIR /usr/local/lib/cmake/opencv4/)

find_package(catkin REQUIRED COMPONENTS
  roscpp cv_bridge image_transport OpenCV
)

add_executable(${PROJECT_NAME} src/my_cam_pub.cpp)
target_link_libraries(${PROJECT_NAME}
  ${catkin_LIBRARIES}
  ${OpenCV_LIBS}
)
```
좀 더 자세한 것은 camera_pub 깃허브 참고 

ros가 아니라면 
```c
cmake_minimum_required(VERSION 2.8)
project( DisplayImage )

set(OpenCV_DIR /usr/local/lib/cmake/opencv4/)
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( DisplayImage DisplayImage.cpp )
target_link_libraries( DisplayImage ${OpenCV_LIBS} )
```

참고로 
```
vi /usr/local/lib/cmake/opencv4/OpenCVConfig.cmake
```
해서 보면 처음에 주석을 설명이 되고 있는데 이 파일이 변수들을 정의하는데  
여기에보면 그 중에 OpenCV_LIBS 가 처음에 나온다 

```
 Usage from an external project:
#    In your CMakeLists.txt, add these lines:
#
#    find_package(OpenCV REQUIRED)
#    include_directories(${OpenCV_INCLUDE_DIRS}) # Not needed for CMake >= 2.8.11
#    target_link_libraries(MY_TARGET_NAME ${OpenCV_LIBS})
#

.... 생략

This file will define the following variables:
#      - OpenCV_LIBS                     : The list of all imported targets for OpenCV modules.
#      - OpenCV_INCLUDE_DIRS             : The OpenCV include directories.

... 생략
```
그래서 find_package(OpenCV )만 하면 될 듯 한데 아마도 버전이 3.2도 설치가 되어 있어서 못 찾는 것 같기도 하다


아쉽게도 워닝이 발생을 하기는 하나 ros cvbridge에서는 opencv3.2를 사용하는 하는 듯  
하지만 build도 잘 되고 카메라 실행도 잘 됨

Warnings   << cam_pub_cpp:make /home/docker_melodic/docker_ws/logs/cam_pub_cpp/build.make.006.log
/usr/bin/ld: warning: libopencv_core.so.3.2, needed by /opt/ros/melodic/lib/libcv_bridge.so, may conflict with libopencv_core.so.406


## 정리
CMakelists.txt 파일에  
set(OpenCV_DIR /usr/local/lib/cmake/opencv4/) 

넣어주자~


## Noetic에서는 
참고로 우분투 20.04 기준, ROS Noetic 에서 OpenCV는 버전 4.2 이고 find_package()을 안해도 문제가 없다  
우분투에서는 apt install python3-opencv 으로 설치됨
```
>>> print(cv2.__version__)P
4.2.0
```
cpp 코드에서 opencv를 include만 해주면 잘 실행된다 


