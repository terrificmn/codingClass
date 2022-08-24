# switch case

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

$1은 파라미터 값. 명령어 다음에 들어온 값을 변수 (VAR)에 넣어준다 