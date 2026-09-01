# header include error
서로 header filed을 include 할 경우에 자주 발생   
```
error: expected class-name before '{' token 

```

서로 중복해서 include를 할 경우에 먼저 include 한 쪽에서  
preprocessor 에서 `#ifndef MY_H` 와 `#define MY_H` 을 진행하고 나서   

다음에 다른 header 파일에서 다시 my_h 파일을 인쿠르드 하게 되면 이미   
define 이 되어 processed 때문에 스킵을 하게 되어서   

해당 클래스 또는 함수 등을 사용하려고 할 때 에러가 발생 하는 것

## forward declaration
forward declaration 을 사용해서 미리 선언해주면  


만약 "my_file.h" 의 클래스가 MyFile 이라면  

#include "my_file.h" 대신에   

cpp 파일에 해줘야 한다.  class MyFile  로 사용


TODO: 좀 더 업데이트 하기



