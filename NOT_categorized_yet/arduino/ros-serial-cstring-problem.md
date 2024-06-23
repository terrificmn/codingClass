# rosserial cstring 에러
아두이노, 나노 등에서 rosserial 라이브러리를 받아서 사용할 경우,  
빌드시에 cstring을 못 찾으면서 에러 발생.  c++ 라이브러리를 사용하는데 없어서 그렇다고 함

자신의 해당 프로젝트에서 .pio/libdeps/ 이하에서 src 디레토리에서  
msg.h 파일을 찾는다.  

include 를 수정하는데 string.h 파일로 변경해준다.   
```cpp
// #include <cstring> 
#include <string.h> 
```

memcpy()를 사용한 부분이 두 곳이 있는데 찾아서 변경해준다.  
std:memcpy 에서 memcpy 로 변경, 파라미터가 있었는지 기억이 안나지만, 함수 이름만 변경한다.
```cpp
// std::memcpy()
memcpy() 
```

이렇게 하면 빌드가 잘 된다.
