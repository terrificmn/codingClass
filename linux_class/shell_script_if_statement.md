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

> bash shell 을 사용하려면 #!/bin/bash

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

## if  파라미터 parameter 받기

if문 사용하기 -   
shell에서는 if문은 fi로 끝난다 (end if)를 의미함
```shell
#!/bin/sh

#echo $0 #0은 파일명을 받는다
#파라미터를 3개를 받아야하는데 2개만 받은 경우

num1=$1
num2=$2
num3=$3

if [ -z "$num3" ]  #-z null인지 확인 null이면 true리턴 
        then
                echo '입력해주세요'
        else
                echo $num1 $num2 $num3

fi #end if

exit 0
```


## if문 사용시 주의

if문 사용시 주의할 점 [] 대괄호를 사용할 때 한칸씩 띄어서 사용해야함  
안그러면 command not found 에러가 발생함
```
#if [$password="password"]  #이렇게 하면 에러발생
if [ $password="password" ]
then
    ...
else 
    ...
fi
```
그리고 == 도 안된다. if문에서 문자열은 = 로 비교가 되지만   
-eq 옵션을 사용하면 원치않는 결과가 나온다  


## 숫자 비교
-eq 등의 옵션은 숫자일 때만 되는 것 같다  
```sh
#!/bin/bash
m=1
n=2

if [ $n -eq $m ]
then
        echo "Both variables are the same"
else
        echo "Both variables are different"
fi
```

부등호는 사용을 안하고 옵션(?)으로 선택해서 사용하는 듯 하다  