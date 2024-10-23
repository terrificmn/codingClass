# colcon build
ros2 colcon build 할 경우에 기본적으로 

```
--symlink-install   
--packages-select <패키지명>
```
많이 사용, 


parallel executor를 이용해서 cpu thread 할당 해주기   
메모리가 부족한 경우 유용하게 사용할 수 있다. 


```
colcon build --parallel-workers 2
```


