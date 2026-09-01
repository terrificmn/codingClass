## radian, theta
각도 theta가 들어온 경우,  

요기에서 라디안을 각도로 바꾸는 작업을 해서 들어왔을 것. yaw*180.0/M_PI --> degree가 된다   

이제 이것을 ros PoseStamped 메세지로 만들 때   
orientation 부분에서 quaternion 방식으로 넣어주기 위해서 변환을 해줘야 한다. 

필요한 것은 radian 값과 tf2:Quaternion 이 있으면 되고   
일단 인쿠르드 하기 

```cpp
#include <tf2/LinearMath/Quaternion.h>
#include <tf/tf.h>
```

이후 
```cpp
tf2::Quaternion quaternion;
float rad_from_theta = theta * M_PI / 180.0;
quaternion.setRPY(0, 0, rad_from_theta);
```

setRPY() 함수를 이용해서 쿼터니언 값을 넣어줄 수가 있는데   
이때 radian으로 다시 만들어줘서 넣어줘야 한다.   

radian은 `(각도) * 3.14 / 180.0` 구해진다.    

ros message 만들기
```cpp
geometry_msgs::PoseStamped msg;
/// position은 생략

msg.pose.orientation.x = q.x();
msg.pose.orientation.y = q.y();
msg.pose.orientation.z = q.z();
msg.pose.orientation.w = q.w();

// 그리고 필요시 ros publish
pub_msg.publish(msg);
```


## 일단 용어 자체를 이해를 ㅠㅜ
theta, yaw, radian.. 등등 정리가 필요할 듯 하다.

그전에는 커터니언 값을 다시 만들어서 getRPY() 함수를 이용해서 다시 yaw 값으로 만들었는데    
tf::Matrix3x3 이란 놈을 만들고 거기에 quaternion 만들어 진 것을 넣어주면   
getRPY() 함수를 사용할 수가 있다.
> 아마도 roll, pitch, yaw가 모두 필요한 경우에 사용하면 될 듯 하다.
```cpp
//    위에서 커터니언으로 나온 값들.. 이미 quat가 살아있는 경우 
//    다시 만들어 준다. 
    tf::Quaternion q (quat.x(), quat.y(), quat.z(), quat.w());
    tf::Matrix3x3 m(q);
    double r, p, yaw;
    m.getRPY(r, p, yaw);
```
이렇게 하면 다시 라디안으로 만들어준다. 

하지만 라디언 값만 필요할 경우에는 위에 처럼 할 **필요가 없는 듯 하다.**

yaw 만 필요할 경우에는 이미 각도가 있으니 다시 radian으로 만들어주는 PI를 곱하고, 다시 180.0로 나눠주면 된다. 
```cpp
float my_radian = theta * M_PI / 180.0;
```

> 위의 Quaternion, Matrix3x3 등으로 안 사용해도 된다.



