# wget ftp 
ftp를 사용할 때 crul을 사용하는 것 처럼, wget를 사용할 수도 있다.  

옵션은 `--user`, `--password` 를 사용한다.   
-P 옵션으로 다운도르 될 디렉토리를 지정할 수 있다. (-P 옵션으로는 파일명은 지정 안됨)   

```shell
user="user_ftp"
pwd="pwd_ftp"
ftp_addr="ftp://ftp아이디@ftp주소/디렉토리/파일명"

wget --user=$user --password=$pwd \
    $ftp_addr \ 
    -P ${HOME}/Downloads/
```

> ftp아이디 는 $user 변수에서 사용한 ftp user와 같음




