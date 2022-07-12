# move_base 사용
wiki.ros.org/navigation/Tutorials/RobotSetup   
https://www.youtube.com/watch?v=4nctAuEaWbI  여기 14분 부터

먼저 turtlebot3를 클론  
https://github.com/ROBOTIS-GIT/turtlebot3   
https://github.com/ROBOTIS-GIT/turtlebot3_msgs   
https://github.com/ROBOTIS-GIT/turtlebot3_simulations   


catkin build

터틀봇 변수 만들기   
export TURTLEBOT3_MODEL=burger

gazebo 실행   
roslaunch turtlebot3_gazebo turtlebot3_world.launch 


다른터미널에서 slam실행   
roslaunch turtlebot_slam turtlebot3_slam.launch


gmapping 필요하면 설치
슬램이 실행되면 teleop_key를 실행해서 슬램을 해준다  


맵을 다 그렷으면 맵 저장  
map-server 필요

rosrun map_server map_saver   
현재 위치에 맵 저장 (map.pgm map.yaml)


이제 이 **map을 move_base**에 사용할 수가 있다 

amcl, move_base 필요

슬램을 한 후에 

rqt_graph를 입력해서 확인해 보면

move_base에서는 /cmd_vel 로   
gazebo 한테 토픽을 보내고 다시 gazebo는 /odom 토픽을 move_base로 보내준다 
(시뮬레이션상에서는 gazebo, 실제로는 로봇이 된다)   
그리고 move_base에서는 goal에 따라서 처리  

wiki.ros.org/navigation/Tutorials/RobotSetup 읽어보기
