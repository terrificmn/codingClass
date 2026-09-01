# joystick
무선 방식으로는 USB 동글 방식, Bluetooth 방식이 있다.   

> 아무래도 usb 방식이, 페어링 하는 블루투스보다 편할 수 있다 (특히, gui가 없는 상태에서)   

joystick 관련 패키지
```
sudo apt install joystick jstest-gtk evtest
```

## 테스트
evtest 는 간단하게 조이스틱 패드를 테스트 할 수 있는 프로그램 
`evtest`를 실행하고   
*/dev/input/event숫자* 로 장치가 나오는데 이중에 선택해서 테스트를 해 볼 수가 있다


jstest-gtk 는 GUI 형식으로 보여준다  


[추후 조이스틱 구매 후 다시 연구](https://www.youtube.com/watch?v=F5XlNiCKbrY)

ROS 같은 경우에는 joy 패키지가 있고   
```
rosrun joy joy_node
```
등으로 실행이 가능 한 듯 하다 


또는 
```
rosrun joy_teleop joy_teleop.py 
```
> 정확한 테스트는 못 해봄 


teleop 에서 사용되는 linear 와 angular가 사용이 되는데  
axis_linear, scale_linear, scale_linear_turbo   
axis_angular, scale_angular, scale_angular_turbo   

예
```
axis_linear:
    x: 1
scale_linear:
    x: 0.5
scale_linear_turbo:
    x: 1.0

axis_angular:
    yaw: 0
scale_angular:
    yaw: 0.5
scale_angular_turbo:
    yaw: 1.0
```

이렇게 해서 작동을 하면  /cmd_vel publish 가 될 수가 있다  

> 좀 더 연구 후에 업데이트 하기


