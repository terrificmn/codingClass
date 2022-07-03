https://github.com/chapulina/dolly/tree/foxy 
깃허브 참고

```
source /opt/ros/foxy/setup.bash
```

먼저 자신의 workspace의 src 디렉토리까지 이동을 해준다
```
cd ~/my_ros2_ws/src
```

깃허브를 클론
```
git clone https://github.com/chapulina/dolly.git -b foxy
```

그리고 dependencies를 설치 해주는데 다시 상위 디렉토리인 자신의 workspace로 이동
```
cd ~/my_ros2_ws
```
그리고 dependencies를 설치
```
rosdep install --from-paths src --ignore-src -r -y -i
```

빌드를 해주는데 ignore를 이용해서 dolly_ignition 패키지는 빌드를 하지 않는다
이유는 gazebo 시뮬레이션을 사용하기 때문
```
colcon build --symlink-install --packages-ignore dolly_ignition
```

가제보를 사용하기 위해서 gazebo의 setup파일을 환경변수를 셋업
```
, /usr/share/gazebo/setup.sh
```

## 런치파일 만들기

workspace디렉토리의 src 디렉토리까지 이동한 후 패키지를 하나 만들어준다

```
cd ~/my_ros2_ws/src
ros2 pkg create --build-type ament_cmake dolly_launch_pkg --dependencies rclcpp
```

패키지가 만들어졌다면
dolly_launch_pkg 디렉토리안에 launch 디렉토리를 만들고 launch파일을 만든다
```
cd dolly_launch_pkg
mkdir launch
```

> vscode등을 이용해서 파일을 생성해주는 것이 더 편하다

런치파일을 만들어준다 (launch 디렉토리 안에), dolly.launch.py로 만들어 줌
붙여넣기
```py
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_dolly_gazebo = get_package_share_directory('dolly_gazebo')

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
        )
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value=[os.path.join(pkg_dolly_gazebo, 'worlds', 'dolly_empty.world'), ''],
            description='SDF world file',
        ),
        gazebo
    ])

```
gazebo.launch.py 을 포함시키고 그 안의 arguments 중에 world를 수정해서 실행이 되게 한다

return LaunchDescription 부분에서 
world 를 dolly_empty.world로 되어 있는데 다른 것으로 변경해도 된다

이제
만들었던 dolly_launch_pkg 패키지의 CmakeLists.txt 파일을 수정한다

find_package() 이후에 추가해준다
```
install(DIRECTORY
	launch
	DESTINATION share/${PROJECT_NAME}/
)
```
저장을 하고나서 다시 컴파일 빌드를 해준다

이번에는 자신이 만들었던 패키지만 빌드해주는 옵션을 넣어준다
```
cd ~/my_ros2_ws
colcon build --symlink-install --packages-select dolly_launch_pkg
```

소싱해주기  (my_ros2_ws 경로에서 해준다)
```
. install/setup.bash
# 또는 source install/setup.bash
```

이제 ros2에서 overlay가 되어서 현재패키지를 인식하게 된다

실행
```
ros2 launch dolly_launch_pkg dolly.launch.py
```
