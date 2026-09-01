## 모델 변경해서 활용하기

gazebo-카메라plugin_camera.md 파일 참고


## 패키지 만들기
world 파일을 그냥 복사한다고 build 할때 인식이 안되면 소용없는 듯 하다
이것 때문에 시간 많이 소요됨 ㅠㅠ

> colcon build 가 중요하다 ㅠㅠ

먼저 런치파일을 실행할 패키지를 만들자

우선 워크 스페이스에서 src 디렉토리로 이동한 후 패키지를 만들어 보자 
cment_cmake 사용할 수 있게 만들어주자
```
cd ~/my_ws/src
ros2 pkg create --build-type ament_cmake dolly_maze --dependencies rclcpp
```

이제 만들어진 dolly_maze 디렉토리로 이동해보자 (또는 본인의 패키지명)

이제 여기에 launch, models, worlds 디렉토리를 만들어준다

```
cd dolly_maze
mkdir launch models worlds
```

이런 디렉토리가 구조가 될 것이다
```
dolly_maze/
├── include
├── launch
├── models
├── worlds
├── src
├── CMakeLists.txt
└── package.xml
```


## model 복사시키기

먼저 gazebo의 building model 기능등을 이용해서 만들었던 모델이나 다운로드 받은 파일들을 
models 디렉토리에 복사시켜준다

카메라plugin편에서 만들었던 모델을 복사한다. 경로는 다를 수 있으나 자신이 저장했던 곳의 경로로부터 복사하면 된다.

빌딩 복사
```
cd ~/model_editor_models
cp -r dolly_custom ~/my_ws/src/dolly_maze/models
```

이번에는 모델 복사 (자신의 모델을 복사시키면 됨)
```
cd ~/model_editor_models/
cp -r dolly_custom ~/my_ws/src/dolly_maze/models
```

이런식으로 원하는 모델 디렉토리를 전부 자신의 패키지의 models 디렉토리로 복사 시킨다


## world 파일 만들기
world에는 가제보에서 실행할 때의 모델들이 들어가는 파일이라고 생각하면 된다
모델들이 모여서 world를 된다고 볼 수도 있을 것 같다

그래서 위의 model 디렉토리를 만들거나 복사시키지 않고 모델 파일들을 전부다 world 디렉토리에 넣어버리면
그걸로 world 완성이다

하지만 좀 더 깔끔하고 구조적으로 더 좋다고 생각

empty_world 파일 내용인데 world 파일을 만들어주자. 파일명은 dolly_maze.world 로 함
여기에서의 파일명은 런치파일에서 사용하게 됨
```xml
<?xml version="1.0" ?>

<sdf version="1.7">
  <world name="default">

    <include>
      <uri>model://sun</uri>
    </include>
    <include>
      <uri>model://ground_plane</uri>
    </include>
    
  </world>
</sdf>
```

이제 모델 파일들을 include를 시키자. pose 태그를 넣어주면 xyz로 지정해 줄 수 있다
world 태그 안에 위치하게 복사하자
```xml
<include>
    <pose>-5.4 4.0 0.33 0 0 0</pose>
    <uri>model://dolly_custom</uri>
</include>

<include>
    <pose>2.417 0.2725 0 0 -0 0</pose>
    <uri>model://wall</uri>
</include>
```

## launch 파일 패키지로 만들기
launch 디렉토리로 이동해서 런치파일을 dolly_maze.launch.py 로 만들자

> vscode같은 에디터로 만드는게 편하다. 맘에 드는 에디터를 사용하자

아래 내용을 복사
```py
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_dolly_maze = get_package_share_directory('dolly_maze')

    # Gazebo launch
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py'),
        )
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value=[os.path.join(pkg_dolly_maze, 'worlds', 'dolly_maze.world'), ''],
            description='SDF world file'),
        gazebo,
    ])
```

## CMakeLists.txt 파일 설계도
CMakeLists.txt 파일에 
install(DIRECTORY) 경로명을 적어주는 부분이 중요하다~ launch 파일을 만들때는 
launch 경로를 넣어주기만 하면 되지만
models worlds 디렉토리를 사용할 것 이므로 꼭 넣어준다

그리고 가장 중요한(?) gazebo_ros 환경변수를 셋팅을 해줘야한다

2가지 방법이 있는데 먼저 첫번째 방법은

resource들을 설치를 해주는 것, (models, plugins, wolrds 파일들..)

