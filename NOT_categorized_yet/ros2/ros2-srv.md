

서비스 목록 보기
```
ros2 service list
```


service 에 대한 type보기
```
ros2 service type /spawn_entity
```

타입을 보게 되면 
gazebo_msgs 이런식으로 나온다 

그러면 이거를 자세하게 알아볼 수 있다

```
ros2 interface show gazebo_msgs/srv/SpawnEntity
```
--- 윗부분은 request 
아랫부분은 response

또 다른 예:
```
ros2 interface show geometry_msgs/msg/Twist
```

결과는 
```
# This expresses velocity in free space broken into its linear and angular parts.

Vector3  linear
Vector3  angular
```

> ros 에서는 geometry_msgs/Twist 이런식으로 되어있었는데  
ROS2에서는 중간에 msg가 들어가게 됨



