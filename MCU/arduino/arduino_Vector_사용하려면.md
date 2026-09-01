# arduino에서 vector 사용하기
stl vector와 비슷한 arduino용 vector 라이브러리 

PlatformIO 를 사용하면 해당 자신의 프로젝트 디렉토리 안의 lib 디렉토리에 깃 클론 해준다   

```
cd ~/Documents/PlatformIO/Projects/my_project/lib
git clone https://github.com/janelia-arduino/Vector.git
```

플랫폼IO 해당 프로젝트의 platformio.ini 파일에 추가
```
lib_deps = Vector
```

main.cpp 파일에서는 `#include "Vector.h"` 로 해주면 된다  

> std:vector 다르다 . 거의 비슷한 기능

해당 깃허브에 가면 아두이노와 platformio 용 예제가 잘 되어 있다 참고하면 된다   

[여기 example 참고](https://github.com/janelia-arduino/Vector.git) 


## 사용

일단 인쿠르드
```cpp
#include <Vector.h>
```

대문자 Vector 로 사용한다. (std::vector<char> 이렇게 말고)  
```cpp
Vector<char> my_vector
```

std::vector 와 비슷하지만, 크게 다른 점은 Dynamically 메모리 할당이 아니라는 점이다.   
컨테이너는 external, statically array로 (c style) 할당한다   
그래서 array와 비슷하지만, 배열은 컨테이너에 내부적(internally) 로 할당,


사용 예제
```cpp
const int ELEMENT_COUNT_MAX = 5;
int storage_array[ELEMENT_COUNT_MAX];
Vector<int> vector(storage_array);
vector.push_back(77);
```



### STL 를 arduino에서 사용하게 해주는 라이브러리 

**경고! 해당 빌드가 잘 안될 수가 있다.**  일단 참고만 하자  

> opencr에서는 실패

Standard C++ for Arduino  

STL 의 vector 등을 사용하려면  

[여기 StandardCplusplus 에서 다운](https://github.com/maniacbug/StandardCplusplus)   

사용법은 lib , 아두이노(libaries) 에 넣어주는 것인데 일단 실패함 . 

그래서 위의 Vector.h 를 사용하자


