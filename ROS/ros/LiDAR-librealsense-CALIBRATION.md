# 리얼센스2 l515 조정하기

pip으로 pyrealsense2를 설치해줘야한다

파이썬 사용도 가능해서 3.7 이하부터
파이썬3로 설치 (파이썬2도 가능, 그냥 pip, python으로 실행할 것)
```
pip3 install pyrealsense2
```

그리고 librealsense/tools/rs-imu-calibration 경로로 가보면 py 실행파일이 있음
이동 후에 실행하는데 
```
python3 rs-imu-calibration.py  
```
원하는 각도로 카메라를 위치시키면 칼리브레이션을 진행하고 기다리고 있으면 

참고 진행 예시
Align to direction:  [ 0. -1.  0.]  
Upright facing out  Status.collect_data[...................]
Direction data collected.

최대한 방향을 맞추면 몇 초 기다리라고 하고 
정보를 수집한다.

방향별로 5~6번 수행



https://www.intelrealsense.com/wp-content/uploads/2020/07/IMU_Calibration_Tool_for_Intel_RealSense-Depth_Cameras_Whitepaper.pdf?_ga=2.139707440.2081722235.1626336447-1345194574.1624255042

