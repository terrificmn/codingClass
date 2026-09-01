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

## meta 패키지 가 아닌 colcon build 옵션
결론 부터 말하자면 ROS2 에서는 메타 패키지는 필요 없을 듯 하고,,  
만약 특정 패키지, 예를 들어 custom ros2 메세지 등이라던가.. 같이 필요한 경우에 유용하게 사용할 수 있는 옵션이다.  

메인으로 사용하는 나의 패키지에 예를 들어 my_main_pkg 라는 프로그램이 있다고 하면  
dependency 를 depend 태그를 이용해서 package.xml 에 꼭 넣어주고   
CMakeLists.txt 파일에 find_package() 로 같이 빌드 해야 할 패키지를 등록해주면 대충 준비는 끝난다. 

```
colcon build --packages-up-to my_main_pkg
```

이렇게 하면 의존성이 필요한 패키지를 같이 자동으로 빌드해주게 된다. (물론 소스코드가 있는 경우)   
> 왜 필요하냐면 다른 패키지로 나눠져 있는 경우, 메인 패키지만 빌드하게 되면   
의존성 패키지가 아직 빌드가 안 되었으므로 찾지를 못하는 에러가 발생하기 때문   
물론 그냥 따로 따로 빌드를 해도 된다 ㅋ


#### 이하는 ros2 meta 패키지 관련.... (참고만)
ros2 에서는 딱히 meta 패키지라고 하는 것이 없는 듯하다. 물론 만들 수는 있다.  
ros1 과 같은 방법으로 비슷 하게 만드며, 

```
ros2 pkg create my_meta
```
이후 package.xml 에서 필요한 패키지가 있다면 depend 태그 등을 이용해서 넣어준다.   

ros1 에서는 package.xml 에서 catkin_metapackage() 라는 게 있었지만,, ros2에는 없는 듯 하다.  
대신 기본적으로  ament_package()만 있는 듯 하다.  

**하지만** 이렇게 해도 dependency가 있는 프로그램을 자동으로 빌드를 해주지는 않는다.

FYI: 물론 방법이 있을 수도 있다, 아직 모르겠지만?




