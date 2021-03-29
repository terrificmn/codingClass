# 
.sh 파일로 생성한다
```
$vi test.sh
```

파일의 내용에는 sh shell로 실행하겠다는 의미의 특수 주석을 작성한다  
즉 전처리의 역활을 한다 
끝에는 exit 0 라고 해준다

```
#!/bin/sh

exit 0
```

변수 설정
변수에 넣는 것은 숫자로 넣어도 모두 문자로 인식  
VAR=test 처럼 = 사이는 없어야 하고 
출력을 할 때는 변수 앞에 $을 붙인다. $VAR
```
echo $VAR
```

실행은 sh로 할 수 있음
```
sh test.sh
```

숫자도 문자열이기 때문에 사칙연산을 하려면
expr을 사용해서 계산할 수 있다. 이때 백틱으로 감싸준다
```
num1=10
num2=20
result=`expr $num1 + $num2`
echo $result
```



