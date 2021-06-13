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
  apt-get -y install libgl1-mesa-glx libgl1-mesa-dri && \
  rm -rf /var/lib/apt/lists/*

# rsodep 최초실행  init 및 update만 하면 sudo 로 하라는 에러발생
RUN rosdep init \
  && rosdep update \
  && rosdep fix-permissions

#RUN echo 'source /opt/ros/$ROS_DISTRO/setup.bash' >> /root/.bashrc

# RUN echo "source /root/catkin_ws/devel/setup.bash" >> /root/.bashrc
#CMD ["/bin/bash", "-c", "source /opt/ros/$ROS_DISTRO/setup.bash && roscore"]

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


# 로컬 GUI 사용 예 (아직까지는 실패)
# docker run \
#     --device=/dev/dri \
#     --group-add video \
#     --volume=/tmp/.X11-unix:/tmp/.X11-unix \
#     --env="DISPLAY=$DISPLAY" \
#   #your_image
#   docker-ros_ros

# docker run -it --rm --device=/dev/dri --group-add video --volume=/tmp/.X11-unix:/tmp/.X11-unix --env="DISPLAY=$DISPLAY", docker-ros_ros gazebo


# 먼저 xhost +  를 해준다


## 실행은 잘 되나 amdgpu는 안됨
# docker run -it --rm \
#     --device=/dev/dri \
#     --group-add video\
#     --env="DISPLAY" \
#     --env="QT_X11_NO_MITSHM=1" \
#     --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
#     docker-ros_ros bash
    


##다른 창으로 로그인할 때 컨테이너로 들어가기

##docker exec -it --device=/dev/dri --group-add video --volume=/tmp/.X11-unix:/tmp/.X11-unix --env="DISPLAY=$DISPLAY" 34459eebf073 bash

## 아직까지는 안됨 


# 현재 에러는 
# xcb_connection_has_error() returned true
# ALSA lib confmisc.c:767:(parse_card) cannot find card '0'
# ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_card_driver returned error: No such file or directory
# ALSA lib confmisc.c:392:(snd_func_concat) error evaluating strings
# ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_concat returned error: No such file or directory
# ALSA lib confmisc.c:1246:(snd_func_refer) error evaluating name
# ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
# ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
# ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM default
# AL lib: (EE) ALCplaybackAlsa_open: Could not open playback device 'default': No such file or directory

