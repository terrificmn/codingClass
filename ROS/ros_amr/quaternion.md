
quat.setRPY(0,0, theta_to_radian);

은 라디안 값이 되는 듯 하다. 공부가 더 필요 

이 값을 넘겨주면 원하는 rpy의 yaw값이 아닌 듯 하다 

> tf2는 getRPY()는 없다. 어떤 점이 tf 와 다른지 공부가 필요  

```
#include <tf2/LinearMath/Quaternion.h>
tf2::Quaternion quat ;
        quat.setRPY(0,0,theta*M_PI/180.0);
        msg.pose.orientation.x =quat.x();
        msg.pose.orientation.y =quat.y();
        msg.pose.orientation.z =quat.z();
        msg.pose.orientation.w =quat.w();
```
이런 느낌으로 생성  


하지만 yaw 값이 필요한 경우에는 

그래서 tf를 인쿠르드 한 후에 
quaternion 을 다시 만들어서 getRPY() 함수를 사용하면 yaw 값이 나오게 된다 

```
#include <tf/tf.h>
tf::Quaternion q (quat.x(), quat.y(), quat.z(), quat.w());
        tf::Matrix3x3 m(q);
        double r, p, yaw;
        m.getRPY(r, p, yaw);
```

이때 double 형 3개의 변수가 필요하다.   
이렇게 하면 getRPY()함수를 통해서 나온 값은 yaw 값은 꽤 잘 된다  




tf2::Quaternion 을 이용해서 나온 값의 z값을 바로 적용시키면 원하는 값이 안나옴

`double yaw = quat.z() *180.0/M_PI;`
 이렇게 해보았으나 실패, 


