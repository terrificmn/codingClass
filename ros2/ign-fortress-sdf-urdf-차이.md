# fortress SDF and URDF
ros2 에서 특히  joint state pulbisher, robot state publisher 등은 urdf 파일을 읽어서  
robot description 파라미터로 이용하는데  

sdf 파일을 열어도 잘 작동하는 편이지만 특정 joint의 type을 해석하지 못하으로 (SDF) 일 경우   
위의 패키지(joint state publisher 등..) 이 종료되게 되어   
rviz2 상에서 robot description 이 완성이 되지 못해서 안 나오는 경우가 있다.  

```
stauts Error  
No transform from [left_wheel] to [base_link]  
```

특히 sdf 에서는 revolute 를 사용하지만, urdf 에서는 continuous 를 사용  
sdf 에서는 ball (캐스터 휠 따위), urdf 에서는 해석 못함. 


그래서 gazebo world는 SDF 파일을 통해서 열고   
robot description 는 urdf 로 열어서 rviz에서도 잘 가능하게 해주는데    

`ign sdf` 명령을 통해서 변경 가능. 먼저 model.sdf 파일이 있는 곳으로 이동
```
cd ~/my_pkg/models/my_model
ign sdf -p  model.sdf > robot.urdf
```

자동으로 sdf 파일에서  urdf 파일로 만들어주지만 위에서 언급한 type은 전혀 바꿔주지 못하므로   

sdf에서 revolute 로 되어 있는 link는 continuous   
sdf에서 ball 은 continuous  로 변경

```xml
<!-- in a urdf file... -->
<joint name='wheel_link_joint' type='continuous'>
    <parent>base_link<parent>
    <child>wheel_link<child>
    <axis>
        <xyz>0 0 -1</xyz>
        <limit>
            <lower>-1.79769e+308</lower>
            <upper>1.79769e+308</upper>
        </limit>
    </axis>
</joint>
```
> continuous 는 axis가 필요하므로 limit , xyz 를 지정해줘야 한다.  


## urdf 와 sdf 차지
urdf 는 특정 태그 안에서 속성으로 많이 넣어주는 편이고   
sdf 는 특정 태그 안에 sub 태그로 다 부여하는 편  

urdf 예
```xml
<joint name="joint1" type="continuous">
    <parent link="base_link"/>
    <child link=-"child_link"/>
    <origin xyz="0 0 0" rpy="0 0 0"/>
    <axis xyz="0 0 1"/>
    <limit effort="50" velocity="1.0" lower="-1.57" upper="1.57"/>
</joint>
```

sdf 예
```xml
<joint name="joint1" type="revolute">
    <parent>base_link</parent>
    <child>child_link</child>
    <axis>
        <xyz>0 0 1</xyz>
        <limit>
            <lower>-1.57</lower>
            <upper>1.57</upper>
        </limit>
    </axis>
</joint>
```

이상하게도 urdf 에서는 revolute가 적용이 안됨. 
