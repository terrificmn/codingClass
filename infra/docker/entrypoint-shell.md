# entrypoint.sh 
entrypoint.sh 에서 실행할 것을 스크립트로 작성한 후에  

docker container 에 복사해서 사용  

docker-ros 깃허브 참고  

entrypoint.sh
```
#!/bin/bash

set -e ##If any command fails, stop 

source /opt/ros/jazzy/setup.bash
source /home/docker_jazzy/docker_ws/install/setup.bash

## FYI: it becomes docker-compose's command. and exec enables that PID 1 is a ros2 launch not a bash
exec "$@" ## all arguments passed to this script 
```

"$@" 모든 아규먼트를 통과해서 받아준다고 한다. 이거 자체가 ros2 launch 커맨드가 되어버린다.  
쉘크립트가 bash 로 실행하기 때문에  PID 자체는 docker 에서 bash가 되어야 하는데  
exec 를 붙여서 이거 자체가 예) PID 1 이 되어서 docker 에서 직접 SIGTERM 등의 시그널을 바로 보낼 수 있게 되어서   
exec 를 사용하는 것을 추천한다고 함  

without exec
```
PID 1: bash
   └── ros2 launch
       └── ...
```

with exec
```
PID 1: ros2 launch
   └── ...
```

## docker-compose.yml
여기에서는 사용할 container 에서 command 를 사용하면 된다.  

```
services:
  ros2:
    build: .
    command: ["ros2", "launch", "servo_ros2_node", "pan_tilt_launch.py"]
    restart: always
```

## Dockerfile
이를 Dockerfile 에서 COPY 및 ENTRYPOINT 를 사용하면 된다.   

먼저 위의 스크립트를 복사해준다.   


```
COPY ./path/to/ros_entrypoint.sh ./ros_entrypoint.sh

## ownership 관련해서는 아래처럼 할 수도 있다. 물론 UID, GID 있어야 함.
ARG UID=1000
ARG GID=1000
## 그냥 1000:1000 해도 됨
COPY --chown=${UID}:${GID} ./path/to/ros_entrypoint.sh ./ros_entrypoint.sh

ENTRYPOINT ["./ros_entrypoint.sh"]
```
> 이 경우에는 docker 내에 user가 있는 경우, ./디렉토리가 포인트


보통 root 권한으로 할 때는 아래처럼 
```
COPY ros_entrypoint.sh /ros_entrypoint.sh
RUN chmod +x /ros_entrypoint.sh

ENTRYPOINT ["/ros_entrypoint.sh"]
```

