## add_library 직접 설정하기
find_library() 를 경로만 있으면 해당 라이브러리를 찾아주지만 
> 물론 경로가 안 맞으면 잘 못 찾는다 ㅠ

add_library는 직접 .a .so 파일의 경로까지 입력해서 넣어준다  

원래는 g++로 해서 컴파일을 할 때에는 -l 옵션을 넣어서 라이브러리를 넣어줘야지 라이브러리까지 잘 컴파일이 되는데 cmake에서는 import를 할 수가 있다   

예
```cmake
add_library(bar SHARED IMPORTED) 
set_target_properties(bar PROPERTIES
  IMPORTED_LOCATION "${CMAKE_SOURCE_DIR}/lib/libbar.so"
  INTERFACE_INCLUDE_DIRECTORIES "${CMAKE_SOURCE_DIR}/include/libbar"
)

set(FOO_SRCS "foo.cpp")
add_executable(foo ${FOO_SRCS})
target_link_libraries(foo bar) 
```

add_library에서 SHARED (.so) 대신에 STATIC으로 할 수도 있다 (.a파일)

~~wiringPI를 예를 들면~~   
실제로는 wiringPi는 so 파일이 없고, h 헤더파일만 있어서 아래 방법으로 성공하지 못함   

어쨋든 아래 방식은 안되지만, 이런식으로 한다는 느낌만 가져가자 ㅋㅋ
```cmake
add_library(wiringPi SHARED IMPORTED) 
set_target_properties(wiringPi PROPERTIES
  IMPORTED_LOCATION "/usr/local/share/gpio_lib_c_rk3399/wiringPi/파일명.so"
)

set(MAIN_SRCS "main.cpp")
add_executable(myProject ${MAIN_SRCS})
target_link_libraries(myProject wiringPi) 
```

