1. 먼저 empty map이 필요하다   
왜냐하면 navigation package (robot_localization) 그렇게 원함  
map 디렉토리를 만들고 map.pgd, map.yaml 파일을 만들어 준다  

2. 그리고 이 맵을 실행을 해줄 런치파일을 만든다  
map_server가 필요하다  
```
sudo apt install ros-melodic-map-server
```


3. navsat 노드를 이용해서 gps 신호를 converting 해주는데 런치파일을 작성한다   
여기에는 navsat 노드에 필요한 parameter를 정의한다   
robot_localization 패키지 필요하다. 이 패키지를 설치하기 위해서 의존성 패키지 먼저 설치해주기       
--> robot_localization은 geographic_msgs가 필요함   
```
sudo apt install ros-melodic-geographic-msgs
sudo apt install libgeographic-dev
```

4. config 관련해서 yaml파일을 만들고 config관련해서 패키지 만듬
이제 robot_localization 패키지 필요    
```
git clone -b melodic-devel https://github.com/cra-ros-pkg/robot_localization.git
```

그리고 catkin build 해주기


5. ekf_localization.launch 파일에서  
ekf_localization 노드를 이용해서 (robot_localization패키지)  
robot odometry, robot IMU, GPS odometry를 이용하게 된다 (fuse하게 됨)   
여기에서는 gps_localization.config.yaml 파일이 필요하다  



6. hector gps plugin을 사용하기 위해서 apt install 
```
sudo apt install ros-melodic-hector-gazebo-plugins
```








