rosbag으로 필요한 topics

```
rosbag record /clock /cmd_vel /joint_states /map /map_updates /odom /robotpose /scan /scan_matched_points2 /submap_list /tf /tf_static
```
대충 이 정도는 필요한 듯 하다


1. 가제보 시뮬레이션 실행   
2. cartographer 실행 해서 슬램 
3. 위의 토픽 rosbag으로 저장
4. 다 끝나면 ctrl+c 로 꺼준 다음에 해당 bag파일을 (기본은 날짜-시간으로 저장됨)    
offline으로 할 수 있는 런치파일 실행.. offline_backpack_2d.launch 파일에서 지정 후 실행  

