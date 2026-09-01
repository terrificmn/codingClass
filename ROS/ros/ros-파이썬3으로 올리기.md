# ros 파이썬 3 이상으로 올리기
```
sudo apt-get install python3-pip python3-yaml
pip3 install rospkg catkin_pkg
```
그리고 cv_brige가 파이썬 2.7로 빌드되어 잇기 때문에 python3 을 위해서 빌드를 해줘야한다고 함

```
sudo apt-get install python-catkin-tools python3-dev python3-numpy
```
catkin_make를 빌드할 때 사용하므로 
catkin_bulid_ws로 새로만들어서 충돌이 안나게 해줘야함

```
mkdir ~/catkin_build_ws && cd ~/catkin_build_ws
mkdir src

catkin config -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so

catkin config --install
```

그리고 미리 만들어 놓은 src로 들어간다
그리고 클론하기
```
git clone -b melodic https://github.com/ros-perception/vision_opencv.git
```
cd .. 또는 cd ~/catkin_build_ws 로 이동한 후에 
```
catkin build cv_bridge
source install/setup.bash --extend
```