# rmf traffic editor

pyhton3 dependencies pkgs
```
sudo apt install python3-shapely python3-yaml python3-requests
```

워크스페이스로 이동 후 git 클론
```
cd ~/my_ros2_ws/src
git clone https://github.com/open-rmf/rmf_traffic_editor.git
```

빌드  `colcon build` 한 후
```
colcon build --packages-select rmf_traffic_editor
```

소스 한 후에 실행
```
source install/setup.bash
traffic-editor 
```


