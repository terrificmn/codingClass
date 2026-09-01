라이브러리 만들기 위해서 .h (header 파일)을 추가하고  
CMakeLists.txt 파일을 수정하는데  

C++ library로 추가해준다면 같은 소스로(경로)로 add_executable() 이 추가가 되지 않는다   

어차피 라이브러리화 한다면 다른 cpp파일에서 include해서 사용하면 될 듯 하지만  

테스트 할 경우에는 C++ library 추가하는 부분을 주석처리하고  
add_executable() 부분을 넣어서 사용하다가 


```cpp
## Declare a C++ library
# add_library(${PROJECT_NAME}
# src/pubcmd.cpp
# )

add_executable(${PROJECT_NAME} src/pubcmd.cpp)
add_dependencies(${PROJECT_NAME} ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(${PROJECT_NAME}
${catkin_LIBRARIES}
)
```

> 추후  테스트가 끝마면 main함수를 제거한 후  다시 C++ library 부분을 주석처리를 다시 해제하고 
반대로 add_executable()을 주석처리 한 후 사용하면 될 듯 하다


