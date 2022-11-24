먼저 catkin tools 를 사용할 때

catkin_ws를 먼저 만들어준다 
```
mkdir -p catkin_ws/src
```

그리고 2번째 워크스페이스를 또 만들어 준다

```
mkdir -p catkin_second_ws/src
```


첫 번째 catkin_ws에서 catkin_second_ws를 같이 열 수 있게 해주는데  
$CMAKE_PREFIX_PATH를 쏜을 봐야한다. 

caktin config --extend /opt/ros/noetic  처럼 해주게 되면 
explicit 이라고 생기는데 --extend로는 2개의 워크 스페이스를 할 수가 없다

먼저 처음의 catkin_ws에서 catkin build 를 해준다 
그러면 devel, build 등이 생기는데 devel 디렉토리에서 _setup_util.py 확인해 보면
```
ls -l devel/_setup_util.py
```

심볼릭 링크로 되어 있고(참고하자)
```
_setup_util.py -> /home/sgtubunamr/catkin_ws/devel/.private/catkin_tools_prebuild/_setup_util.py

```
이 파일을 수정해주면 같이 적용이 되니... 열어준다 

```
cd devel
vi _setup_util.py
```

/ 를 입력 후 검색을 하자 CMAKE_PREFIX_PATH = 까지 검색을 해주면 한개가 나오는데..
```
if not args.local:
    # environment at generation time
    CMAKE_PREFIX_PATH = r'/home/sgtubunamr/catkin_ws/devel;/opt/ros/noetic'.split(';')
```

이런식으로 되어 있는데 중간에 catkin_second_ws 를 넣어주고 ;로 마무리 한 후 저장 후   
한번 clean 후에 다시 빌드를 해준다 
```
CMAKE_PREFIX_PATH = r'/home/sgtubunamr/catkin_ws/devel;${HOME}/catkin_second_ws/devel;/opt/ros/noetic'.split(';')
```

이렇게 하고 .bashrc 파일에는 최소 2번째 ws를 넣어준 후에 source ~/.bashrc 를 하거나   
새로운 터미널을 띄운다음에  

cd ~/catkin_second_ws
로 이동을  한 후에 빌드를 해보자 (src 파일에는 아무것도 없어도 됨)

빌드가 끝난후에 
```
catkin build
catkin config
```
를 해서 보면

```
Profile:                     default
Extending:          [env] /home/sgtubunamr/catkin_second_ws/devel:/opt/ros/noetic
Workspace:                   /home/sgtubunamr/catkin_ws
```
이런식으로 나오게 된다   


이렇게 되면, 1번째 catkin_ws를 에서 패키지 A를 build를 하려고 할 때, 의존성 패키지가 catkin_second_ws 의 패키지B 가 필요하다고 하면   
원래는 빌드가 실패를 하는데,  

이제는 워크 스테이션을 두 개다 인식을 하므로 빌드를 잘 하게 된다 

> 혹시라도 catkin build 를 하다가 현재 CMAKE_PREFIX_PATH가 다르다고 나오는 경우가 있다, 그런 경우에   
catkin clean 을 해 준뒤에 다시 catkin build 를 해주면 된다  


