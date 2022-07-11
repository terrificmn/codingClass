urdf 파일을 확인은   
sudo apt install liburdfdom-tools   

설치 후 확인은 아래 명령어로
```
check_urdf ./test_urdf.urdf
```

이상이 없다면 아래처럼 나온다
```
robot name is: testrobot
---------- Successfully Parsed XML ---------------
root Link: base_link has 4 child(ren)
    child(1):  left_wheel_link
    child(2):  rear_left_wheel_link
    child(3):  rear_right_wheel_link
    child(4):  right_wheel_link

```


rviz에서 회전 등을 잘 되는지 볼 수 있다.
```
sudo apt install ros-melodic-joint-state-publisher-gui
```

urdf에서 xacro로 사용하기   
아래처럼 robot 태그에 xmlns 을 적어주고  
property를 이용해서 변수 처럼 사용할 수가 있다.  
``` xml
<robot xmlns:xacro="http://www.ros.org/wiki/xacro" name="md_v100">
<xacro:property name="base_link_size" value="1.5 1.0 0.2">

    <link name="base_link">
        <visual>
            <geometry>
                <box size="${base_link_size}"/>
            </geometry>
            <origin rpy="0 0 0" xyz="0 0 0"/>
        </visual>
    </link>
```


