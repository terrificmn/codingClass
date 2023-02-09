
메세지 타입을 이용해서 visualization_msgs 을 사용


```
ImageMarker.msg                InteractiveMarker.msg        Marker.msg
InteractiveMarkerControl.msg   InteractiveMarkerPose.msg    MenuEntry.msg
InteractiveMarkerFeedback.msg  InteractiveMarkerUpdate.msg
InteractiveMarkerInit.msg      MarkerArray.msg
```

다양한 msg 타입이 있음   

Marker,  MarkerArray 등을 이용해서 퍼블리쉬 하면 (예 topic을 /marker_example) rviz에서 볼 수가 있고   

> 아직 못해봄 , 추후 구현해볼 예정  


```
visualization_msgs::Marker marker_msg

marker_msg.header.frame_id = "odom";
marker_msg.header.stamp = ros::Time::now();
marker_msg.ns = "robot";
marker_msg.id = index
marker_msg.type = 타입지정이 가능 예 (SPHRE)
marker_msg.action = msg.ADD (이것도 안해봄)

marker_msg.pose.position.x  = 3.0; 로봇 위치
marker_msg.pose.position.y = 1.0;
marker_msg.pose.position.z = 0.0;

marker_msg.pose.orientation.x =0.0;
marker_msg.pose.orientation.y =0.0;
marker_msg.pose.orientation.z =0.0;
marker_msg.pose.orientation.w =0.0;
marker_msg.scale.x = 1.0; 화면에 표시될 크기(rviz)
marker_msg.scale.y = 1.0;
marker_msg.scale.z = 1.0;

marker_msg.color.r = 1.0; rviz에 색표시 rgb
marker_msg.color.g = 0.0;
marker_msg.color.b = 0.0;
marker_msg.color.a = 1.0;

```

이런식으로 구성해서 퍼블리쉬를 해준다  

> geometry_msgs::Point를 이용해서 pose.postion 값을 넣어주는 방식도 있음



```
rosmsg info Marker.msg
또는 
rosmsg info visualization_msgs/Marker
```

unit8 로 지정되어 있는 값들이 있는데  이 값을 위의 marker_msg.type 에서 지정해주면 된다     
marker_msg.action은 Add 부터? MODIFY, DELETE, DELETEALL 인 듯 하다  


