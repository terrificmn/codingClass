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


