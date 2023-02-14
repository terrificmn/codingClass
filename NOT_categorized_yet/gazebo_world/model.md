
ros패키지 하나 구성을 한 다음에  
models 디레토리를 만들고 그 안에 모델 디렉토리를 또 만들어 준다   
예를 들어 bicycle_01 이라고 한다면    그 안에  
materials, meshes 디렉토리와 model.config, model.sdf 파일이 위치하게 된다   

```
pkg1
 |---models
 |    |---materials
 |    |---meshes
 |    |model.config
 |    |model.sdf
 |---worlds
 |    |examle.world
 |CMakeLists.txt
 |package.xml
 
```

패키안에 CMakeLists.txt 예
```
cmake_minimum_required(VERSION 2.8.3)
project(my_examle_world)

find_package(catkin REQUIRED COMPONENTS
	gazebo_ros
)

catkin_package()

install(DIRECTORY launch models worlds
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
```

gazebo 프로그램안에서 Building Editor를 이용해서 만들면   (materails, meshes 디렉토리는 생성 안됨)

/home/userhome디렉토리/building_editor_models/  안에 생기는데   
한번 gazebo에서 인식이 되었으면 다음부터는 왼쪽메뉴의 insert 탭을 통해서 추가해주면 되나  

모델이 없었던 곳에서 시작할 때는 model 파일을 다운 받아서 같은 위치에 하던가   
gazebo상의 왼쪽메뉴 insert메뉴에서 Add Path를 통해서 인식시키면 될 듯 하다   


