# rc.local 특정 유저

일단 bashrc source 로 해주면 한방에 해결 될 것 같으나, 안됨

하나씩 모두 source를 처리해줘야지 실제 roslaunch 파일이 먹힘. 
ROS_MASTER 도 마찬가지..


```
#!/bin/bash
## currently not working with .bashrc alone..
su - amrnano -c "source /opt/ros/noetic/setup.bash &&
                source /home/amrnano/catkin_ws/devel/setup.bash &&
                export ROS_MASTER_URI=http://192.168.20.10:11311 &&
                export ROS_HOSTNAME=192.168.20.200 &&
                roslaunch etri_flower etri_flower.launch" &
echo "etri_flower launched"
```

이유는 root로 시작하게 되면 python의 패키지를 실행 못 함

물론 심링크나 환경 변수로 실행할 수 있지만.. 실행은 되지만 오류가 발생

참고로 
export PYTHONPATH:특정유저/.local/lib/python3.버전/site-packages

로 해주면 root로 실행을 해도 파이썬 모듈을 인식한다.. (특정 유저에서 깔려있는 모듈들..)  다만, 에러가 발생할 수도 있음(약간 제한적 사용 가능할 듯)

