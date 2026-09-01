# Qt 관련 core 패키지를 못 찾는 경우

qt QSettings 를 사용하려고 할 때 이런 현상이 발생.   

```
undefined reference to `vtable for Settings qt
```

헤더파일을 못찾는 현상, ros에서 include 관련 CMakeLists.txt 파일을 설정해주면 보통은 헤더파일을   
따로 정의 안해도 컴파일이 잘 되었는데, 뭔가 꼬였을지는 몰라도 헤더파일을 못 찾음   

헤더파일을 
```
add_executable(${PROJECT_NAME}
    include/myPkg/settings.h
)
```

식으로 해결..


그 외에 QTcore 관련 패키지를 사용하려면  
```
find_package(Qt5 REQUIRED COMPONENTS Core)
target_link_libraries(myta${PROJECT_NAME} PRIVATE Qt5::Core)  ## or PUBLIC
```

> QT관련해서는 qt 공식 사이트 매뉴얼을 참고하면 좋다. Header 및 CMake관련 잘 나와 있다.   

