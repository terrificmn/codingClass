# rc.local root
rc.local 은 시작할 때 실행이 되니, root 유저로 실행이 되는데  
일부 프로그램 모듈이나 호환성 때문에 제대로 실행이 안될 경우가 있다.  
예를 들어서 파이썬 모듈이 특정 my_user 의 .local 디렉토리에 있을 경우   
당연히 root 는 해당 어떤 특정 모듈을 찾지 못해서 프로그램들이 시작되도 에러로 끝나게 된다.   

그래서 이를 해결하려면   
PYTHONPATH 등의 환경 변수를 사용해서 해당 .local 의 경로를 
아마도 /home/my_user/.local/lib/python3.8/site...어쩌구 였던 것 같음   
root쪽에서 일단 export 명령을 사용해서 하면 특정 라이브러리 자체는 잘 찾으나   
`export PYTHONPATH:특정유저/.local/lib/python3.버전/site-packages`      
특정 유저에서 깔려있는 모듈들을 찾는데는 문제가 없어지지만, 그래도 에러가 발생할 수도 있음(약간 제한적 사용 가능할 듯)   


## rc.local 에서 아예 유저로 실행해주기
아예 `su -` 명령을 통해서 특정 유저로 실행해준다.

> 단, source 등의 문제 등이 있는데 이때 .bashrc를 source 를 해주면 한방에 통할 듯 했으나   
제대로 source setup.bash 등의 파일이 안 올라가지는 듯 하다.

그래서 하나씩 source을 해주는 식으로 일단 처리   
(추후 더 좋은 방법이 있다면 업데이트!)   
> 하나씩 모두 source를 처리해줘야지 실제 rosrun , roslaunch 등 및 패키지를 찾아간다.   
ROS_MASTER 등을 사용한다면.. 그것도 마찬가지   



### rc.local  유저로 사용 예
```
#!/bin/bash
su - my_user -c "source /opt/ros/noetic/setup.bash &&
                source /home/my_user/catkin_ws/devel/setup.bash &&
                export ROS_MASTER_URI=http://192.168.10.11:11311 &&
                export ROS_HOSTNAME=192.168.11.111 &&
                roslaunch my_pkg my_launch.launch" &
echo "my_pkg program has been launched successfully."
```
