# Open RMF
- osrf 에서 만든 open source, robot   
- Robot Middleware 프로그램   
- 서로 다른 회사의 로봇, 각기 다른 종류의 로봇을 Open-rmf 프로그램으로 계획 및 제어

> fleet_adapter 라는 개념으로 각기 다른 회사들의 로봇들을 제어하는 fleet_adapter가 된다. 

1. open-rmf 깃허브로 해보기  (demo 많음)  
2. ~~docker ros2 로 만들어보기~~ : docker-ros: humble branch 참고

mapping을 하면 pgm파일이 만들어지는 png 파일로 변환해서 사용한다   
> pgm 파일 말고 png 파일 지원함

다운받은 rosject를 참고(structure를 참고)

## traffic-editor 
터미널에서 traffic-editor 를 실행할 수가 있다. 주행 경로, 벽 등을 만들 수 있는 프로그램  

building->new 로 새로운 파일을 만들고   
오른쪽 패널에서 add를 눌러서 map파일인 png 파일을 넣어준다   

그리고 가장 간단하게 add_lane 을 눌러서 포인트들을 지정하면 way point를 만들 수 있다  
(모든 점은 연결되어야 하는 듯 하다)

마지막으로 save

이제 starbots_rmf 패키지를 build를 해야하는데  
CMakeLists.txt 파일에서 command 지정된 부분이 rosrun을 실행하는데   
nav graphs 를 생성하는 부분인  
rmf_building_map_tools 에서 map_path를 잘 맞춰준다   


colcon build -- release 빌드로 해준다   (옵션은 찾아서;;)

launch 파일을 참고해서  barista_rmf_schedule.launch.xml 
실행은 rmf_schedule.launch.xml 이고 내용은 더 연구해야함  



