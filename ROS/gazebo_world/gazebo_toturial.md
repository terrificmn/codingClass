sdf format: super powerful but less compatible with ROS   
urdf+xacro format less powerful but fully compatible with ROS


The pose: That pose indicates the position of that link related to the center of the robot.  
You must specity the x y z roll pitch yaw value

The inertial: Provides the mass of the link and its mass distribution (inertial matrix)   

The collision. indicates the dimensions of the link and how the simulator physiscs  
engine shuould treat that link. that is, which shape should the physics engine use to compute collisions   
whth other objects in the simulation. The simpler the shape, the faster the simulator will run   

The visual: how that link should look in the simulator. It is used for representation purpose.


inertial의 value 태그는 kg   

collision의 geometry 태그의 xyz는 visual의 geometry태그의 xyz와 수치가 같다 



joint태그에는 각 parent link와 child link가 연결이 된다  
joint태그에는  
axis, limit, joint_properties등을 정의할 수가 있다  (바퀴인 경우)



meshes를 적용하려면  
dae파일이 있어야 한다. 이 부분은 공부가 더 필요할 듯 하다
```
<geomtry>
    <mesh filename="package://my_descrition/meshes/chasis.dae" scale=""/>
</geomtry>
```


가제보 플러그인은 robot태그가 끝나기 전에 넣어준다  

예를 들어서 differential_drive_controller 플러그인을 넣는다면  

wheelSeparation, wheelDiameter   태그는 odom을 계산하는데 쓰이므로 중요
여기에서는 leftJoint, rightJoint 등의 바퀴 joint 이름을 적어주고  odometryTocic, odometryFrame도 정해준다  
```xml
<gazebo>
    <plugin name="differential_drive_controller" filename="libgazebo_ros_diff_drive.so">
      <rosDebugLevel>Debug</rosDebugLevel>
      <publishWheelTF>True</publishWheelTF>
      <publishTf>1</publishTf>
      <publishWheelJointState>true</publishWheelJointState>
      <alwaysOn>true</alwaysOn>
      <updateRate>100.0</updateRate>
      <leftJoint>left_wheel_joint</leftJoint>
      <rightJoint>right_wheel_joint</rightJoint>
      <wheelSeparation>0.44</wheelSeparation>
      <wheelDiameter>${wheel_radius * 2}</wheelDiameter>
      <broadcastTF>1</broadcastTF>
      <wheelTorque>30</wheelTorque>
      <wheelAcceleration>1.8</wheelAcceleration>
      <commandTopic>cmd_vel</commandTopic>
      <odometryFrame>odom</odometryFrame>
      <odometryTopic>odom</odometryTopic>
      <robotBaseFrame>base_link</robotBaseFrame>
    </plugin>
  </gazebo>

</robot>
```

https://3dwarehouse.sketchup.com


위의 사이트에서 원하는 모델을 선택한 후에 Download를 받는데, Collada file로 받는다  

패캐지에서 meshes 안에 models 디렉토리를 만들고 다운받은 파일을 넣어준다  
예를 들어서 chair라는 모델을 받았다면  

meshes 안에 chiar를 위치시키고 그 안에 다시 meshes 디렉토리를 만들고 model디렉토리를 만든다 
meshes->chair->meshes->model->model.dae파일, model.config파일 위치

model.config 파일을 만들어 준다  
```xml
<?xml version="1.0"?>
<model>
    <name>my_chair</name>
    <version>1.0</version>
    <sdf version="1.5">chair.sdf</sdf>
    <author>
        <name>your name</name>
        <email>your email</email>
    </author>

    <description>
        A chair
    </description>
</model>
```

이제 sdf파일을 만들어 주는데 위의 model.config 파일에서 sdf으로 지정한 이름으로 만들어준다  

chair.sdf

```xml
<?xml version="1.0" ?>
<sdf version="1.5">
    <model name="my_chair">
        <static>true</static>
        <link name="chair_link">
            <collision name="chair_collision">
                <geometry>
                    <box>
                        <size>1.70 0.51 0.55 </size>
                    </bod>
                </geometry>
           </collision>
            <visual name="chair_mesh">
                <cast_shadows>true</cast_shadows>
                <geometry>
                    <mesh>
                        <uri>model://my_chair/meshes/model.dae</uri>
                    </mesh>
                </geometry>
            </visual>
        </link>
    </model>
</sdf>
```
static을 true로 주면  physics calculations를 disable시킨다 (immovable)  
false로 해주면 로봇이 의자에 부딪치면 physics에 의해서 계산이 되어서 의자가 움직이거나 한다  
true면 시뮬레이션에서 컴퓨팅하는 것을 줄여주는 효과가 있다  

urdf 만든는 것 처럼 link가 필요하다   
collision, visual 태그가 필요하고 visual태그의 geometry안에 mesh uri를 지정해준다    
크기는 아마도 모델의 실제크기를 봐야지 아는 것인지 그냥 알아서 지정하는 것인지 모르겠음??  
여기에서는 mesh부분의 uri에 model.dae 파일을 지정해준다  

collision에서는 가제보에서는 보이지는 않지만 물건이 부딪칠 때 시뮬레이션 안에서 크기를 지정해준다  


## world 파일만들기
world 디렉토리를 만들고  
예를 들어 my_world.world 파일을 만든다면  
```xml
<?xml version="1.0" ?>
<sdf version="1.5">
    <world name="my_world">
        <include> <!-- add in a light source -->
            <uri>model://sun</uri>
        </include>
        <include>  <!-- 모델 -->
            <uri>model://my_chair</uri>
            <name>simple_chair</name>
            <pose>0 0 1.5 0 0 0</pose>
        </include>
    </world>
</sdf>
```
이제 world파일안에 model 만들어 놓은 것을 지정해준다  

launch 파일을 만들고 내용은 아래의 예를 참고한다  
```xml
<launch>
    <inculde file="$(find gazebo_ros)/launch/empty_world.launch">
        <arg name="world_name" value="$(find my_pkg_name)/worlds/my_world.world" />
    </include>
</launch>
```

collision은 지정한 만큼 의자가 제대로 위치하지 않을 수 있다   
(아마 chair.sdf 의 collision 태그의 다시 조정해준다)

여기에서 하는 방법이 나와 있다고 함
Download a 3D model and load it into a Gazebo simulation (유투브 검색)  을 참고한다 

https://www.youtube.com/watch?v=aP4sDyrRzpU