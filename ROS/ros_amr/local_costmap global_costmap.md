## local_costmap
local_costmap

local planner uses the local costmap in order to calculate local plans

로봇 센서로 부터 만들어진다 (laser sensor 등)

costmap 생성된 것 지우는 서비스
```
rosservice call /move_base/clear_costmaps "{}"
```
그러면 costmap 생성되었던 것이 없어진다  

> 장애물이 갑자기 생긴다면 먼저 슬램으로 만들었던 static map 에는 global cost_map에는 나오지를 않는다.   
하지만 로봇이 움직이면서 장애물 가까이로 가면 local_cost_map에서 레이저 센서를 통해서 장애물을 인식하게 된다  

local_costmap에는 obstacles_laser와 inflation만 사용이 되었다 
그리고 obstacles_laser 부분의 플러그인이 ObstacleLayer가 사용됨  
```yaml
plugins:
    - {name: obstacles_layer,    type: "costmap_2d::ObstacleLayer"}
    - {name: inflation,         type: "costmap_2d::InflationLayer"}
```

static_map은 false, rolling_window는 true

예:  
```yaml
local_costmap:
#  update_frequency: 10.0
#  publish_frequency: 10.0
  global_frame: odom
  static_map: false
  rolling_window: true
  width: 10.0
  height: 10.0
  origin_x: -5.0
  origin_y: -5.0

  plugins:
    - {name: obstacle,      type: "costmap_2d::ObstacleLayer"}
    - {name: inflation,     type: "costmap_2d::InflationLayer"}"
```
width, height에 따라서 크기가 결정이 된다, origin_x,y는 -1/2 값을 사용   

## global costmap
global_costmap에는 plugins가 3가지 layers가 사용되었는데, static, obstacles_layer, inflation   
obstacles_layer의 플러그인이 Voxellayer 이다   
```yaml
plugins:
    - {name: static_layer,             type: "costmap_2d::StaticLayer"}
    - {name: obstacles_layer,    type: "costmap_2d::VoxelLayer"}
    - {name: inflation,          type: "costmap_2d::InflationLayer"}
```
static_map: true   
rolling_window: false 로 사용


예 
```yaml 
golbal_costmap:
  global_frame: map
  static_map: true  ## when using a map, then true  // false: doesn't need a map_server
  rolling_window: false
  track_unknown_space: true
  
  plugins: 
    - {name: static,         type: "costmap_2d::StaticLayer"}
    - {name: obstacles,      type: "costmap_2d::VoxelLayer"}
    - {name: inflation,      type: "costmap_2d::InflationLayer"}
```
단 여기에서 플러그인 이름을 쓰인 것은 common_costmap에서 그대로 쓰이므로 name들을 잘 매칭 시켜야함   
common_costmap parameter에서 사용하게 된다   


## common_costmap
파라미터는  
footprint  contour of the mobile base, ROS에서는 two-dimensional array 로 표현   
[x0, y0], [x1, y1], [x2, y2], [x3, y3]

robot_radius, obstacle_range 등
obstacle_range가 작으면 가까이에 있는것만 인식  
inflation_radius 작으면 장애물에 가까이 다가가게 됨 (장애물의 지나갈 수 있고 없음의 일종의 보호막?? 같은 역할)

각 layers 에 대한 parameters 등이 있다 (staic, obstacle, inflation등)  
주의할 점은 각 costmap에서 name으로 지정한 이름을 사용하면 된다 

예
```yaml
footprint: [[],[],[],[]]
footprint_padding: 0.01

robot_base_frame: base_link
update_frequency: 4.0
publish_frequency: 3.0
transform_tolerance: 0.5

resolution: 0.05

obstacle_range: 5.5
raytrace_range: 6.0

## layer definitions (global / local costmap)
static:
    map_topic: /map
    subscribe_to_updates: true

obstacles_laser:
    observation_sources: laser
    laser: {data_type: LaserScan, clearing:true, marking: true, topic: scan, inf_is_valid: true}

inflation:
    inflation_radius: 1.0
```



## recovery behaviors
2가지 방법이 있다  

Rotate Recovery  
360도 회전을 하면서 obstacle이 없는 부분을 찾을려고 한다   


Clear Costmap
장애물을 한번 인식하면 장애물이 사라져도 그대로 있게 되는데  local costmap상에는 계속 있음  

서비스 콜을 해서 사라지게 할 수 있다  
```
rosservice call /move_base/clear_costmap "{}"
```

장애물이 사라지게 된다 




## dynamin reconfigure
그래픽 툴로 파라미터들을 조정할 수 있다  
```
rosrun rqt_reconfigure rqt_reconfigure
```


## robot footprint


