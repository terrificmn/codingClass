이 md파일은 ros2이미지를 받아서 실행하는 심플한 방법 소개이고   
Dockerfile, docker-compose.yaml 파일등은 

ros2인 foxy 버전을 사용하기 위해서는 우분투 20 버전이 필요한데 
그래서 외장하드에서 우분투 20.01 버전을 설치해서 ros2도 설치를 해보려고 했으나

전에 우분투를 설치할 때에도 발생했던 문제였던 usb 장치 문제로 인해서 
그냥 내 컴 하드웨어가 조금 이상한 듯 하다~ (조금 오래된 컴이라 그런가..?)
그래서 우분투 설치가 막 시작되었을 때 외장 하드를 인식을 못한다~

그래서 그냥 docker로 ros2를 실행해보기로 했다

# docker를 이용해서 ros2 설치해보기, 도커에서 ros2이미지를 받은 후 사용하기

우선 docker가 설치가 되어 있어야 한다

간단하게 하려면 osrf/ros2의 이미지를 다운을 받아보자  
먼저 pull 명령어를 사용해서 다운을 받는다~

이미지명은 osrf/ros 이고 태그는 foxy데스크탑 버전이다
터미널에서   
```
docker pull osrf/ros:foxy-desktop
```

이렇게 되면 이미지를 다운을 받는다

<이미지~ 넣기>

완료가 되었다면 docker 이미지를 확인하려면 아래 명령어를 사용해보자
```
docker images
```

약 데스크탑 버전의 용량은 3기가 넘는다 

그냥 기본적으로 도커를 이용해서 컨테이너를 실행시켜보자  

> 간단하게 ros2 작동이 어떤식으로 되는지 확인보려고한다

run 명령어로 이미지를 실행을 시키고 
```
docker run -it osrf/ros:foxy-desktop bash
```

그러면 root 계정으로 bash쉘이 실행이되어 있는 것을 알 수 있다~
프롬포트부분이 바뀌어 있다

```
[octa@localhost docker-ros2]$
root@b8ed00c3e29a:/# 
```

/opt/ros/foxy/setup.bash 파일을 읽어들여서 ros2가 명령어를 알 수 있게 해준다
```
source /opt/ros/foxy/setup.bash
```
실행이 되면 아무런 반응이 없다. 하지만 이제 ros2 명령어를 사용할 수가 있는데  
ros2 한칸 뛰고 run 명령어를 칠 수가 있게 된다~ (탭키를 이용해서 자동완성을 시키면 편하다)

데모 노드를 실행을 해서 잘 작동이 되는지 확인해보자~

>ros에서는 rosrun 이런식으로 했지만 ros2에서는 ros2 run 이런식으로 명령어가 조금 바뀐다

이제 다른 터미널을 실행 (새로운 창을 열어준다)을 해서   
도커 컨테이너에 다시 접근을 해본다

docker ps를 해보면
```
docker ps 
```

```
CONTAINER ID   IMAGE                   COMMAND                  CREATED          STATUS          PORTS                                   NAMES
763acf5dbdb9   osrf/ros:foxy-desktop   "/ros_entrypoint.sh …"   15 seconds ago   Up 14 seconds                                           confident_carson

```
이렇게 컨테이너가 실행되고 있음을 알 수가 있고 컨테이너가 실행이 되고 있으므로 
run명령어가 아닌 exec로 다시 컨테이너로 접근을 할 수가 있다

아래처럼 입력
```
docker exec -it confident_carson bash
```

>여기에서 confident_carson 은 자동으로 생성된 컴테이너 이름이다 

컨테이너가 실행이 된다면 source로 setup.bash 파일을 읽어준다
```
source /opt/ros/foxy/setup.bash
```

이번에는 퍼블리싱이 되고 있는 데모 노드의 talker 노드를 구독해보자

```
ros2 run demo_nodes_cpp listener
```

그러면 구독을 잘해서 메세지가 보여지는 것을 알 수 있다~

[이미지 넣기]


이제 두 개의 터미널 각각에서 exit 를 입력하게 되면 원래의 localhost 터미널로 빠져나오게 된다


[]이지미 지우기 링크 걸기





## Dockerfile 에 유저만들기
아래처럼 만들 수 있다
```Dockerfile
# Create user "ros"
RUN useradd -m ros && \
    cp /root/.bashrc /home/ros/ && \
    mkdir /home/ros/workspace && \
    chown -R --from=root ros /home/ros
######
# # HOME 지정해주고 USER도 지정
ENV HOME /home/ros
USER ros
WORKDIR ${HOME}/workspace
```

이렇게 하면 유저 ros로 만들어지고 로그인 된다.
하지만 로컬 host에서 권한이 어떻게 될지 몰라서 일단 보류함. (정상 작동함)

