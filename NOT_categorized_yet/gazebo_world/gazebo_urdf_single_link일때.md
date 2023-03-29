# from urdf to sdf
아직 테스트를 다 끝내지는 못했지만 각 joint에 preserveFixedJoint 를 true를 주면 링크가 하나로 되지 않고 기존 urdf 파일의 링크 하나씩 연결된다  

launch파일에서는 
```
<param name="robot_description"
        command="xacro '$(find md_description)/urdf/my_robot.xacro'" />

  <param name="use_gui" value="True" />
```
식으로 연다  

또는 urdf에서 sdf파일로 변경시키려면 
```
gz sdf -p my_robot.urdf > my_robot.sdf
```
sdf파일 변경 관련해서는   
https://nu-msr.github.io/me495_site/lecture10_sdf_gazebo.html   
  
여기를 참고~  
아직 테스트가 덜 됨

```
<gazebo reference="horizontal_laser_joint">
    <turnGravityOff>false</turnGravityOff>
    <preserveFixedJoint>true</preserveFixedJoint>
  </gazebo>
  <gazebo reference="camera_link_joint">
    <turnGravityOff>false</turnGravityOff>
    <preserveFixedJoint>true</preserveFixedJoint>
  </gazebo>
```

preseveFixedJoint true로 사용하면 안되는 듯 하다   
모델이 joint별로 마구마구 떨리는 현상 발생  


## urdf -> sdf 변경 시
일단 위의 명령어 처럼 사용하면 잘 된다.  
일단 기존의 urdf에서 xacro를 사용했다면 빼줘야 한다. xacro가 있다면 에러가 발생한다 

만약 **단순한 움직임**을 원한다면 (기존의 모델 등에 inertial, inertia 등이 들어가 있다면)  
해당 부분을 주석 처리하고 visual에 있는 pose로 대체 

예
```xml
 <link name='wheel_link'>
    <pose relative_to='wheel_joint'>0 0 0 0 -0 0</pose>
    <!-- <inertial> -->
    <!-- <pose>0 0 0 0 -0 0</pose> -->
    <!-- <mass>1.15845</mass>
    <inertia>
        <ixx>0.00208358</ixx>
        <ixy>-9.04606e-11</ixy>
        <ixz>-1.0452e-11</ixz>
        <iyy>0.00346787</iyy>
        <iyz>1.2456e-07</iyz>
        <izz>0.00208354</izz>
    </inertia>
    </inertial> -->
    <pose>0.137 0.185 0.052 0 -0 0</pose>
    <collision name='wheel_link_collision'>
    <pose>0.137 0.185 0.052 0 -0 0</pose>
    <geometry>
        <mesh>
        <scale>1 1 1</scale>
        <uri>model://model_name/meshes/wheel_link.STL</uri>
        </mesh>
    </geometry>
    </collision>
    <visual name='wheel_link_visual'>
    <pose>0.137 0.185 0.052 0 -0 0</pose>
    <geometry>
        <mesh>
        <scale>1 1 1</scale>
        <uri>model://model_name/meshes/wheel_link.STL</uri>
        </mesh>
    </geometry>
    </visual>
</link>
```

