imu_filter_madgwick
```
sudo apt install ros-melodic-imu-filter-madgwick
```

먼저 rs camera의 런치파일에서 arg로 unite_imu_method 을 linear_interpolation 로 넣어준다  
추후 parameter로 사용됨

```
<launch>
    
    <!-- <include file="$(find realsense2_camera)/launch/rs_camera.launch"> -->
    <include file="$(find md)/launch/rs_d435_camera.launch">
        <arg name="align_depth" value="true"/>
        <arg name="linear_accel_cov" value="1.0"/>
        <arg name="unite_imu_method" value="linear_interpolation"/>
    </include>
    
    <node pkg="imu_filter_madgwick" type="imu_filter_node" name="ImuFilter">
        <param name="use_mag" type="bool" value="false" />
        <param name="_publish_tf" type="bool" value="false" />
        <param name="_world_frame" type="string" value="enu" />
        <param name="fixed_frame" type="string" value="base_link" />
        <param name="publish_tf" type="bool" value="true" />
        <remap from="/imu/data_raw" to="/camera/imu"/>
        <!-- ImuFilter publishes /imu/data -->
    </node>
</launch>
```
예시


또는 imu_complementary_filter 사용해보기    
비슷할 것으로 예상  

http://wiki.ros.org/imu_complementary_filter?distro=melodic

멜로딕 버전 클론
```
git clone -b melodic https://github.com/CCNYRoboticsLab/imu_tools.git
```