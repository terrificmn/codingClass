original ros_entrypoint.sh
/ (root) 경로에 만들어지며
```
#!/bin/bash
set -e

# setup ros environment
source "/opt/ros/$ROS_DISTRO/setup.bash" --
exec "$@"
```
요렇게 기본적으로 만들어 진다. 일반 도커 이미지를 사용했을 경우   
그래서 ENTRYPOINT를 지정하지 않아도 noetic의 setup.bash 까지 source를 하고  
기본으로 roscore 등이 작동이 되는 듯 하다   

그 외에 command (docker-compose.yml)에 roslaunch 등을 넣어주면 실행은 되지만  
패키지를 찾지를 못한다. 이유는 catkin_ws 여기에서는 (docker_ws)의 setup.bash가 실행이 안되었기 때문인 듯 하고   
처음에 빌드 할 때 .bashrc에 setup.bash 가 포함되게 했지만, 적용이 안되는 듯도 하다  

```
error msg
/ros_entrypoint.sh: line 6: exec: roslaunch servo_ros servo_ros_bridge_web.launch: not found
```

테스트 해볼 것은 docker-compose의 environment에 아예 넣어서 해보는 방법도 있을 듯 하다 

> 다른 쉘 스크립트를 만들어서 copy 후 entrypoint를 사용하면 roslaunch도 잘 작동하고,    
> 또는 아예 쉘 스크립트 없이 bash 명령어로 커맨드 조합으로 실행시킬 수 있다 (docker-compose에서 설정)
> 기존 docker-ros의 tinker-board관련 브랜치를 참고   


