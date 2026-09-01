# gazebo hello world

패키지 gazebo_plugin_tutorial을 참고한다  




## 소스파일
소스파일은 hello_world파일을 보면 .cpp로 저장을 하고,   
특정 장소에 디렉토리를 만들어준다  

> catkin 을 사용안하고 mkdir로 만듬

```
mkdir -p ~/gazebo_plugin_tutorial/src
```

```cpp
#include <gazebo/gazebo.hh>

namespace gazebo
{
    class WorldPluginTutorial : public WorldPlugin   // WorldPlugin을 상속
    {
        public: WorldPluginTutorial() : WorldPlugin()
                {
                printf("Hello World From Gazebo\n");
                }

        public: void Load(physics::WorldPtr _world, sdf::ElementPtr _sdf)
                {
                }
    };
    GZ_REGISTER_WORLD_PLUGIN(WorldPluginTutorial)

    // GZ_REGISTER_WORLD_PLUGIN marcro 인데 각각의 plugin 타입을 매칭해 register matcro라고 함
}
```

클래스의 생성자에 간단하게 print로 출력   


## CMakeLists.txt 만들고 빌드
CMakeLists.txt 의 list(APPEND... )는 사용하지 않는다. make가 안됨  
```
#list(APPEND CMAKE_CXX_FLAGS "${GAZEBO_CXX_FLAGS}") 지워 버리는 게 좋다
```

이런 의견들이 있음 
> C++11 mode (or higher) have been default since GCC version 6.   
That specific flag for that specific C++ standard version  
isn't needed since a few years back.

위를 사용하면 아래처럼 오류 발생
```
c++: fatal error: no input files
compilation terminated. 
```

> 예제 사이트가 예전 버전이어서 그런듯..

## CMakeLists.txt 파일 
딱 이정도면 빌드하는데에는 문제가 없었음   
ubuntu20.04,  g++ (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0

```c
cmake_minimum_required(VERSION 2.8 FATAL_ERROR)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")
find_package(gazebo REQUIRED)
include_directories(${GAZEBO_INCLUDE_DIRS})
link_directories(${GAZEBO_LIBRARY_DIRS})

add_library(hello_world_gazebo SHARED src/hello_world.cpp)
target_link_libraries(hello_world_gazebo ${GAZEBO_LIBRARIES})
```

cakin 을 사용안하고 직접 cmake을 할 수 있다  
디렉토리로 이동 후에 build 디렉토리를 만들고 cmake을 해준다 

```
cd ~/gazebo_plugin_tutorial
mkidr build
cd build
cmake ..
```

빌드가 되면 (build디렉토리), make을 해준다. so 파일 라이브러리가 생긴다 
```
make
```

```
Scanning dependencies of target hello_world_gazebo
[100%] Linking CXX shared library libhello_world_gazebo.so
[100%] Built target hello_world_gazebo
```



## world파일 생성하기
월드 파일안에 plugin 태그를 생성해서 so파일 라이브러리를 연결시켜주게 된다.  

월드 디렉토리를 만들고 그 안에 hello.world 로 파일을 만든다 (같은 패키지 내)

```xml
<?xml version='1.0'?>
<sdf version='1.6'>
    <world name="default">
        <plugin name="hello_world_gazebo" filename="libhello_world_gazebo.so"/>
    </world>
</sdf>
```

이제 이 world파일을 통해서 실행을 하게 된다 


## gzserver 실행하기
먼저 환경 변수를 등록해준다 `GAZEBO_PLUGIN_PATH`  
so 파일이 있는 build 디렉토리까지 지정을 해준다 
```
export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:~/패키지가_있는_디렉토리/gazebo_plugin_tutorial/build
```


실행은   
`gzserver {월드파일의 경로} {--옵션}`

```
gzserver /home/user/gazebo_plugin_tutorial/world/hello.world --verbose
```

이제 hello world가 출력되는 것을 볼 수 있다


## 나머지는 소스코드를 확인하자

gazebo_plugin_tutorial  패키지를 참고하자  



## 참고 model_push 클래스를 추가하고 cpp 및 cmake

CMakelists.txt
```c
add_library(model_push_gazebo SHARED src/model_push.cpp)
target_link_libraries(model_push_gazebo ${GAZEBO_LIBRARIES})
```


모델 같은 경우에는 다른 점은 gzclient를 실행을 시켜주는 것이다   
world파일을 여는 것은 같다. 전체 경로를 열거나 직접 이동 후에 world파일 경로를 지정해도 된다    

```
//패키지로 이동 후에
gzserver -u model_push.world
```
> gazebo를 실행한 상태라면 gzserver를 실행할 수가 없다 



이런 오류
```
[Err] [Master.cc:96] EXCEPTION: Unable to start server[bind: Address already in use]. There is probably another Gazebo process running.

```

gazebo를 끄거나   그리고 다른 터미널에서 client를 실행. 가제보가 열린다  

```
gzclient
```
