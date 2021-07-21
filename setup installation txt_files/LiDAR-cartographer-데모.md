
wget -P ~/Downloads https://storage.googleapis.com/cartographer-public-data/bags/backpack_2d/cartographer_paper_deutsches_museum.bag

roslaunch cartographer_ros demo_backpack_2d.launch bag_filename:=${HOME}/Downloads/cartographer_paper_deutsches_museum.bag


___

먼저 lua 파일을 만들어야하고
cartographer_ros/configuration_files 에 보면 각종(?) .lua 파일이 있는데 
하나를 만들어 주면된다

catkin_create_pkg 를 하나 만들어 주고
```
catkin_create_pkg slam_cartographer roscpp 
```
그리고 만들어진 패키지 디렉토리로 이동

그리고 
mkdir config launch

config 디렉토리에 lua파일을 만들어 주는데 summit.lua 로 만들어 준다

기존에 cartographer_ros 안에 있는 파일을 참고해서 만들어 준다


노드가 실행되고 있을 때 트리 확인하기 pdf 파일로 만들어 준다
```
 rosrun tf view_frames 
```

launch 파일도 비슷하게 참고해서 복사해서 만들어준다

catkin_iso_ws (다른 워크스테이션으로 만듬) 로 이동해서 아래명령어를 해줌
```
cd catkin_iso_ws
source install_isolated/setup.bash
ropack profile
```
이렇게 해줘야지 제대로 인식한다 (이것도 되는 듯 source devel_isolated/setup.bash)
bashrc 파일을 열어서 맨 아래에 추가해주자
```
vi ~/.bashrc
source $HOME/catkin_ws_iso/install_isolated/setup.bash
```


아마도 런치파일과 lua 파일을 잘 바꿔야지 잘 나올 듯 하다

런치파일을 실행해보면 cartographer_node 가 실행이 되는데

rostopic list 및 echo로 확인을 해보면
```
ubun@ubun-sc:~$ rostopic list

ubun@ubun-sc:~$ rostopic info /points2
Type: sensor_msgs/PointCloud2

Publishers: None

Subscribers: 
 * /cartographer_node (http://ubun-sc:38707/)


ubun@ubun-sc:~$ rostopic info /imu/data
Type: sensor_msgs/Imu

Publishers: None

Subscribers: 
 * /cartographer_node (http://ubun-sc:38707/)

```
위의 두개의 토픽을 cartographer_node에서 구독하고 있는 것을 알 수 있고







그리고 조작은 일단 scout-mini는 시리얼통신으로 무선조종으로 움직이자




맵 저장하기 (2D)
```
rosrun map_server map_saver -f map_name
```

2D 맵이 생성이 되었으면 Navigation부분을 만들어줘야하는데 일단 패키지로 만들어준다
패키지에서는 launch, map, src 디렉토리등을 포함하고 위에 만들어진 map.pgm, map.yaml 파일을 넣어준다
launch 디렉토리에는 필요한 amcl, move_base, navigation 런치파일등이 필요하게 된다

(navigation에는 map server, localization, move_base, rviz가 필요하다)
scout-mini 의 acml 과 move_base 참고하기 (description)


https://www.youtube.com/watch?v=GzZGl0kzGOM
이어서 봐야할 듯



https://www.youtube.com/watch?v=bXNK8VTQ4zo 참고



https://www.programmersought.com/article/53468612944/ 추후 참고