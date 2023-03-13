
gazebo 플러그 인  먼저 설치할 ...  

sudo apt install ros-melodic-gazebo-ros-control   
sudo apt install ros-melodic-diff-drive-controller   



참고 사이트:  https://ros-mobile-robots.com/diffbot_gazebo/  



## gazebo_model_path
gazebo로 시뮬레이션을 열려면 world 파일이 있어야 하는데, 이 world 파일이 바로 model들이 모여있는 파일이라고 생각하면 된다   

worlds, models 디렉토리가 있는데 
models에는 각 모델들의 model.sdf, model.config 및 meshes 파일들로 되어 있고   
worlds 에서 world파일은 이 모델들이 모여 있게 되는 것. 

> gazebo의 building editor 에서 만들 수 있다   


이제 launch 파일에서 world파일을 실행할 수 있게 구성하는데.. 

그 전에 CMakeLists.txt, package.xml 에서 패키지 관련 정리할 게 있음
먼저 CMakeLists 에서는 find_package()를 통해서 gazebo_ros를 입력해주고  

대충
```
find_package(catkin REQUIRED COMPONENTS
    gazebo_ros    
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES s100_gazebo
    CATKIN_DEPENDS gazebo_ros
    DEPENDS GAZEBO
)
```

그리고 package.xml 에서는 
```xml
<buildtool_depend>catkin</buildtool_depend>
    <build_depend>gazebo_ros</build_depend>
    <exec_depend>gazebo_ros</exec_depend>

  <!-- The export tag contains other, unspecified, tags -->
  <export>
    <gazebo_ros gazebo_model_path="${prefix}/models" />
    <gazebo_ros plugin_path="${prefix}/lib" gazebo_media_path="${prefix}" />
  </export>
```
의존성과  export를 해주는데  
export 같은 경우에는 $prefix 현재의 프로젝트 디렉토리의 위치가 되고, 그 안의 models 디렉토리를   
gazebo_model_path 로 사용할 수 있게 하는데, 내부적으로 작동하는 것 같다.    

왜냐하면 export로 GAZEBO_MODEL_PATH를 등록할 수가 있는데, 이 때에는 패키지의 전체 절대 경로를 작성을 해주고  
echo를 통해서 잘 등록이 되었는지 알 수 가 있는데  

export 태그에 넣어주면 일단 환경변수로 직접 만들어 지는 것은 아닌것 같다.  
대신 roslaunch 로 실행을 할 때 gazebo에 path가 등록이 되어서 월드 화면이 잘 나옴

> 만약 안된다면 주로 sdf 등의 파일 문제 일 수 있음

> 모델 패스는 잘 등록이 되어서 gazebo에서 실행이 되나, world파일 같은 경우는 GAZEBO_RESOURCE_PATH 환경 변수에  
등록을 해주는데 실패함;; world파일은 등록이 안되는 듯 하다


환경 변수로 등록하려면   
```
export GAZEBO_MODEL_PATH=$HOME/catkin_ws/src/my패키지명/models
export GAZEBO_RESOURCE_PATH=$HOME/catkin_ws/src/my패키지명/worlds
```
임시적으로 사용할 경우에는 위처럼 하고, 아니면 .bashrc 파일에 저장해준다 

한번 gazebo에서 파일 경로가 인식이 되면 모델을 잘 불러오는 것 같다. gazebo의 insert 탭에서 모델 추가

