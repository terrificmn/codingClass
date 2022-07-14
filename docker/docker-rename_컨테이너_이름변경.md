먼저 컨테이너 이름 확인  
```
docker ps -a
```

아래처럼 이름이 숫자로 되어 있어서 docker exec 로 실행하기 불편하다
```
CONTAINER ID   IMAGE                         COMMAND                  CREATED        STATUS                        PORTS                                           NAMES
81fc2d16f179   docker-ros_ros                "/ros_entrypoint.sh …"   4 days ago     Up 30 seconds                 0.0.0.0:11311->11311/tcp, :::11311->11311/tcp   81fc2d16f179_ros
```
맨 앞에 컨테이너 ID 와 NAMES를 보면 81fc2d16f179 로 시작하는 것을 알 수 있다   


컨테이너 이름 변경은 간단하다. rename을 사용하면 된다   
```
docker rename 81fc ros
```

> 컨테이너 이름은 다 안 적어도 된다 