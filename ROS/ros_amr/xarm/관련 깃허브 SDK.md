
[파이썬 버전 깃 허브](https://github.com/xArm-Developer/xArm-Python-SDK)


깃 클론 한 후, 해당 디렉토리로 이동한 후에   
```
python3 setup.py install
```
로 해주면 잘 설치가 되었으나.. 

ROS melodic, 우분투 18.04, 파이썬 3.6 인지는 몰라도..  

$PYTHONPATH 관련 에러 발생  
기존의 $PYTHONPATH 변수에는 
```
/home/유저명/catkin_ws/devel/lib/python2.7/dist-packages:/opt/ros/melodic/lib/python2.7/dist-packages
```
이런식으로 되어 있는데 

퍼미션 에러가 발생한다 ...

퍼미션 에러일 경우
[Errno 13] Permission denied: '/usr/local/lib/python3.6/dist-packages/test-easy-install-28840.write-test'

그래서 '/usr/local/lib/python3.6/dist-packages/' 에 퍼미션을 추가할 수 있지만..
```
sudo chmod a+x /usr/local/lib/python3.6/dist-packages/
```

> 소용없음;;, sudo 로 설치를 해도 마찬가지


그래서 다시 설치를 --user 옵션을 넣어서 해결
```
python3 setup.py install --user
```

이렇게 되면 .local 안에 설치를 한다 (/usr/local/lib/python3.6이 아닌!)   

설치는 홈디렉토리의 유저 디렉토리의 .local 안에 설치가 되므로 /usr/bin/python3 으로 실행을 했을 때 xarm 파일을 import를 못하는 에러가 발생함

그냥 python3로 실행을 해주면 잘 실행이 된다   

> vscode에서 실행할 시에 /usr/bin/python3 로 실행이 되게 되어 있어서 일단은 그러하다   
> 아마도 환경변수, 심볼릭링크 등을 동원하면 해결 될 듯 하나..  
> 아직 해보지는 못하고 그냥 터미널에서 python3 로 실행함

그리고 python3.8, 3.7 버전 windows, ubuntu 에서는 각각 문제 없이 잘 설치되었고 실행도 잘 됨





