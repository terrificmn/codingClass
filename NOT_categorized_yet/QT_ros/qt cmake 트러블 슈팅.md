
처음 Project를 만들 경우에   
Application(qt)를 Qt Widgets Application, Qt Quick Application으로 만들 수가 있는데    
Build system을 정해야하는데 build system을 CMake로 정해서 할 경우에 위와 같은 문제가 발생하는 듯   

프로젝트를 cmake 빌드시스템으로 만들고 시작하게 되면 최초 cmake 빌드가 한번 실행해야하는데  
CMake 에러가 나면서 빌드가 중단 된다   
그리고 
```
CMake process exited with exit code 1.
No CMake configuration found
```

최초 cmake로 빌드가 안되어서 최초 파일 디렉토리 및 파일들도 생성이 제대로 안된다  

일단 CATKIN_DEVL_PREFIX와 상관이 있는 것 같기도 하고,...    

catkin 관련해서는 bashrc에서 주석처리 후 해도 결과는 같음   
LD_LIBRARY_PATH ,  CATKIN_PREFIX_PATH 등도 별 소득은 없었음..   

아마도 CMAKE_PREFIX_PATH 등이 이미 정의 되어 있어서 그것들이 자꾸 처음 빌드할 때 끼어들어서  /catin_ws/devel 등을 참조하게 되어서 파일을 찾을 수 없다고 하는 듯 하다   

어쨋든  ..

## 해결법 


왼쪽의 Projects 탭을 가서  
Build & Run 부분을 보면 build, Build Settings를 보게 되면   

여기에서도 Build directory부분에서 No CMake configuration found라고 뜬다  

Initial Configuration 부분이 있는데 열심히 바꾸려고 했지만 별 소용없고  그냥 그대로 두는 것이 좋고   

Additional CMake options 부분이 있는데   
이부분에 CATKIN_DEVEL_PREFIX가 들어가 있다. 아마도 ros plugin 때문에 혹은 catkin_ws 관련해서   
옵션 부분이 붙게 되는 것 같은데  

**여기 전체를 다 지워준다. 어차피 ros 관련해서 사용할 게 아니기 때문에    
그리고 Re-configure with Initial Parameters 를 클릭해준다  **

그러면 최초 빌드가 되면서 파일들도 잘 만들어준다   (최초 빌드가 안되면 Source Files 등, 다른 디렉토리가 없다 )

추후 다시 Projects의 Build & Run 부분을 보면  
CMAKE_PREFIX_PATH 가 /home/유저/Qt/6.3.0/gcc_64 로  되어 있다   
QT_QMAKE_EXECUTABLE 은 /home/sgtubunamr/Qt/6.3.0/gcc_64/bin/qmake  
등.. 더 많은 변수들이 정의 되어 있음   

> 아마도 CMAKE_PREFIX_PATH 부분에 catkin_ws/devel 등이 (ROS관련) 들어가면서   
> 정작 qt 관련 파일들을 못찾아서 발생하는 문제 였던 거 같다   


이제 소스 코드를 고치고 빌드를 해보면 잘 된다!

