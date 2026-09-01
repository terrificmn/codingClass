# trajectory warn
trajectroy 메세지를 만들어서 publish를 했는데 이런 비슷한 워닝이 나오고 잘 작동하지 않는다면   
Dropping 된다고 하면서 워닝...  이면 워닝이지, 작동도 안한다 ㅠ
```
[ WARN] [1686736960.260305750, 3.864000000]: Dropping all 1 trajectory point(s), as they occur before the current time.
Last point is 0.002000s in the past.
```

이럴 때에는 `tarjectory_msgs::JointTrajectory` 메세지 에서 중첩으로  Point 메세지도 가지고 있는데  
```cpp
trajectory_msgs::JointTrajectory joint_tra_msg;
trajectory_msgs::JointTrajectoryPoint point_msg;

///생략..
point_msg.position = vector_position; /// std::vector로 만들어진  double 값이 들어가야함
point_msg.time_from_start.sec = 1;

joint_tra_msg.points.push_back(point_msg);

// 이후 joint_tra_msg 퍼블리쉬 한다
pub_trajectory.publish(joint_tra_msg);  // pub_trajectory 는 ros::Publisher
```

여기에서 point_msg 변수 (JointTrajectoryPoint) 의 `time_from_start`   
는 0 보다 큰 수가 입력이 되어야 한다고 한다   

**1** 값만 넣어줘도 워닝 메세지는 사라지게된다.  

> 단, 1의 하드코딩이 아닌 더 적합한 `time_from_start 시작으로 부터의 시간.sec` 더 알아봐야 할 듯   





