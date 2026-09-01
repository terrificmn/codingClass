# ROS 분석하기
ROS를 사용하면서 여태까지 공부했던 topic통신, service통신은 노드 2개~3개인 패키지를 만들어 사용했지만,

오픈 소스 패키지를 사용하거나 다른 패키지를 사용할 때에는 많은 노드와 패키지, 메타 패키지들이 있기 때문에
각각의 노드들이 어떤 통신 방식을 취하고 있는지 일일이 코드를 열어가며 확인하기 어렵다.

그래서 ROS에서는 분석을 할 수 있는 명령어를 제공하는데 그것들에 대해서 공부해보자

[다음은 rostopic 알아보기](/blog) 링크 업데이트 해야함


<br/>

## rosservice 해보기 - 서비스 확인하기

시작하기에 전에 보고 오세요~ 😍  
[ROS service-server/client 튜토리얼 보러가기](/tag/service%20server)

이번에는 yh_tuto_service 패키지를 통해 튜토리얼을 진행합니다~

마찬가지로 이제 roscore 로 마스터가 실행이 되고 있고 rosrun으로 서비스 서버가 작동한다면 
topic과 비슷하게 서비스 목록 및 확인할 수 있다

먼저 roscore를 해주자~ 
```
$ roscore
```
그리고  
```
rosrun yh_tuto_service srv_server
```
해서 서비스 서버를 노드를 실행을 시켜주자~ 그러면 서비스 서버 노드가 작동된다

이제 서버 리스트 볼 수 있다. 즉, 서비스 노드가 시작되면 아래처럼 명령어를 쳐서   
어떤 service인지 알 수 있다. 먼저 rosservice list를 해보자
```
rosservice list
```

결과는 아래와 같다
```
/hamburger
/rosout/get_loggers
/rosout/set_logger_level
/srv_server/get_loggers
/srv_server/set_logger_level
```

/hamburger 를 제외하고    
이렇게 4개는 기본적으로 마스터랑 통신하고 있는 서비스이다.

조금 엉뚱하지만 서비스 서버의 이름이 /hamburger 이다 
(yh_tuto_service패키지를 그렇게 만들었다 ㅋㅋ)

이제 작동 중인 서비스 정보보기 (인포)
```
$ rosservice info /hamburger
```

결과를 보면
```
Node: /srv_server
URI: rosrpc://ubun-sc:40245
Type: yh_tuto_service/yh_srv
Args: a b
```
Node: 노드의 이름을 알 수 있고, Type: 패키지와 서비스 이름을 알 수 있다  
Args: 아규먼트의 2개를 받는 것도 알 수 있다


이제 call을 해서 결과를 받을 수도 있다. topic에서 테스트 할 때는 echo로 했었는데   
이번에는 call로 한다고 이해하면 될 것 같다. 왜냐하면 서버는 요청 call을 해야지  
응답을 하기 때문이다

rosservice call 이라고 하며 뒤에 서비스 이름을 적어준다 그리고 아규먼트 2개 넘겨주기

```
$ rosservice call /hamburger 10 20
```

```
10 20
result: 30
```
이라는 결과를 서버로 부터 즉각 받는 모습을 볼 수 있다. 


<img src=0>



rqt를 실행해보자 

```
rqt
```

rqt프로그램이 뜨면 Plugins -> Services -> Service caller 메뉴를 눌러서 진입하면  

서비스 노드를 확인할 수 있다. 눌러보면 서비스의 이름 패키지이름, 아규먼트 등을 볼 수 있다


<br/>


[다음은 분석하기3탄: ros launch 알아보기](/blog/ROS-분석하기-3탄-roslaunch-실행해보기-launch-파일-만들어서-실행하기) 