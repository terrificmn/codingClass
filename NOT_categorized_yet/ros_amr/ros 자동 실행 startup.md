실패기록 -

먼저 sh 파일인 script 파일이 있어야 한다  
원하는 장소에 만들어 준다   
```
touch test_start.sh
```

파일 내용을 편집한다 
```
#!/bin/bash
source /opt/ros/noetic/setup.bash
source /home/sgtubunamr/catkin_fund_ws/devel/setup.bash
source /home/sgtubunamr/catkin_ws/devel/setup.bash
export ROS_MASTER_URI=http://localhost:11311
roscore & --wait
bash -c "roslaunch cartoros lidarodom_fordebug.launch" --wait
#rosrun send_data_mqtt send_data_mqtt_node --wait
PID=$!
wait "$PID"
```

이 파일은 실행이 될 수 있게 실행 권한을 준다  
```
sudo chmod +x ./test_start.sh
```

이제 이 파일을 참고하는 service를 만들어준다

/lib/systemd/system 디렉토리에 sudo 권한으로 service 파일을 하나 만들어 준다 
```
cd /lib/systemd/system
sudo touch test_start.service
```

만든 후 파일을 열어서 내용을 넣어준다 
```
sudo vi test_start.service
```

```
[Unit]
After=network-online.target 
[Service]
Type=simple
ExecStart=/home/sgtubunamr/test_start.sh
[Install]
WantedBy=multi-user.target
```


sudo systemctl daemon-reload
이제 service 파일을 다시 로드했기 때문에 서비스를 enable 시킬 수 있다   

sudo systemctl enable test_start.service




하지만 이대로 하면 잘 되지는 않는 듯 하다.. 서비스는 잘 등록되는데 재부팅시 자동으로실행이 되지는 않는다.  

참고할 것들...  


서비스 disable은  
```
sudo systemctl stop test_start.service
sudo systemctl disable test_start.service
```


https://github.com/magazino/systemd_ros

https://github.com/LucidOne/robot_systemd/blob/master/user/roslaunch%40.service

https://discourse.ros.org/t/automatic-launch-on-os-startup/23462


[여기 블로그 내용이 조금 더 도움이 되는 듯 하기도...](https://mshields.name/blog/2022-03-16-running-ros-nodes-on-boot/)

