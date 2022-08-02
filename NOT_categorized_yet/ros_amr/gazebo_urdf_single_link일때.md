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

