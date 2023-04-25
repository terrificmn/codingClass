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

최근 업데이트가 되면서   
Geographic coordinates, Reference-image coordinates 의 2가지 방식을 지원한다   
Geographic coordinates 는 WGS 84 latitude, longitude, UTM Zone 등으로 만들어지고,   
Reference-image coordinates 는 기존의 이미지를 사용


오른쪽 패널의 levels 탭에서 Add를 눌러서 map파일인 png 파일을 넣어준다   
- name, 등을 입력해주고   
- drawing 에서 이미지 파일을 추가해준다 

> png 파일만 지원하므로 적절히 변환한다   


그리고 가장 간단하게 add_lane 을 눌러서 포인트들을 지정하면 way point를 만들 수 있다    
> 모든 점은 연결되어야 하는 듯 하다: 하나의 경로가 시작과 끝이 만날 필요는 없지만    
2개의 경로가 있다면 서로 다른 경로가 만나는 지점이 있어야 하는 듯 하다  

연결이 안될 시에는 Select 툴을 누르고 포인트를 눌러서 Properties를 볼 수가 있는데   
시작점에 name을 start로 지정, 끝 점을 end로 지정해준다 

포인트 한 지점에 다른 한 지점으로 한 면을 클릭하면 역시 Properties를 볼 수가 있는데  
한방향으로 움직이게 하려면 bidirectional을 true로 해준다 , false 이면 한 방향으로 움직이면서 화살표가 생긴다  


Add_wall 로 벽을 추가한다. 


마지막으로 save

## 빌드
현 디렉토리에 있는 CMakeLists.txt 파일을 사용하는데   
`project(my_pkg_name)` 정도만 변경을 하면 된다.  

그리고 my_pkg 패키지를 먼저 만들어 준다  
```
cd ~/my_ws/src
ros2 pkg create --build-type ament_cmake my_pkg
```

그리고 필요한 디렉토리를 만들어 준다 
```
cd my_pkg
mkdir adapter_conifg dashboard_config include launch maps rviz_config
```

traffic-editor로 만들어진 building.yaml 파일도 위에 만들어진 maps 디렉토리에 넣어준다 
```
mv ~/my_ws/my_test_building.yaml ~/my_ws/my_pkg/maps
```

그리고 만들 my_pkg 디렉토리에 CMakeLists.txt 도 복사한다   

cmakelists 를 보면 이 부분이 실행이 rmf_building_map_tools 패키지에서 map generate를 하게 된다
```
COMMAND ros2 run rmf_building_map_tools building_map_generator gazebo ${map_path} ${output_world_path} ${output_model_dir}
    COMMAND ros2 run rmf_building_map_tools building_map_model_downloader ${map_path} -f -e ${output_model_dir}
```

이제 패키지를 build를 해야하는데 Release 버전으로 빌드를 한다 
```
cd ~/my_ws
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release 
source install/setup.bash
```


그리고 CMakeLists.txt 파일에서 command 지정된 부분이 rosrun을 실행하는데 nav graphs 를 생성하는 부분에서는 
워크스페이스안의 build  디렉토리안에 해당 패키지 디렉토리안에 만들어져 있으므로 잘 네비게이션 해서 찾아보면   
models,(모델파일들) nav_graph의 0.yaml 파일 등도 찾아 볼 수가 있다.  


## 여기가 끝이 아니고 launch file, yaml 파일 등이 필요
이렇게 하면 빌드 자체는 되는데  런치 파일, config 파일, yaml파일등 여러개가 필요하고 어느정도는 수정을 해야하는 듯 하다 

실행을 하면 역시 dashboard_config 의 파일을 제대로 못 찾는다던가... 암튼 rviz2만 뜨게 된다;;

**추후 다시 한번 수정해보자;;**

## my_pkg 
를 참고해서 
