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


switch case 문   
주목할 점은 조건을 in 뒤에다 적어주는데 ''나 ""의 문자열 상태로 적어주지 않는다  
파라미터 $VAR 로 들어온 값을 비교하는데 문자열이 각각 --start, --stop, --restart면 출력을 하는 프로그램  
*) 조건은 default 조건임
```shell
#!/bin/sh


VAR=$1

case "$VAR" in
        '--start')
        echo 'start~!';;

        '--stop')
        echo 'stop~!';;

        '--restart')
        echo 'restart';;

*)
        echo 'no codition';;

esac #case문 종료

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
