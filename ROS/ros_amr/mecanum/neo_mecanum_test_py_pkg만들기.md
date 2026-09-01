# python pkg 및 테스트 코드

rospy를 이용해서 python3로 실행시키는 것은 꽤 빠르면서 편리하다   

먼저 pkg 만들기 (catkin_create_pkg 명령어)
```
cd ~/catkin_ws/src
catkin_create_pkg mpo_500_test rospy
```

그리고 에디터로 열어서 mpo_500_test로 만든 패키지의 src 디렉토리에 py파일을 만들어준다 

간단한 예제 파일
```py
#! /usr/bin/env python3

import rospy
from std_msgs.msg import Float32MultiArray

rospy.init_node('basic_motion', anonymous=True)
pub = rospy.Publisher('wheel_speed', Float32MultiArray, queue_size=10)
rospy.sleep(3)

backward = [-1, -1, -1, -1]
msg = Float32MultiArray(data=backward)
pub.publish(msg)

rospy.sleep(3)

left = [-1, 1, -1, 1]
msg = Float32MultiArray(data=left)
pub.publish(msg)

rospy.sleep(3)

right = [1, -1, 1, -1]
msg = Float32MultiArray(data=right)
pub.publish(msg)

rospy.sleep(3)

counterclockwise = [-1, 1, 1, -1]
msg = Float32MultiArray(data=counterclockwise)
pub.publish(msg)

rospy.sleep(3)

clockwise = [1, -1, -1, 1]
msg = Float32MultiArray(data=clockwise)
pub.publish(msg)

rospy.sleep(3)

stop = [0,0,0,0]
msg = Float32MultiArray(data=stop)
pub.publish(msg)
```

저장한 후에 catkin_ws로 이동 후 빌드를 한번 해준다 
```
cd ~/catkin_ws
catkin build mpo_500_test
```

그리고 source를 해준다 
```
source devel/setup.bash 
```

이제 다른 것 추가할 필요도 없이 바로 rosrun 가능
```
rosrun mpo_500_test basic_motion.py 
```

> 실행은 잘 되지만, 일단 시뮬레이션이에서는 cmd_vel만 받는 듯 하다. 좀 더 연구가 필요할 듯 하다 


