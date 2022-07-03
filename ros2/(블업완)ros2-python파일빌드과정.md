파이썬은 스크립트가 필요없기에 한번 빌드를 시켜주면
ros2 run 명령어로 노드로 만들기 위해서 한번 노드 및 패키지를 설정했다면
그 다음부터는 파이썬 내용을 고친 후에 따로 다시 빌드할 필요가 없다

## 패키지 만들기
워크 스페이스로 이동 한 후에 py_prac 라는 패키지를 먼저 만들어보자  
의존성에는 rclpy를 추가해준다
```
cd ~/my_ws/src
ros2 pkg create --build-type ament_python py_prac  --dependencies rclpy
```

<br/>

## 코드 작성

터틀심의 cmd_vel 토픽에 퍼블리싱을 하는 pub_spin 노드를 만들어 보자   
형태는 oop로 클래스를 이용해서 만드는 예제
```py
#!/usr/bin/env python3
## python3을 사용하겠다는 의미 #shebang line 이라고 함

import rclpy #python을 할 수 있게 해주는 의존성 불러오기
from rclpy.node import Node ## Node를 가져와서 사용할 때 

from geometry_msgs.msg import Twist  #msg 가져오기
## Node 클래스를 상속받아서 클래스 형태로 만들어서 개발해야한다 (추천) 
## composition 이라고 한다

class CmdVelPublisher(Node):
    def __init__ (self):
        # 현재 CmdVelPublisher()클래스의 이름을 정해줌
        super().__init__("cmd_vel_pub_node")

        # publisher의 type을 지정해준다 (Twist, /토픽명)
        self.publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

        #3 create_publisher()에는 3개의 파라미터가 있는데 
        ## 첫 번째는 topic에 사용되는 msg type 이고
        ## 두 번째는 /토픽명 이 되고
        ## 마지막은 대기열의 크기라고 생각하면 된다고 한다
        ## topic 통신을 할 때에 데이터를 바로 보낼 수 없다면 10개만큼 데이터를 모아둔다는 뜻
        
        # pub주기를 설정 
        timer_period = 0.5 #sec
        # callback 함수 호출
        self.timer = self.create_timer(timer_period, self.publish_callback)

    def publish_callback(self):

        # geometry_msgs/msg/Twist의 메세지 타입에 따라서 속성값으로 가져온다
        twist_msg = Twist()

        twist_msg.linear.x = 0.5
        twist_msg.angular.z = 1.0 #각 속도
        self.publisher.publish(twist_msg) # publish를 한다


def main(args=None):
    rclpy.init(args=args)  #초기화 시키기

    #publisher객체 만들기
    cmd_vel_publisher = CmdVelPublisher()

    #spin()이 알아서 while루프를 돌게 된다 (publishing 하게된다)
    rclpy.spin(cmd_vel_publisher)

    #publisher의 로그를 볼 수 있는 메소드
    #콘솔에 로그를 찍어준다 (ROS에서 기본으로 지원해주는 것)
    cmd_vel_publisher.get_logger().info('\n----- Stop publishing -----')

    #노드 종료
    cmd_vel_publisher.destory_node()
    
    #자원 종료
    rclpy.shutdown()
```

이제 파일을 저장을 한다. 원하는 파일로 저장 (pub_spin.py 로 저장함)

<br/>

## 빌드하기전에 package.xml 
패키지 디렉토리를 보면은 package.xml, setup.cfg, setup.py 파일이 있는데 


package.xml 파일을 열어보자   
exec_depend 태그에 추가하라고 하는데 depend 태그로 rclpy가 들어가있다면 생략가능하다     
없다면 아래처럼 추가해준다. 의존성 패키지를 넣어주는 것인데  
```xml
<exec_depend>rclpy</exec_depend>
```

예를 들어 만약 std_msgs를 사용하는 경우라면 아래 처럼 더 추가해주는 식이다
```xml
<exec_depend>std_msgs</exec_depend>
```
현재는 rclpy만 추가해도 무리가 없다   

> 처음에 패키지를 만들떄 --dependencies 옵션을 넣었다면 depend 태그에 이미 추가되어 있음   
의존성 rclpy가 되어 있다면 스킵

> package.xml에는 사실 만들고 관리하는 사람의 이메일, 설명, 버전등을 적어줄 수 있다

<br/>

## setup.py 수정하기
이번에는 setup.py 을 확인해야한다   

setup.py에서 entry_points 부분을 수정해준다   
console_scripts 부분을 아래의 형식으로 수정하는데 방식은 아래처럼 한다   
'console_scripts': [ '노드명 = 패키지명.파이썬파일:main' ]  
```py
entry_points={
        'console_scripts': [
            'pub_spin_node = my_prac.pub_spin:main'
        ],
    },
```
여기에서 pub_spin_node는 터미널에서 ros2 run으로 명령어를 입력할 때의 노드 이름이다  
자동완성을 할 때 여기에서 사용한 이름으로 된다   
그 다음으로 py_prac은 패키지명이고 .(닷) 이하 pub_spin는 파이썬으로 작성된 파일명을 말한다
수정완료 후 저장한다   

워크 스페이스로 이동 후 다음으로는 패키지를 빌드해준다
```
cd ~/my_ws
colcon build --packages-select py_prac
```

셋업파일을 source 해주기
```
. install/setup.bash
```

위 프로그램은 /turtle1/cmd_vel 로 퍼블리싱을 하기 때문에 터틀심이 잘 움직이는 지 확인하기 위해서   
터틀심을 실행하자 

```
ros2 run turtlesim turtlesim_node
```
그리고 나서 최종적으로 타른터미널을 열어서 실행
```
ros2 run py_prac pub_spin_node
```
이제 빙글빙글 도는 거북이가 보일 것이다 

<br/>

## 추가로 파이썬 노드를 더 추가
setup.py 에다 node들 더 추가해주면 된다 
```py
entry_points={
        'console_scripts': [
            'pub_spin_node = py_prac.pub_spin:main',
            'sub_laser_node = py_prac.sub_laser:main'
        ],
    },
```

