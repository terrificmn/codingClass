하나의 메타 패키지로 만들 이름의 디렉토리를 만들어 주고 (먼저 catkin_ws로 이동)   
```
cd ~/catkin_ws/src
mkdir meta_pkg
cd meta_pkg
```

같은 이름의 처음 만든 디렉토리와 같은 이름의 패키지를 하나 만든다   

```
catkin_create_pkg meta_pkg
```

방금 만든 패키지로 이동해보면  
이제 다른 의존성은 하나도 안 주고 만들었으므로 package.xml과 CMakeLists.txt 파일만 만들어 진다  

```
cd meta_pkg
```

package.xml 파일을 열어서 그 안에 넣고 싶은 패키지를 exec_depend에 추가한다  
```
...생략
<buildtool_depend>catkin</buildtool_depend>
<exec_depend>pkg_1</exec_depend>
<exec_depend>pkg_2</exec_depend>
<exec_depend>pkg_3</exec_depend>
<export><metapackage/></export>
```


CMakeLists.txt 파일의 프로젝트에는 meta_pkg 만 넣어주고   
catkin_metapackage() 를 추가해준다 
```
cmake_minimum_required(VERSION 3.0.2)
project(meta_pkg)
find_package(catkin REQUIRED)
catkin_metapackage()
```


이제 다시 상위 디렉토리로 이동해서 메타 패키지 안에 필요한 pkg_1, pkg_2, pkg_3을 이동 시켜주면 된다  

이런 구조가 되게 된다 

meta_pkg/   
├── meta_pkg   
├── pkg_1  
│   ├── launch  
│   ├── rviz  
│   └── urdf  
├── pkg_2  
│   ├── config  
│   ├── launch  
│   ├── models  
│   └── worlds  
└── pkg_3  
    ├── include  
    ├── src  
    └── srv  



