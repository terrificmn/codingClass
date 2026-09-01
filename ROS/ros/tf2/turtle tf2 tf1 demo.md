the second generation of the transform library

여러개의 좌표 프레임을 시간에 따라 추적할 수 있게 도와준다  

1. compute inverse and forwrd kinemataics of multi joint robots
2. carry out obstacle avoidance
3. convey location of robot
4. convert sensor data from one reference to another
5. control robot about a particluar point
6. analyze multiple robot data in global frame
7. referencing external object about robot frame

urdf가 있다면 robot_state_publisher로 tf를 publish 할 수 가 있다 

demo install

```
sudo apt install ros-noetic-turtle-tf2 ros-noetic-tf2-tools ros-noetic-tf
```

터틀봇 데모 실행
```
roslaunch turtle_tf2 turtle_tf2_demo.launch
```


터틀봇을 움직여 보면 turtle2가 turtle1를 따라간다 

static_transform_publisher를 이용해서 camera 프레임 연결해보기
```
rosrun tf static_transform_publisher 0 0 1 0 0 0 turtle1 camera 10
```

rviz를 실행해서 보면 z 로 1 m 간격을 두고 tuttle1 을 tf가 생성되는 것을 알 수 있다  


