# colcon build with ament_cmake
(블업완)ros2-cpp파일빌드과정.md 파일에서 설명되어 있는 것 참고  

일단 CMakeList.txt 파일에서 의존성 패키지로 ament_cmake, rclcpp 등을 찾게 해줘야 하고  
이를 빌드할 때 사용하게 된다.  

> ament_cmake 를 사용하지 않는다면 보통 build 디텍토리를 만들고 `cmake ..` 식으로 사용했으나  
이제 colcon build 를 사용할 수가 있다 .


```
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

include_directories(
    ${PROJECT_SOURCE_DIR}/include
)

add_executable(${PROJECT_NAME} 
    src/main.cpp
)

# for an excutable or symlink file
# 노드 실행파일 연결 
install(TARGETS
    ${PROJECT_NAME}
    DESTINATION lib/${PROJECT_NAME}
)

# 필요시 dependencies link
ament_target_dependencies(${PROJECT_NAME}
...
)
# 또는 
target_link_libraries(${PROJECT_NAME}
...
)


ament_package()
```

ros2 에서 관련 의존성 패지키를 연결하려면 ament_target_dependencies() 를 사용
```
## ros2 dependencies
ament_target_dependencies(${PROJECT_NAME}
    rclcpp
    std_msgs
)
```
ros2 관련 패키지에서 사용할 수 있고, includes 등을 자동으로 처리해줌

그 밖에 system 및 다른 lib 등은 필요시 타겟 링크 및 target include 로 처리해준다.
```
# 예
target_link_libraries(${PROJECT_NAME}
    proto
    pthread
    OpenSSL::Crypto 
    OpenSSL::SSL
)

target_include_directories(${PROJECT_NAME} PUBLIC
    ${Protobuf_INCLUDE_DIRS}
)
```

## colcon_ws 안의 install 에 복사
ros2 에서 사용되는 luanch files, config files 등을 복사해서 사용   
ros2 에서는 주로 패키지에서 사용되는 파일들을 symlink 또는 복사해서 사용하게 되므로...

```
install(DIRECTORY 
    config/
    DESTINATION share/${PROJECT_NAME}/config
)

```
> DIRECTORY 부분에서 자신의 패키지 내의 특정 디렉토리를 지정해주는데 예를 들어, config/ launch/ 이런식으로 적어준다.  
/까지 꼭 붙여야지 중복으로 안 만들고 잘 만드는 듯 하다.  

##
package.xml 은
```xml
<package>
    <!-- 생략 -->
  <buildtool_depend>ament_cmake</buildtool_depend>

  <depend>rclcpp</depend>

  <test_depend>ament_lint_auto</test_depend>
  <test_depend>ament_lint_common</test_depend>

  <export>
    <build_type>ament_cmake</build_type>
  </export>
</package>
```
