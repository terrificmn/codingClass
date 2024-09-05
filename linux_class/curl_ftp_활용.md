# curl을 이용해서 
curl로 ftp로 자료를 다운 받을 수 있다  

`curl -u ftp유저명:ftp패스워드 "ftp://ftp유저명@ftp주소/받고싶은디렉토리/to/파일명" -o ${HOME}/Downloads/저장할파일명`   
요런 방식으로 사용하면 된다   

-o 옵션은 내 컴에 다운받는 위치를 만들어 주는 것

그대로 대입해서 변수로 만들어서 사용하면 좋다

```shell
ftp_user="ftp_user_1"
ftp_passwd="1234"
... 생략...

curl -u $ftp_user:$ftp_passwd \
    "ftp://$ftp_user@$ftp_address/$path/$file_name" \
    -o ${HOME}/Downloads/$file_name
```

아주 좋으다~!   

> 패스워드는 다른 파일에서 불러와서 변수에 저장해서 사용하는 방법이 있겠다.   

## 옵션
-v 로그를 보여준다. 디버깅 할 때 좋다.  
예 로그인이 되었는지 여부도 확인 가능

```
User: 땡떙
Completed password authentication
Authentication complete
```

-k  sftp 등을 사용할 때 ssl 인증서 관련해서 물어볼 수 있는데, insecure 하게 그냥 작업하는 방법   
--insecure 와 동일   

그래서 stp로 접속해서 사용하는 경우에는 위의 옵션을 안 넣으면
```
curl: (60) SSL peer certificate or SSH remote key was not OK
```
라고 나온다.   

위의 에러를 방지하려면 ssl 인증서를 받거나 openssl 등으로 받을 수 있음  추후 더 업데이트   

위의 -k 또는 --insecure 로 넣어준다.  
또는 홈디렉토리에 ~/.curlrc 파일을 만들고 

```
vi ~/.curlrc
```
```
insecure
```
라고 넣어준다. 


추가로 sftp로 접속할 경우에는 ftp와 다르게 주소 뒤에 `/home/userid/directory` 로 넣어줘야지 접근 에러가 안남.

예
```
ip주소:포트/home/userid/path-to-dir
```


참고 사이트

https://www.warp.dev/terminus/curl-file-upload
