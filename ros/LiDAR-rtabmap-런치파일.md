런치파일 실행해보기

시리얼 넘버 바꾸기, 

## rtabmap, rtabmap_ros 빌드로 설치하는게 좋은 듯,  libpointmatcher 설치

참고 
http://official-rtab-map-forum.67519.x6.nabble.com/Kinect-For-Azure-L515-ICP-lighting-invariant-mapping-td7187.html


# 런치파일

```xml
<launch>
    <!-- use_sim_time?! T/F  -->
    <arg name="sim_time" value="false"/>
    <arg name="use_t265" value="true"/>
    <!-- start l515 -->
    <param unless="$(arg sim_time)" name="/l515/motion_module/global_time_enabled" value="true" />
    <param unless="$(arg sim_time)" name="/l515/rgb_camera/global_time_enabled" value="true" />
    <param unless="$(arg sim_time)" name="/l515/rgb_camera/enable_auto_exposure" value="false"/>
    <param unless="$(arg sim_time)" name="/l515/l500_depth_sensor/sensor_mode" value ="0"/>
    <!-- <param unless="$(arg sim_time)" name="/l515/rgb_camera/gain" value ="4096"/> -->
    <!-- HD MODE? true/false  --> 
    <arg unless="$(arg sim_time)" name="HD" value="false"/>
    <!-- Launch l515  -->  
    <include unless="$(arg sim_time)" file="$(find realsense2_camera)/launch/rs_camera.launch">
        <arg name="serial_no" value="L515_SERIAL_NUMBER"/>
        <arg name="unite_imu_method" value="linear_interpolation"/>
        <arg name="camera" value="l515"/>
        <arg name="enable_gyro" value="true"/>
        <arg name="enable_accel" value="true"/>
        <arg name="accel_fps" value="400"/>
        <arg name="gyro_fps" value="400"/>
        <arg name="filters" value="pointcloud"/>
        <arg name="color_fps" value="30"/>
        <arg name="pointcloud_texture_stream" value="RS2_STREAM_ANY"/>
        <arg name="align_depth" value="false"/>
        <!-- <arg name="initial_reset" value="true"/> -->
        <!-- High DEF CAM -->
        <arg if="$(arg HD)" name="depth_width" value="1024"/>
        <arg if="$(arg HD)" name="depth_height" value="768"/>
        <arg if="$(arg HD)" name="color_width" value="1920"/>
        <arg if="$(arg HD)" name="color_height" value="1080"/>        
        <!-- STANDARD DEF CAM -->
        <arg unless="$(arg HD)" name="depth_width" value="640"/>
        <arg unless="$(arg HD)" name="depth_height" value="480"/>
        <arg unless="$(arg HD)" name="color_width" value="1280"/>
        <arg unless="$(arg HD)" name="color_height" value="720"/>
    </include>

    <node if="$(arg use_t265)" pkg="tf" type="static_transform_publisher" name="static_tf" args="0 0 0.05 0 0 0 t265_link l515_link 10" />
    <node if="$(arg sim_time)" pkg="tf" type="static_transform_publisher" name="static_tf_1" args="0 0 0 0 0 0 t265_pose_frame t265_link 10" />

    <param if="$(arg use_t265)" name="/t265/tracking_module/enable_mapping" value="false"/>
    <include if="$(arg use_t265)" file="$(find realsense2_camera)/launch/rs_t265.launch">
        <arg name="serial_no" value="T265_SERIAL_NUMBER"/>
        <arg name="camera" value="t265"/>
        <arg name="unite_imu_method" value="linear_interpolation"/>
        <arg name="enable_fisheye1" value="true"/>
        <arg name="enable_fisheye2" value="true"/>
        <arg name="enable_sync" value="true"/>
        <arg name="publish_odom_tf" value="true"/>          
    </include>

    <arg name="rtabmapviz"    default="true"/>
    <arg name="scan_rate"    default="30"/>
    <arg name="rate"            value="2"/>
    <arg if="$(arg sim_time)" name="use_sim_time" value="true"/>
    <arg name="scan_cloud_assembling" value="false"/>
    <arg name="use_imu" value="true"/>
    <arg name="imu_topic" value="/imu/data"/>
    <arg name="frame_id" default="l515_link"/>
    <arg name="voxel_size" value="0.1"/>
    <!-- individual scan max size -->
    <arg name="scan_cloud_max_points" value="0"/>

    <arg name="wait_imu_to_init" value="true"/>
    <node pkg="imu_complementary_filter" type="complementary_filter_node" name="complementary_filter_node">
        <remap from="imu/data_raw" to="/l515/imu"/>
      </node>

    <group ns="rtabmap">
      <node pkg="rtabmap_ros" type="icp_odometry" name="icp_odometry" output="screen">
        <remap from="scan_cloud" to="/l515/depth/color/points"/>
        <param name="frame_id"        type="string" value="$(arg frame_id)"/>  
        <param name="odom_frame_id"   type="string" value="odom"/>
        <param name="expected_update_rate" type="double" value="$(arg scan_rate)"/>
        <param name="max_update_rate" value="$(arg scan_rate)"/>
        <param name="scan_cloud_max_points"       type="int"    value="$(arg scan_cloud_max_points)"/>
        <param if="$(arg use_imu)" name="wait_imu_to_init"            type="bool"   value="$(arg wait_imu_to_init)"/>
        <param name="publish_tf"          type="bool"   value="true"/>
        <remap from="imu"           to="$(arg imu_topic)"/>
        <param if="$(arg use_t265)" name="guess_frame_id" value="t265_odom_frame"/>
        <!-- <remap     if="$(arg scan_cloud_filtered)" from="cloud" to="odom_filtered_input_scan"/> -->
        <!-- <remap unless="$(arg scan_cloud_filtered)" from="cloud" to="$(arg scan_cloud_topic)"/> -->
    
        <!-- ICP parameters -->
        <param name="Icp/PointToPlane"        type="string" value="true"/>
        <param name="Icp/Iterations"          type="string" value="10"/>
        <param name="Icp/VoxelSize"           type="string" value="$(arg voxel_size)"/>
        <param name="Icp/DownsamplingStep"    type="string" value="1"/>
        <param name="Icp/Epsilon"             type="string" value="0.0001"/>
        <param name="Icp/PointToPlaneK"       type="string" value="10"/>
        <param name="Icp/PointToPlaneRadius"  type="string" value="0"/>
        <param name="Icp/MaxTranslation"      type="string" value="1"/>
        <param name="Icp/MaxCorrespondenceDistance" type="string" value="$(arg voxel_size)"/>
        <param name="Icp/PM"                  type="string" value="true"/> 
        <param name="Icp/PMOutlierRatio"      type="string" value="0.9"/>
        <param name="Icp/CorrespondenceRatio" type="string" value="0.01"/>
        <param name="Icp/MaxRange" type="string" value="0"/>
        <param name="Icp/PointToPlaneMinComplexity" value="0.0001"/> 

        <!-- Odom parameters -->       
        <param name="Odom/ScanKeyFrameThr"       type="string" value="0.9"/>
        <param name="Odom/Strategy"              type="string" value="0"/>
        <param name="OdomF2M/ScanSubtractRadius" type="string" value="$(arg voxel_size)"/>
        <!-- Max Size of Global Map to keep in "history" -->
        <param name="OdomF2M/ScanMaxSize"        type="string" value="40000"/> 
      </node>    
      
    // 이 부분에서 odom 값을 t265로 바꿔보기 odom값 확인한 후 
    <node if="$(arg scan_cloud_assembling)" pkg="rtabmap_ros" type="point_cloud_assembler" name="point_cloud_assembler" output="screen">
        <remap from="cloud"           to="/l515/depth/color/points"/>
        <remap from="odom"            to="odom"/>
        <param name="max_clouds"      type="int"    value="$(eval arg('scan_rate') / arg('rate'))" />
        <param name="fixed_frame_id"  type="string" value="" />
        <param name="assembling_time" type="double" value="$(eval 1 / arg('rate'))"/>
        <param name="voxel_size"      type="double" value="0.05"/>
        <param name="noise_radius"        type="double" value="0"/>
        <param name="noise_min_neighbors" type="int"    value="5"/>
    </node>

        <!-- RTABMAP NODE  -->
      <node pkg="rtabmap_ros" type="rtabmap" name="rtabmap" output="screen" args="-d">	  
        <param name="frame_id"             type="string" value="$(arg frame_id)"/>  
        <param name="subscribe_depth"      type="bool" value="false"/>
        <param name="subscribe_scan_cloud" type="bool" value="true"/>
        <param name="approx_sync"          type="bool" value="false"/>
        <remap from="imu"           to="$(arg imu_topic)"/>
        
        <remap if="$(arg scan_cloud_assembling)" from="scan_cloud" to="assembled_cloud"/>
        <remap unless="$(arg scan_cloud_assembling)" from="scan_cloud" to="/l515/depth/color/points"/>

        <param if="$(arg use_t265)" name="subscribe_rgb" value="true"/>
        <param unless="$(arg use_t265)" name="subscribe_rgb" value="false"/>
        <remap if="$(arg use_t265)" from="rgb/image"   to="/l515/color/image_raw" />
        <remap if="$(arg use_t265)" from="rgb/camera_info" to="/l515/color/camera_info"/>
        
        <!-- RTAB-Map's parameters -->
        <param name="Rtabmap/DetectionRate"          type="string" value="$(arg rate)"/>  
        <param name="RGBD/NeighborLinkRefining"      type="string" value="false"/>
        <param name="RGBD/ProximityBySpace"          type="string" value="true"/>
        <param name="RGBD/ProximityMaxGraphDepth"    type="string" value="0"/>
        <param name="RGBD/ProximityPathMaxNeighbors" type="string" value="1"/>
        <param name="RGBD/AngularUpdate"             type="string" value="0.05"/>
        <param name="RGBD/LinearUpdate"              type="string" value="0.05"/>
        <param name="Mem/NotLinkedNodesKept"         type="string" value="false"/>
        <param name="Mem/STMSize"                    type="string" value="30"/>
        
        <!-- Reg/Strategy 파라미터  0=Visual, 1=ICP, 2=Visual+ICP -->
        <param name="Reg/Strategy"                   type="string" value="1"/> 
        
        <param name="Grid/CellSize"                  type="string" value="0.1"/>
        <param name="Grid/RangeMax"                  type="string" value="20"/>
        <param name="Grid/ClusterRadius"             type="string" value="1"/>
        <param name="Grid/GroundIsObstacle"          type="string" value="true"/>
        <!-- ICP parameters -->
        <param name="Icp/VoxelSize"                  type="string" value="$(arg voxel_size)"/>
        <param name="Icp/PointToPlaneK"              type="string" value="10"/>
        <param name="Icp/PointToPlaneRadius"         type="string" value="0"/>
        <param name="Icp/PointToPlane"               type="string" value="true"/>
        <param name="Icp/Iterations"                 type="string" value="10"/>
        <param name="Icp/Epsilon"                    type="string" value="0.0001"/>
        <param name="Icp/MaxTranslation"             type="string" value="1"/>
        <param name="Icp/MaxCorrespondenceDistance"  type="string" value="$(arg voxel_size)"/>
        <param name="Icp/PM"                         type="string" value="true"/> 
        <param name="Icp/PMOutlierRatio"             type="string" value="0.9"/>
        <param name="Icp/CorrespondenceRatio"        type="string" value="0.01"/>
        <param name="Icp/PointToPlaneMinComplexity" value="0.0001"/> 

      </node>

    <!-- RTABMAPVIZ NODE  -->
      <node if="$(arg rtabmapviz)" name="rtabmapviz" pkg="rtabmap_ros" type="rtabmapviz" output="screen">
        <param name="frame_id" type="string" value="$(arg frame_id)"/>
        <param name="odom_frame_id" type="string" value="odom"/>
        <param name="subscribe_odom_info" type="bool" value="true"/>
        <param name="subscribe_scan_cloud" type="bool" value="true"/>
        <param name="approx_sync" type="bool" value="false"/>
        <remap if="$(arg scan_cloud_assembling)" from="scan_cloud" to="assembled_cloud"/>
        <remap unless="$(arg scan_cloud_assembling)" from="scan_cloud" to="/l515/depth/color/points"/>

      </node>
  </group>
</launch>

```