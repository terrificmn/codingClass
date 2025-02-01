# shell script function

함수이름() {   
    local 변수=$1 // 변수에서 파라미터를 받아서 사용
}  

실제로 호출을 할 경우에는 () 안에 argument를 넣어주는 것이 아니라  
차례차례 입력을 하게 된다 

예

```shell
#!/bin/bash

myShellFunction() {
    local param1=$1
    local param2=$2

    echo "param 1 is $param1"

    if [ "$param2" == "true" ]; then
        echo "yes true! $param2"
    fi
}

myShellFunction "hello world" true

```

유용하게 사용할 수가 있다.
