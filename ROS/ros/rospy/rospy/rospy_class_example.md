# Subscripber, Publisher 같은 노드에서 사용하기
publisher는 다른 rate로 퍼블리싱 할 수 있다.  
일단 c++와 다르게 spinOnce가 없는 듯 하다.  
spin을 하게 되면 서로 멀티(?)로 돌아가는 듯 하다 . 클래스 컨스트럭터 함수가 시작될 때  
publishPose() 메소드를 호출하게 했는데 그 안에서 spin()을 돌릴 필요없이  
(돌리면 에러 발생) 서브스크라이브와 퍼블리싱이 서로 잘 된다  

PoseStamped Type같은 경우는 클래스로 전역변수화 해서 사용했다 
rospy.loginfo는 
c++ ROS_INFO와 비슷한데 사용법을 업데이트 해야겠다 


```py
#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped

poseData = PoseStamped()

class SendExample:
    def __init__ (self):
        self.counter = 0
        self.odomSub = rospy.Subscriber('/odom', Odometry, self.odomCb)
        self.posePub = rospy.Publisher('/send_example', PoseStamped, queue_size=10)

        rospy.loginfo('started node')
        self.publishPose()

    def odomCb(self, odomMsg):
        poseData.header.frame_id = "odom" 
        poseData.header.seq += self.counter
        poseData.header.stamp = rospy.Time.now()

        poseData.pose.position.x = odomMsg.pose.pose.position.x;
        poseData.pose.position.y = odomMsg.pose.pose.position.y;
        poseData.pose.position.z = odomMsg.pose.pose.position.z;

        poseData.pose.orientation.x = 0.0;
        poseData.pose.orientation.y = 0.0;
        poseData.pose.orientation.z = odomMsg.pose.pose.orientation.z;
        poseData.pose.orientation.w = odomMsg.pose.pose.orientation.w;

        rospy.loginfo('header')

    def publishPose(self):
        loopRate = rospy.Rate(1)
        while not rospy.is_shutdown():
            self.posePub.publish(poseData)
            
            loopRate.sleep()

def main():
    rospy.init_node('pose_send_node')

    sendPoseObj = PoseStamped()

    rospy.spin()


if __name__ == '__main__':
    main()
```