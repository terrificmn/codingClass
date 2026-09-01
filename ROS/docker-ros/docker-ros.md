# ROS 도커로 사용하기

ROS 이미지가 받아져 있다면 docker run 또는 docker exec 를 통해서 ros 컨테이너를 사용할 수가 있다
별다른 옵션을 넣어주지 않고 
```
docker run -it docker-ros /bin/bash
```
로만 해주게 되면 컨테이너 안으로 들어가서 작업을 해 볼 수는 있지만
원래 HOST컴퓨터의 GUI 자원을 전혀 사용할 수가 없다~ 즉 터틀심 같은 화면이 표시되는 것들을 할 수가 없다

그래서 publisher와 subscriber 등을 CLI 환경, 즉 터미널로 command로만 입력하면서 text로만 보는 상태라면
위의 명령어 처럼 해주면 된다.


# GUI 연동하기
그런데 그래픽 화면을 보러면 파라미터로 옵션을 넣어줘야하는 것들이 조금(?) 있다.

그 전에 중요하게 할 작업
```
xhost +local:docker
```
non-network local connections being added to access control list 이렇게 나오면서
위의 명령어로 원래 컴퓨터의 GUI를 사용할 수가 있게 된다. (docker그룹만)

xhost + 만 해주면
access control disabled, clients can connect from any host


옵션을 아래처럼 넣어서 실행을 하면 된다
```
docker run --rm -it -v $HOME/Workspace/docker-ros/catkin_ws:/root/catkin_ws -v ~/.ssh:/root/.ssh --network host --env ROS_MASTER_URI=http://localhost:11311 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /dev:/dev --env="QT_X11_NO_MITSHM=1" --privileged  docker-ros_ros bash
```

# docker-compose.yml 로 만들기
명령어가 너무 길고 복잡하다 
그래서 docker-compose.yml과 Dockerfile로 만들어서 사용을 할 수가 있다.

깃허브를 참고하자
