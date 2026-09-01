## global planner  
golobal planner is in charge of calculating a sfae path in order to arrive at that goal pose 
This path is calculated before teh robot starts moving, so it will not take into  
account the readings that the robot sensors are doing while moving

연관 토픽   
/plan  

종류 
Navfn: 많이 사용되고, Dijikstar's 알고리즘 사용
Carrot Planner   
GlobalPlanner

global planner의 종류에는 GlobalPlanner도 하나의 종류이기도 하다 (navfn과 비슷한것 같음)   
차이점 중 하나는 navfn은 장애물에 목표goal로 보낼 수 없으나  
carrot 은 장애물있는 곳을 목표로 지정해도 그 근처로 이동한 후 회피해서 근접해서 도달하게 됨



base_global_planner: "navfn/NavfnROS"  
base_global_planner: "carrot_planner/CarrotPlanner"  
base_global_planner: "global_planner/GlobalPlanner"  

런치파일에서 선택하기  
```xml
<!-- 아규먼트 만들기 -->
  <arg name="base_global_planner" default="navfn/NavfnROS"/>
  <arg name="base_local_planner" default="dwa_local_planner/DWAPlannerROS"/>

  <node pkg="move_base" type="move_base" respawn="false" name="move_base" output="screen">
    <!-- 파라미터 설정 -->
    <param name="base_global_planner" value="$(arg base_global_planner)"/>
    <param name="base_local_planner" value="$(arg base_local_planner)"/> 
```

또는 rosparam을 이용해서 yaml파일을 각각 load를 해준다음에 위에서 고르는 방법이 있는 듯하고   
아니면 planner 파일에 global planner관련된 파라미터를 다 넣어준다음에 선택할 수 있는 듯함 

만약 planner.yaml 파일 식으로 하나의 파일로 할 경우에는  
yaml파일에 base_global_planner: "navfn/NavfnROS"  식으로 정의 해주거나 위의 런치파일에서 param태그를 이용해서 지정해준다  

어쨌든 global planner 및 local planner를 어떤 것을 사용할 지는 결정을 해줘야한다 


