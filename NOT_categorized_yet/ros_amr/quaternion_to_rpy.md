
## quartnion to r p y

일단 yaw 값만 ..변환
```cpp
#include <tf/tf.h>

// quartnion to r p y
    tf::Quaternion q(
        pubPosePtr->pose.orientation.x,
        pubPosePtr->pose.orientation.y,
        pubPosePtr->pose.orientation.z,
        pubPosePtr->pose.orientation.w
    );

    tf::Matrix3x3 m(q);
    double r, p, yaw;
    m.getRPY(r, p, yaw);
    // ROS_ERROR("tf:q %lf", yaw);

    // the same above
    // double t1 = 2.0 * (pubPosePtr->pose.orientation.w * pubPosePtr->pose.orientation.z + pubPosePtr->pose.orientation.x * pubPosePtr->pose.orientation.y);
    // double t2 = 1.0 - 2.0 * (pubPosePtr->pose.orientation.y * pubPosePtr->pose.orientation.y + pubPosePtr->pose.orientation.z * pubPosePtr->pose.orientation.z);
    // double yaw = std::atan2(t1, t2);
    // ROS_ERROR("new %lf", yaw);
```                



### x, y, theta 에서 quaternion
```cpp
#include <tf2/LinearMath/Quaternion.h>

tf2::Quaternion quat ;
  quat.setRPY(0,0,theta*M_PI/180.0);
  robotposeMsg.pose.orientation.x =quat.x();
  robotposeMsg.pose.orientation.y =quat.y();
  robotposeMsg.pose.orientation.z =quat.z();
  robotposeMsg.pose.orientation.w =quat.w();
```
그리고   robotposeMsg.pose.orientation.z 를 사용하면 됨 



