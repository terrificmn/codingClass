# 터틀심 튜토리얼 터틀심 실행해보기

먼저 ROS에서 roscore 명령어로 실행을 해서 master를 실행을 시켜주자~
```
$ roscore
```

다음은 터틀심 실행하기하기 (터틀심 패키지의 터틀심노드를 실행)
```
$ rosrun turtlesim turtlesim_node
```
(탭키를 눌러서 하면 더 쉽고 빠르게 할 수 있다)

그러면 그래픽 화면이 창이 뜨면서 거북이 보인다~ ROS의 마스코트?

<img src=0>

<br>

> 새로 실행할 때 마다 거북이가 바뀐다 ㅋㅋ


이번에는 키보드로 조작을 하기 위해서 다른 노드를 또 실행해준다
아래처럼 입력하자
```
$ rosrun turtlesim turtle_teleop_key 
```

이제 키보드로 조종하는데로 거북이가 움직이게 된다
```
Reading from keyboard
---------------------------
Use arrow keys to move the turtle. 'q' to quit.
```
빠져나오려면 q를 눌러주고 키보드로 입력을 하면 된다


<br/>

## 이제 어떤 topic 통신인지 확인해보자
rostopic을 이용해서 확인해보자

```
 rostopic list 
```

아래의 결과가 나온다
```
/rosout
/rosout_agg
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose
```

여기에서 원하는 것은 /turtle1/cmd_vel 토픽이 보인다. 추가로 info까지 봐보자

```
$ rostopic info /turtle1/cmd_vel
```


<img src=1> 


처럼 나오는데 

geometry_msgs 패키지를 사용하고 있고 msg는 Twist 디렉토리 안에 있는 것을 알 수 있고  

> 터미널에 roscd geometry 라고 입력하면 패키지 디렉토리로 한번에 이동할 수 있다

<br/>

Publishers는   
/teleop_turtle 노드이고 (키보드 조작을 했던 )  

Subscribers에는  
/turtlesim 노드가 있는 것을 알 수 있다  


<br/>

# 추가로 rosbag을 이용해서 저장하기
ROS에서 bag의 의미는 저장하는 것과 관련이 있는데 이를 이용해보자

터틀심 turtle_teleop_key가 노드가 작동되고 있을 때

다른 터미널을 열고 위의 topic을 이용해서 저장해보자 (rostopic list 로 알 수 있다. 또는 탭키를 활용하자!)
```
rosbag record /turtle1/cmd_vel
```

```
bag record /turtle1/cmd_vel
[ INFO] [1623383299.544184296]: Subscribing to /turtle1/cmd_vel
[ INFO] [1623383299.546579495]: Recording to '2021-06-11-12-48-19.bag'.
```
저장을 시작했다고 나오고 파일명이 나온다

이제는 조작을 해주기 위해서 다시 turtle_teleop_key 가 실행되고 있는 터미널에서 조작을 해주자
이리저리 움직이면 값들을 저장한다. 

rosbag 으로 저장되고 있는 터미널로 이동해서 어느정도 조작이 되면 ctrl+c를 눌러서 빠져나오자

이제 bag에 저장된 것으로 실행을 시켜볼 수가 있는데,  
play를 해서 위에 나오는 '파일명.bag' 으로 다시 실행을 시켜줄 수 있다
(복사를 해서 사용하자~ )

>터미널에서 복사는 ctrl+shift+c, 붙여넣기는 ctrl+shift+v


아래처럼 입력해보자
```
$ rosbag play 2021-06-11-12-44-44.bag
```

이제 거북이 저장된 데이터를 토대로 다시 움직이기 시작한다~



