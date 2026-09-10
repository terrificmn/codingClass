## colcon 빌드 에러 
모듈을 못찾는다. 갑자기 빌드를 못하게 된다.
``` 
ModuleNotFoundError: No module named 'em'  
em 을 못찾고 할 때 
```

```
CMake Error at /opt/ros/humble/share/rosidl_adapter/cmake/rosidl_adapt_interfaces.cmake:59 (message):
  execute_process(/home/myuser/.platformio/penv/bin/python3 -m
  rosidl_adapter --package-name cartographer_ros_msgs --arguments-file
  /home/myuser/colcon_cg_ws/build/cartographer_ros_msgs/rosidl_adapter__arguments__cartographer_ros_msgs.json
  --output-dir
  /home/myuser/colcon_cg_ws/build/cartographer_ros_msgs/rosidl_adapter/cartographer_ros_msgs
  --output-file
  /home/myuser/colcon_cg_ws/build/cartographer_ros_msgs/rosidl_adapter/cartographer_ros_msgs.idls)
  returned error code 1:

  AttributeError processing template 'msg.idl.em'

  Traceback (most recent call last):

    File "/opt/ros/humble/local/lib/python3.10/dist-packages/rosidl_adapter/resource/__init__.py", line 51, in evaluate_template
      em.BUFFERED_OPT: True,

  AttributeError: module 'em' has no attribute 'BUFFERED_OPT'
```
자세히 들여다 보면 execute_process가 .platformio/penv/bin/python3 -m 를 사용함을 알 수가 있다.   

원인은 .bashrc 파일에 PATH 를 지정해 놓은게 문제 였다.  
export 에서 
```
export PATH="/home/myuser/.platformio/penv/bin:$PATH"
```

가장 큰 이유는   
`which python` 을 해보면 platformio 에서 계속 사용하는 것을 알 수가 있음..  

바로 해당 내용을 제거하고 source 해주고  

그리고 나서 다시 터미널을 열어보면 
`which python`  
/usr/bin/python3 제대로 나온다. 이제 colcon 빌드를 할 때 문제가 없다.  

다만, 이미 꼬여 있는 경우에는 install/build/log 를 지우고 다시 빌드 하면 잘 된다. 



platformio 의 pio run 을 사용할 경우에는 일단 터미널에서 export 만 일시적으로 사용하자   
새로운 터미널을 열고  
```
export PATH="/home/myuser/.platformio/penv/bin:$PATH"
```

이렇게 하면 `pio run` 등일 잘 작동하고, colcon build 하는데에도 영향을 미치지 않는다. 

