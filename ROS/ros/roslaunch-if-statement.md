# roslaunch 에서 if 사용하기
그룹 태그를 사용해서 if를 사용해 줄 수가 있다.   
먼저 arg 를 먼저 만들어준다. **default**  값을 꼭 넣어 준다.

```xml
   <arg name="use_example" default="true" /> 

    <group if="$(arg use_example)" > <!-- 위의 arg가 true이면 Go -->
      <!-- <node ... /> 를 실행하거나
      <include ... /> 등을 실행하거나  -->
    </group>

```

- false 상황 만들기  
위와 거의 똑같고, *if* 대신에 *unless* 를 사용해주면 되고, 이때에는 arg가 false 일 경우에만 작동하게 된다.


## eval 을 사용하기
`$(arg foo)` 사용하는 것 처럼 eval 을 사용해서 값을 비교할 수 있는 듯 하다.   
> 하지만 테스트는 못 해봄. 다음에 테스트 후 업데이트 하자

```xml
<arg name="team" default="blue" />

<group if="$(eval team == 'Blue')">
</group>

```



## passing argument [CLI]
일반적으로 roslaunch 명령어에다가, `아규먼트변수:=값` 를 사용해서 실행하면 된다.
```
$ roslaunch my_file.launch use_example:=my_value 
$ roslaunch %YOUR_ROS_PKG% my_file.launch use_example:=my_value
```

