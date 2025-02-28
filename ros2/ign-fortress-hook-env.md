# fortress hook env 설정하기
모델 sdf 파일에서 특정 파일 위치의 모델위치를 설정 지정할 경우에  

예
```xml
<link name="wheel_link">
<visual name="visual_wheel_link">
    <geometry>
        <mesh>
        <scale>1 1 1</scale>
        <uri>package://my_pkg/models/my_model/meshes/my_model.STL</uri>
        </mesh>
    </geometry>
<!-- 이하 생략 -->
```

이때 해당 package의 위치를 잘 불러오려면 환경 변수 설정이 필요  
> 아니면 절대 경로를 적어준다.


## CMakeLists.txt 
먼저 관련된 프로그램을  ros의 자신의 workspace 이하의 install/my_pkg/ 이하에 install 하기 위해서   
```c
# Install project launch files
install(
  DIRECTORY
    launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

# Install project configuration files
install(
  DIRECTORY
    config/
  DESTINATION share/${PROJECT_NAME}/config
)

install(
  DIRECTORY
    models/
  DESTINATION share/${PROJECT_NAME}/models
)

install(
  DIRECTORY
    worlds/
  DESTINATION share/${PROJECT_NAME}/worlds
)
```
등을 추가해주고  


그 아래에 ament_environment_hooks 을 넣어준다.
```
ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/hooks/${PROJECT_NAME}.dsv.in")
ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/hooks/${PROJECT_NAME}.sh.in")
```


## hooks 디렉토리 이하 파일 생성
그리고 자신의 패키지 디렉토리 이하에 /hooks 이하에 패키지명.dsv.in,  패키지명.sh.in 을 만들어 주고  


dsv.in 에는  
```
prepend-non-duplicate;IGN_GAZEBO_RESOURCE_PATH;share;@CMAKE_INSTALL_PREFIX@/share;
```

sh.in 에는
```
ament_prepend_unique_value IGN_GAZEBO_RESOURCE_PATH "$AMENT_CURRENT_PREFIX/share/@PROJECT_NAME@/models"
```

> 여기에는 model 들이 있는 경로를 지정해준다. ros2 면 symlink-install 을 통해서 빌드를 할 때 install이 되어 지므로   
우선 자신의 프로젝트의 model들이 있는 경로를 지정  

잘 안될 경우에는 dsv.in 에다가 둘 다 넣어 버린다.
```
prepend-non-duplicate;IGN_GAZEBO_RESOURCE_PATH;share;@CMAKE_INSTALL_PREFIX@/share;$AMENT_CURRENT_PREFIX/share/@PROJECT_NAME@/models
```


## colcon build 빌드
빌드 이후 symlink-install은 넣어주자 
echo로 확인
```
echo $IGN_GAZEBO_RESOURCE_PATH
```

