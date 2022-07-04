백업을 복사를 했다고 해도 일단 cartographer 설치하는 법에 따라서 그대로 따라서 설치를 진행해야 한다  

https://google-cartographer-ros.readthedocs.io/en/latest/compilation.html

단, 여기에서 wstool merge 는 하지 않는다. 이미 파일들이 있으므로 다운은 안 받는다.   

> wstool merge 는 카토그래퍼를 다운을 받는다 

마지막으로 ninja로도 build를 진행하지 않고 catkin tools를 이용해서 빌드를 해보자

디버그용으로 빌드
```
catkin build --cmake-args -DCMAKE_BUILD_TYPE=RelWithDebinfo
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


