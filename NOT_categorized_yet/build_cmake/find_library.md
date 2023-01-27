
## foo.so 라는 라이브러리를 추가하고 싶을 때 

먼저 find_library() 를 이용해서 라이브러리를 찾아준다.  
리눅스 기준으로 .so 파일로 되어 있는데~ gpio 라이브러리를 예를 들어서 ...  

find_library(FOO_LIB foo [path])    
FOO_LIB에 foo 라는 라이브러리를 찾아서 그 path를 이용하게 된다.

```cmake
find_library(WIRINGPI_LIB wiringPi)
```

CMake는 이제 /usr/lib,  /usr/lib64, 그리고 환경변수 PATH의 경로를 다 찾는다   

즉, wiringPi 가 설치되어 있는 경로를 설정해줘야한다. 해당라이브러리는 /usr/... 에 없으므로   
PATH에 넣을 수도 있을 듯 하나, 

해보지는 않음 (그냥 참고) 어차피 해당 터미널에서만 적용된다  
```
export PATH=$PATH:여기에라이브러리실경로
```

그것도 보다는 CMakeList 파일에서 set을 이용하면 될 듯 하다. find_library하기 전에 사용해야함
```cmake
set(WIRINGPI_LIB "/path")
```



## target_link 하기
위의 FOO_LIB으로 사용할 수가 있다. 연습으로는 WIRINGPI_LIB이 됨
`target_link_libraries(프로젝트명 PRIVATE ${FOO_LIB})`


현재 내 프로젝트가 myProject라면  
```
target_link_libraries(myProject PRIVATE ${WIRINGPI_LIB}
```

여기에서 PRIVATE, PUBLIC, INTERFACE 등을 선택해서 사용한다  

[더 알아보려면 여기 참고 cmake]([https://cmake.org/cmake/help/latest/command/target_link_libraries.html](https://cmake.org/cmake/help/latest/command/target_link_libraries.html))


## 헤더파일 추가
추가로 헤더파일을 추가할 때에는   
find_path 를 이용해서 설정을 해주고 
```
find_path(FOO_LIB foo "/path/헤더파일")
```
이것도 테스트 안 해봄;;

그리고 target_include_directories() 를 해준다    
> target_link_libraries와 비슷하다

위의 FOO_LIB을 이용해서 
```cmake
target_include_directories(myProject PUBLIC ${FOO_LIB})
```



## prefix와 확장자는 생략

위에서 라이브러리를 가져올 때 보면 .a 파일이나 .so 파일인데   
prefix로 lib이 붙는다.  예를 들면 libamcl_map.so, libsend_data_mqtt.so, liblib_path_sub.so

그래서 prefix인 lib 빼고, 확장자 빼고 사용하면 된다   
실제 라이브러리 이름은 amcl_map, send_data_mqtt, lib_path_sub 이 되게 된다   

그래서 예를 들면  
```
target_link_libraries(myProject send_data_mqtt)
```

