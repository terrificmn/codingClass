# ubuntu 18.04 melodic 버전 

백업을 복사를 했다고 해도 일단 cartographer 설치하는 법에 따라서 그대로 따라서 설치를 진행해야 한다  

https://google-cartographer-ros.readthedocs.io/en/latest/compilation.html


여기에서 우분투 18 melodic은 python버전으로 설치를 해야하고  
```
sudo apt-get install -y python-wstool python-rosdep ninja-build stow 
```

우분투 20.04 noetic 은 python3 버전으로 설치함에 유의한다


단, 여기에서 wstool merge 는 하지 않는다. 이미 파일들이 있으므로 다운은 안 받는다.   

> wstool merge 는 카토그래퍼를 다운을 받는다 

마지막으로 ninja로도 build를 진행하지 않고 catkin tools를 이용해서 빌드를 해보자

디버그용으로 빌드
```
catkin build --cmake-args -DCMAKE_BUILD_TYPE=RelWithDebinfo
```



## ubuntu 20.04 - Noetic 버전
```
sudo apt update  
sudo apt-get install -y python3-rosdep stow 
```
> 사실 ninja-build python3-wstool 은 필요 없을 듯.. 한번 해보고 안되면 설치   
sudo apt-get install -y python3-wstool python3-rosdep ninja-build stow 

catkin_ws가 이미 만들어져있으므로 이동  
```
cd catkin_ws
```
wools 툴은 사용하지 않는다. 기존에 있는 cartographer 사용함   
> 기존 파일 압축해서 복사하면 됨. 없다면 메뉴얼대로 따르면 되고, 그때는 wools를 써야할 함

catkin_ws 위치에서 실행한다  
```
cd ~/catkin_ws  
```
```
sudo rosdep init  
```
> The command ‘sudo rosdep init’ will print an error if you have already executed it since installing ROS. This error can be ignored.

```
rosdep update

rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y
```

여기에서 이제 catkin build를 실행하면 abseil 패키지를 찾지를 못한다 
> 여기에서 닌자로 빌드하지 않고 catkin tools로 build 한다   

```
Reading state information... Done
E: Unable to locate package libceres-dev
ERROR: the following rosdeps failed to install
```
위와 같은 에러 발생함

abseil을 찾지 못하므로 cartographer에 있는 스크립트 파일을 직접 설치해줘야한다  
충돌 가능성이 있을 수 있어서 만약 패키지가 이미 설치가 되어 있다면 삭제 한다
```
sudo apt-get remove ros-${ROS_DISTRO}-abseil-cpp
```

그리고 cartographer에 있는 scripts 디렉토리에서 sh파일 실행
```
cd src/cartographer/scripts
./install_abseil.sh
```

쉘 스크립트를 진행하려고 하는 abseil-cpp가 디렉토리가 있다고 하는 경우가 있다 (실패했다가 다시 진행하는 경우)   
scripts 디렉토리에 생긴 abseil-cpp 를 지우고 다시 실행
```
rm -rf abseil-cpp  
./install_abseil.sh
```

이렇게 되면 깃클론을 받으면서 바로 빌드를 해준다  (물론 git도 설치 되어있어야 함)
```
cd /usr/local/stow
sudo stow absl
```
요렇게 나오면 끝

이제 다시 워크 스페이스로 돌아가서 rosdep으로 설치를 다시 해준다   
```
cd catkin_ws  ## or cd catkin_fund_ws
rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y
```
관련 패키지가 설치가 되고 나서  `#All required rosdeps installed successfully` 끝나게 되면


여기에서 닌자로 빌드하지 않고 catkin tools로 build 한다   
```
catkin build
```


## ROS 관련 환경 변수 확인
.bashrc 에는 
```
source /opt/ros/noetic/setup.bash
source ~/catkin_ws/devel/setup.bash  
alias sb='source ~/.bashrc'
alias eb='gedit ~/.bashrc' 
```
정도 넣어준다


```
env | grep ROS   
env | grep LD_   
env | grep CMAKE   
```
등을 해서 2개의 워크 스테이션이 잘 나오는지 확인해준다


catkin_ws 에는   
```
catkin_init_workspace 
```
을 해주면서 시작

그리고 빌드가 마친 후에는  
```
catkin build
```

## 필요한 패키지

tf관련해서 에러가 발생하면 tf2 관련 패키지도 설치
```
 sudo apt-get install ros-noetic-tf2*
```
___


___


omo_r1 패키지 설치할 때 (빌드 시)
```
sudo apt install ros-noetic-navigation
```

설치해야한다


