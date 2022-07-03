# roslaunch 를 이용해서 여러개의 노드 동시에 시작하기

저번에는 기본적으로 하나의 노드를 launch 파일을 이용해서 roslaunch하는 방법을 배웠는데 

[ROS 분석하기 3탄! roslaunch 실행해보기~ .launch 파일 만들어서 실행하기 보러가기](http://54.180.113.157/blog/ROS-%EB%B6%84%EC%84%9D%ED%95%98%EA%B8%B0-3%ED%83%84-roslaunch-%EC%8B%A4%ED%96%89%ED%95%B4%EB%B3%B4%EA%B8%B0-launch-%ED%8C%8C%EC%9D%BC-%EB%A7%8C%EB%93%A4%EC%96%B4%EC%84%9C-%EC%8B%A4%ED%96%89%ED%95%98%EA%B8%B0)

이번에는 launch파일을 이용해서 더 많은 노드들(최소 실행 가능한 프로그램)을 실행해보자~

먼저 패키지가 있어야 하는데 publisher 2개 노드와 subsrciber 1개 노드를 동시에 실행하는 luanch파일을 만들어보자




처음에는 숨김파일로 .launch 파일을 만들어야하는줄 알았는데 그런게 아니고 확장자가 
.launch파일로 만들라는 것이였다. 리눅스에서는 . (dot)이 숨김파일이기 때문에 착각을 했다 

어쨌든, 패키지 디렉토리 안에 launch 디렉토리를 만들고 이동
```
$ mkdir launch && cd launch
```

그리고 원하는 편집기로 launch파일을 만들어 준다
```
$ code double_check.launch
```

xml의 launch와 node라는 태그를 이용해서 내용을 만들어 준다
```xml
<launch>
    <node pkg="yh_double_check" type="yh_check_pub1" name="yh_check_pub1" />
    <node pkg="yh_double_check" type="yh_check_pub2" name="yh_check_pub2" />
    <node pkg="yh_double_check" type="yh_check_sub" name="yh_check_sub" output="screen" />
    <!-- output="screen" 옵션을 넣어주면 그 해당 노드에서는 터미널에서 출력이 된다 -->
</launch>
```
pkg에는 패키지이름, type은 노드 이름을 적어주고, name은 해당노드가 실행될 때 붙어지는 이름이다  (대개 노드이름과 같게 해준다)

> 추후 roslaunch로 실행을 하면 터미널에 다른 출력이 되지 않는데, 화면 출력을 하게 해주는것이   
node 태그안에 output이다. 특정노드의 출력을 보고 싶으면 output="screen"이라고 해주면 된다

<br/>

> xml 은 태그들 한 쌍을 이루고 있다. 그래서 \<launch> \</launch> 이런식으로 여는태그와 닫는 태그가 있다. 
하지만 태그를 하나만 사용하는 상태라면 /로 꼭 태그를 닫아 줘야한다. 위 처럼  <node ...생략. /> 이렇게 입력해준다


먼저 launch파일이 없었다면 
```
$ rosrun 패키지명 노드명
```
해서 위의 3개의 노드를 일일이 실행했어야하나, 이제 launch파일이 있다

실행은 launch 디렉토리안에서 해야한다. 이제 실행을 해보자~
```
$ roslaunch yh_double_check.launch
```
이제 2개의 publisher 실행이 되고 subscriber는 화면에는 출력되는 것을 볼 수 있다.



<br/>

## 터틀심 노드 실행하기 서버파라미터 넣어주기
이제는 터틀심을 roslaunch로 실행해보자

먼저 실행을 하고싶은 패키지로 이동해 주자
역시 마찬가지로 패키지 안에 launch 디렉토리와 launch 파일을 만들어 준다

```
$ cd ~/catkin_ws/src/turtle_practice
$ mkdir launch
$ cd launch
$ code turtle_practice.launch
```
이제 내용을 입력할 차례 인데, 위에서 했던 것 처럼 launch태그와 node태그를 이용해서 만들면 된다

잠깐 하기전에 앞서, 원래 터틀심을 실행을 하게 되면
```
$ rosrun turtlesim turtlesim_node
```

<img src=0>

요렇게 배경이 파란색이 기본인데, 이런 부분을 ROS의 파라미터 서버를 이용해서 바꿀 수가 있다
이때에는 /<param/>이라는 태그가 쓰이는데 백그라운드를 rgb값을 이용해서 넣어주면 해당 색으로 터틀심이 시작된다

> 파라미터 서버는 rosparam이라는 명령어로도 확인이 가능하지만 아직은 잘 모름 더 공부가 필요하다

자 이제 launch파일을 입력하자. 파일명은 하고싶은대로 해주면 된다. turtlelaunch.launch 라고 해줬다
```xml
<launch>
    <node pkg="turtlesim" type="turtlesim_node" name="turtle1">
     <!-- 터틀심 배경 바꾸기 background_r,g,b 로 바꾸고 type은 미리 정해진 형식으로 int
     value는 0~255 사이로 넣어준다 -->
        <param name="background_r" type="int" value="0" />
        <param name="background_g" type="int" value="0" />
        <param name="background_b" type="int" value="0 "/>
    </node>
    <node pkg="yh_turtle_keyboard" type="yh_turtle_circle" name="yh_turtle_circle" output="screen"/>
    <node pkg="teleop_twist_keyboard" type="teleop_twist_keyboard.py" name="teleop_twist_keyboard" />
</launch>
```

background_r, background_g, background_b 값을 각각 0으로 넣었으니 검정색 화면으로 나오게 된다

먼저 거북이 배경이 잘 바뀌는지 확인해보자

```
$ roslaunch turtlelaunch.launch
```

<img src=1>


만약 이런 에러가 발생한다면
```
[rospack] Error: package 'teleop_twist_keyboard' not found
```

설치가 안되어 있는 것이므로,   
turtlesim과 자기가 실행하고 싶은 패키지의 노드만 실행을 해도 된다.

설치를 하려면 이렇게 해주면 된다
```
sudo apt-get install ros-melodic-teleop-twist-keyboard
```

[teleop-twist-keyboard 설치/실행 보러가기](/blog) NOT UPDATED

