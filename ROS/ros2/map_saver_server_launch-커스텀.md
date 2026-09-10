# life cycle map_saver_server.launch
기존에 map_saver_server 를 런치 할 경우  

크게 문제가 없다면 아래처럼 사용해도 되지만,,,   
```py
map_server_launch = IncludeLaunchDescription(
                        PythonLaunchDescriptionSource(
                            FindPackageShare('nav2_map_server').find('nav2_map_server') + '/launch/
                                            map_saver_server.launch.py'
                            )
                    )

return LaunchDescription([
    map_server_launch
])
```

life cycle 관련해서 bond_time 초과로 강제로 프로그램이 종료되는 경우가 생길 수가 있는데  
해당 nav2_map_server 에 argument 등을 넘길 수가 있는데, 실제 런치 파일은 /opt 이하에 root 권한으로 되어 있어서  
아규먼트를 변경하는데 불편할 수가 있다.  

그래서 따로 launch 파일 복사해서 내 패키지 내에서 만들어서 사용할 수가 있다.  

먼저 자신의 패키지안에 luanch 디렉토리에 launch 파일을 하나 만든다. map_saver_server.launch.py 정도면 되겠다.  
> 실제 map_saver_server 에서 복사

```py
#!/usr/bin/env python3

# Copyright (c) 2020 Samsung Research Russia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import launch_ros.actions


def generate_launch_description():
    # Parameters
    lifecycle_nodes = ['map_saver']

    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time', default_value='false', description='Use simulation clock')
    bond_timeout_arg = DeclareLaunchArgument(
        'bond_timeout', default_value='10.0', description='Timeout for heartbeat')

    # 2. Map the variables to the LaunchConfigurations
    # Note: These are now "placeholders" that resolve when the file actually runs
    use_sim_time = LaunchConfiguration('use_sim_time')
    bond_timeout = LaunchConfiguration('bond_timeout')
    
    ## static params
    autostart = True
    save_map_timeout = 2.0
    free_thresh_default = 0.25
    occupied_thresh_default = 0.65
    attempt_respawn_reconnection = True

    # Nodes launching commands
    start_map_saver_server_cmd = launch_ros.actions.Node(
            package='nav2_map_server',
            executable='map_saver_server',
            output='screen',
            respawn=True,
            respawn_delay=1.5,
            emulate_tty=True,  # https://github.com/ros2/launch/issues/188
            parameters=[{'save_map_timeout': save_map_timeout},
                        {'free_thresh_default': free_thresh_default},
                        {'occupied_thresh_default': occupied_thresh_default}])

    start_lifecycle_manager_cmd = launch_ros.actions.Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager',
            output='screen',
            emulate_tty=True,  # https://github.com/ros2/launch/issues/188
            parameters=[{'use_sim_time': use_sim_time},
                        {'autostart': autostart},
                        {'node_names': lifecycle_nodes},
                        {'attempt_respawn_reconnection': attempt_respawn_reconnection}, ## even if it's in a Failure state, tell the lifecycle_manager to attempt a recovery
                        {'bond_timeout': bond_timeout}
                        ])

    ld = LaunchDescription()

    ## IMPORTANT
    ld.add_action(use_sim_time_arg)
    ld.add_action(bond_timeout_arg)

    ld.add_action(start_map_saver_server_cmd)
    ld.add_action(start_lifecycle_manager_cmd)
    

    return ld
```

이를 불러와서 사용할 수가 있는데 여기에서 지정한 argument 를 보내서 실행하면 된다. 


실제 대표로 실행할 main 런치 파일에서 
```py
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, RegisterEventHandler, LogInfo, EmitEvent
from ament_index_python.packages import get_package_share_directory



def generate_launch_description():

    ## copied from share nav2_map_server
    map_server_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('my_package'), 'launch', 'map_saver_server.launch.py')
        ),
        launch_arguments={
            'use_sim_time': 'False'
            ## 'bond_timeout' default
        }.items()
    )

    return LaunchDescription([
        map_server_launch
        ## other node or launch 
    ])

```

map_saver_server.launch.py 에서      
use_sim_time_arg = 'use_sim_time',   
bond_timeout_arg = 'bond_timeout' 로 사용하므로 원하는 arguments 를 보내주면 된다.   
> 더 필요할 경우에는   
map_saver_server.launch.py 에서 DeclareLaunchArgument() 를 사용해서 더 늘려준다.  

