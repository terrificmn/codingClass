# sheel source include
흔히 말하는 include 같은 기능을 bash 쉘에서는 쉽게 가능하다.   

많이 사용했던 `source` 기능이다  
include 하려고 하는 파일을 불러오게 된다  

먼저 main으로 사용할 shell script를 만들어 준다 
```shell
#!/bin/bash

### 쉬뱅을 해준 후에 불러오고 싶은 파일을 넣어준다.
source ./example_include

echo $test
```

그리고 인쿠르드할 example_include 파일이 있다고 치면  
```shell
## 쉬뱅을 할 필요 없다 (#!/bin/bash)

test="hello sheel"
```

이것을 활용하면 script 파일을 나눠서 사용할 수가 있고, 읽은 (include한) 파일에서는  
변수들을 다 활용할 수 있으니 편하다 