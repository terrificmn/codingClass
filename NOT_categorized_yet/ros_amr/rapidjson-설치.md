깃 클론을 받은 후에 


```
git clone 
```
이제 디렉토리로 이동
```
cd ~/rapidjson/include
```
이 안에 또 rapidjson 디렉토리가 있는데  
디렉토리 파일 통으로 /usr/include/ 또는 프로젝트 include path에 넣어 준다 

```
sudo mv rapidjson/ usr/include/
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

