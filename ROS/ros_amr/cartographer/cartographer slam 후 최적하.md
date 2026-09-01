## 슬램 먼저

슬램을 하기 전에 bag 파일을 만들어 주고 바로 시작하면 된다  
```
rosbag record -a
```

기본적으로 bag file은 파일명을 지정 안 하면 날짜-시간.bag 파일로 된다 

단, 카메라 노드가 켜져 있다면 잠시 런치파일에서 주석처리를 해준다   
> 다 그런것은 아니겠지만, bag파일이 용량이 엄청 크고, 압축(?) 에서 에러 발생한다 

이제 cartographer 을 사용해서 slam을 한 후에 모든 slam 맵핑이 끝나면...   

map_server 패키지를 이용해서 pgm 파일로 맵 파일을 저장을 한 번 해도 된다
```
rosrun map_server map_saver -f my_cartographer
```

이제 cartographer 노드와 bag파일 저장 하던 것을 ^C 를 눌러서 종료해준다 


## offline_backpack_2d 런치 파일 사용
offline_backpack_2d.launch 파일을 이용해서 실행을 한 후 bag파일을 지정해주면 된다 
```
roslaunch cartographer offline_lidarodom_2d.launch bag_filenames:=/home/username/try1_cartographer.bag
```

런치파일 내용 예:)
```xml
<launch>
  <arg name="bag_filenames"/>
  <arg name="no_rviz" default="false"/>
  <arg name="rviz_config" default="$(find cartographer_ros)/configuration_files/demo_2d.rviz"/>
  <!--<arg name="configuration_directory" default="$(find cartographer_ros)/configuration_files"/>
  <arg name="configuration_basenames" default="backpack_2d.lua"/> 원래 기본 설정 값들 -->
  <arg name="configuration_directory" default="$(find 패키지명)/config"/>
  <arg name="configuration_basenames" default="custom_lua.lua"/> <!-- 기본값은 위에 주석 참고 -->
  <arg name="urdf_filenames" default="$(find 패키지명)/urdf/urdf파일_basic.urdf"/>
  <arg name="launch_prefix" default=""/>

  <remap from="echoes" to="horizontal_laser_2d"/>
  <include file="$(find cartographer_ros)/launch/offline_node.launch">
    <arg name="bag_filenames" value="$(arg bag_filenames)"/>
    <arg name="no_rviz" value="$(arg no_rviz)"/>
    <arg name="rviz_config" value="$(arg rviz_config)"/>
    <arg name="configuration_directory" value="$(arg configuration_directory)"/>
    <arg name="configuration_basenames" value="$(arg configuration_basenames)"/>
    <arg name="urdf_filenames" value="$(arg urdf_filenames)"/>
    <arg name="launch_prefix" value="$(arg launch_prefix)"/>
  </include>
</launch>

```

> 위의 offline_backpack_2d.launch 파일은 조금 변형해서 사용   
   아래의 offline_node.launch 파일을 그대로 사용함

이렇게 실행을 하게 되면 맵 최적화를 해주고나서, pbstream 으로 만들어 준다 (bag파일과 같은 이름으로 만들어준다)

또는 런치파일의 arg를 이용해서 파일 경로를 지정해줘도 된다   
```xml
<launch>
  <arg name="bag_filenames" default="/home/username/boxbag.bag" />
  <arg name="no_rviz" default="false"/>
  ... 생략
```
이제 런치파일만 실행해주면 됨




