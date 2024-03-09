# cat 커맨드로 파일 쓰기

file 이름을 지정해주고 cat 파일명을 읽는다. 아래와 같이 사용한다
```sh
#!/bin/bash

FILENAME=test_log
cat > $FILENAME << END_LABEL
문자열을 입력1
문자열을 입력2
END_LABEL
```

이렇게 해서 쉘스크립트를 실행해주면 파일이 작성이 된다.

여기에서 사용한 END_LABEL 이라는 것은 해당 END_LABEL 을 만나기 전까지는 계속 입력을 해주게 된다.   
마지막 줄에서 END_LABEL 을 만나면 끝

END_LABEL 은 EOF 등으로 사용자 맘대로 정하면 됨


또한 END_LABEL 을 지정할 때 따옴표를 사용해서 "END_LABEL" 처럼 해줄 수가 있는데 이때에는  
shell script 내에서 변수 등을 처리 안하고 문자 그대로 만들어 준다.   

예를 들어 
```sh
#!/bin/bash

MY_NUMBER=123

FILENAME=test_log
cat > $FILENAME << "EOF"
문자열을 입력1
문자열을 입력2
변수 $MY_NUMBER 
EOF
```

이렇게 하면 변수 자체의 값이 123 이 들어가는 것이 아닌 문자 그대로인 *$MY_NUMBER* 로 생성이 되게 된다.   

> 끝낼 때에는 EOF (따옴표 없이) 사용하면 됨,   
위의 경우 처럼 아예 따옴표를 안 사용하는 경우에는 변수에 들어가 있는 값을 사용하게 된다



## 단순하게 echo 를 사용하기

echo 와 >> 리다이렉트를 사용해서 직접 입력해 주는 방법도 있다.

```shell
#!/bin/bash

echo "hello" >> test.log
echo "world" >> test.log
```
계속 라인을 만들어 갈 수가 있다.

다만, 여기에서 그냥 *>* 만 사용하게 되면 파일을 덮어 씌어 버린다.

