# google cartographer 사용하기 
참고할 사이트
https://google-cartographer-ros.readthedocs.io/en/latest/compilation.html
https://opensource.google/projects/cartographer

오픈cv 참고할 것 
https://www.opencv-srf.com/2010/09/object-detection-using-color-seperation.html

중요 catkin_make_isolated 명령어로 패키지를 빌드하게 되는데 
기존 catkin_ws 디렉토리에 넣어서 하게 되면 
다음부터하는 패키지 변경시에는 catkin_make가 동작을 안하게 된다
실수로라도 catkin_make_isolated 로 하게되면 빌드가 깨지게 되므로 주의해야하는 듯
하나의 패키지만 따로 하려면 
```
catkin_make_isolated --pkg <your package name> 
```
위 처럼 해준다

그래서 차라리 워크스테이션을 따로 다시 만들어 준다


```
mkdir catkin_iso_ws
```
그래서 이하 catkin_ws 는 catkin_iso_ws 디렉토리에서 작업을 해주면 
catkin_ws 에서는 이제 catkin_make를 하는데 문제가 없다!!! 

중요한 것은 ~/.bashrc 에서 setup.bash 파일을 넣어줘서 실행이 되게 해줘야함

source $HOME/catkin_ws_iso/install_isolated/setup.bash
위에꺼만해도 됨 (source $HOME/catkin_ws_iso/devel_isolated/setup.bash) 
를 추가해준다

그리고 
```
rospack profile
```
을 해주면 런치파일 및 rosrun 으로 노드들이 바로 잘 인식된다


# 본격 설치

툴 설치 wstool rosdep ninja (build를 하기 위한 툴이라고 함)
```
sudo apt-get update
sudo apt-get install -y python-wstool python-rosdep ninja-build stow
```

catkin_ws에 cartographer_ros 워크스페이스 만들기
```
cd catkin_iso_ws   ### 또는 cd catkin_ws
wstool init src
wstool merge -t src https://raw.githubusercontent.com/cartographer-project/cartographer_ros/master/cartographer_ros.rosinstall
wstool update -t src
```

[cartographer_ros] Done. 이라고 나오면 잘 되고 있는 것  
이제 dependencies 설치하기 (경로는 catkin_ws 에서)
```
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y
```
한번 실행했으면 에러가 발생하지만 무시하면 됨
ERROR: default sources list file already exists:

설치가 잘 되었다면 #All required rosdeps installed successfully 
나온다

만약 이런 비슷한 에러가 나면 해당 패키지의 package.xml 에 의존성 패키지를 잘 못 써준경우
수정해주면 된다
l515-pcl Cannot locate rosdep definition for [std_msg]
std_msgs 임

계속 catkin_ws 위치임. abseil-cpp가 필요하다고 함 스크립트 파일로 설치
```
src/cartographer/scripts/install_abseil.sh
```
충돌방지를 위해서 apt-get으로 설치했다면 지워준다
```
sudo apt-get remove ros-${ROS_DISTRO}-abseil-cpp
```
설치가 안되어 있으면 설치가 안되어 있으므로 안 지운다라고 뜨면 정상

마지막으로 빌드 
```
catkin_make_isolated --install --use-ninja

```

___

## 트러블 슈팅

만약 
에러발생
CMake Error at /usr/local/lib/cmake/Ceres/CeresConfig.cmake:85 (message):
  Failed to find Ceres - Missing requested Ceres components: [SuiteSparse]
  ..생략

CMake Error at CMakeLists.txt:39 (find_package):
  Found package configuration file:

    /usr/local/lib/cmake/Ceres/CeresConfig.cmake

  but it set Ceres_FOUND to FALSE so package "Ceres" is considered to be NOT
  FOUND.


ceres-solver 없다는 식으로 나오면 설치를 해줘야한다
위에서 ninja툴을 설치했으므로 ninja를 이용

먼저 필요한 의존성해결
```
sudo apt-get update
sudo apt-get install -y \
    cmake \
    g++ \
    git \
    google-mock \
    libboost-all-dev \
    libcairo2-dev \
    libeigen3-dev \
    libgflags-dev \
    libgoogle-glog-dev \
    liblua5.2-dev \
    libsuitesparse-dev \
    ninja-build \
    python-sphinx \
    stow
```
그리고 catkin_ws에 만들지 말고 다른 곳에서 빌드하면 됨 예: Libraries

깃허브에서 받은 후 빌드
```
git clone https://ceres-solver.googlesource.com/ceres-solver
cd ceres-solver
mkdir build
cd build
cmake .. -G Ninja -DCXX11=ON  -DCMAKE_INSTALL_PREFIX=/usr/local/stow/ceres
ninja -j15
sudo ninja install
cd /usr/local/stow/ 
sudo stow ceres
```

깃허브로 ceres를 설치했다면 catkin_ws 에서
```
catkin_make_isolated --install --use-ninja
```

다시 같은 에러가 발생하면 아예 소스파일 받아서 빌드하기 ceres-solver 설치
위의 깃허브로 ceres-solver 받았던 것은 지워준다
대신 이 방법은 시간이 조금 오래걸린다

```
wget http://ceres-solver.org/ceres-solver-2.0.0.tar.gz
tar zxf ceres-solver-2.0.0.tar.gz
mkdir ceres-bin
cd ceres-bin
cmake ../ceres-solver-2.0.0
make -j3
make test
# Optionally install Ceres, it can also be exported using CMake which
# allows Ceres to be used without requiring installation, see the documentation
# for the EXPORT_BUILD_DIR option for more information.
sudo make install
```


다시 cartographer 설치 마무리
```
catkin_make_isolated --install --use-ninja
```
설치가 꽤 오래걸린다



또 에러 발생

ninja: error: '/usr/lib/x86_64-linux-gnu/libGL.so', needed by '/home/ubun/catkin_ws/devel_isolated/cartographer_rviz/lib/libcartographer_rviz.so', missing and no known rule to make it


그래서 ls -li /usr/lib/x86_64-linux-gnu/libGL.so
를 검색해보면 파일이 없다. 이럴때 싱볼릭 링크를 만들어줘야한다
```
sudo ln -s /usr/lib/libGL.so.1 /usr/lib/x86_64-linux-gnu/libGL.so

```

최종 아래 처럼 나오면 성공! 
<== Finished processing package [31 of 31]:

