rosbag 의 내용을 csv 파일로 볼려면 패키지 하나 설치를 해주면 된다  
다행히 opensource MIT

클론
git clone https://github.com/AtsushiSakai/rosbag_to_csv


파이썬3 경우  
```
cd ~/catkin_ws/src  
git clone https://github.com/AtsushiSakai/rosbag_to_csv.git  
cd ~/catkin_ws && rosdep install -r --ignore-src --from-paths src
catkin_make
```

파이썬2를 사용하는 경우는 브랜치를 python2로 해서 받는다 

```

git clone -b python2 https://github.com/AtsushiSakai/rosbag_to_csv.git  
```
나머지는 같음  

빌드 후
```
rosrun rosbag_to_csv rosbag_to_csv.py
```

