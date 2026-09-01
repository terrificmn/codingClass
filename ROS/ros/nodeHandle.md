
노드 핸드를 만들때 문자열 주고   
그걸로 publisher를 만들면 토픽 앞에 네임스페이스 같은 효과가 있는 듯 하다 

> 이를 private 노드 핸들러라고 한다

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

# private nodehandle
생성을 할 때 
```cpp
ros::NodeHandle nh;
```
이런식으로 하게 되면 보통의 노드 핸들러가 되고, 네임스페이가 붙지 않는다.   

단, 
```cpp
ros::init(argc, argv, "mynode");
ros::NodeHandle nh("~");
```
이렇게 하면, "~" 의미는 현재 노드의 이름이 되는 듯 하다. 그래서 만약 ros가 init 할 때 만든 노드 이름으로 
네임스페이스 효과로 토픽등을 퍼블리싱 할 때 추가로 붙어진다

예를 들어 토픽 cmd_vel을 publish 한다고 하면  
이제 토픽은 /mynode/cmd_vel 이런식으로 만들어 지게 된다 

이렇게 나오되게 됨
```
$ rostopic list
/mynode/my_topic
```

근데 노드핸들러를 생성할 때 "~"라고 안하고 특정 문장열을 주면 예를 들어서   
"mynode_handler" 라고 nh()에주며 그 노드 이름으로 토픽 발행된다
```
$ rostopic list
/mynode_handler/my_topic
```

또는 
```cpp
ros::NodeHandle nh("");
```
위 처럼 "" 빈 칸이면, 
```
$ rostopic list
/my_topic

```

그냥 토픽명만 나오게 된다. `ros::NodeHandle nh;` 와 결과가 같게 된다


## 결론
ros::NodeHandle nh(""), ros::NodeHandle nh("~"), ros::NodeHandle nh("my_special_node")
노드 핸들에 이름을 부여하면 private NodeHandle이 되게 된다 

그리고 private으로 만들게 되면 네임스페이가 붙으므로, 일반적인 토픽은 subscribe를 못하는 상황이 생길 수도 있다