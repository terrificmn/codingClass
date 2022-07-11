

# summit_xl_common 패키지
summit_xl_common 설치하는데에는 실패했지만, 의존성 관련 해결해주면 build까지는 문제 없음  
GPS 관련해서 참고하자 


의존성 패키지 필요
ros-melodic-velocity-controllers  
sudo apt install ros-melodic-geographic-msgs  
https://github.com/RobotnikAutomation/robotnik_msgs.git   
https://github.com/RobotnikAutomation/robotnik_sensors.git   
git clone -b melodic-devel https://github.com/ros-teleop/twist_mux.git   
sudo apt-get install ros-melodic-mavros ros-melodic-mavros-extras  
sudo apt install ros-melodic-robot-localization  
sudo apt install ros-melodic-gmapping  
sudo apt install ros-melodic-map-server   
sudo apt install ros-melodic-amcl


# summit_xl_sim 패키지
시뮬레이션 gazebo  
git clone https://github.com/RobotnikAutomation/summit_xl_sim.git










 Could not find a package configuration file provided by "twist_mux" with
  any of the following names:

Could not find a package configuration file provided by "robotnik_sensors"
  with any of the following names:

  Could not find a package configuration file provided by "robotnik_msgs"
  with any of the following names:

이렇게 나오는 것을   

