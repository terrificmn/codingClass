ros::package class를 사용하려고 인쿠르드를 해서 사용할려고 하지만....   

이렇게만 하면 package.h 파일을 제대로 불러오지를 못해서  
`ros::package::getPath()` 를 사용을 하면 에러가 발생  


## CMakeLists.txt 파일 수정
CMakeLists.txt을 수정해야한다  
```
find_package(catkin REQUIRED COMPONENTS
	roscpp roslib
)
```

> find_package에만 추가를 해주면 되고 catkin_pakcage에는 필요없다   
> 그리고 package.xml에도 넣어줄 필요가 없음 (catkin_package에 넣어주는 경우에는 package.xml에도 dependencies를 추가해줘야한다)

고로 이제는 cpp 파일내에서 인쿠르드만 해주면 되겠음

```cpp
#include <ros/package.h>

std::string pkg_path = ros::package::getPath("pckage이름");
```

그러면 ros 패키지의 경로를 알아서 string 변수에 넣어준다.  
