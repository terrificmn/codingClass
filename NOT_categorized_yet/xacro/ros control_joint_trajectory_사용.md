# Joint Trajectory
Joint 을 하나씩 yaml 파일에 파라미터로 만든 후에 load 후에 실행을 할 수도 있지만   

trajectory 로 만들어서 사용하는 방법도 있다  

먼저 yaml 파일을 로드 할 수 있도록 trajectory.yaml 파일을 만들어준다   

> 이때 joint_state_controller는 공통으로 들어간다. (그냥 joint로만 yaml 구성할 경우에도)    
controller를 하나 만들어 준 후에 그 컨트롤러에 각 joint를 더 넣어주게 된다 

예
```yaml
my_robot:
  # publish all joint states
  joint_state_controller:
    type: joint_state_controller/JointStateController
    publish_rate: 30
  
  ## many joints can be defined here
  my_controller:
    type: position_controllers/JointTrajectoryController
    joints:
      - joint1
      - joint2
      - joint3
      - joint4

    # parmmeters
    constraints:
      goal_time: 0.6
      stopped_velolcity_tolerance: 0.05
      joint1: { trajectory: 0.1, goal: 0.1 }
      joint2: { trajectory: 0.1, goal: 0.1 }
      joint3: { trajectory: 0.1, goal: 0.1 }
      joint4: { trajectory: 0.1, goal: 0.1 }

    stop_trajectory_duration: 0.5
    state_publish_rate: 30
    action_monitor_rate: 30

```

my_controller를 만들고 그 안의 로봇 팔의 joint를 넣어주게 되고   
type은 `position_controllers/JointTrajectoryController` 를 사용   

나머지는 파라미터 이며    
[자세한 정보는 wiki.ros 여기 참고](http://wiki.ros.org/joint_trajectory_controller)


controller 가 정의된  yaml파일을 로드 시키기 위해서 rosparam 으로 로드를 시켜주고   
controller_manager 패키지의 controller_spawner 노드로 실행을 해주는데   

각 컨트롤러를 각각 만들어서 args로 넣어줬던 것과는 다르게 이번에는 my_controller 한개만 추가를 해주면 된다   

```xml
 <rosparam command="load"
                file="$(find my_pkg)/config/trajectory.yaml" />
    <!-- load the controller -->
    <node name="controller_spawner" pkg="controller_manager" type="spawner"
                respawn="false" output="screen"
                ns="my_robot"
                args="joint_state_controller
                        my_controller" />
```


## rqt 플러그인 사용하기
rqt 플러그인을 사용해서 각 joint를 컨트롤 할 수가 있는데 먼저 플러그인을 설치해줘야 함

```
sudo apt install ros-noetic-rqt-joint-trajectory-controller
```

이제 터미널에 `rqt` 를 실행한 후에   
Plugins->Robot Tools->Joint trajectory controller를 선택해주면 된다   

또는 rosrun 으로 rqt_joint_trajecotry_controller를 실행할 수도 있다 

```
 rosrun rqt_joint_trajectory_controller rqt_joint_trajectory_controller 
```


