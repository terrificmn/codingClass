```
    /* This is just for reference
    void poseCallback(const turtlesim::PoseConstPtr& msg){
    static tf::TransformBroadcaster br;
    tf::Transform transform;
    transform.setOrigin( tf::Vector3(msg->x, msg->y, 0.0) );
    tf::Quaternion q;
    q.setRPY(0, 0, msg->theta);
    transform.setRotation(q);
    br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "world", turtle_name));
}
*/

```


odom frame 만들어서 sendTransform() 하기  
odom 토픽 퍼블리쉬 되는 것과 비슷하게 만들어 준다. 함수로 만들어서 실행
```cpp
void mapTfBroadcaster(float Md_f_theta)
{
    static tf2_ros::TransformBroadcaster tf_br;
    geometry_msgs::TransformStamped transformStamped;
    tf2::Quaternion q;

    transformStamped.header.stamp = ros::Time::now();
    transformStamped.header.frame_id = "odom";
    transformStamped.child_frame_id = "base_footprint";
    transformStamped.transform.translation.x = Md.lPosiY/1000.0; 
    transformStamped.transform.translation.y = Md.lPosiX/1000.0;
    transformStamped.transform.translation.z = 0.0;
    q.setRPY(0, 0, Md_f_theta*3.141592/180.0);
    transformStamped.transform.rotation.x = q.x();
    transformStamped.transform.rotation.y = q.y();
    transformStamped.transform.rotation.z = q.z();
    transformStamped.transform.rotation.w = q.w();
    
    //send transform
    tf_br.sendTransform(transformStamped);
}
```