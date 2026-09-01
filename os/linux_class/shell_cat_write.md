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

markdown 을 넣어서 \`를 사용하게 되는데 \`등의 표시를 하게 되면 만약 해당 문자열이  
sh 스크립트 실행을 하는 경우에는 해당 스크립트를 실행해버게 된다   
```shell
`./my_script` 실행하기  
```
이럴 경우에는 `\./my_script\` 처럼 이스케이프를 해준다.  


> 리다이렉션으로 ..   
또한 cat 으로 열때 *>* , *>>* 사용하는 것에 따라서 아예 파일 덮어쓰기, 또는 이이서 라인별로 저장이 가능해진다.


### EOF 사용 시 주의
처음 EOF까지 사용한다고 한 다음 줄 부터는  띄어쓰기까지 모두 포함하게 된다.  

그리고 마지막줄에 EOF 로 끝낼 때에는 반드시 첫 째줄 라인에 맞춰서 끝내주고  
예를 들어서 if 문 등에서 들여쓰기로 사용을 했다면 오류가 발생한다.

EOF 를 못찾는 경우
```shell
#!/bin/bash

abc = 1
if [ $abc -eq 1 ]; then
    cat > /home/myuser/myfile << EOF
    "hello world"
    EOF
fi
```
> 마지막 fi 를 vim이나 code에서 인식 못한다.

이렇게 하면 EOF 를 찾지 못하는 워닝이 발생되며, 잘 저장이 안된다.
```
line 34: warning: here-document at line 23 delimited by end-of-file (wanted `EOF')
```

제대로 사용하기. (올바른 예)
```shell
#!/bin/bash

abc = 1
if [ $abc -eq 1 ]; then
    cat > /home/myuser/myfile << EOF
"hello world"
EOF
fi
```
> vim이나 code에서 마지막 fi를 잘 인식 해준다.  
EOF 전까지는 tab, 스페이스 모두 인식해서 넣어준다.


## 단순하게 echo 를 사용하기

echo 와 >> 리다이렉트를 사용해서 직접 입력해 주는 방법도 있다.

```shell
#!/bin/bash

echo "hello" >> test.log
echo "world" >> test.log
```
계속 라인을 만들어 갈 수가 있다.

다만, 여기에서 그냥 *>* 만 사용하게 되면 파일을 덮어 씌어 버린다.

