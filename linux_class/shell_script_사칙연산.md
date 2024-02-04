# 사칙연산

let 을 사용해서 연산을 할 수 있고.  
띄어쓰기는 허용되지 않는다.

```sh
#!/bin/bash

test_a=100

let result=test_a/10
echo ${result}
let result=$test_a+100
echo $result
```

> 변수는 $변수, ${변수} 식으로 사용할 수가 있다.   
연산 중 =으로 할당할 때에는 변수명을 그대로 사용할 수가 있다  
대신 echo로 출력할 때에는 $를 붙여줘야한다.






