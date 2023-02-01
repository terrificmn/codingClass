main.cpp로 프로젝트 파일이 시작되겠지만, 다른 이름일 경우도 많고   

만약 다른 cpp파일이 있다면~ 이미 만들어진 라이브러리가 아니고  
예를 들어 class1_test.cpp 파일이 있다고하면, 그 파일 class를 main.cpp에서 include해서 사용하는 경우라면 다같이 컴파일이 되어야한다  

CMakeLists.txt 파일에서   

add_executable() 에 추가를 해준다   
```
add_executable(${PROJECT_NAME}
	src/main.cpp
	src/class1_test.cpp
)
```

이후 
```
add_dependencies(${PROJECT_NAME}_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(${PROJECT_NAME}
	${catkin_LIBRARIES}
)
```

이 경우는 main만 실행이 되고, ROS 기준으로 rosrun이 가능하게 되는데  class1_test.cpp 는 따로 실행되는 것이 아니다  

만약 main에서 사용된 class가 아닌 자체적으로 사용해야하는 cpp 파일이라면

아마도 add_executable()을 할 때 프로젝트 네임을 조금 다르게 해주고  
그 이름을 target_link_libraries()로 해야 둘 다 실행이 될 수 있을 것이다   

테스트는 안해봤지만..  
```
add_executable(${PROJECT_NAME}_2 
   src/....cpp
)

//또는 
add_executable(my_project_2 
   src/....cpp
)

//같은 프로젝트명으로 target_link_libraries()를 해준다
target_link_libraries(${PROJECT_NAME}_2
	${catkin_LIBRARIES}
)

또는
target_link_libraries(my_project_2
	${catkin_LIBRARIES}
)
```

테스트는 안 해봄. 안될 가능성 높음!