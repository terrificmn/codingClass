xmin: -50.0  
ymin: -50.0  
xmax: 50.0  
ymax: 50.0 
delta: 0.05  

관련 파라미터 들이 사이즈 관련 파라미터   
delta는 해상도가 되겠다 (기본값 0.05, in meters per occupancy grid block)

> 0.05로 셋팅을 했을 경우에 grid에서 하나의 square 는 0.05 meters 각 사이드가 5cm 가 된다  


xmin, ymin 의 default: -100.0 이고 xmax, ymax는 디폴트는 100.0 (float)  

map->odom 으로 tf Transforms 발행해줌    
the current estimate of the robot's pose within the map frame   


