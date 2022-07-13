실제 로봇을 구동하려고 로봇 모터, 라이다, 카메라 등을 가동을 하면  
rviz 상에서 제대로 데이터를 볼 수가 없다  

No tf data.  Actual error: Fixed Frame [map] does not exist   

이런식으로 나오는데  
그래서 예를 들어서 rplidar의 런치파일을 실행하게 되면 라이다가 구동이 되게 되고   
이제 rviz에서 laser_scan을 보려고 하면 위의 메세지가 반복되며 화면에 데이터가 표시되지 않는다  

이게 실제 로봇 frame 마다 서로 위치를 알 수 있게 해주는 transform 이 있어야 하는데(?)  
그게 없어서 그런것이라고 하는 듯 하다.  

그래서 robot의 odom 데이터를 활용할 수도 있고   

이 때 주의 해야할 것은 frame 과 topic은 다르기 때문에 혼동하지 말아야 한다. 


## 임시로 할 때 static_transform_publisher 를 이용한다   
런치파일을 만들어서 노드르 실행해준다 
```xml
<launch>
    <node pkg="tf2_ros" type="static_transform_publisher" name="link_rplidar_tf" output="screen"
        args="0 0 0 0 0 0 base_link laser" />
</launch>
```

이렇게 되면 laser 프레임이 tf로 확인이 된다  

이제 rviz에서 frame을 laser로 바꿔주면 라이다가 잘 나오게 된다  

## robot 파일 이용하기  
아예 로봇 모델을 만든다  urdf 파일   
link 태그로 base_footprint, base_link, imu_link, laser  등의 프레임 (link 가 프레임 id가 된다)  
joint 태그로 link들을 묶어 준다   

이제 이렇게 만들어진 robot.urdf 파일로 노드를 실행해준다   

```xml
<?xml version="1.0"?>
<launch>
    <arg name="model" />
    <param name="robot_description" textfile="$(find md_description)/urdf/md_robot.urdf" />
    <node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher"/>
    <node name="rviz" pkg="rviz" type="rviz" args="-d $(find md_description)/urdf.rviz" required="true"/>
</launch>
```

이렇게 해서 런치파일을 실행하게 되면은 로봇 md_robot.urdf 를 이용해서 robot_state_publisher가 tf를 만들어준다

xacro 파일로 만들었다면 파라미터를 조금 다르게 쓴다
```xml
<param name="robot_description" command="$(find xacro)/xacro --inorder '$(find md_description)/urdf/md_v100_with_gps.xacro'" />
```

이제 rviz에서 frame을 base_link 로 바꿔주면 라이다 데이터가 잘 표시 된다 


여하튼 frame id를 지정해주는 곳이 많이 있으므로 (런치파일 등에서)  
내 로봇과 같은 프레임 아이디를 지정해줘야한다  
