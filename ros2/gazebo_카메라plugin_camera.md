가제보 ros2용 튜토리얼, 조금 짧음
https://classic.gazebosim.org/tutorials?tut=ros2_installing&cat=connect_ros

colcon 빌드를 할려면 깃 허브에서 다운 

보아하니 설치가 되어 있다


```
sudo apt install ros-foxy-gazebo-ros-pkgs
```

데모 카메라를 실행할 수 있다

대신에 조금 길다;; (전체 경로를 적어줘야하는 듯)
```
source /usr/share/gazebo/setup.sh
```

```
gazebo /opt/ros/foxy/share/gazebo_plugins/worlds/gazebo_ros_camera_demo.world 
```
먼저 데모 파일의 내용을 찾아서 사용하자

위의 gazebo_ros_camera_demo.world 파일을 먼저 복사해서 살펴보거나 아님 그냥 내용을 복사하자


camera를 publish 까지 해준다

일단 모델sdf 파일에 카메라 sdf 코드와 plugin 코드를 넣어줘야하고 

모델.sdf 파일에는 
카메라 link 부분안에 (카메라 모양으로 만들어 놓은 부분, 그냥 원통으로 만들어줬다)
visual, collision, 등의 태그 바로 다음에 sensor로 시작하는 태그 부터 넣어주면 된다

그리고 나서 joint 태그를 만들어서 부모와 자식 태그를 지정해주게 된다
(부모는 몸통, 내가 했던 것에서는 chassis, 자식은 카메라link가 된다)



카메라 위치 선정은 gazebo에서 해결했다. 우선 원 모델을 불러와서 편집에 들어간 다음에
하는게 좋다 
!!! 업데이트 할 것!!!
!!! 업데이트 할 것!!!!!! 업데이트 할 것!!!
여기에서는 joint 등의 이름등도 편하게 편집할 수가 있다





가장 단순한 방법으로 해보면

먼저 gazebo 를 실행시킨다음에 거기에서 
Edit 메뉴에 있는 Building Editor 가 있는데 실행 시킨 후에 
벽, 창문등을 만든 다음에 File 메뉴의 Save as 로 저장을 시키면 추후 다시 불러올 수 있다

이제 Building Editor를 빠져나오고 Gazebo도 끄면 

해당 경로에 ~/building_editor_models 에서 모델 파일을 찾아서보면 model.sdf 파일이 생겼고, 추후 이 파일을 사용한다

그래서 가제보가 실행되고 있을 때 언제라도 왼쪽의 Insert 메뉴를 통해서 추가가 가능하다
gazebo가 경로를 알고 있어서 쉽게 클릭만 하면 추가가 된다







먼저 테스트로 가제보 내에서 잘 불러와 지는지 확인해본다

그리고 나서 world 파일에서 런치파일로 열었을 때 모델들을 불러오고 싶다면
모델 sdf 파일 내용을 다 때려 넣거나, 즉, 모델 태그부터 /모델 태그까지

아니면 가제보에서 편집시 저장했던 디렉토리 자체를 패키지 내에 넣어주면 된다

그리고 나서 world 파일에 
```xml
<include>
      <pose>-0.153 -5.549 0.5 0 0 0</pose>
      <uri>model://dolly_custom</uri>
</include>
```
식으로 넣어주면 된다

런치파일 편집법 업데이트하기
런치파일 편집법 업데이트하기런치파일 편집법 업데이트하기런치파일 편집법 업데이트하기런치파일 편집법 업데이트하기


여기는 각종 플러그인의 소스들만 모아놓은 곳
https://medium.com/@bytesrobotics/a-review-of-the-ros2-urdf-gazebo-sensor-91e947c633d7


이 사람 블로그가 정말 많은 도움이 되었음
막연했지만, 결국 하다보니 이해가 어느 정도 되었음
https://robotisim.com/2021/06/21/ros2-tesla-self-driving-robot-p2-gazebo-skid-steering-and-camera-plugins/


그리고 최종적으로 런치파일을 빌드를 한번 해줘야지 제대로 작동한다

> 파이썬 파일도 처음에 빌드 한번 해주고 그냥 코드 고치는 대로 빌드가 할 필요가 없었는데  
인터프리터 랭귀지 이므로, 하지만 가끔 코드 내용을 고쳤는데도 그 전 내용이 실행되는 경우가 있었는데
이 경우에도 colcon build를 해주니 됨









