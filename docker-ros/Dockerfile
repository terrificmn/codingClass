# 이 부분은 테스트 해보기 # windows10 에서 안됨 - 더 테스트 해봐야할 듯
FROM ros:melodic-ros-core-bionic

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

ENV ROS_DISTRO melodic

# rsodep 최초실행
RUN rosdep init && \
  rosdep update --rosdistro $ROS_DISTRO

## http://wiki.ros.org/docker/Tutorials/Hardware%20Acceleration

# 사용 예
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

