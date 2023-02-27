
노드 핸드를 만들때 문자열 주고   
그걸로 publisher를 만들면 토픽 앞에 네임스페이스 같은 효과가 있는 듯 하다 

```cpp
ros::NodeHandle nh("move_base");

action_goal_pub_ = nh.advertise<move_base_msgs::MoveBaseActionGoal>("goal", 1);

recovery_status_pub_= nh.advertise<move_base_msgs::RecoveryStatus>("recovery_status", 1);
```

그러면 이런식으로

/move_base/recovery_status 으로 생성이 된다  


rostopic으로 확인해보면 rostopic info /move_base/recovery_status
```
Type: move_base_msgs/RecoveryStatus

Publishers: 
 * /move_base (http://unamr:45929/)

Subscribers: None
```




