
yaml-cpp/yaml.h 파일을 인쿠르드해서 사용하려고 하니~ 패키지를 못찾는다 

패키지는 apt를 이용해서 설치를 할 수 있다 
```
sudo apt install libyaml-cpp-dev
```


c++ 코드내에서 YAML::LoadFile() 함수를 사용하고, 빌드를 하니...

바로 에러가 발생
```
undefined reference to `YAML::LoadFile(std::_ ....생략
undefined reference to `vtable for YAML::Exception'
...
...
...
```
아무튼 이런 undefined reference가 엄청나게 나온다 

이럴 경우에는 먼저 CMakeLists.txt 파일에서 find_package()를 사용해서 yaml-cpp를 찾아주고 
```
find_package(catkin REQUIRED COMPONENTS
roscpp yaml-cpp
)
```

이렇게 해서 yaml-cpp를 넣은 후 다시 빌드를 하면 이번에는 
```
Could not find a package configuration file provided by "yaml-cpp" with any
  of the following names:

    yaml-cppConfig.cmake
    yaml-cpp-config.cmake

  Add the installation prefix of "yaml-cpp" to CMAKE_PREFIX_PATH or set
  "yaml-cpp_DIR" to a directory containing one of the above files.  If
  "yaml-cpp" provides a separate development package or SDK, be sure it has
  been installed.

```

패키지 설정파일을 못 찾는다고 한다. 친절하게 에러 메세지에 나오는 것 처럼 yaml-cpp_DIR 을 set으로 지정을 해줘야지 제대로 경로를 찾는다.  


먼저 yaml-cppConfig.cmake 파일이나 또는, yaml-cpp_config.cmake 파일의 위치를 찾아봐야한다  
파일 탐색기 nautilus를 사용하거나 

```
sudo find / -name yaml-cpp-config.cmake > result
```

> yaml-cppConfig.cmake 파일을 없었음, 두 번째 파일로 찾아본다  result 파일을 만들고 저장해줌   
> 이유는 결과가 너무 많이 빨리 지나감


```
cat result

결과
/usr/lib/x86_64-linux-gnu/cmake/yaml-cpp/yaml-cpp-config.cmake
```

> ubuntu 20.04 기준에는 위의 경로에 설치가 되어 있었음   
Rocky linux 기준에는 `/usr/lib64/cmake/yaml-cpp/yaml-cpp-config.cmake`   

위 cmake 파일을 열어보면 
```
set(YAML_CPP_INCLUDE_DIR "${YAML_CPP_CMAKE_DIR}/../../../../../include")

set(YAML_CPP_LIBRARIES "yaml-cpp")
```
이렇게 되어 있는데, 이제 yaml-cpp_DIR를  경로를 제대로 설정을 해주게 되면  
위의 YAML_CPP_INCLUDE_DIR, YAML_CPP_LIBRARIES 변수들을 사용할 수 있게 된다  

실제로는 yaml-cpp 경로까지만 SET으로 지정해준다

이제 최종 정리를 하면 아래와 같다 
```
cmake_minimum_required(VERSION 3.0.2)
project(my_project)

set(yaml-cpp_DIR /usr/lib/x86_64-linux-gnu/cmake/yaml-cpp/)

find_package(catkin REQUIRED COMPONENTS
	roscpp roslib yaml-cpp
)

include_directories(
	include
	${catkin_INCLUDE_DIRS}
	${YAML_CPP_INCLUDE_DIR}
)

target_link_libraries(${PROJECT_NAME}
	${catkin_LIBRARIES}
	${YAML_CPP_LIBRARIES}
)
```

### qt cmake에서도 비슷하다
- set을 해주고   `set(yaml-cpp_DIR ....)`
- find_package 추가 `find_package(yaml-cpp REQUIRED)`
- 마지막으로 target_link_librearies에 추가해준다    
`target_link_libraries(appmyapp PRIVATE Qt6::Quick ${YAML_CPP_LIBRARIES})`
- include_directories까지는 안해도 작동하는 듯 하다


이제 파일에서 인쿠드를 하고 사용하면 됨
```cpp
#include <yaml-cpp/yaml.h>
#include <iostream>

int main() {
	std::string = "data.yaml"
	YAML::Node yaml_load = YAML::LoadFile(path);
	std::cout << yaml_load["name"].as<std::string>() << std::endl;

	return 0;
}

```


yaml 파일은 이런식이라고 가정하면
```yaml
name: Mark
age: 20
```
결과는 `Mark` 라고 나오게 된다 


[cpp로 yaml-cpp튜토리얼은 여기에서 살펴보자](https://github.com/jbeder/yaml-cpp/wiki/Tutorial)

