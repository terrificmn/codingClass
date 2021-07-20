
rostopic echo /l515/color/points -n1 한번 해보기


https://pointclouds.org/documentation/classpcl_1_1_point_cloud.html#details
를 참고해서 PCL로 할 수 있는지 봐볼 것 



[깃허브 클론후 catkin_make](https://github.com/ros-perception/pointcloud_to_laserscan)

!!! 주의: 깃클론 받아서 시도 (깃허브로 클론해서 하려면 ros2이므로 브랜치 lunar-devel 로 사용)

[참고](http://wiki.ros.org/pointcloud_to_laserscan)

안되면 그냥 apt-get으로 다운
```
apt-get install ros-melodic-pointcloud-to-laserscan
```


사실 sensor_msg/laserscan 에 있는 것이라서 적용이 안되기 할 것이지만 한번 참고만;; ㅜㅜ

클래스인데 적용을 좀 바꿔서 해볼것
변수로 선언 rospy.on_shutdown(self.shutdownhook)
self.shutdownhook 은 함수

def shutdownhook(self):
    self.ctrl_c = True

그래서 실제 루프가 돌아갈 때 사용이 되는 것 같음
while not self.ctrl_c:
    실제 내용 코드

속성으로 만들어줄 것들

self.a = 0.0
self.b = 0.0
self.c = 0.0
self.d = 0.0


그리고 서브크라이브에서 callback 함수에서 
self.a = msg.ranges[180] //left
self.c = msg.ranges[len(msg.rages)/2] //back
self.d = msg.ranges[540] //right
self.e = msg.ranges[1] // front


앵글이 -3.14 에서 3.14 까지 된다고 가정하면 180
