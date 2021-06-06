# This is an auto generated Dockerfile for ros:ros-base
# generated from docker_images/create_ros_image.Dockerfile.em
# 이 부분은 테스트 해보기
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

# Mesa libraries 설치 (AMD)
RUN apt-get update && \
  apt-get -y install libgl1-mesa-glx libgl1-mesa-dri && \
  rm -rf /var/lib/apt/lists/*

# rsodep 최초실행
RUN rosdep init && \
  rosdep update --rosdistro $ROS_DISTRO



# docker run \
#     --device=/dev/dri \
#     --group-add video \
#     --volume=/tmp/.X11-unix:/tmp/.X11-unix \
#     --env="DISPLAY=$DISPLAY" \
#   #your_image
#   docker-ros_ros

# docker run -it --device=/dev/dri --group-add video --volume=/tmp/.X11-unix:/tmp/.X11-unix --env="DISPLAY=$DISPLAY" docker-ros_ros gazebo


## http://wiki.ros.org/docker/Tutorials/Hardware%20Acceleration
