# roslaunch wait
rosrun과는 달리 roslaunch 로 실행할 경우에  
RLException: ERROR: unable to contact ROS master at [http://192.168.10.7:11311]
The traceback for the exception was written to the log file

--wait 옵션을 넣어준다.  
`roslaunch rosserial_test serial_test.launch --wait`

roscore/master is not yet running, will wait for it to start



