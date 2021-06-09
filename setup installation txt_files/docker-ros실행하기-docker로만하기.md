http://wiki.ros.org/docker/Tutorials/GUI

테스트 중 

libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: radeonsi
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: radeonsi
에러 발생 중


Topic 통신 테스트 해보기


먼저 도커ros를 실행한 후에 도커 (Dockerfile 참고하기)
```
ros run -it --rm .....
```

컨테이너가 실행되고 있을 때 exec로 접근한다
docker ps -a

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


