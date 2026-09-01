```
[ WARN] [1658748544.215231878]: The robot's start position is off the global costmap. Planning will always fail, are you sure the robot has been properly localized?


The origin for the sensor at (0.31, -0.00) is out of map bounds. So, the costmap cannot raytrace for it.
```

global의 costmap은 static map을 사용해야하는데~ gps를 사용할 때는 일단 false를 사용... 아직 정확하지 않다. 테스트 중    

rolling window만 사용하겠다는 것인데  센서 워닝만 나온다   


global_costmap에서는 
static_map: true  
rolling_window: false

local_costmap에서는   
static_map: false    
rolling_window: true  

식으로 사용해주고~  
width:  
height;  
각각 값을 넣어준다  

맵파일의 map.yaml 파일도 origin의 위치를 같은 값으로 설정해본다  






rolling_window 파라미터 설명
~<name>/rolling_window (bool, default: false) Whether or not to use a rolling window version of the costmap. If the static_map parameter is set to true, this parameter must be set to false.

"Rolling window" means that you do not use the costmap to represent your complete environment, but only to represent your local surroundings (e.g. 5m x 5m around your robot). The costmap will then move along with your robot and will be updated by incoming sensor data.



