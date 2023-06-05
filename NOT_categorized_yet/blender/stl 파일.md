# std to stl
ROS 에서 urdf 에서 mesh를 표현할 수 있는 파일은 .dae, .stl 파일이 있는데   

만약 stp 파일이 있다면, stl 파일로 변환을 할 수가 있는데  (std 파일은 cad 관련 파일인 듯 하다)
stl 파일은 free CAD 등을 이용해서 변환을 할 수가 있다.   
일단 해당 xyz rpy 위치까지는 나오지 않는 듯 하다. 단순히 mesh 만 변환 할 수가 있는 듯 한데   

한번에 통으로 변환하면 모델은 나오기는 하지만 크기가 굉장히 크게 나오는 것 같고  
링크별로 필요하기 때문에 통째로 변환하면 안될 듯 하고, 하나 링크씩 변환을 해야하는 듯 하다   

> 단순히 mesh만 얻을려면 유용하지만   
다만, urdf 의 xyz rpy 위치를 알아야 하는 문제가 있고   

그래서 해당 모델링 파일에서 dae 파일이 있는지 알아보거나 전체 urdf 파일이 있는지 검색을 잘 해봐야 할 듯  


어쨋든 stl 파일도 urdf 에서는 visual 부분에 넣어주면 된다  

예
```xml
<?xml version="1.0" ?>

<robot name="my_arm" xmlns:xacro="http://ros.org/wiki/xacro">
    <link name="arm_link">
        <visual>
            <origin xyz="0 0 0" />
            <geometry>
                <mesh filename="package://my_pkg/meshes/arm_file.stl" />
            </geometry>
        </visual>
        <collision>
            <geometry>
                <mesh filename="package://my_pkg/meshes/arm_file.stl" />
            </geometry>
        </collision>
    </link>
</robot>
```
