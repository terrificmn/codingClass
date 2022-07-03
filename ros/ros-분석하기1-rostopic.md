# ROS 분석하기
ROS를 사용하면서 여태까지 공부했던 topic통신, service통신은 노드 2개~3개인 패키지를 만들어 사용했지만,

오픈 소스 패키지를 사용하거나 다른 패키지를 사용할 때에는 많은 노드와 패키지, 메타 패키지들이 있기 때문에
각각의 노드들이 어떤 통신 방식을 취하고 있는지 일일이 코드를 열어가며 확인하기 어렵다.

그래서 ROS에서는 분석을 할 수 있는 명령어를 제공하는데 그것들에 대해서 공부해보자


<br/>

## rostopic 를 사용해보자 - 토픽 확인하기
시작하기에 전에 보고 오세요~ 😍  
[ROS 패키지 만들기 및 topic 튜토리얼 보러가기](/tag/catkin_create_pkg)


yh_tutorial 패키지를 이용해서 rostopic 명령어로 topic에 대한 정보를 알아보자~

> rostopic list 명령어는   
topic 리스트를 보여준다 (지금 활성화된 topic의 리스트를 보여준다)


먼저 roscore를 해서 마스터를 실행을 한다. 노드간의 통신을 하려면 중요!😃 
```
$ roscore
```

이제 topic을 확인해보자
```
$ rostopic list
```

결과:
```
/rosout ()
/rosout_agg
```
결과를 보면 위의 둘 은 마스터랑 자동으로 통신하는 것을 의미한다~ 고로 자세히는 들여보지 않겠다~  사실 잘 모른다 ㅋㅋ 😋  

그래서 roscore 명령어가 실행이 되고 있다면 ctrl+c 로 끄거나 실행을 안시켰을 때
master가 실행이 안되니 rostopic list를 해도 아래처럼 나온다
```
ERROR: Unable to communicate with master!
```

그래서 다시 roscore를 실행을 하고 

rosrun yh_tutorial pub_test 를 실행을 해본다
```
$ rosrun yh_tutorial pub_test
```

그리고 다른 다른 터미널을 열어서 rostopic 리스트를 해본다
```
$ rostopic list
```

이번에는 결과가 아래와 같다
```
/rosout
/rosout_agg
/yh_topic
```

토픽이 **/yh_topic**이라고 나온다.   

토픽의 정보를 확인해보자
```
$ rostopic info /yh_topic
```
결과는 아래 처럼 나온다
```
Type: yh_tutorial/yh_msg_tutorial

Publishers: 
 * /pub_test (http://f61579209fde:46157/)

Subscribers: None
```

먼저 rosrun으로 노드 실행을 시켰던 것은 Publisher 인 것을 알 수가 있고   
토픽 yh_topic는 type부분에서 yh_toturial 패키지의 msg 디렉토리의 yh_msg_tutorial을 사용한다는 것을 알 수가 있다

이번에는 직접 토픽을 이용해서 subscriber 처럼 내용을 직접 받아 볼 수 있다  
바로 **echo** 인데, 해보면 yh_topic에서 퍼블리싱되는 내용을 받아준다

rostopic echo로 테스트 해보기
```
$ rostopic echo /yh_topic
```
내용은 이렇다
```
생략...
---
stamp: 
  secs: 1623701264
  nsecs: 827808734
data: 153
---
stamp: 
  secs: 1623701264
  nsecs: 927906854
data: 154
---
```

stamp와 data 변수 사용을 하고 있는 것을 알 수 있다    
stamp에서 secs, nsecs 부분이 나오는 것을 봐서 time 데이터 인것을 유추할 수 있다  



<img src=0>

화면은 이런식으로 되서 출력이 되는 것을 확인할 수 있음


이번에는 type을 입력해보자

```
rostopic type /yh_topic 
```

아래 처럼 나오며 패키지이름을 알 수 있다
```
yh_tutorial/yh_msg_tutorial
```


마지막으로 -h 옵션으로 명령어에 대한 설명을 볼 수 있다. (헬프 기능)
```
rostopic -h
```

[다음은 ROS분석하기 2탄- service 알아보기](/blog/ROS-분석하기-2탄-rosservice-사용해보기-service-분석하기)