CMakeLists.txt 파일을 열어서 
find_package() 아래에 넣어준다
```c
install(DIRECTORY
	launch
  models
  worlds
	DESTINATION share/${PROJECT_NAME}/
)
```
> worlds 디렉토리를 포함 안시켰더니 gazebo에서 아무런 반응이 없어서 뭐가 문제인지 알기 어려웠다

colcon 빌드를 할 때 패키지에 포함된 model, world 파일들을 워크스페이스 install 디렉토리안에 
설치를 해준다. (복사해줌)

이번에는 pckage.xml 에 환경변수로 export 할 수 있게 경로를 지정해준다
export 태그 안에 넣어준다
```xml
<export>
  <gazebo_ros gazebo_plugin_path="lib"/>
  <gazebo_ros gazebo_model_path="${prefix}/models"/>
  <gazebo_ros gazebo_media_path="${prefix}/worlds:${prefix}/media"/>
</export>
```
위의 환경 변수들은 아래 처럼 된다

| vaiables | environment variables |
| --- | --- |
| gazebo_plugin_path | GAZEBO_PLUGIN_PATH |
| gazebo_model_path | GAZEBO_MODEL_PATH |
| gazebo_media_path | GAZEBO_RESOURCE_PATH |

이 환경 변수들은 런치파일을 실행할 때 gazebo.launch.py를 넣어주면 환경변수를 set 해준다고 함

그래서 런치파일에 아래처럼 gazebo.launch.py 를 넣어준다
```py
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py'),
            )
        )
    ])
```

막상 터미널에 GAZEBO_MODEL_PATH 를 패스가 추가되어 있는게 없다
```
echo $GAZEBO_MODEL_PATH
```
하지만 빌드를 하고 나서 런치파일을 실행하면 world파일이 잘 열리게 된다 (모델들이 잘 나옴)


## 환경변수 설정 두 번째 방법은 env-hooks
env-hooks을 설정하는 것

env-hooks 디렉토리를 하나 만들어 준다. 그리고 그 안에 project_name.sh.in 파일을 만들어준다
패키지 이름과 같게 해주면 된다
```
cd ~/my_ws/src/dolly_maze
mkdir env-hooks
cd env-hooks && touch dolly_maze.sh.in
```

파일안에는 아래 내용을 넣어준다
```
ament_prepend_unique_value GAZEBO_MODEL_PATH "$AMENT_CURRENT_PREFIX/share/@PROJECT_NAME@/models"
ament_prepend_unique_value GAZEBO_RESOURCE_PATH "$AMENT_CURRENT_PREFIX/share/@PROJECT_NAME@/worlds:$AMENT_CURRENT_PREFIX/share/@PROJECT_NAME@/media"
ament_prepend_unique_value GAZEBO_PLUGIN_PATH "$AMENT_CURRENT_PREFIX/lib"
```

그리고 porject_name.dsv.in 파일도 만들어 준다. 템플릿은 아래와 같다
```
prepend-non-duplicate;GAZEBO_MODEL_PATH;share/@PROJECT_NAME@/models
prepend-non-duplicate;GAZEBO_RESOURCE_PATH;share/@PROJECT_NAME@/worlds
prepend-non-duplicate;GAZEBO_RESOURCE_PATH;share/@PROJECT_NAME@/media
prepend-non-duplicate;GAZEBO_PLUGIN_PATH;share/@PROJECT_NAME@/plugins
```
현재 media와 plugins은 필요없어서 뺏음

그리고 CmakeLists.txt 파일을 열어서 템플릿을 생성하는데 위의 만들어줬던 파일들을 설정해준다
```
ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/env-hooks/${PROJECT_NAME}.sh.in")
ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/env-hooks/${PROJECT_NAME}.dsv.in")
```

이제 빌드를 해보자

첫번재, 두번째 방법 중에 하나 선택해서 하면 됨
확실하게 작동함

만약 런치파일로 gazebo실행 했을때 에러메세지 없이 블랙아웃 된 상태에서 응답없음으로 넘어간다면
model 파일에 문제가 있을 경우가 높다

트러블슈팅할 때 gazebo를 실행해서   
모델들을 insert로 추가를 해줘서 (경로 추가해줌)  
모델이 불러와지는지 확인
이때 문제가 있는 경우라면 프리징 발생한다~ 그 모델의 world, sdf, scripts 파일등에 문제가 없는지 확인한다



## 환경변수도 문제지만 원래 dolly 모델이 남아 있는 있어서 에러
먼저 원 dolly 모델이 install 디렉토리에 깔려있기 때문에 모델의 텍스쳐 부분이 그대로 적용되서 별 문제가 없어보였으나

