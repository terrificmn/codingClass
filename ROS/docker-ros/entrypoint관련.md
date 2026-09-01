# ros docker entry point

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



## ros entrypoint 방법
일단 2가지 방법 정도가 있다.   

docker-compose.yml 파일에서 ros 컨테이너의 command 부분에 `roscore`을 실행하는 방법

또는 Dockerfile 내에서 ENTRYPOINT 명령으로 수행하는 방법 (sh 스크립트 실행)



### docker-compose.yml 이용
orsf/의 이미지는 command 부분에 roscore만 해도 바로 실행이 된다  

```yaml
ros
    ...생략
    command:
        - roscore
```
> roscore가 실행이 되는 것은 기본적으로 /opt/ros/$ROS_DISTRO/setup.bash 가 source가 되었기 때문으로 보인다  

하지만, 워크 스테이션 까지 수행을 하려면 ~/.bashrc랑은 상관없이.. 터미널이 열려야 하는데   
그렇게는 수행이 되지는 않는 것 같다.  
catkin_ws 의 setup.bash를 열어주면서 실행을 하게 되면 된다  

```yaml
ros
    ...생략
    command:
        ["bash", "-c", "source /user의catkin_ws경로/devel/setup.bash && roslaunch 패키지 런치파일.launch"]
```

### Dockerfile에 ENTRYPOINT로 수행
nvidia 이미지로 사용하는 경우에는 setup.bash 때문에 roscore가 수행이 안된다.  

Dockerfile 안에 빌드를 할 때 shell script를 복사한 후에 그 파일을 수행하는 방법이 있다  

```Dockerfile
COPY ./ros_entrypoint.sh ./
ENTRYPOINT [ "./ros_entrypoint.sh"]
```

현재 패키지의 root 안에 ros_entrypoint.sh 스크립트 파일을 컨테이너 안으로 복사한 후에   
실행하는 방법이다  

쉘 스크립트는 이런식..
```shell
#!/bin/bash
source "/opt/ros/noetic/setup.bash"
source "/home/docker_noetic/docker_ws/devel/setup.bash"

##########################
### roscore || rosrun pkg_name node_name || roslaunch pkg_name launchfile_name 중에 선택해서 사용
### roslaunch 실행이 없다면 도커 up하면 바로 exit하게 됨 
##########################
roscore
```

> 단, ros_entrypoint.sh 런치파일 변경 시에는 docker compose build를 다시 해야함

nvidia image 같은 경우에는 setup.bash 를 source를 못해서 그런 것이므로...  

> 두 가지 방법을 믹스해서 사용하면 될 듯 했는데, 빌드할 때 ENTRYPOINT 하고  
docker-compose 에서 command에 넣어주면 될 듯 했는데.. 그렇게는 안되었던 기억이 있다   


### 최종! docker-compose에서 source 시켜주기
빌드 시에 쉡 스크립트를 수행하는 것도 참 좋으나, 뭔가 내용이 바뀌면 빌드를 다시 해야하는 문제가 있다.  
캐쉬된 데이터를 쓰기 때문에 빌드는 금방 되나,   
빌드 후에 따로 컨테이너에 설치된 것들이 날라가 버린다;;;;

그래서 차라리 docker-compose.yml 파일의 command 부분에 bash 쉘로 수행을 하면서   
source도 해준다. 단, &&를 붙여서 catkin_ws 의 setup.bash도 해주고 또 && 해서 런치파일 명령어까지 써주면 된다   

굉장히 길어

짧은 예:
```yaml
command :
    ["bash", "-c", "source /opt/ros/noetic/setup.bash && roscore"]
```

어쨋든 nvidia 이미지를 활용한 ros등은 이렇게 적용하면 좋을 듯 하다.   

> 보통의 ros image도 catkin_ws의 setup.bash는 해야하므로 큰 차이는 아니다.  
단, 빌드를 안해도 되니 좋은 것!
