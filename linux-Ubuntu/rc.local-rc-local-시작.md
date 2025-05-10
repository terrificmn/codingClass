# rc.local, rc-local 프로그램 등록하기

먼저 리눅스에서 /etc/rc.local 파일을 만들어서 (쉘 스크립트 파일)을 만들고   
systemctl을 등록해서 시작프로그램을 등록할 수가 있는데, 기본적으로는 disable 되어 있다.

systecmctl status  rc.servcice
rc.service
  Loaded: masked (Reason: Unit rc.service is masked.)
  Active: inative (dead)


먼저 /etc/rc.local 파일을 만들어준다. (없으면 만들어 준다)

```shell
#!/bin/bash
source /opt/ros/noetic/setup.bash
source /home/myuser/catkin_ws/devel/setup.bash
roscore &
return 0
```

이후 파일을 실행 권한이 필요
`sudo chmod +x /etc/rc.local`

rc-local 이라는 서비스에서 등록이 필요해서 enable을 해줘야 하는데   
만약 rc-local 을 enable을 했을 경우 
아래와 같은 에러의 경우 아직 등록이 안된 것

```
The unit files have no installation config (WantedBy=, RequiredBy=, Also=,
Alias= settings in the [Install] section, and DefaultInstance= for template
units). This means they are not meant to be enabled using systemctl.
 
Possible reasons for having this kind of units are:
• A unit may be statically enabled by being symlinked from another unit's
  .wants/ or .requires/ directory.
• A unit's purpose may be to act as a helper for some other unit which has
  a requirement dependency on it.
• A unit may be started when needed via activation (socket, path, timer,
  D-Bus, udev, scripted systemctl call, ...).
• In case of template units, the unit is meant to be enabled with some
  instance name specified.

```

> 인스톨 관련 config가 없다고 나온다면..

또는 status 를 확인했을 때에   
Active: inactive (dead)  
일 경우에는 start를 먼저 시켜준다.

```
sudo vi /etc/systemd/system/rc-local.service
```

파일을 만들고 아래내용으로 만들어준다.

```shell
[Unit]
Description=/etc/rc.local Compatibility
ConditionPathExists=/etc/rc.local

[Service]
Type=forking
ExecStart=/etc/rc.local start
TimeoutSec=0
StandardOutput=tty
RemainAfterExit=yes
SysVStartPriority=99

[Install]
WantedBy=multi-user.target
```

저장 후에 enable 을 시켜준다 
```
sudo systemctl enable rc-local
```

아래 처럼 심링크가 만들어진다.
```
Created symlink /etc/systemd/system/multi-user.target.wants/rc-local.service → /etc/systemd/system/rc-local.service.
```

이제 재부팅을 하면 roscore가 실행된 것을 알 수 가 있다.


우분투 22 같은 경우에는 /etc 이하가 아닌 /lib 이하에 이미 만들어져 있다. 
`/lib/systemd/system/rc-local.service`  
이미 example 로 만들어져 있고, /etc/rc.local 경로까지 되어 있으므로  
/etc/rc.local 만들고, 위의 /lib/이하의 경로에서 수정하면 된다.

> 아마도 /etc/systemd 이하에서도 가능은 한 듯 하다.
```
Removed /etc/systemd/system/multi-user.target.wants/rc-local.service.
Created symlink /etc/systemd/system/multi-user.target.wants/rc-local.service → /lib/systemd/system/rc-local.service.
```

rc.local, rc-local.service 둘 다 실행 가능하게 퍼미션 올려준다. (+x)  
이후 stop service / restart



## rc.local 스크립트 파일 작성 예시

roscore를 실행 하려면 source를 해서 setup.bash 파일을 읽어줘야지만 roscore 등을 사용할 수 가 있다

```shell
#!/bin/bash
source /opt/ros/noetic/setup.bash
source /home/myuser/catkin_ws/devel/setup.bash
roscore &

## 또는 
roscore &
ROSCORE_PID=$!
echo $ROSCORE_PID

sleep 1s   ## roscore 를 하고 좀 여유있게 기다려준다?? ㅋ 

## 또는 bash 명령어 사용
bash -c "roslaunch mypkg mylaunch.launch "

## 또는 그냥 사용
rosrun mypkg mynode &
NODE_PID=$!
echo $NODE_PID
roslaunch mypkg mylaunchfile &

return 0
```

> 변수를 만들어주고 $! 로 넣어주면 pid를 받을 수 가 있다.   
$! 은 백그라운드에서 돌아가고 있는 마지막 실행 PID를 받아올 수가 있다.  

> 참고로 --wait 이란 명령어는 없는 듯 하다. 블로그 등 자료에서는  & --wait 으로 사용하는데  
그런 명령어는 없는 듯 하다. 대신 wait 명령어는 있으나, 끝날 때까지 block을 해준다.


PID 를 받는 것은 아주 잘 되므로 파일을 만들어서 추후 관리해도 좋을 듯 하다.












