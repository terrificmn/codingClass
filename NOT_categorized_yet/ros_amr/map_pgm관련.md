튜토리얼  

here are some sources I have found, both ROS1 and ROS2, maybe they will help you:

    (ROS2, a few demonstrations to highlight a couple of simple autonomy applications)https://github.com/ros-planning/navigation2/tree/main/nav2_simple_commander

    (overall step by step guide to Nav2)https://automaticaddison.com/the-ultimate-guide-to-the-ros-2-navigation-stack/

    (traffic-editor from OpenRMF could be an example of how to export map points as a robot path)https://osrf.github.io/ros2multirobotbook/simulation.html


.yaml 파일에서 나오는 2D transformation matrix를 이용해서  
해상도와 곱해주면 m 길이가 된다  
픽셀과 해상도 곱하기  

맵과 nav관련 튜토리얼

http://edu.gaitech.hk/turtlebot/map-navigation.html


뭔가 유용한 공식??

https://github.com/tu-darmstadt-ros-pkg/mapstitch/blob/hector_mapstitch/src/mapstitch.cpp



https://answers.ros.org/question/205521/robot-coordinates-in-map/

로봇 맵 관련 

pdf 
https://www.pishrobot.com/wp-content/uploads/2021/05/ros-robot-programming-book-by-turtlebo3-developers-en.pdf


Chapter 11 _ SLAM and Navigation 325
Figure 11-9 Occupancy Grid Map
The area in the map is represented by grayscale values that range from ‘0’ to ‘255’. This value
is obtained through the posterior probability of the Bayes’ theorem, which calculates the
occupancy probability that represents the occupancy state. The occupancy probability ‘occ’ is
expressed as ‘occ = (255 - color_avg) / 255.0’. If the image is 24 bit, ‘color_avg = (grayscale value of
one cell / 0xFFFFFF x 255)’. The closer this ‘occ’ is to 1, the higher the probability that it is
occupied, and the closer to ‘0’, it is the less likely to be occupied.

When the occupancy probability is published as ROS message (nav_msgs/OccupancyGrid), it
is redefined to an integer [0 ~ 100]. An area close to ‘0’ is the free area defined as an unoccupied
area whereas ‘100’ is defined as an occupied area, and ‘-1’ is especially defined for unknown area.
In ROS, actual map is stored in ‘*.pgm’ file format(portable graymap format) and the ‘*.yaml’
file contains map information. For example, if we check out the map information(map.yaml) we
saved in Section 11.2, the image parameter defines the map file name and resolution defines the

map resolution in meters/pixel.
image: map.pgm
resolution: 0.050000
origin: [-10.000000, -10.000000, 0.000000]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.196

That is to say, each pixel can be converted to 5cm. Origin is the origin of the map, and each
value represents x, y and yaw respectively. The lower left corner of the map represents x = -10m,
y = -10m. Negate inverts black and white color. The color of each pixel is determined by the
occupancy probability. If the occupancy probability exceeds occupied threshold (occupied_
thresh), the pixel is expressed as an occupi