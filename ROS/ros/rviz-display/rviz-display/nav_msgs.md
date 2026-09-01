# rviz nav_msgs
rviz로 표시할 수 있는 것 중에 nav_msgs 의 Path 타입의 메세지를 사용해서 표시할 수가 있는데   
move_base에서 로봇의 경로를 표시할 때 사용하는 토픽의 예를 들어서   
`/move_base/global_costmap/costmap` 등의 토픽의 type이 **nav_msgs::Path** 인데   

geometry_msgs::PoseStamped 와 중첩이 되어 있는 메세지 되겠다


## msg 만들기
중요한 것은 Path msg의 poses 가 벡터로 되어 있으므로 중첩된 `geometry_msgs::PoseStamped` type으로 메세지를 만들어서   
경로를 push_back() 로 넣어준다음에 경로가 여러개의 PoseStamed 메세지로 (그 안은 Pose) 로 만들어준다음에 publish를 해줘야 한다  

그렇게 만들어진 메세지는 rviz에서 토픽으로 추가해서 보게되면 경로를 볼 수가 있다   


```cpp
ros::init(argc, argv, "nav_msgs_example_node");
ros::NodeHandle nh;
ros::Publisher pub = nh.advertise<nav_msgs::Path>("my_path", 10);
nav_msgs::Path msg;
```

메세지를 만들어서 퍼블리싱
```cpp
// 테스트를 위해서 메세지 만들기
for(int i=0; i< 10; i++) {
    geometry_msgs::Pose pose;
    geometry_msgs::PoseStamped pose_stamped;

    msg.header.frame_id = "map";
    msg.header.stamp = ros::Time::now();

    pose.position.x = (double)i;
    pose.position.y = 0.0;
    pose.position.z = 0.0;
    pose.orientation.x = 0.0;
    pose.orientation.y = 0.0;
    pose.orientation.z = -0.0023;  // 임의로 지정
    pose.orientation.w = 0.1826; // 임의로 지정

    pose_stamped.pose = pose;
    msg.poses.push_back(pose_stamped);
}
```

이제 위의 for문을 `while(ros::ok())` 안에 넣어서 `pub.publish(msg);` 해주면 된다  

rviz에서는 토픽 my_path를 추가하게되면 x 축 방향으로 path 가 생기는 것을 볼 수가 있다.  

## rviz
터미널에 `rviz`로 입력해서 rviz를 띄운다음에   
Add 버튼을 눌러서 Path를 추가해준 다음, Topic 에 해당 토픽을 입력해주고   
(my_path 즉 nav_msgs::Path 타입을 구독)하게 한 상태에서 위의 cpp 노드를 실행해서 퍼블리쉬가 되면   
path가 표시되는 것을 볼 수 가 있다 

> urdf, joint_states 등은 없어도 작동 한다  

### 필요시 간단한 urdf 추가
기본적인 urdf 파일 (base_link와 base_footprint) 로 간략하게 만들어서 모델을 띄울 수도 있고   
map 프레임이 필요할 수도 있는데 static_transform_publisher를 이용해서 map 과 base_link을 연결해준다   

런치파일 예 
```xml
<launch>
<param name="robot_description" command="xacro $(find my_nav_path)/urdf/urdf.xacro" />
<node pkg="tf2_ros" type="static_transform_publisher" name="link_map_tf" output="screen"
    args="0 0 0 0 0 0  map base_link" />
</launch>
```




