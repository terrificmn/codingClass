## cartographer 설치 중에 - Noetic
ubuntu foscal 에서는 libabsl-dev 를 지원하지 않는 것(?) 같음  
에러 발생 시 
```
libabsl-dev] defined as "not available" for OS version [focal]
```


/home/sgtubunamr/catkin_fund_ws/src/cartographer  
의 package.xml의
```xml
<!--depend>libabsl-dev</depend-->
```

libabsl-dev depend를 주석 처리한다. 


[카토그래퍼설치 https://google-cartographer-ros.readthedocs.io/en/latest/compilation.html](https://google-cartographer-ros.readthedocs.io/en/latest/compilation.html)  



```
echo $CMAKE_PREFIX_PATH   
```
를 했을 때 예를 들어서   
```
/home/sgtubunamr/catkin_fund_ws/devel:/opt/ros/noetic
```

