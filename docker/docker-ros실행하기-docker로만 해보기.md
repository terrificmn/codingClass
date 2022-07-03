http://wiki.ros.org/docker/Tutorials/GUI  

테스트 중 

```
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: radeonsi
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: radeonsi
```
에러 발생 중


# docker ros 실행하기

먼저 docker-ros 파일을 만들어서 docker-compose build 랑 up을 해준다

일단 도커에서 Dockerfile 에서   
```
CMD ["/bin/bash", "-c", "source /opt/ros/$ROS_DISTRO/setup.bash && roscore"]
```

마지막에 이렇게 되어 있는데, 그러면 docker-compose up을 했을 때   
실행이 된다~ 단 출력이 표시가 안되서 아무것도 안보이지만 도커 컨테이너가 잘 실행이 된다. 

그러면 다른 창을 열어서 

```
$docker exec -it ros bash
```
라고 해주면 도커-컴포즈로 업 시킨 컨테이너에 들어가서 실행을 할 수 있게 된다.   
그래서 여기에서 터미널 열고 2~3개 실행시킨 후에 통신 테스트를 하면된다. (예: topic, service등..)

docker-compose에서 이름을 ros로 해 놓았기 때문에 ros로 열리지만 안 되면 컨테이너를 확인한다
```
docker ps -a
```

> 참고로 여기에서 cmd와 같은 효과를 해주는 가장 편한 방법은 (아직까지는) CMD 부분을 지우고  
docker-compose.yml파일에서 command 부분을 추가해주는것 임   
그러면 첫 번째 방법과 같은 효과가 나타난다

이 방법의 단점은 내가 컨테이너 bash셀을 사용하지 못한다는 것, 컨테이너가 실행된 상태에서 멈춰져 있다.  
원래 roscore가 처음 안내등을 해준다음에 백그라운드에서 돌아가기 때문에 그렇다



또 다른 방법은 도커-컴포즈 run을 사용한다.  
이 방법의 장점은 바로 컨테이너에서 bash셀로 터미널을 자유롭게 사용할 수 있다.   
대신 컨테이너가 run할 때마다 만들어진다. --rm 옵션으로 exit할 때 자동으로 삭제할 수는 있다.

하는 방법: 위에서 Dockerfile에서 마지막 CMD부분을 제거하고 (또는 주석처리) 하고 

build up을 다시 해주면

```
Recreating ros ... done
Attaching to ros
ros exited with code 0
```
이러면서 바로 꺼지게 된다. 에러는 없음  

여기에서 run 명령어를 쓴다. docker run 아님
```
docker-compose run ros
```
이러면 바로 컨테이너가 실행되면서 bash쉘로 들어가 진다

대신 이 방법은 새로운 컨테이너를 만든다는 것   

> --rm 옵션을 사용할 수 있다. 컨테이너를 지워준다

그래서 
```
docker ps -a
```
컨테이너 확인하든, 아니면 run을 실행한 터미널에서 프롬포트쪽을 확인해서   
```
root@3ebfe7462daa:/# 
```
예를 들면 이렇게.. 그래서 다른 터미널 열고
```
docker exec -it 3ebfe7462daa bash
```
들어가도 된다.. 

방법은 많지만, 흠.. 도커 컴포즈를 사용하는데 아무래도 하나의 컨테이너로 계속 사용하려는 목적도 있는데   
좀 더 공부를 해봐야겠다.






## Topic 통신 테스트 해보기

```
ros run -it --rm .....
```

컨테이너가 실행되고 있을 때 exec로 접근한다  
```
docker ps -a
```

컨테이너 번호 복사 후   
docker exec -it 컨테이너번호

예를 들어 
```
docker exec -it 43059571b157 bash
```

그리고 컨테이너 안에서 
```
source /opt/ros/melodic/setup.bash
```
실행해 준다

한쪽에서는 
```
rostopic pub /test std_msgs/String "data: '123'" -r 1
```
이렇게 입력해준다



다른 컨테이너도 마찬가지로 열어준다   
순서는 1. source 2.  rostopic echo /test


