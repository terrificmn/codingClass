# ros 분석하기가 중요하다
ROS를 배우면서 느끼는 것은 내가 데이터를 받거나 줄 때 그것이 topic 인지 service인지   
확인해야하는 경우가 우선 중요할테고,   
topic명 확인, 그 안의 데이터 타입, 변수가 어떻게 되는지 알아야지   
정확하게 사용을 할 수가 있는 것 같다고 느꼈다. 그리고 직접 소스코드를 분석을 해야겠지만    
소스코드를 안 보고도 어떤 메세지를 받아야하는지도 많이 해봐야하는 것 같다

<br/>

# 메세지를 볼 수 있는 rosmsg 에 대해서 알아보자

이번에는 msg 메세지 topic 통신 중에서 
msg가 (message)가 주는 것에 대해서 알아보자

먼저 터틀심을 켜주자

```
$ roscore
```

다른 터미널 열고 
```
$ rosrun turtlesim turtlesim_node 
```

이제 거북이 화면이 올라오게 될 것이다

<img src=0>
<br/>

> 이번에는 빨간 거북이군 🧐, 매번 실행 할 때마다 바뀐다 ㅋ


이제 rostopic을 입력해보자
```
$ rostopic list
```

결과
```
/rosout
/rosout_agg
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose
```

이제 topic의 종류가 나왔다~ topic 중에 /turtle1/cmd_vel 정보를 봐보자

```
$ rostopic info /turtle1/cmd_vel
```
그러면
현재는 터틀심 거북이 그래픽 화면만 나와있기 때문에 subscriber라고 나오고 있고
Type도 알 수가 있는데 이 Type이 패키지/msg 가 된다

```
Type: geometry_msgs/Twist

Publishers: None

Subscribers: 
 * /turtlesim (http://localhost.localdomain:41823/)
```

> 잠깐 터틀심이 구독자인것을 알겠네~ 그럼 누가 퍼블리쉬를 할까?   
rosrun turtlesim turtle_teleop_key 이라고 터미널에 입력을 해보자~
그러면 키로 입력해서 거북이 조종할 수 있는 노드가 실행이 된다

그리고 다시 
```
$ rostopic info /turtle1/cmd_vel
```
해보면 

```
Type: geometry_msgs/Twist

Publishers: 
 * /teleop_turtle (http://localhost.localdomain:40553/)

Subscribers: 
 * /turtlesim (http://localhost.localdomain:41823/)
```

> 방금 실행한 turtle_teleop_key가 키보드 조작하는 노드인데, 이놈이 퍼블리싱을 하고 
거북이가 그 topic을 받아서 움직이는 거구나 👏👏 라고 알 수 있다

<br/>


## rosmsg 사용
잠깐 rosmsg를 사용하기 전에 전체적으로 살펴보았다~ 원래 오늘 하려고 했던 메세지 보는 법에 대해서 해보자~  
rosmsg show를 아래처럼 입력
```
$ rosmsg show geometry_msgs/Twist
```
아래처럼 결과가 나온다
```
geometry_msgs/Vector3 linear
  float64 x
  float64 y
  float64 z
geometry_msgs/Vector3 angular
  float64 x
  float64 y
  float64 z
```
geometry_msgs 패키지는 Twist라는 msg를 사용하고 변수는 vector로 선언되어 있고
각 linear와 angular라는 것이 사용되었다는 것을 알 수 있다

즉 Vector(3) 이라는 의미 인 것 같고, 3개의 배열요소에는 x, y, z가 float64형으로 선언되어 있음

이것을 사용할 때에는 이런식으로 사용할 수 있다 
(콜백함수내에서 사용 - 일반적으로 사용 가능한지는 테스트 안해봄)
```
geometry_msgs::Twist msg
msg.linear.x = 1.0;
msg.linear.y = 0;
msg.angular.y = 0;
```

어떻게 보면 associative array와 비슷하다는 생각을 했다. 배열에 Key가 있으니 
물론 다르기는 하지만 그런 느낌이 들었다. 다른 언어에서는 linear['x'] = 0  
이렇게 사용하기도 하니깐 말이다. 어쨋든 이 부분도 더 알아봐야겠다

토픽 통신에 대해서는 이런식으로 하고 
서비스 통신(서버, 클라이언트) 도 비슷하다. 조금씩 차이는 있지만

서비스 파일, 변수등을 보는 것은
rossrv show 서비스타입 (즉, 패키지명/srv명)이 되겠다. 아마 비슷하게 사용할 수 있다


<br/>

## help 기능 rosmsg 좀 더 사용해보기
위에서 서비스 통신에 대해서도 말했지만 비슷한 구조로 되어 있기 때문에 
명령어를 안 다면은 --help, -h 기능을 적극 활용하자

이번에는 rosmsg --help 기능을 써보자
--help는 리눅스에서 사용되는 프로그램이라면 거의 비슷하게 먹힌다(?)

대개 명령어까지 친 다음에 --help 라고 하면, 이번 경우에는 rosmsg --help
그 명령어에 대한 설명/ 옵션을 볼 수가 있다

> 리눅스에서 돌아가는 프로그램들은 거의 비슷하게 help기능이 작동한다. 그냥 아무 프로그램이나 
붙잡고(?) --help 해도 될 정도다 😁


```
$ rosmsg --help
```
결과는 
```
rosmsg is a command-line tool for displaying information about ROS Message types.

Commands:
	rosmsg show	Show message description
	rosmsg info	Alias for rosmsg show
	rosmsg list	List all messages
	rosmsg md5	Display message md5sum
	rosmsg package	List messages in a package
	rosmsg packages	List packages that contain messages

Type rosmsg <command> -h for more detailed usage
```
이중에서 쓸 만 한 것은 일단 show, info(show랑 비슷한 것 같다), list (모든 msg를 보여준다)
등이 있는 듯 하다

더 좋은 것은 rosmsg [command] -h 이 부분
rosmsg의 show를 어떻게 사용하는 지 보자
```
$ rosmsg show -h
```

그러면 
```
Usage: rosmsg show [options] <message type>

Options:
  -h, --help            show this help message and exit
  -r, --raw             show raw message text, including comments
  -b BAGFILE, --bag=BAGFILE
                        show message from .bag file
```
이번 위에서 입력을 해서 알겠지만 옵션 다음에 메세지타입을 입력하라고 되어 있다
그리고 재미 있는 것은 -r 옵션을 할 수 있다는 것이다

```
$ rosmsg show -r geometry_msgs/Twist
```

결과는 아까전에 옵션없는 show봤던 결과와는 다르게 단순 텍스트(주석포함) 로 보여준다
```
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular
```

이제 실제 그러한지 패키지로 이동해보자 ㅋㅋ
이제 직접 파일을 보고 싶으면 roscd [패키지명] 을 이용해서 입력

```
$ roscd geometry_msgs/Twist
```

그러면 바로 /opt/ros/melodic/share/geometry_msgs 쪽으로 이동을 하게 된다
원래 타입이 geometry_msgs/Twist 였으므로 
패키는 geometry_msgs 였고, 이제는 msg를 찾을 차례

```
$ cd msg
$ ls
```

이제 꽤 많은 msg가 보일 것이다. 여기서 원하는 것은 Twist.msg

이제 파일을 찾았으니 열어보자
```
$ vi Twist.msg
```

```
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular
```
아까전에 보았던 rosmsg show -r geometry_msgs/Twist 와 같다 

ros에서는 꽤 다양하고 편리한 기능들을 제공하는 것 같다~ 👍👍👍



