참고  
http://docs.ros.org/en/jade/api/catkin/html/howto/format2/building_libraries.html   

ad_library()를 사용하지만 headers 파일은 안되고 cpp만 되는 듯 하다

# 외부 라이브러리를 사용하려면 target_link_libraries()에 설정해준다 
일단 mqtt 라이브러리를 예를 들면 (Paho C, Paho C++ 라이브러리를 빌드 후 cmake install이 된 후에)   
-- 설치법 참고  

해당 라이브러러를 연결을 해줘야 하는데   
Eclipse Paho MQTT C++ Client Library 의 경우에는 그 이름이 paho-mqttpp3 인 모양이다;;;  
파일을 검색해도 나오지를 않는다;;;

어쨋든 이것을 해줘야  
```cpp
#include "mqtt/async_client.h"
```
인쿠르드 인식하고 

undefined reference to `mqtt::async_client::async_client...   
undefined reference to `mqtt::async_client::set_callback(mqtt::callback&) ..  
등의 에러가 발생을 하지 않는다.  

CMakelists.txt에 아래 처럼 추가 한다 
```
target_link_libraries(${PROJECT_NAME}_node
  ${catkin_LIBRARIES}
  paho-mqttpp3 paho-mqtt3as
) 
```


### 헤더 파일 불러오기 
그 밖에 헤더 파일이 모여 있는 라이브러리 등을 불러올 때는 아래와 같이 사용할 수가 있다  
set()을 이용해서 변수를 만들어 주고 경로를 넣어준다   

그리고 header files을 include 하기 위해서는 target_include_directories()를 이용해서 경로를 넣어준다  

```
set(MQTT_HPP_DIR /usr/local/include/mqtt)
set(HEADER_FILES ${MQTT_HPP_DIR}/async_client.h)

## Declare a C++ executable
## With catkin_make all packages are built within a single CMake context
## The recommended prefix ensures that target names across packages don't collide
add_executable(${PROJECT_NAME}_node 
  src/go_mqtt.cpp
  ${HEADER_FILES}
)

add_dependencies(${PROJECT_NAME}_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
target_link_libraries(${PROJECT_NAME}_node
  ${catkin_LIBRARIES}
  paho-mqttpp3 paho-mqtt3as
) 

## header files include
target_include_directories(${PROJECT_NAME}
  PRIVATE
  ${MQTT_HPP_DIR}
)
```

단 위의 경우에도 target_link_libraries()에 연결하지 않으면 에러가 발생한다.  
하지만 기본적으로 헤더파일만 있는 경우, 즉 외부 헤더파일을 위와 같은 방법으로 불러올 수가 있다  

일단

https://github.com/eclipse/paho.mqtt.cpp/blob/master/CMakeLists.txt

CMakeLists.txt 파일 여기에서 89번째와, 91번째에서 단서를 발견;;

일단 set(PAHO_CPP_LIB paho-mqttpp3) 을 한 것이지만 paho-mattpp3을 사용했다느 것을 알 수 있음   
ROS에서 계속 빌드 실패할 때에는 ${PAHO_CPP_LIB} 변수를 계속 사용 했었으나 set으로 설정이 안 되어 있었음   



