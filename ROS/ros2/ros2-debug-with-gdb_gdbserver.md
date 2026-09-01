# gdbserver
gdb 설치  
```
sudo apt install gdb gdbserver
```

먼저 Debug 모드로 빌드 
```
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Debug -DFORCE_DEBUG_BUILD=True --symlink-install --packages-select my_pkg
```

ros run 실행
```
ros2 run --prefix 'gdbserver localhost:3000' my_pkg my_pkg_node 
```

또는 파라미터 관련 파일을 같이 열어야 하는 경우
```
ros2 run --prefix 'gdbserver localhost:3000' my_pkg my_pkg_node --params-file ~/docker_ros2_ws/install/my_pkg/share/my_pkg/app_config/config.yaml
```

또 다른 예, 
```
ros2 run --prefix 'gdbserver localhost:3000' my_pkg my_pkg_node --ros-args --params-file ~/docker_ros2_ws/install/my_pkg/share/my_pkg/app_config/config.yaml -p use_sim_time:=true
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




