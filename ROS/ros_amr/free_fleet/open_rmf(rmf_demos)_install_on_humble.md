## open-rmf (rmf_demos) install on ROS2 Humble
ROS humble에서는 소스코드 빌드를 할 경우 

> free fleet 과는 또 다른 패키지

디펜던시 설치
```
sudo apt update && sudo apt install -y cmake python3-vcstool curl
python3 -m pip install flask-socketio fastapi uvicorn datamodel_code_generator
sudo apt install python3-colcon*
```

workspace를 만들어준다. 그리고 깃허브 클론을 함
```
mkdir ~/ws_rmf_demos/src -p
cd ~/ws_rmf_demos/src
git clone https://github.com/open-rmf/rmf_demos.git
```

> 워크 스페이스는 기존 것을 사용해도 상관 없음 ..

rosdep 으로 필요한 패키지 추가 설치
```
cd ~/ws_rmf_demos
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro humble -y
colcon build
```


## rmf_demo 실행
rviz2와 ignition Gazebo - version 6.11 로 열기
```
ros2 launch rmf_demos_gz office.launch.xml
```

또는 가제보 클래식으로 실행
```
ros2 launch rmf_demos_gz_classic office.launch.xml
```


서버가 실행이 되고 웹소켓으로 연결을 해줘야하는데.. web-rmf를 설치를 해야하는 하는 듯 하다   
```
ros2 launch rmf_demos_gz office.launch.xml server_uri:="ws://localhost:8000/_internal"
```

> 웹서버가 없으니 실제로 해볼 수 있는 것은 rviz2 프로그램에서 문 열고 닫는 것 정도 밖에 할 수 없는 듯 함   
RMF Panle 로 Task를 전송하거나, json으로 되어 있는 일종의 list(tasks)를 업로드 할 수가 있는데..   
현재는 그런것들을 할 수는 없음 -- 먼저 web-rmf가 설치가 되어야 하는 듯 하다   


**web-rmf는 설치 실패** on Apr25 2023

현재 docker상에서 bash 쉘에서 pnpm 이 설치가 안되는 현상;; npm말고 좀 더 새로운 패키지 매니저 프로그램인데;;   
일단은 포기;;


### 대신 rmf_demos_tasks 패키지를 통해서 명령을 전달할 수는 있다

1. 첫 번째 task 보내기
```
ros2 run rmf_demos_tasks dispatch_patrol -p coe lounge -n 3 --use_sim_time
```
rosrun을 하면 json으로 만들어서 전송
```json
{
  "type": "dispatch_task_request",
  "request": {
    "unix_millis_earliest_start_time": 0,
    "category": "patrol",
    "description": {
      "places": [
        "coe",
        "lounge"
      ],
      "rounds": 3
    }
  }
}
```

2. 두 번째 task 보내기
```
ros2 run rmf_demos_tasks dispatch_delivery -p pantry -ph coke_dispenser -d hardware_2 -dh coke_ingestor --use_sim_time
```

```json
{
  "type": "dispatch_task_request",
  "request": {
    "unix_millis_earliest_start_time": 0,
    "category": "delivery",
    "description": {
      "pickup": {
        "place": "pantry",
        "handler": "coke_dispenser",
        "payload": []
      },
      "dropoff": {
        "place": "hardware_2",
        "handler": "coke_ingestor",
        "payload": []
      }
    }
  }
}
```

> 현재는 rmf_deoms_tasks 패키지에 직접 전달을 했지만, 아마도 RMF_panel을 이용해서(rmf-web)   
을 이용해서 JSON 으로 전달을 하고 websocket 통신을(tcp/ip)을 하는 듯 하다  
사실, open-rmf 리포 안에 많은 패키지가 있어서.. 많아서 헤깔린다;; 