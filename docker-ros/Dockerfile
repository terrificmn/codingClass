####  테스트 중
# 이 부분은 테스트 해보기 # windows10 에서 안됨 - 더 테스트 해봐야할 듯
FROM ros:melodic-ros-core-bionic

# 또는 아예 desktop풀이미지 FROM osrf/ros:noetic-desktop-full 로 받기

#FROM ros:melodic  //다음에는 이걸로!!!!!! 위에 지우자

RUN apt-get update && apt-get install -y \
    ros-melodic-desktop-full

# 일반적인 melodic 설치위한 과정
RUN apt-get install --no-install-recommends -y \
    build-essential \
    python-rosdep \
    python-rosinstall \
    python-vcstools \
    python-rosinstall-generator \
    python-wstool \
    && rm -rf /var/lib/apt/lists/*

# Mesa libraries 설치 (AMD용)
RUN apt-get update && \
  apt-get -y install libgl1-mesa-glx libgl1-mesa-dri mesa-utils && \
  rm -rf /var/lib/apt/lists/*

# rsodep 최초실행  init 및 update만 하면 sudo 로 하라는 에러발생
RUN rosdep init \
  && rosdep update \
  && rosdep fix-permissions


RUN echo 'source /opt/ros/$ROS_DISTRO/setup.bash' >> /root/.bashrc
RUN echo "source /root/catkin_ws/devel/setup.bash" >> /root/.bashrc

#CMD ["/bin/bash", "-c", "source /opt/ros/$ROS_DISTRO/setup.bash && roscore"]

#위의 CMD 또는 docker-compose.yml 파일에서 command 부분에 roscore 를 안 사용한다면
#터미널에서 docker-compose run 으로 사용할 수 있음1

## http://wiki.ros.org/docker/Tutorials/Hardware%20Acceleration


#이제 실행은 아래처럼만 하면 됨
#현재 catkin_ws 연결이 되어 있는 상태
# 다만 docker-compose에서는 아직 실행이 잘 안되서 연결이 안됨 주의

# 그냥 실행 잘됨
# docker run \
#     -it \
#     -v ./catkin_ws:/root/catkin_ws \
#     -v ~/.ssh:/root/.ssh \
#     --network host \
#     --env ROS_MASTER_URI=http://localhost:11311 \
#     --name ros
#     docker-ros_ros
# 네임 겹침 주의


# cli 한줄로 바꾼것 (위에 꺼를 )
#docker run -it -v ~/Workspace/docker-ros/catkin_ws:/root/catkin_ws -v ~/.ssh:/root/.ssh --network host --env ROS_MASTER_URI=http://localhost:11311 docker-ros_ros
# 이렇게 하면 컨테이너에 들어가 진다
# volumn도 연결이 되어 있어서 로컬의 catkin_ws가 도커로 연결이 됨

# 컨테이너로 들어가면 
#source /opt/ros/melodic/setup.sh
#해주고
# 이제 /root/catkin_ws 로 가보면 (도커 컨테이너 안)
# 로컬 호스트에 넣어두었던 파일이 보임

#이제 작업은 작업은 로컬 호스트에서 해주면 된다
# 뭔가 실행을 하려면 다시 컨테이너로 와서 

# catkin_make 로 빌드하면 됨
# 그리고 패키지를 인식하게 하려면 catkin_ws로 이동해서 source devel/setup.bash
# 해준다
# 이제 roscore rosrun 차례로 하면 됨


# 들어가면 
#  $source /opt/ros/melodic/setup.sh
#  해주기


# 참고사이트 
# http://wiki.ros.org/docker/Tutorials/Hardware%20Acceleration#nvidia-docker2

####################################################333
# 01JUL2021까지는 docker-compose up해도 작동이 되게 했음 
# 하지만 터틀심까지만 실행이 되고 아직까지는 
# libGL error: No matching fbConfigs or visuals found
# libGL error: failed to load driver: radeonsi
# 에러가 발생하는 중


###################GUI 성공###########################
## X11로 하지 말자. (불가능한것은 아닌 듯?)
## Wayland display server로 실행한다. 처음에 로그인시 변경 
## 이게 참;; obs스튜디오나, davinch resolve프로그램은 X11 에서 실행되는데 참;; ㅋㅋㅋ

## 
# 참고하기
# https://stackoverflow.com/questions/16296753/can-you-run-gui-applications-in-a-linux-docker-container/25280523#25280523

# xhost +local:docker 를 해준다
# 그냥 쉽게 하려면 xhost + 처음에는 이렇게 했는데  xhost +local:docker를 한 이후로는 xhost + 로는 안됨

# 아래 코드는 실행은 됨 turtlesim, rqt, rqt_graph 정도는 되나, gazebo rviz 는 실행 안됨

##################################################
## (그래픽+catkin_ws 연동 - 거북이 , rqt, rqt_graph까지는 됨)
##이거는 docker-compose와 관계없이 실행~ docker-compose file하는 법도 알아볼 것
## docker run --rm -it -v $HOME/Workspace/docker-ros/catkin_ws:/root/catkin_ws -v ~/.ssh:/root/.ssh --network host --env ROS_MASTER_URI=http://localhost:11311 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --env="QT_X11_NO_MITSHM=1" docker-ros_ros bash

## MEANING:
# The flag -v /tmp/.X11-unix:/tmp/.X11-unix gives the container access to your X socket and -e DISPLAY=$DISPLAY sets the DISPLAY environment variable in the container the same as that of your desktop.

# 참고 사이트 
# https://www.pugetsystems.com/labs/hpc/Docker-and-NVIDIA-docker-on-your-workstation-Using-Graphical-Applications-915/