## world파일에 추가를 하려면 
사실 이 부분은 include로 해결이 가능할 듯 한데 아직까지는 정확한 방법을 못 찾았음...

일단 단순 복사 붙여넣기로 사용하는 방법으로 정리
가제보로 ~/building_editor_models에 저장했던 model.sdf 파일이 있는데 
여기의 내용을 모델 태그가 시작하는 부분부터 끝나는 부분까지 복사한다
```xml
<model name='maze_dolly'>
    <pose>2.417 0.2725 0 0 -0 0</pose>
    <link name='Wall_0'>
      <collision name='Wall_0_Collision'>
        <geometry>
          <box>
            <size>7.5 0.15 2.5</size>
          </box>
    
    ... 생략

</model>
```
world 파일에 붙여넣기를 해주면 된다.
world파일을 만들려면 gazebo 상에서 다른 이름으로 저장으로 해서 만들 수도 있고
기존의 empty.world 파일을 복사해서 사용해도 된다

dolly 패키지를 예를 들자면 

먼저 워크스페이스의 src 안의 dolly 패키지 디렉토리로 이동
```
cd ~/my_ws/src/dolly/dolly_gazebo/world
```
여기에 보면 world 디렉토리가 있는데 그 안에 보면
dolly_empty.world가 있다. 복사하고 시작
```
cp dolly_empty.world dolly_backup.world
```

복사한 내용을 이제 dolly_empty.world 파일을 열어서 
```xml
<include>
      <pose>-5.4 4.0 0.33 0 0 0</pose>
      <uri>model://dolly</uri>
</include>
```
> 백업파일을 만들고 원파일을 직접 수정한 이유는 런치파일 실행 단계에서
런치파일에서 empty.world 부분을 바꿔도 건물과 모델이 시작했을 때 보이지를 않는다
그래서 그냥 기존의 empty.world 파일을 사용하고 런치파일도 수정을 안하고 함

막상 런치파일에서 아래 부분을 새로 만든 world 파일로 수정해주면 되는 것 같으나
```
default_value=[os.path.join(pkg_dolly_gazebo, 'worlds', 'dolly_empty.world'), ''],
```

위에서 말한것 처럼 제대로 뜨지를 않는다. 

그래서 일단 empty.world (파일을 백업을 해놓고) empty.world 파일에 건물 추가했던 xml 태그를 몽땅 붙여넣고 런치파일은 수정하지 않는다. (empty.world가 실행 되게 해준다)

어쨋든, 처음 시작을 할때 모델, 건물 한번에 뜨게 하려면 위 방법으로 하면 확실히 된다


## pose 찾아서 태그에 넣어주기
모델과 건물의 시작 위치를 잘 고정해주고 싶다면 
gazebo 프로그램을 실행시킨 다음에 이동 툴을 선택을 해준다음에 (상단에서 2번째 아이콘)

이제 모델을 클릭을 하게 되면 원하는 위치에 이동을 시키고 나서 보면
왼쪽에 Property와 Value가 나오는데 
pose 데이터를 볼 수가 있다 
pose 를 삼각형 모양을(펼치기 버튼)를 클릭해서 보면 xyz rpy 가 나오는데  
x y 의 값을 

empty.world 파일 혹은 실행시킨 world 파일의 열어서 그 안의 pose 태그를 고쳐주면 된다
예를 들어 dolly_empty.world 를 열면 (패키지내의 world 디렉토리)

pose가 0 0 0 0 0 0 /pose 이런식으로 되어 있는 것을 

```xml
    <include>
      <pose>-5.4 4.0 0.33 0 0 0</pose>
      <uri>model://dolly</uri>
    </include>
    
    <model name='maze_dolly'>
        <pose>2.417 0.2725 0 0 -0 0</pose>  
        
        ,.. 생략
``` 

위에서 봤던 x y 값으로 고쳐주게 되면 다시 가제보 world 파일을 실행하면
원하는 위치에서 시작하게 된다



## 하지만 empty.world가 아닌 새로운 파일에 적용하는 방법은 더 찾아봐야할 듯, include만 하면 될 듯 한데 ..쩝.. 방법 찾으면 업데이트 하기
