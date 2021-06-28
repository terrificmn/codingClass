# 설치

https://github.com/wh200720041/ssl_slam

여기의 리드미 참고해서 설치한다

Prerequisites 을 다 설치한 후 
그 중 Ceres Solver 설치는
링크 눌러서 나온 맨첨에 나온 것을 다운로드 받은 후 (latest버전) 그리고 
리눅스 부분에 가서 make 및 make install을 하면 됨


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
