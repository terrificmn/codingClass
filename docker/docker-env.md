환경변수를 Dockerfile 에서는 
ENV USER=name  식으로 해야지 정확히 인식하는 듯 하다.  
조금 테스트가 필요하지만  
.evn 파일에서 정의했던 환경변수가 Dockerfile에서 인식이 안된다? 이유는 잘 모르겠다.  
Rocky 에서는 잘 되었는데 docker버전이 달라서 그럴 수도? 일단 Ubuntu에서는 안 되서   
Dockerfile 에도 ENV USER=${USER} 로 설정해줬다. (그리고 .env 파일에도 설정)



docker run -it --net=host --gpus all \
    --env="NVIDIA_DRIVER_CAPABILITIES=all" \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    docker-ros_ros \
    bash -it -c "roslaunch gazebo_ros empty_world.launch"