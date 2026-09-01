# test shell script 

-x, 옵션 -r 옵션 등이 있다. 

-x 는 실행가능한 파일인지 알아볼 경우, 

-r 은 읽기 가능한지 보는 것

```shell
[ -x /etc/a-file ] && exec /etc/a-file
```

/etc 이하의 a-file 이 실행가능한 파일이면 실행한다.

```shell
[ -r /etc/a-file ] && cat /etc/a-file
```
/etc 이하의 a-file 이 읽기 가능하면 cat 명령으로 출력




