# gdbserver

sudp apt install gdb gdbserver

```
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Debug -DFORCE_DEBUG_BUILD=True --symlink-install --packages-select my_pkg
```



ros2 run --prefix 'gdbserver localhost:3000' amrslam_app amrslam_app_node 


ros2 run amrslam_app amrslam_app_node --ros-args --params-file ~/docker_ros2_ws/install/amrslam_app/share/amrslam_app/app_config/config.yaml 


ros2 run --prefix 'gdbserver localhost:3000' amrslam_app amrslam_app_node --ros-args --params-file ~/docker_ros2_ws/install/amrslam_app/share/amrslam_app/app_config/config.yaml


```
ros2 run --prefix 'gdbserver localhost:3000' amrslam_app amrslam_app_node --ros-args --params-file ~/docker_ros2_ws/install/amrslam_app/share/amrslam_app/app_config/config.yaml -p use_sim_time:=true
```

vscode 에서 debug 부분에서 아래 처럼 설정
Run and Debug tab 에서 launch.json 파일을 불러올 수가 있는데  
configurations 안 쪽의 컬링 브라켓에서 아래 부분을 복사해서 넣어준다. 
핵심은 miDebuggerServerAddress과 program, program은 전체 shared 경로를 입력한다.

```json
"configurations": [
        {
          "name": "C++ Debugger",
          "request": "launch",
          "type": "cppdbg",
          "miDebuggerServerAddress": "localhost:3000",
          "cwd": "/",
          "program": "/home/docker_humble/my_ws/install/my_app/lib/my_app/my_app_node"
        },
    
```

그리고 name 은 아무렇게나 정의해주고  이는 vscode 에서 쉽게 찾을 수 있게 된다. 해당 이름 옆에 재생 버튼을 눌러준다.  
먼저 실행한 ros2 노드가 대기하고 있다가 디버깅 버튼이 눌리면 디버깅을 하게 된다.   




