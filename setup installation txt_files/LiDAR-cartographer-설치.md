# google cartographer 사용하기 
***** 먼저 설치하기 전에 l515-pcl 패키지 해결해야함 - 그리고 git commit 할 것
그리고 참고할 사이트
https://google-cartographer-ros.readthedocs.io/en/latest/compilation.html
https://opensource.google/projects/cartographer

오픈cv 참고할 것 
https://www.opencv-srf.com/2010/09/object-detection-using-color-seperation.html

###############################################################3



툴 설치 wstool rosdep ninja (build를 하기 위한 툴이라고 함)
```
sudo apt-get update
sudo apt-get install -y python-wstool python-rosdep ninja-build stow
```

catkin_ws에 cartographer_ros 워크스페이스 만들기
```
cd catkin_ws
wstool init src
wstool merge -t src https://raw.githubusercontent.com/cartographer-project/cartographer_ros/master/cartographer_ros.rosinstall
wstool update -t src
```

dependencies 설치하기
```
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y
```
한번 실행했으면 에러가 발생하지만 무시하면 됨
ERROR: default sources list file already exists:

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

마지막으로 빌드 
```
catkin_make_isolated --install --use-ninja

```


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

