# ros_gz_bridge QOS 셋팅
런치 파일에서 쉽게 설정 가능 

```py
# Bridge ROS topics and Gazebo messages for establishing communication
bridge = Node(
    package='ros_gz_bridge',
    executable='parameter_bridge',
    parameters=[{
        'config_file': os.path.join(pkg_project_description, 'config', 'ros_gz_example_bridge.yaml'),
        'qos_overrides./tf_static.publisher.durability': 'transient_local',
        'qos_overrides./scan.subscriber.reliability': 'reliable',
        # 또는
        'qos_overrides./scan.publisher.reliability': 'best_effort',
    }],
    output='screen'
)
```

> ros2 topic 은 yaml 파일에서 정의 할 수 있다.   
ros_gz_bridge exmaple 깃허브를 참고하자