모델을 변경한 custom_dolly 같은 경우에는 gazebo에서 원 모델을 변경해서 새로 저장한 것이어서
model.config, model.sdf 파일 밖에 없다

원래 모델에는 materials 디렉토리에 scripts, textures 디렉토리가 둘다 있어서 복사해야함

```
├── materials
│   ├── scripts
│   │   └── script.material
│   └── textures
│       └── iron.jpg
├── model.config
└── model.sdf

3 directories, 4 files
```

위의 파일들이 모두 필요하므로 다 복사해주자. 



script 및 이미지 변경을 하려면 일단 원하는 이미지를 다운 (혹시 모르니 원래 800x600 사이즈로 조정했음)

script.material 파일에서 처음 dolly로 설정이 되어있는데 이를 변경
```
material Dolly/fur
```

변경해준다
```
material Dolly_custom/iron
```
이 부분은 model.sdf 파일에서 script 부분에서 찾으므로 이름을 변경한다면 model.sdf 파일도 변경해줘야한다

그리고 script.material 파일의 이미지를 변경하려고 한다면
```
 texture_unit
  {
    texture iron.jpg
    filtering anistropic
    max_anisotropy 16
  }
```
부분의 texture 에 이미지 파일을 넣어준다

그리고 모델명을 dolly에서 dolly_custom으로 변경했으므로 model.sdf 열어서 변경

```
<script>
  <uri>model://dolly/materials/scripts</uri>
  <uri>model://dolly/materials/textures</uri>
  <name>Dolly/fur</name>
</script>
```
스크립트 지정된 태그 부분을 변경된 모델명으로 바꾼다
그리고 name 태그 부분도 script.material 파일에서 변경된 내용으로 변경해준다
```
<script>
  <uri>model://dolly_custom/materials/scripts</uri>
  <uri>model://dolly_custom/materials/textures</uri>
  <name>Dolly_custom/iron</name>
</script>
```

스키립트 태그는 2번 나오므로 검색을 해서 모두 변경해준다

그리고 모델명은 당연히 변경
```
<model name='dolly_custom'>
```

> ros태그의 플러그인에 namespace는 topic 앞에 붙는 네임스페이스이므로 변경할 필요는 없다


## colcon 빌드
다시 자신의 워크 스페이스로 돌아온다음에 빌드를 해준다
```
cd ~/my_ws
colcon build
```

빌드를 하게 되면 차이점은 첫 번째 방법으로 환경변수 설정을 했다면 GAZEBO_MODEL_PATH 를 확인해도 
변화가 없지만

env hooks 방법으로 했다면 워크스페이스를 오버레이로 소싱하는 순간 패스가 들어가진다

```
$echo $GAZEBO_MODEL_PATH

$
```
아무런 값이 없지만 

소싱 오버레이하면
```
cd ~/my_ws
. install/setup.bash
```
결과는
```
/home/ubun/my_ws/install/dolly_maze/share/dolly_maze/models
```

그래서 가제보를 실행할 때 무리없이 모델 파일을 불러오는게 된다

> 역시 고생했어 ㅠㅠ


이제 런치파일 실행
```
ros2 launch dolly_maze dolly_maze.launch.py 
```
모델들이 다 잘 실행된다




## 문제의 모델 파일이 있는데 왜 안되냐고? 
> 위의 CMakeLists.txt 와 package.xml 에서 셋팅을 안했다면 model 못 찾아서 모델을 
로딩을 못하게 된다

```
[gzserver-1] Error Code 12 Msg: Unable to find uri[model://wall_maze]
```

어쨋든 이 경우는 모델 파일이 없거나, 모델파일의 경로를 환경변수로 gazebo에서 인식을 못하고 있거나 
해서 파일은 있는데도 계속 모델 로딩을 못해주는 문제 발생

이게 되면 한꺼번에 다 안 되야 하는데 어떤 모델은 되고 어떤 건 안 되고;;
그 이유는 원본 dolly 패키지에서 모델들을 변경하거나 가져온 것이였으므로 환경변수에 경로가 있어서 
문제가 없었는데 아예 새로 만든 것은 경로 인식을 못했던 것 ㅠㅠ

> 그래서... 삽질을 많이 했다는 소리 ㅠ ㅋㅋ

[ros2 위키 참고](https://github.com/ros-simulation/gazebo_ros_pkgs/wiki/ROS-2-Migration%3A-Gazebo-ROS-Paths)
