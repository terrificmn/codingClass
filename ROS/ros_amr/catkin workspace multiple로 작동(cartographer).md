## 여러개 catkin_ws 등록하기
먼저 하나의 워크스페이스를 만든 후에는 catkin_init_workspace가 중요하다. 그래야 이후 여러개가 잘 인식이 된다 

한 2~3개 워크스페이스를 만들어보자  

```
cd ~
mkdir -p catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
```

이렇게 하면 src 디렉토리에 CMakeLists.txt 파일이 생긴다 . 이 파일이 있어야 CMAKE_PREFIX_PATH 변수 등에서 사용이 가능한 듯하다.  
그리고 catkin build 를 해줘서 devel, build 디렉토리가 생기게 한다   

```
cd ~/catkin_ws
catkin build
```

이제 마찬가지로 catkin_ws1, catkin_ws2 를 만들고 같은 방식으로 작업을 해준다   

이제 .bashrc 파일을 열어서 source를 해준다  
```
source /opt/ros/noetic/setup.bash
source $HOME/catkin_ws/devel/setup.bash
source $HOME/catkin_ws_2/devel/setup.bash
source $HOME/catkin_ws_3/devel/setup.bash
```

먼저 ros noeitc를 먼저 해주고, 그 다음에 catkin_ws 하나씩 해주면 됨   
저장 후  `source ~/.bashrc` 를 해주거나 새로운 터미널 창을 열어준다    


이제 터미널에서 echo $CMAKE_PREFIX_PATH 해보면 3개의 워크스페이스를 모두 포함하고,   
/opt/ros/noetic 를 포함하고 있으면 잘 될 것임  

빌드한 것이 이미 있다면 catkin clean 으로 먼저 정리한 후에, bashrc 파일에도 source 지정하지 말고   
처음 상태로 해놓고 하면 더 잘 됨

> 만약 catkin_ws가 인식이 잘 안 된다면  ~/.bashrc 파일에서 source를 제일 마지막에 해주자  
> 처음 설정 부터 꼬였는지는 몰라도.. 처음에 넣어주면 catkin_ws를 잘 인식이 안되고, 마지막에 넣으니 잘됨;;; 이상하지만.. 참고

아래 하드코딩으로 직접 하는 방법과도 연결이 되는 부분이.. 
처음에 ws를 catkin build를 해주게 되면 그 때의 워크 스페이스 경로가 CMAKE_PREFIX_PATH에 저장되는데 그게 바로 아래서 설명하는 `_seup_util.py` 파일에 생성이 되면서 지정되므로 
추후 ws를 지우고 다시 하려고 할 때에도 직접 입력해서 지울 수도 있고, 또는 catkin clean으로 빌드 된 것 포함 지우고 다시 할 수도 있다


## 하드코딩으로 직접 ws를 지정해주는 방법 1
먼저 catkin tools 를 사용할 때

요약:  각각의 catkin_ws 즉, 워크스페이스에는 devel 디렉토리가 생기는데 (빌드 시)   
devel 디렉토리의 심볼릭링크 파일에서 직접 CMAKE_PREFIX_PATH 변수에 직접 하드코딩으로 넣어주는 방법임. 

> 처음에 catkin_init_workspace를 안해서 .bashrc 파일에 넣어도 마지막 하나의 워크스페이스만 인식 되는 문제가 있어서.. 결국 직접 지정을 했지만  워크스페이스를 잘 지정한다면 무리없이 하드코딩 없이도 가능하다...!

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
main 함수 안에 있음
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


