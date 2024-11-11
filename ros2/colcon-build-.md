# colcon build
ros2 colcon build 할 경우에 기본적으로 

```
--symlink-install   
--packages-select <패키지명>
```
많이 사용, 


parallel executor를 이용해서 cpu thread 할당 해주기   
메모리가 부족한 경우 유용하게 사용할 수 있다. 
**단** 패키지의 jobs 수를 제어해서 하는 방법인 듯 하다.  
그래서 패키지 하나를 빌드할 경우에는 거의 효과가 없는 듯 하다.

좀 더 정확하게 하려면 cmake -j 옵션을 사용해서 빌드에 사용할 cpu 를 제한 해주는 것이 좋은데  
colcon build 에서는 `MAKEFLAGS`를 이용하면 된다. -j 옵션을 사용할 것이므로 cpu 숫자를 결합해서 사용   
```
MAKEFLAGS=-j6
```

일회성으로 사용하게 된다. 
```
MAKEFLAGS=-j6 colcon build --symlink-install --packages-select my_package
```

parallel 도 같이 사용하려면 
```
MAKEFLAGS=-j6 colcon build --parallel-workers 3
```


터미널에 내에서 계속 사용하려면 export 로 MAKEFLAGS 를 지정해주거나 .bashrc 파일에 export 구문을 넣어주자.
