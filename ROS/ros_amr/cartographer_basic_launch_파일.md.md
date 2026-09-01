## launch file
```xml
<launch>

<!-- Load robot description and start state publisher-->

   <param name="robot_description" textfile="$(find gbot_core)/urdf/head_2d.urdf" />

<node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher" />

<!-- Start RPLIDAR sensor node which provides LaserScan data -->

<node name="rplidarNode" pkg="rplidar_ros" type="rplidarNode" output="screen">

<param name="serial_port" type="string" value="/dev/ttyUSB0"/>

<param name="serial_baudrate" type="int" value="115200"/>

<param name="frame_id" type="string" value="laser"/>

<param name="inverted" type="bool" value="false"/>

<param name="angle_compensate" type="bool" value="true"/>

</node>

<!-- Start Google Cartographer node with custom configuration file-->

<node name="cartographer_node" pkg="cartographer_ros" type="cartographer_node" args="

-configuration_directory

$(find gbot_core)/configuration_files

-configuration_basename gbot_lidar_2d.lua" output="screen">

</node>

<!-- Additional node which converts Cartographer map into ROS occupancy grid map. Not used and can be skipped in this case -->

<node name="cartographer_occupancy_grid_node" pkg="cartographer_ros" type="cartographer_occupancy_grid_node" args="-resolution 0.05" />

</launch>
```


## 2d.lua 파일

```lua
-- Copyright 2016 The Cartographer Authors

--

-- Licensed under the Apache License, Version 2.0 (the "License");

-- you may not use this file except in compliance with the License.

-- You may obtain a copy of the License at

--

-- http://www.apache.org/licenses/LICENSE-2.0

--

-- Unless required by applicable law or agreed to in writing, software

-- distributed under the License is distributed on an "AS IS" BASIS,

-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

-- See the License for the specific language governing permissions and

-- limitations under the License.

include "map_builder.lua"

include "trajectory_builder.lua"

options = {

map_builder = MAP_BUILDER,

trajectory_builder = TRAJECTORY_BUILDER,

map_frame = "map",

tracking_frame = "base_link",

published_frame = "base_link",

odom_frame = "odom",

provide_odom_frame = true,

publish_frame_projected_to_2d = true,

use_odometry = false,

use_nav_sat = false,

use_landmarks = false,

num_laser_scans = 1,

num_multi_echo_laser_scans = 0,

num_subdivisions_per_laser_scan = 1,

num_point_clouds = 0,

lookup_transform_timeout_sec = 0.2,

submap_publish_period_sec = 0.3,

pose_publish_period_sec = 5e-3,

trajectory_publish_period_sec = 30e-3,

rangefinder_sampling_ratio = 1.,

odometry_sampling_ratio = 1.,

fixed_frame_pose_sampling_ratio = 1.,

imu_sampling_ratio = 1.,

landmarks_sampling_ratio = 1.,

}

MAP_BUILDER.use_trajectory_builder_2d = true

TRAJECTORY_BUILDER_2D.min_range = 0.5

TRAJECTORY_BUILDER_2D.max_range = 8.

TRAJECTORY_BUILDER_2D.missing_data_ray_length = 8.5

TRAJECTORY_BUILDER_2D.use_imu_data = false

TRAJECTORY_BUILDER_2D.use_online_correlative_scan_matching = true

TRAJECTORY_BUILDER_2D.real_time_correlative_scan_matcher.linear_search_window = 0.1

TRAJECTORY_BUILDER_2D.real_time_correlative_scan_matcher.translation_delta_cost_weight = 10.

TRAJECTORY_BUILDER_2D.real_time_correlative_scan_matcher.rotation_delta_cost_weight = 1e-1

TRAJECTORY_BUILDER_2D.motion_filter.max_angle_radians = math.rad(0.2)

-- for current lidar only 1 is good value

TRAJECTORY_BUILDER_2D.num_accumulated_range_data = 1

POSE_GRAPH.constraint_builder.min_score = 0.65

POSE_GRAPH.constraint_builder.global_localization_min_score = 0.65

POSE_GRAPH.optimization_problem.huber_scale = 1e2

POSE_GRAPH.optimize_every_n_nodes = 35

return options
```

