# docker compose volumn  연결 시
docker-compose에서 volumn을 지정해서 연결을 해도,  
빌드시에는 소용없다. 아직 연결이 안 된 상태라서 해당 경로를 못 찾게 된다.   

방법은 아예 파일을 COPY 한 후에 사용을 하거나, 또는 빌드가 완료가 된 후에  
docker exec 를 이용해서 하는 것이 속 편하다   

## compose.yml 에서 연결
일단 compose.yml 파일에서 volume 으로 지정이 되어 있는 경우에는  
build 할 경우에는 변경/수정이 불가능 하므로   

일단 ros/ros2 컨벤션 상 특정 워크 스테이션에 src 까지 되어 있어 이 src 디렉토리에 각 패키지가 깔리는 상태인데  
compose.yml 에서 volume 부분을 연결 하면 예를 들어 `docker_ws` 라고 했다면 해당 디렉토리가 container 에 연결은 되지만   
docker compose build를 하는 동안에는 변경/수정/추가 안된다.  (퍼미션과 관계없음)   

크게 두 가지 방법이 있는 듯 하다.   
1. 아예 연결 안 된 컨테이너 안에서 script를 실행하거나 디렉토리를 만들고 깃 클론, 더 나아가 colcon build/ (catkin등) 도 가능하다   
  즉 아예 volume 과는 상관 없는 상태   
  대신 장점은 docker compose build 시에 완성이 되므로 중간에 날라갈 일이 없다.   
  단점은 host 쪽 container 가 아닌 상태에서는 내용을 확인 할 수가 없다.  
  물론 이점도 vscode에서 remote container를 할 수가 있어서 크게 단점은 아니게 된다.   

2. volume 으로 연결된 디렉토리를 사용하려고 할 경우에는 각종 의존성 패키지까지 설치해주는 것이 좋다.  
  (TODO: 단, rosdep install 을 사용하기가 힘들 수가 있으므로 src 가 상관없는 식으로 하면 가능할 수도 있을 듯)  *아직 안해봄**   
  깃 클론도 volume 연결된 root 디렉토리에서 받는 것 정도까지 해놓을 수가 있다.  
  (이유는 ros/ros2 워크스테이션을 만들고 src 를 만들 수가 없다. volume 으로 연결되면 build 시 수정 불가)
  이후 docker compose build & up이 마무리가 되면 컨테이너 실행을 해서 colcon build 로 직접 마무리 한다.   
  장점은 한번 빌드가 되면 host 내컴쪽에서도 확인이 가능하므로 코드 실행이 편하다,   
  중간에 build가 다시 되거나 날라가더라도 의존성 및 build된 파일(한번 했다면) 유지되므로 크게 문제가 안됨(아주 가끔 build layer가 초기화 되거나 다시build되는 불상사가 생길 수도 있다.)  
  단점은 수동으로 한번은 colcon build 따위를 해줘야 함.

3. 세 번째는 compose.yml 에서 command를 사용하거나, 아예 Dockerfile 에서 ENTRYPOINT 에서 "bash -c "path/" 를 실행하는 방법인데   
이때에는 sciprt 파일을 만들고 COPY 커맨드를 이용해서 컨테이너에 복사시킨 후에 실행하게 된다.   
이 단계에서는 docker compose build 시에 안 하기 때문에 volume 디렉토리에 사용할 수가 있지만 (디레토리 수정 추가 가능)   
단, docker compose up이 되는 시기에 무조건 계속 실행 되기 때문에 계속 사용하기에는 특히 ros/ros2 환경에서는 무리라고 판단됨!

4. 추가 방법은 예전에 다른 volume 디렉토리에 만들었던 것을 압축을 풀면서 이동했을 경우에 되었던 기억이 있다.  
예를 들어 volume1 에서 압축을 풀어 volume2 에 이동을 했을 경우에  가능했었던 거 같은데  
확실하지는 않지만 volume으로 연결했을 때 이런 방법으로 가능할 지도 모르겠다. **TODO** 추후 테스트를 해봐야 하겠다  
```
COPY ./source_tar/파일.tar.xz ./source_tar/
```

## script 에서 sudo 사용
도커에서 user을 만든다면 script나 컨맨드를 사용할 때  
sudo 를 사용해도 입력을 할 수가 없으므로 `echo "my_password" | sudo -S ` 등을 사용해서 사용   
예를 들면 echo "1234" | sudo -S mkdir mynewdir


