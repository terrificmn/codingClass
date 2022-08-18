
예를 들어서 이런식으로 사용하다가 

```cpp
#include <tf/transform_listener.h>

...

this->listener.waitForTransform(this->odom_frame_id, this->base_frame_id, now, ros::Duration(4.0));
```

컴파일 단계에서 
```
"undefined reference to tf::Transformer..." 
including "tf" in the "find_package" part of the CMakeLists.
```

의외로 간단하다  

먼저 find_pakcage에 추가
```
find_package(catkin REQUIRED COMPONENTS
    roscpp
    ...
    ...
    생략..
    tf
)
```

그리고 pakcage.xml 에도 추가해준다 
```xml
<build_depend>roscpp</build_depend>
...
생략
<build_depend>tf</build_depend>

<build_export_depend>roscpp</build_export_depend>

<exec_depend>roscpp</exec_depend>
... 생략..
<exec_depend>tf</exec_depend>
```


