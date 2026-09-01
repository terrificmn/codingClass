# tinker board2 debain buster 10
팅커보드2 기준으로는 일단 docker engine을 debain 으로 설치를 하게 되면 
docker-compose도 설치가 된다.

> 그전에는 docker-compose를 설치를 따로 했어야하는데 뭔가 바뀐 듯하다

설치는 이쪽에 되어 있음   
`/usr/libexec/docker/cli-plugins/docker-compose`  

하지만 다른 경로에서는 인식을 못하므로 심볼릭 링크를 만들어 주거나, $PATH 변수에 등록시켜준다  


## docker-compose build 시 문제 
```
 > [5/9] RUN rosdep init   && rosdep update --rosdistro noetic:                 
#0 2.765 ERROR: default sources list file already exists:                       
#0 2.765        /etc/ros/rosdep/sources.list.d/20-default.list                  
#0 2.765 Please delete if you wish to re-initialize                             
------
failed to solve: executor failed running [/bin/sh -c rosdep init   && rosdep update --rosdistro $ROS_DISTRO]: exit code: 1
```

이런식으로 에러가 발생. 처음에 키보드 설치하는 문제 때문에 빌드를 하다가 취소가 되어서 그런지  
(원래 기본 소스 리스트가 존재한다고 하는 것을 봐서) 어쨋든..  
Dockerfile의 `RUN rosdep init ...` 부분을 주석처리하고 다시 빌드를 했더니 잘 통과가 되었음

후에 ROS 컨테이너도.. roscore도 잘 켜지고 잘 작동한다. 



## 빌드 시에 키보드 설정을 물어보는 경우

debain buster 10 에서 docker-compose build를 하는 중에 
`Country of origin for keyboard` 라고 나오면서 키보드를 지정해달라고 나오면서 
더 이상 진행이 안 되는 경우 (입력이 안되고 계속 대기 상태에 있게 된다)

Dockerfile 에 변수를 하나 설정해준다. 

```
FROM=.....
DEBIAN_FRONTEND=noninteractive
```

다시 빌드를 해주자. 그러면 막힘없이 잘 진행이 된다



## Host의 display 사용
libGL 관련 error가 발생...   
도커 컨테이너 안에서 실행 시 다행히 rviz등의 그래픽 툴을 사용하는데 문제는 없다. 잘 실행이 된다.  

좀 더 알아봐야겠다
```
libGL error: failed to create dri screen
libGL error: failed to load driver: rockchip
libGL error: failed to create dri screen
libGL error: failed to load driver: rockchip
libGL error: failed to create dri screen
libGL error: failed to load driver: rockchip
libGL error: failed to create dri screen
libGL error: failed to load driver: rockchip
```
