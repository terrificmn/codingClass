# joint states 
joint state는 joint_state_publisher 노드를 실행해주면 알아서 joint 관련 정보를 퍼블리싱 해준다   

## yaml파일 load
yaml 파일을 만들어서 로드를 하는 경우에 대해서 알아보는 중

rosparam 태그를 이용해서 yaml 파일을 load를 해준다   

controller.launch 파일을 만들고 그 안에서 yaml파일을 로드
```xml
<rosparam command="load"
                file="$(find my_pkg)/config/controller.yaml" />
        
    <node name="my_pkg_spawner" pkg="controller_manager" type="spawner"
                output="screen"
                ns="my_controller"
                args="joint_state_controller
                        ...." />

```

자신의 패키지(특정 패키지)에서 yaml 파일을 로드할 수 있게 준비를 해주고  
노드는 controller_manager 를 사용해서 ns(네임 스페이스)를 주는데 my_controller 처럼   
지정을 해줬다면  yaml 파일에서 대표(?) 이름이 되게 된다 

> 물론 gazebo의 empty world 또는 world 파일에서 로봇이 시뮬레이션으로 구동될 수 있게  
런치파일을 구성해야한다. 당연 로봇의 urdf 파일 필요


이제 yaml 파일
```yaml
my_controller:
    joint_state_controller:
        type: joint_state_controller/JointStateController
        publish_rate: 50
```

공통적인 것은 이렇게 구성하고, 이제 추가로 joint별로 position을 더 추가해줄 수가 있다 

이 부분은 좀 더 연구를 해봐야 할 듯 하다  


[joint controller 유투부 좀 더 참고하기](https://www.youtube.com/watch?v=K09E-_2M-vQ)
