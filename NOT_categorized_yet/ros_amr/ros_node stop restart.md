# ros node 재시작 kill 

특정 rosnode를 종료할 때에는 rosnode cli 를 이용할 수가 있다   
터미널에서  
```
rosnode list
```
로 rosnode의 이름을 확인한 후에 

```
rosnode kill /my_node_name
```
으로 종료시킬 수가 있다   

그리고 나서 원한다면 rosrun pkg nodename 으로 다시 실행을 시킬 수도 있겠다  

이것을 cpp로 적용시키려면 system() 함수를 이용하면 된다   

```cpp
std::string cmd="rosnode kill /my_node_name"

if(무슨무슨 조건일 때) {
	system(cmd);
}
```

이런식으로 사용이 가능하다  


## 더 좋은 추천 방법은?

만약 특정노드를 종료시킨 후에 다시 다시 실행을 해야한다면 위의 경우 처럼 다시 system() 함수를 이용해서 다시 rosrun 명령어를 적용시키면 될 듯 하지만  

roslaunch 파일을 이용해서 node 태그에 respawn 파라미터를 넘겨주는 방식으로 사용할 수가 있다  

> 노드를 재시작하는 경우에 사용

```xml
<launch>
	<node pkg="my_restart_pkg" name="my_restart_pkg" type="my_restart_pkg" output="screen" respawn="true" />
</launch>
```

위의 예 처럼 respawn 옵션을 *true*을 주게 되면 프로그램 내에서 종료시킨다면 다시 재실행이 되게 된다   

> Ctrl+c 로 프로그램을 종료하지 않는 한, 프로그램 내의 코드에 의해서 종료될 경우 다시 node가 재실행이 된다. 물론 roslaunch로 실행을 해준다

cpp 코드 내에서도 특별히 system() 함수를 이용해서 종료시킬 필요 없이  
ros::shutdown() 정도만 해서 SIGINT를 준다면 다시 노드가 재 실행되는 것을 알 수 있다  
(rosnode kill 도 사용하는 방식이라고 한다 xmlrpc shutdown call)

그래서 if구문으로 적절히 사용하면 될 듯 하다.  또는 재시작이 필요할 때 특정 topic을 정해서 구독을 하거나 service topic등으로 이용할 수도 있을 듯 하다  




