
# visualization_msgs::Marker 사용하기

메세지 타입을 이용해서 visualization_msgs 을 사용   
대표적인 Marker 사용하기
```cpp
#include <visualization_msgs/Marker.h>
```

다양한 msg 타입이 있음   
```
ImageMarker.msg                InteractiveMarker.msg        Marker.msg
InteractiveMarkerControl.msg   InteractiveMarkerPose.msg    MenuEntry.msg
InteractiveMarkerFeedback.msg  InteractiveMarkerUpdate.msg
InteractiveMarkerInit.msg      MarkerArray.msg
```

Marker,  MarkerArray 등을 이용해서 퍼블리쉬 하면 (예 topic을 /marker_example) rviz에서 볼 수가 있고   

## 메세지 작성

```
visualization_msgs::Marker marker_msg;

marker_msg.header.frame_id = "map";
marker_msg.header.stamp = ros::Time::now();
marker_msg.ns = "robot";
marker_msg.id = 1;
marker_msg.type = visualization_msgs::Marker::ARROW;
marker_msg.action = visualization_msgs::Marker::ADD;

marker_msg.pose.position.x = x;
marker_msg.pose.position.y = y;
marker_msg.pose.position.z = 0.0;

marker_msg.pose.orientation.x =0.0;
marker_msg.pose.orientation.y =0.0;
marker_msg.pose.orientation.z =0.0;
marker_msg.pose.orientation.w =0.0;

marker_msg.scale.x = 0.5; // display scale
marker_msg.scale.y = 0.5;
marker_msg.scale.z = 0.5;

marker_msg.color.r = 0.0;
marker_msg.color.g = 1.0;
marker_msg.color.b = 0.0;
marker_msg.color.a = 1.0;

pub_marker.publish(marker_msg);

```

이런식으로 구성해서 퍼블리쉬를 해준다.   

> geometry_msgs::Point를 이용해서 pose.postion 값을 넣어주는 방식도 있음


생각보다 msg의 scale 크다. rviz에서 add 버튼을 눌러서 Marker를 추가해준다   
rviz에서 subscribe 하고 있는 토픽은 **/visualization_marker** 이다




```
rosmsg info Marker.msg
또는 
rosmsg info visualization_msgs/Marker
```

unit8 로 지정되어 있는 값들이 있는데  이 값을 위의 marker_msg.type 에서 지정해주면 된다     
marker_msg.action은 Add 부터? MODIFY, DELETE, DELETEALL 인 듯 하다  


