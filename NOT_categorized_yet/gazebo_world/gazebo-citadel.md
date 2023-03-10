# gazebo noetic 버전은 Citadel, Garden

**일단 레포지터리가 틀릴 수도 있지만(ros2용 일 수도..) 잘 안됨! 그냥 ros의 gazebo11 을 사용하자**

## 주의사항은!!
아래의 리포지터리를 등록한 후에 `sudo apt-get install gz-garden` 를 하지 말 것!!!!!
왜냐하면 설치는 잘 되지만, 새로운 버전 7.0   
하지만 기존의 gazebo11이 지워지거나 이상해진다. 그래서 설치도 잘 안되게 됨  

만약 문제 발생시 
```
sudo apt remove gz-garden ros-noetic-gazebo-*
sudo apt autoremove
sudo apt install ros-noetic-gazebo-ros-pkgs  ros-noetic-gazebo-ros ros-noetic-gazebo-ros-control
```

### 시타델 설치? 잘 안됨 추후 업데이트

기존에 설치되어 있는 ros-noetic-gazebo- 는 버전 11  

추천 버전은 Gazebo Garden이고, ros와 연동하려면 Gazebo Citadel 이 추천이라고 하는데   

ros와 버전을 맞춰서 설치하기
```
sudo apt-get install ros-${ROS_DISTRO}-ros-gz
```
하지만 패키지를 못 찾는다   

ROS-1에서는 시타델로 설치를 해주는 듯 한데.. 어쨋든 안됨  

그래서 apt sources list에 추가 먼저 해준다 
```
sudo wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
sudo apt-get update
```

```


```