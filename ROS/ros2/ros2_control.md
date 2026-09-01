# ros2_control
gazebo 용 xacro 파일 
```xml
<?xml version="1.0"?>
<robot smlns:xacro="http://www.ros.org/wiki/xacro">
    <ros2_control name="GazeboSystem" type="system">
        <hardware>
            <plugin>gazebo_ros2_control/GazeboSystem</plugin>
        </hardware>
        <joint name="left_wheel_joint">
            <command_interface name="velocity">
                <param name="min">-10</param>
                <param name="max">10</param>
            </command_interface>
            <state_interface name="velocity"/>
            <state_interface name="position"/>
        </joint>
        <joint name="right_wheel_joint">
            <command_interface name="velocity">
                <param name="min">-10</param>
                <param name="max">10</param>
            </command_interface>
            <state_interface name="velocity"/>
            <state_interface name="position"/>
        </joint>
    </ros2_control>

    <!-- 가제보 플러그인 추가 -->
    <gazebo>
        <plugin name=-"gazebo_ros2_control" filename="libgazebo_ros2_control.so">
            <!-- yaml파일로 지정을해서 파라미터 설정을 함 -->
            <parameters>$(find 패키지네임)/config/my_controller.yaml </parameters>
        </plugin>
    </gazebo>

</robot>
```

> 참고로 libgazebo_ros_diff_drive.so 플러그인을 추가하듯이 비슷하게 추가해주는 것임   
gazebo를 사용안한다고 하면   
`ros2 run controller_manager ros2_control_node` 를 실행해준다  



ros2_control은 여러 종류의 하드웨어에서 오는 정보들을 취합해서 컨트롤 할 수 있게 도와주는 패키지   

joint 이름은 urdf 의 joint 이름을 사용해야 하며(urdf는 만들어야 함)

보통 모터에서는 command_interface가 가능한데 입력 및 보기가 되는 기능  
state_interface는 read only가 되겠다.    
velocity 는 speed로 모터를 제어하고, encoder로 부터 position 정보를 받는 것을 의미   

ros2는 개인 프로젝트에서 적용할 예정이나, 현재는 아두이노로 컨트롤러를 만들 예정이므로 interface를 참고하면 좋을 듯 하다   


가제보 플러그인을 추가할 때 파라미터를 태그를 통해서 파라미터를 추가하는데  
이는 yaml 파일로 되어 있는 파일을 지정해준다  

```yaml
controller_manager:
    ros__parameters:
        update_rate: 30
        use_sim_time: true  ## gazebo 사용할 경우

        diff_cont:
            type: diff_drive_controller//DiffDriveController

        joint_broad:
            type: joint_state_broadcaster/JointStateBroadcaster

### 생략 
## 이하 추가로 더 찾아볼 것 

```



[추후 좀 더 연구해보기youtube](https://www.youtube.com/watch?v=4QKsDf1c4hc)
