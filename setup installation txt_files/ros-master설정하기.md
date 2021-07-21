# 로봇 컴퓨터와 pc를 서로 연결하기

먼저 로봇의 컴퓨터가 마스터가 된다면 
환경변수 ROS_MASTER_URI 설정해주면 된다

로봇컴의 ~/.bashrc 파일을 열어준다
```
export ROS_MASTER_URI=http://192.168.0.9:11311/
export ROS_HOSTNAME=192.168.0.9
```

그리고 ifconfig로 확인한 아이피주소를 넣어준다
ROS_HOSTNAME 에도 자기의 아이피 (로봇컴)

그리고 보통 pc에 넘어와서 ~/.bashrc 파일을 열어준다
```
export ROS_MASTER_URI=http://192.168.0.9:11311/
export ROS_HOSTNAME=192.168.0.98
```

마스터를 사용할 로봇컴의 아이피를 넣어준다
그리고 ROS_HOSTNAME 에는 pc의 아이피를 적어주고 저장 후 빠져나오기

그리고 
```
source ~/.bashrc
```

이제 roscore는 로봇 컴에서 키면 되고 
pc에서 특정 노드에서 publish를 하면 
롯봇 컴에서 subscribe 해서 통신을 할 수 있게 된다

> 기존 터미널에 열려 있으면 환경변수가 적용이 안되니 기존 창에서는 source ~/.bashrc 를 하거나
새로운 창을 띄워서 한다~

