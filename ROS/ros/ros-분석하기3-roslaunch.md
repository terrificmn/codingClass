
# roslaunch 실행해보기~

> 많이 노드들을 실행하려면 번거롭고 힘들다. 예를 들어 100개의 노드가 있다면 
100개 노드를 rosrun으로 실행하고 물론 roscore 를 포함해서 101번을 실행해야한다

그래서 ROS에서 roslaunch라는 명령어를 제공해서 실행을 할 수 있게 되어 있다

패키지로 이동을 하는데 cd [pkgname] 디렉토리로 이동을 해준다

yh_tutorial 디렉토리로 이동을 하자

```
$ cd ~/catkin_ws/src/yh_tutorial
```

패키지안에 launch 디렉토리가 있어야 한다. 그래서 launch 디렉토리를 만들어 주자
```
$ mkdir launch
```

숨김파일인 .launch 파일도 만들어 줘야한다. xml 형식으로 launch태그로 만들게 된다

```
<launch>
... 이런 형식이다~
</launch>
```

이제 편집기로 파일의 내용을 넣어주자
```
$ code .launch
# 또는
$ vi .launch
```

아래와 같이 넣어주고 저장해 주자~
```xml
<launch>
    <node pkg="yh_tutorial" type="pub_test" name="p_test1"/>
    <node pkg="yh_tutorial" type="sub_test" name="s_test1"/>
    <node pkg="yh_tutorial" type="pub_test" name="p_test2"/>
    <node pkg="yh_tutorial" type="sub_test" name="s_test2"/>

    <!-- pkg=는 패키지이름 type=은 실제실행할 노드이름(파일이름) name=은 그 해당노드가 실행이 될 때 붙어지는 이름 -->
</launch>
```
이제 런치 파일이 만들어 졌다. 혹시 roscore가 실행되고 있다면 roscore가 실행되는 터미널을 ctrl+c를 눌러서 꺼주자~

이제 roslaunch를 이용해서 실행을 시켜보자   
(디렉토리가 launch 디렉토리에 있는지 확인하자)

```
$ roslaunch .launch
```

실행이 되면서 

```
started roslaunch server http://ubun-sc:43625/

SUMMARY
========

PARAMETERS
 * /rosdistro: melodic
 * /rosversion: 1.14.11

NODES
    p_test1 (yh_tutorial/pub_test)
    s_test1 (yh_tutorial/sub_test)
    p_test2 (yh_tutorial/pub_test)
    s_test2 (yh_tutorial/sub_test)
```

이렇게 나오는 것을 알 수 있고 어떤 관계로 표시되는 보기위해서 rqt를 실행해보자

```
rqt_graph
```

해보면 하나의 topic으로 여러개를 실행해서 복잡하게 보인다

<img src=0>

이제 다른 창에 rostopic list 를 해보자  
아래 처럼 topic은 한개만 나온다. 
```
/rosout
/rosout_agg
/yh_topic
```
왜냐하면 실제로 사용하는 것은 topic은 하나 이기 때문임


실제로 사용할 때는 노드를 더 만들거나 패키지를 더 만들 수도 있겠지만
하나의 노드를 가지고 여러번 사용할 때에는 이럴때는 그룹핑을 해주는 것이 좋다.

<br/>

## 그룹핑을 하는 법을 알아보자

다시 로스 런치파일을 수정해주기 위해서 파일 열어 준다

```
$ code .launch
# 또는
$ vi .launch
```

파일 내용은 group 태그를 이용해서 그룹을 지정해주자
```xml
<launch>
    <group ns="yh_group1">
        <node pkg="yh_tutorial" type="pub_test" name="p_test1"/>
        <node pkg="yh_tutorial" type="sub_test" name="s_test1"/>
    </group>
    <group ns="yh_group2">
        <node pkg="yh_tutorial" type="pub_test" name="p_test2"/>
        <node pkg="yh_tutorial" type="sub_test" name="s_test2"/>
    </group>
    <!-- pkg=는 패키지이름 type=은 실제실행할 노드이름(파일이름) name=은 그 해당노드가 실행이 될 때 붙어지는 이름 -->
</launch>
```

저장을 한 후에 다시 로스 런치를 실행해보자
```
$roslaunch .launch
```
그러면 이번에는 화면이 아래처럼 바뀐다

<img src=1>


그리고 나서 다시 rqt_graph 확인하기
```
rqt_graph
```

<img src=2>

그룹화된 것을 알 수 있다





