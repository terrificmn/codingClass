[ WARN] [1658748544.215231878]: The robot's start position is off the global costmap. Planning will always fail, are you sure the robot has been properly localized?


The origin for the sensor at (0.31, -0.00) is out of map bounds. So, the costmap cannot raytrace for it.

global의 costmap을 사용하지 않고 rolling window만 사용하겠다는 것인데  센서 워닝만 나온다   


global_costmap에서는 
static_map: true  
rolling_window: false

local_costmap에서는   
static_map: false    
rolling_window: true  

rolling_window 파라미터 설명
~<name>/rolling_window (bool, default: false) Whether or not to use a rolling window version of the costmap. If the static_map parameter is set to true, this parameter must be set to false.

"Rolling window" means that you do not use the costmap to represent your complete environment, but only to represent your local surroundings (e.g. 5m x 5m around your robot). The costmap will then move along with your robot and will be updated by incoming sensor data.



