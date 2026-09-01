Setting Dynamic reconfig parameters.
/opt/ros/melodic/lib/nodelet/nodelet: symbol lookup error: /home/ubun/catkin_ws/devel/lib//librealsense2_camera.so: undefined symbol: _ZN20ddynamic_reconfigure19DDynamicReconfigureC1ERKN3ros10NodeHandleE

이런 메세지가 나올 때 
ddynamic_reconfigure 가 하나 이상이면 이런 현상이 발생할 수도 있다고 하는데 정확하지는 않다.
ddynamic_reconfigure 관련되보이는 것도 지워보고 아예 realsense-camera 패키지도 지워봐도 소용이 없다;

그래서 catkin_ws/src 패키지중에서 백업을 한 후에 
아예 catkin_ws 안의 디렉토리를 다 지운후에 다시
```
$ cd catkin_ws/
$ rm -rf ./*
$ mkdir src
$ catkin_make clean
```
을 해준다음에 다시 실행을 해주면 이제는 잘 된다

```
roslaunch realsense2_camera rs_camera.launch filter:=pointcloud

```