예:  
```yaml
controller_frequency: 5.0
recovery_behaviour_enabled: true

NavfnROS:
  allow_unknown: true # Specifies whether or not to allow navfn to create plans that traverse unknown space.
  default_tolerance: 0.1 # A tolerance on the goal point for the planner.
  use_dijkstra: true
  use_quadratic: true
  use_grid_path: false
  old_navfn_behavior: false
  visualize_potential: true

DWAPlannerROS:
  # Robot configuration parameters 
  acc_lim_x: 2.5
  acc_lim_y: 0
  acc_lim_th: 3.2

  max_vel_x: 0.8
  min_vel_x: 0.0
  max_vel_y: 0
  min_vel_y: 0

### deprecated
  # max_trans_vel: 0.5
  # min_trans_vel: 0.1
  # max_rot_vel: 1.0
  # min_rot_vel: 0.2

  max_vel_trans: 0.5
  min_vel_trans: 0.1
  max_vel_theta: 1.0
  min_vel_theta: 0.2

  # Goal Tolerance Parameters
  yaw_goal_tolerance: 0.1
  xy_goal_tolerance: 0.2
  latch_xy_goal_tolerance: false

  # # Forward Simulation Parameters
  sim_time: 2.0
  sim_granularity: 0.02
  vx_samples: 6
  vy_samples: 0
  vtheta_samples: 20
  penalize_negative_x: true

  # # Trajectory scoring parameters
  path_distance_bias: 32.0 # The weighting for how much the controller should stay close to the path it was given
  goal_distance_bias: 24.0 # The weighting for how much the controller should attempt to reach its local goal, also controls speed
  occdist_scale: 0.01 # The weighting for how much the controller should attempt to avoid obstacles
  forward_point_distance: 0.325 # The distance from the center point of the robot to place an additional scoring point, in meters
  stop_time_buffer: 0.2  # The amount of time that the robot must stThe absolute value of the veolicty at which to start scaling the robot's footprint, in m/sop before a collision in order for a trajectory to be considered valid in seconds
  scaling_speed: 0.25 # The absolute value of the veolicty at which to start scaling the robot's footprint, in m/s
  max_scaling_factor: 0.2 # The maximum factor to scale the robot's footprint by

  # # Oscillation Prevention Parameters
  oscillation_reset_dist: 0.25 #How far the robot must travel in meters before oscillation flags are reset (double, default: 0.05)


# TrajectoryPlannerROS:
  # Robot Configuration Parameters
  acc_lim_x: 1.5
  acc_lim_theta:  2.0

  max_vel_x: 1.0
  min_vel_x: 0.0

  max_vel_theta: 0.8
  min_vel_theta: -0.8
  min_in_place_vel_theta: 0.2

  holonomic_robot: false
  escape_vel: -0.1
  
  # Goal Tolerance Parameters
  yaw_goal_tolerance: 0.15
  xy_goal_tolerance: 0.25
  latch_xy_goal_tolerance: false

  # Forward Simulation Parameters
  sim_time: 2.0
  sim_granularity: 0.02
  angular_sim_granularity: 0.02
  vx_samples: 6
  vtheta_samples: 20
  controller_frequency: 20.0
  
  # Trajectory scoring parameters
  meter_scoring: true # Whether the gdist_scale and pdist_scale parameters should assume that goal_distance and path_distance are expressed in units of meters or cells. Cells are assumed by default (false).
  occdist_scale:  0.1 #The weighting for how much the controller should attempt to avoid obstacles. default 0.01
  ## deprecated #pdist_scale: 0.75  #The weighting for how much the controller should stay close to the path it was given . default 0.6
  path_distance_bias: 0.6
  ## deprecated #gdist_scale: 1.0 #     The weighting for how much the controller should attempt to reach its local goal, also controls speed  default 0.8
  goal_distance_bias: 0.8

  heading_lookahead: 0.325  #How far to look ahead in meters when scoring different in-place-rotation trajectories
  heading_scoring: false  #Whether to score based on the robot's heading to the path or its distance from the path. default false
  heading_scoring_timestep: 0.8   #How far to look ahead in time in seconds along the simulated trajectory when using heading scoring (double, default: 0.8)
  dwa: true #Whether to use the Dynamic Window Approach (DWA)_ or whether to use Trajectory Rollout
  simple_attractor: false
  publish_cost_grid_pc: true  

  # Oscillation Prevention Parameters
  oscillation_reset_dist: 0.25 #How far the robot must travel in meters before oscillation flags are reset (double, default: 0.05)
  escape_reset_dist: 0.1
  escape_reset_theta: 0.1

```


## local planner

local planner는 odometry, laser scan data를 모니터 하고   
collision-free local plan을 선택한다  
로컬 플레너는 로봇의 path를 다시 연산할 수 있다.   

base_local_plnnaer가 하는 일   
1. Discretely sample from the robot's control space
2. for each sampled velocity, perform forward simulations from the robot's  
current state to predict what would happen if the smapled velocity was applied  
3. Evaluate each trajectory resulting from the forward simulation  
4. Discard illegal trajectories   
5. Pick the highest-scoring trajectory and send the asscociated velocities to the mobile base   
6. Rinse and Repeat 

종류   
dwa_local_planner (commonly used)

eband_local_planner

teb_local_planner

trajetory_locl_planner

런치파일에서 선택하기  
default="base_local_planner/TrajectoryPlannerROS"  
default="base_local_planner/DWAPlannerROS"  
default="base_local_planner/EbandPlannerROS"  
default="base_local_planner/TebLocalPlannerROS"  
```xml
<!-- 아규먼트 만들기 -->
  <arg name="base_global_planner" default="navfn/NavfnROS"/>
  <arg name="base_local_planner" default="dwa_local_planner/DWAPlannerROS"/>

  <node pkg="move_base" type="move_base" respawn="false" name="move_base" output="screen">
    <!-- 파라미터 설정 -->
    <param name="base_global_planner" value="$(arg base_global_planner)"/>
    <param name="base_local_planner" value="$(arg base_local_planner)"/> 
```

