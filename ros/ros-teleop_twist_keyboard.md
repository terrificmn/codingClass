설치
http://wiki.ros.org/teleop_twist_keyboard



설치 후에 
rosrun teleop_twist_keyboard teleop_twist_keyboard.py 

를 실행을 해보면

Waiting for subscriber to connect to /cmd_vel
하면 subscriber를 기다리는 메세지가 나온다.
이를 보고 publisher 이구나 하고 추측은 가능

그래서 
$ rostopic list

해보면 
/cmd_vel
이라는 Topic이 보인다 


 rostopic info /cmd_vel 
라고 info를 봐보면
```
Type: geometry_msgs/Twist

Publishers: 
 * /teleop_twist_keyboard (http://ubun-sc:35921/)

Subscribers: None
```

퍼블리셔인것을 알 수 있고 
패키지가 geometry_msgs/Twist 를 사용하고 있는 것을 알 수 있다

이때 아주 편하게 패키지로 이동할 수 있는데

roscd를 패키지 이름을 쳐주면 바로 디렉토리로 이동해준다
```
roscd geometry_msgs 
```

디렉토리안에 하위 msg 디렉토리가 있는데 이 topic에서 쓰는 변수가 정의되있는 파일을 확인 할 수 있다



