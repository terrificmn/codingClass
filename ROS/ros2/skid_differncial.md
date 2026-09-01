
Skid Steering
Differential Drive 

Skid Steering
4개의 바퀴가 있고 각각의 바퀴가 독립적으로 회전수 또는 속도를 조절해서 움직이는 형태
회전에 취약한 단점이 있다

Differential Drive 
양옆으로 2개의 바퀴가 있고 하나 또는 두개의 보조바퀴가 달려 있는 형태
(예를 들어서 로봇청소기)


TF (TransForm)
로봇의 팔이 있다고 하면 팔끝을 알고 싶다면 그 전에 결합되어 있는 부분을 알아야한다
Joint 결합부를 joint라고 말하게 된다. 이를 행렬로 표시하는데 
ROS에서 이것을 쉽게 할 수 있게 해준다

Rviz로 확인할 수 있다


몸체-바퀴
몸체-카메라
몸체-센서

등의 트리형태 구조를 가진다

예를 들어 양쪽의 바퀴는 직접적으로 서로 만나지 않지만 (직접적으로 )
chassis를 통해서 연결될 수 있게 됨


필요한 것들..
지속적으로 로봇의 이동 동향을 알려주기 Action
특정 방향으로 로봇 회전 -> Odom
충돌 전까지 로봇을 직진시키기 ->LaserScan, Twist
초록 박스 인식 -> Image


이미지 보기
ros2에서 기본 제공하는 image_view 노드를 실행할 수 있다
ros2 run image_view image_view --ros-args --remap /image토픽
```
ros2 run image_view image_view --ros-args --remap /image토픽
```

비전처리를 하기 위해서는 msg형식을 갖고 있다.
OpenCV를(라이브러리) 이용하기 위해 cv_bridge 를 사용

> OpenCv의 형식을 ROS2에서 사용하는 형식으로 바꿔줘야 하게 되는데 (그 반대의 경우에도)
이를 가능케 해주는게 cv_bridge (패키지)

OpenCv (OpenCV ipiimage)

Ros CvBridge
    ROS image message


publish되는 topic을 찾는 것은
ros2 topic list를 해서 
카메라의 image_raw를 찾는다
예: /camera_sensor/image_raw


이제 image를 받는 sub를 만든다


## odom sub 만들기

특정한 각속도와 시간을 통해서 로봇을 회전을 시킬 수가 있다

하지만 이렇게 로봇을 회전시키게 되면 오차가 발생을 하게 된다 
(90도로 회전을 해도 바닥면의 마찰 등으로 오차)

처음에는 괜찮지만 점점 오차가 심해짐
(눈을 감고 걸으면 처음에는 몇 발자국은 잘 걷겠지만 그 이후는 다른곳으로 가고 있을 것이다.)

Odom은 Odometry 이며

/odom 안에 topic안에 정보가 들어가 있다 

> odom의 각도 체계는 quaternion 으로 되어 있으므로  Euler angler로 바꿔야 한다
Euler angler (오일러 각도)는 x,y,z가 Roll, Pitch, Yaw로 구성

odom sub만들기


이제 변환된 데이터는 1.57로 나오는데 이는 R (라디안)을 사용하기 때문에 3.14의 반
90도를 향하고 있는 것


action도 커스텀으로 만들어 진것을 사용하는데 
타입은 int32[] 의 turning-sequence 형태로 되어 있다. --- result는 bool 타입의 success 로 사용
그리고 중간중간의 feedback은 string 타입으로 feedback_msg로 받게된다

터미널 창에서 확인 
```
ros2 interface show custom_interfaces/action/Maze
```

action_server는 바로 만들 수가 없기 대문에 executor를 이용해서 
rclpy.spin()을 이용해서 파라미터로 노드 객체와, executor를 이용하는 방법이 있었고

예: 
```
fibonacci_action_server = FibonacciActionServer()
executor = MultiThreadedExecutor()
rclpy.spin(fibonacci_aciton_server, executor=executor)
```


또 다른 방법은 executor를 실행시키고 executor안에 add_node() 메소드를 이용해서 
노드를 추가해서 executor 자체를 spin을 시키는 방법을 사용할 수가 있다
```
maze_action_server = MazeActionServer()
executor = MultiThreadedExecutor()
executor.add_node(maze_action_server)

try:
    executor.spin()
    ...생략
```

executor를 spin시키는 방식을 사용했다면 executor.shutdown() 및 
액션서버도 따로 destroy를 해줘야 한다
```
executor.shutdown()
maze-acvtion_server._action_server.destroy()
maze_action_server.destroy_node()
```

> 여기에서 MultiThreadedExecutor()를 사용한 이유는 서버를 작동할 때 
Subscriber가 2개에 publisher 도 있고 action_server도 있을 때 중간에 
로드가 걸리는 것을 방지하기 위해서 MultiThreadedExecutor를 사용했다고 보면 됨



P Gain Control
turn_offset = 0.7 * (euler_angle - self.yaw) 은 P Gain Control 이며, 급작스러운
변화를 막아주는 역할을 한다. PID Control 이라는 이름으로 검색하면 더 많이 정보를 얻을 수 있다










