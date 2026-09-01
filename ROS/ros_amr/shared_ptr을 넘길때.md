

```cpp

boost::shared_ptr<geometry_msgs::PoseWithCovarianceStamped const> shared_ptr_;  // std_msgs::Empty::ConstPtr ptr; or std_msgs::Empty::Ptr ptr; both available
shared_ptr_ = ros::topic::waitForMessage<geometry_msgs::PoseWithCovarianceStamped>("/initialpose", ros::Duration(1));  //topic 재확인할 것

///// shared_ptr를 만들고 ros type은 geometry_msgs 사용
///// ros waitForMessage에 의해서 rviz에서 2D Pose Estimate 클릭 시 /initialpose 토픽 퍼블리쉬

/// 함수로 넘기고 싶다면 함수 파라미터는 ConstPtr 을 붙여주면 된다 &로 레퍼렌스를 받는다 (shared_ptr 이므로)
void sharedPtrPass(const geometry_msgs::PoseWithCovarianceStamped::ConstPtr &waypoint_pose, std::string target_frame) {
    ROS_WARN("entered in sharedPtrPass func");
    ROS_WARN("%s ", waypoint_pose->header.frame_id.c_str());

    if (waypoint_pose->header.frame_id != target_frame) {
        ROS_WARN("Ok1");
        try {
            ///... do something

        } catch(tf::TransformException &ex) {
            ROS_ERROR("%s", ex.what());
            ros::Duration(1.0).sleep();
        }
    } else {
        /// 현재는 return이 없고 void 이지만 만약 그대로 값을 그대로 넘기려면 값으로 넘겨준다.
        return *waypoint_pose;
    }
    ROS_WARN("here???");
}


if(!shared_ptr_) {
        ROS_ERROR("not yet: /initialpose from rviz");
        lr.sleep();
        continue;
    }

    /// 문제점~ Quaternion 맞춰야함 아래 if문
    if(shared_ptr_){
        ROS_INFO("execute() --> PoseWithCovarianceStamped ");
        geometry_msgs::PoseWithCovarianceStamped ret_pose;
        
   // shared_ptr pass하는 방법을 찾거나 (ConstPtr로 Segmentation fault) 일단 아래처럼 사용
        geometry_msgs::PoseWithCovarianceStamped tmp_pose;
        tmp_pose.header.frame_id = shared_ptr_->header.frame_id;
        tmp_pose.pose.pose = shared_ptr_->pose.pose;
                            
        // ret_pose = changePose(tmp_pose, "map");
        ret_pose = changePose(shared_ptr_, "map");
        
        ROS_INFO("frame_id : %s", ret_pose.header.frame_id.c_str());
        ROS_INFO("pos x : %lf", ret_pose.pose.pose.position.x);
        ROS_INFO("pos y : %lf", ret_pose.pose.pose.position.y);
        ROS_INFO("ori z : %lf", ret_pose.pose.pose.orientation.z);

        // pushbackFromPose(geometry_msgs::PoseWithCovarianceStamped pose_co_st);
        
        // pushback해야함
        //// 이부분 함수 겹치는 듯 (파라미터로 수정할 수 있을 듯 함)
        // pubPoseArray();

        geometry_msgs::PoseArray result_pose_array;
        result_pose_array = convertToPoseArray(vec_waypoints);
        this->pose_array_pub.publish(result_pose_array);
    }


```


