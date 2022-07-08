https://catkin-tools.readthedocs.io/en/latest/installing.html

ros가 설치된 이후에 apt 로 설치를 해준다  
```
$ sudo sh \
    -c 'echo "deb http://packages.ros.org/ros/ubuntu `lsb_release -sc` main" \
        > /etc/apt/sources.list.d/ros-latest.list'
$ wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
```

```
sudo apt-get update
sudo apt-get install python3-catkin-tools
```

ROS Melodic, Noetic 2개 모두 python3-catkin-tools로 설치한다 

그 외에 pip3, source파일로부터 빌드로 설치할려고 하는 경우에는 맨 위의 링크를 참고


