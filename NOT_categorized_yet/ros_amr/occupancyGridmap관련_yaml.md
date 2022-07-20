맵을 저장  
```
rosrun map_server map_saver -f map_file_name
```

## map_server 패키지를 이용해서 map을 만들게 되면  
yaml.파일이 만들어지는데 6개의 필드 내용을 살펴보면  

Image: Name of the file containing the image of the generated Map (pgm파일)   

resolution: Resulution of the map (in meters/pixel)

origin: Coordinates of teh lower-left pixel in the map. Tahis coordinates are given  
in 2D (x,y). The third value indicates the rotation. If there's no rotation,   
the value will be 0.

occupied_thresh: Pixels which have a value greater than this value will be considered   
as a completely occupied zone.  

free_thresh: Pixel which have a value smaller than this value will be considered    
as a completely free zone.  

negate: Inverts the colours of the map. By default, white means completely free and    
black means completely occupied.  



# map을 사용하려면  
map_metadata, map이 필요하다   

map_metadata는 (nav_msgs/MapMetaData) : Provides the map metadata through this topic   

map (nav_msgs/OccupancyGrid): Provides the map occupancy data through this topic


맵을 띄우려면  
```
rosrun map_server map_server map_file.yaml
```

맵이 실행이 되면  
rostopic echo /map_metadata를 통해서 정보를 볼 수 있다   

rostopic echo /map 을 하게 되면  -1, -1, 0, 100 이런 숫자가 표현되는 것을 알 수가 있다  

0은 white - free zone   
100은 black - occupied zone   
-1은 gray - unknown zone


## 맵 서비스 
```
rosservice call /static_map "{}"  
```
를 하게되면 map_metadata와 map 을 둘 다 보여준다   

처음에 맵을 만들게 되면 static map이 된다. 변경되지 않고 그대로 있는다.  
> this means that the map will stay as it was when you created it. So when you created a map,   
it will capture the environment as it is at the exact memonet that the mapping process is being performed.   
If for any reason, the environment changes in the future, these changes won't appear on the map,   
hence it won't be valid anymore (or it won't correspond to the actual environment)

2d 맵임

## 맵을 저장하려면 
hardware 로 보면 좋은 laser scan이 있어야 하고 좋은 odometry data가 필요하다   


## transforms

need to set a transform between the laser and the robot base, and add it to the transform tree.


in order to able to use the laser data, we need to tell the robot WHERE (position and orientation)   
this laser is mounted in the robot.  
This is what is called a transform between frames.


레이저가 어떤 물체를 발견했을 때 로봇이 어디에 있느지 중요하다 
if you detect an obstacle with the laser at 3 cm in the front, this means that it is 3 cm from the laser,   
not from the center of the robot (that is usually called the /base_link)

To know the distance from the center of the robot, you need to transform the 3 cm  
from the /laser_frame to the /base_link frame   
(which is actually what the obstacle avoidance needs to know, it is,   
what is the distance of the center of the robot to the obstacle   

         |--| <--- base_laser  
         |  |     
|------------|   
|            |   
| base_link  |   
|____________|   


위의 base_laser와 base_link 와의 관게를 robot한테 알려주는것이 transform 이다   
This realtionship betwwen the position of the laser and the base of the robot is known   
in ROS as the Rrnasform between the laser and the robot.


https://www.youtube.com/watch?v=mYwIu4OVMR8  
37
