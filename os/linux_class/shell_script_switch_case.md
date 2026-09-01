# switch case

switch case 문   
주목할 점은 조건을 in 뒤에다 적어주는데 ''나 ""의 문자열 상태로 적어주지 않는다  
파라미터 $VAR 로 들어온 값을 비교하는데 문자열이 각각 --start, --stop, --restart면 출력을 하는 프로그램  
*) 조건은 default 조건임  
$1은 파라미터 값. 명령어 다음에 들어온 값을 변수 (VAR)에 넣어준다 
```shell
#!/bin/sh
VAR=$1 ## parameter

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


### 숫자 형태 case
```sh
#!/bin/sh
echo "enter number either 1 or 2"
read input
print1="hello\nworld"
print2="hi\nmom~"
case "$input" in
        1) 
                echo -e $print1;;

        2)
                echo -e $print2;;

        *)
                echo "error no number";;
esac
```

각 case 가 끝나면 세미콜론을 2번씩 적어준다 ;;   
echo -e 키워드는 newline 같은 \n 이 적용이 된다. (그냥 echo에서는 문자 그대로 출력이 됨)
