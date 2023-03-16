# rapidjson 설치

깃 클론을 받은 후에 
```
git clone https://github.com/Tencent/rapidjson.git
```

이제 디렉토리로 이동해서 보면 include 디렉토리가 있는데 rapidjson 패키지는  
header 파일만 있으므로 빌드나 설치가 필요 없다   

> header only c++ library

그냥 /usr/include 디렉토리에 복사 또는 이동 시켜주면 된다     

```
cd ~/rapidjson/include
```
이 안에 또 rapidjson 디렉토리가 있는데  
디렉토리 파일 통으로 /usr/include/ 또는 프로젝트 include path에 넣어 준다 

```
sudo mv rapidjson/ /usr/include/
```

이제 나머지 파일은 지워도 됨

```
cd
rm -rf rapidjson/
```


이제 cpp 코드에서 인쿠르드해서 사용하면 된다 
```cpp
#include "rapidjson/document.h"
#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"
#include <iostream>
```


https://github.com/Tencent/rapidjson/

현재는 json을 받은 상태는 아니므로 추후 업데이트 

튜토리얼은  여기  
https://rapidjson.org/md_doc_tutorial.html


필요할 경우에는 넣지만, include만 넣어준 것이기 때문에 필요 없겠지만 혹시라도...참고로
흠.. 잘 되던 것인데, 아마도 다른 방식으로 설치를 하던가 했었나보다..  
find_package를 하게 되면 찾지를 못한다  흠.. 결론은 필요는 없다 
```c
#rapidjson
# find_package(RapidJSON REQUIRED)
# target_include_directories(${PROJECT_NAME} SYSTEM PUBLIC
#   "${RapidJSON_INCLUDE_DIR}")
```