파라미터 설명  
/acc_lim_x (default:2.5): The x acceleration limit of the robot in meters/sec  

/acc_lim_th (default:3.2): The rotational acceleration limit of the robot in radians/sec  

/max_trans_vel (default:0.55): The absolute value of the maximum translational  
velocity for the robot in m/s   

/min_trans_vel (defaul: 0.1):  The absolute value of the minimum translational   
velocity for the robot in m/s    

/max_vel_x (default: 0.55): tHE maximum x velocity for the robot in m/s   

/min_vel_x (default: 0.0) The minimum x velocity for the robot in m/s   

/max_rot_vel (default: 1.0) The absolute value of the maximum rotational velocity 
for the robot in rad/s     

/min_rot_vel (default:0.4): The absolute value of the minimum rotational velocity 
for the robot in rad/s  


Goal Tolerance Parameters 파라미터 중  
/yaw_goal_tolerance (double default:0.05) The tolerance, in radians, for the controller  
in the yaw/rotation when achieving its goal  
DWAPlanner 에서 골 도착 지점에서 회전을 하면서 목표지점에서 회전하면서 goal의 orientation을 찾으려고 하는 것    

xy_goal_tolerance를 높게 주면 골에서 조금 떨어져 있어도 도착으로 인정    
xy_goal_tolerance를 작게 주면 최종골까지 이동해서 도착

/xy_goal_tolerance (double, default: 0.10): The tolerance, in meters, for the controller  
in the x and y distance when achieving a goal  

dwa_local_planner 
```yaml
DWAPlannerROS:
  max_vel_x: 0.5  # 0.55
  min_vel_x: 0.0 

  max_vel_y: 0.0  # diff drive robot
  min_vel_y: 0.0  # diff drive robot

  # Warning!
  #   do not set min_trans_vel(min_vel_trans) to 0.0 otherwise dwa will always think translational velocities
  #   are non-negligible and small in place rotational velocities will be created.
### deprecated : # max_trans_vel, min_trans_vel: 0.1, max_rot_vel: 1.0, min_rot_vel: 0.2

  max_vel_trans: 0.4  # choose slightly less than the base's capability
  min_vel_trans: 0.1 # this is the min trans velocity when there is negligible rotational velocity
  max_vel_theta: 1.0 # choose slightly less than the base's capability
  min_vel_theta: 0.2  # this is the min angular velocity when there is negligible translational velocity

  acc_lim_x: 0.5 # maximum is theoretically 2.0, but we 
  acc_lim_theta: 0.5
  acc_lim_y: 0.0      # diff drive robot

# Goal Tolerance Parameters
  yaw_goal_tolerance: 0.3  # 0.05
  xy_goal_tolerance: 0.15  # 0.10
  # latch_xy_goal_tolerance: false

# Forward Simulation Parameters
  sim_time: 1.0       # 1.7
  vx_samples: 6       # 3
  vy_samples: 1       # diff drive robot, there is only one sample
  vtheta_samples: 20  # 20

# Trajectory Scoring Parameters
  path_distance_bias: 64.0      # 32.0   - weighting for how much it should stick to the global path plan
  goal_distance_bias: 24.0      # 24.0   - wighting for how much it should attempt to reach its goal
  occdist_scale: 0.5            # 0.01   - weighting for how much the controller should avoid obstacles
  forward_point_distance: 0.325 # 0.325  - how far along to place an additional scoring point
  stop_time_buffer: 0.2         # 0.2    - amount of time a robot must stop in before colliding for a valid traj.
  scaling_speed: 0.25           # 0.25   - absolute velocity at which to start scaling the robot's footprint
  max_scaling_factor: 0.2       # 0.2    - how much to scale the robot's footprint when at speed.

# Oscillation Prevention Parameters
  oscillation_reset_dist: 0.05  # 0.05   - how far to travel before resetting oscillation flags

# Debugging
  publish_traj_pc : true
  publish_cost_grid_pc: true
  global_frame_id: map

```

rosparam 으로 확인하기
```
rosparam get /move_base/base_global_planner
```
현재 사용하고 있는 플래너를 출력해준다 