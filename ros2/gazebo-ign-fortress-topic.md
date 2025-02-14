# ign topic 확인하기


리스트 보기
```
ign topic -l
```
리스트 예
```
/clock
/gazebo/resource_paths
/gui/camera/pose
/model/vehicle_blue/cmd_vel
/model/vehicle_blue/odometry
/model/vehicle_blue/tf
/model/vehicle_green/cmd_vel
/model/vehicle_green/odometry
/model/vehicle_green/tf
/stats
/world/diff_drive/clock
/world/diff_drive/dynamic_pose/info
/world/diff_drive/pose/info
/world/diff_drive/scene/deletion
/world/diff_drive/scene/info
/world/diff_drive/state
/world/diff_drive/stats

```


info 보기, topic 옵션도 같이 넣어야 한다.
```
ign topic -i --topic /model/vehicle_blue/cmd_vel
```

결과 예
```
Publishers [Address, Message Type]:
  tcp://172.17.0.1:41827, ignition.msgs.Twist
```


-e 에코 옵션
```
ign topic -e --topic /model/vehicle_blue/cmd_vel

```

퍼브리쉬가 있다면 예

```
linear {
  x: 0.1
}
angular {
  z: 0.1
}
```


ign 토픽 퍼블리쉬
```
ign topic -t "/cmd_vel" -m ignition.msgs.Twist -p "linear: {x: 0.1}, angular: {z: 0.0}" 
```
