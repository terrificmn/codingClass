# ros 파이썬 파일 실행가능하게 만들어 주기
직업학교에서 최종 프로젝트를 하느라고 블로그를 계속 못했는데~  
이제 마무리가 되어서 정말 오랜만에 블로그 포스팅을 한다~

Python 코드로 되어있는 프로그램을 ROS 에서 실행시킬 때 하는 방법이다~

먼저 패키지를 만들어 주자~  catkin_ws/src 로 이동
```
cd catkin_ws/src
```
간단하게 기본적인 패키지로 만들어보자, 패키지를 만들때 rospy는 넣어줘야한다  
아래의 my_pkg 부분은 패키지명이 된다 (원하는 이름으로 만들어 준다)
```
catkin_create_pkg my_pkg rospy
```

> rospy는 ROS에서 파이썬 코드를 실행할 수 있게 만들어주는 Python client library 이다  
신기하게도 많은 ROS tool들 rostopic, rosservice 등이 rospy가 사용되었다고 한다

<br/>

이제 패키지 디렉토리가 만들어 지면 my_pkg 로 이동을 한 후에 scripts 디렉토리를 만들자
```
cd my_pkg
mkdir scripts
```

이제 사용할 파이썬 코드를 scripts 디렉토리에 복사/이동 해주면 된다
이동한 파이썬 파일을 py_test.py라고 가정해보면

이제 중요한 CMakelists.txt 파일을 수정해주자   
파일을 열어보자

install 부분으로 내려간 후 catkin_install_python(PROGRAMS 로 시작되는 부분의 파일 경로를 적어주면 된다   
아래 처럼 경로와 파일명만 적어준다
```
catkin_install_python(PROGRAMS
  scripts/py_test.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

만약 scripts 디렉토리에 넣지 않고 c++ 코드처럼 src 디렉토리에 만들고 싶으면   
src 디렉토리를 만들고 위의 경로를 scripts가 아닌 src/py_test.py 처럼 해주면 된다

원래 기존에 c++ 코드와 다르게 수정해줘야 할 부분이 많지 않다. 
아마도 python은 빌드가 필요없어서 그런 듯 하다

이제 python 파일을 실행이 가능하게 만들어 줘야한다

예를 들어 py_test.py란 파일을 실행하려면 먼저 권한을 실행 가능하게 바꿔준다
```
cd scripts
sudo chmod +x py_test.py
```

catkin_make 를 하자~
```
cd ~/catkin_ws
catkin_make
```

그리고 이제 rosrun을 실행을 할 수 있다. (실행 권한이 없다면 자동탭 완성이 안됨)

```
rosrun my_pkg py_test.py
```

😁 이제 ros에서도 파이썬코드를 하나의 노드로 실행이 된다! 굿 ㅋㅋ
