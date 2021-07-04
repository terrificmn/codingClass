# 설치

https://github.com/wh200720041/ssl_slam

여기의 리드미 참고해서 설치한다

Prerequisites 을 다 설치한 후 
그 중 Ceres Solver 설치는
링크 눌러서 나온 맨첨에 나오는 latest stable release 버전을 다운 받은 후
리눅스 부분에 가서 make 및 make install을 하면 됨

Ceres Solver를 설치하기 위한 의존성 해결 설치
```
# CMake
sudo apt-get install cmake
# google-glog + gflags
sudo apt-get install libgoogle-glog-dev libgflags-dev
# BLAS & LAPACK
sudo apt-get install libatlas-base-dev
# Eigen3
sudo apt-get install libeigen3-dev
# SuiteSparse and CXSparse (optional)
sudo apt-get install libsuitesparse-dev
```

ceres-solver 설치
```
wget http://ceres-solver.org/ceres-solver-2.0.0.tar.gz
tar zxf ceres-solver-2.0.0.tar.gz
mkdir ceres-bin
cd ceres-bin
cmake ../ceres-solver-2.0.0
make -j3
make test
# Optionally install Ceres, it can also be exported using CMake which
# allows Ceres to be used without requiring installation, see the documentation
# for the EXPORT_BUILD_DIR option for more information.
sudo make install
```


## plc 다운도르
https://pointclouds.org/downloads/

아래 커맨드 입력해서 설치
```
sudo apt install libpcl-dev
```
## OctoMap 다운도르

```
sudo apt-get install ros-melodic-octomap*
```

## Trajectory visualization 
sudo apt-get install ros-melodic-hector-trajectory-server


rosbag 파일은 일단 받을 필요 없고

roslaunch ssl_slam ssl_slam.launch 로 실행할 때 
런치파일에서 

```
<!--- Comment this if you use real sensor -->
    <node pkg="rosbag" type="play" name="rosbag_play" args="--clock $(env HOME)/Downloads/L515_test.bag"/> 
    <param name="/use_sim_time" value="true" />

<!--- Uncomment this if you use real sensor
    <include file="$(find realsense2_camera)/launch/rs_camera.launch"/>
-->
```
이 부분을 주석처리하고 반대로 real sensor를 사용할 때는 주석을 풀어준다

일단 에러는 발생하지 않지만, 실행도 안 되므로 트러블슈팅 해야함
