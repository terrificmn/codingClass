## 로그인은 할 수 없는 상태로 만들기
```
$sudo usermod /sbin/nologin ftpuser
```
혹시 안되면 -s 옵션을 붙인다. (인자)   

아무튼 이렇게 되면 유저는 그대로 남아있지만 로그인은 할 수 없는 상태가 된다     
(로그인화면도 안나옴)

그 다음에 cat /etc/passwd 를 확인해보면     
ftpuser:x:1001:1001::/home/ftpuser:/sbin/nologin 요렇게 바뀌어 있음   
이렇게 되면 처음로그인 화면에도 안나오고, ftp로도 접속을 못하게 된다  
(-L 옵션도 있기는 함, lock the user account 기능인데    
암호화 시킨 패스워드 앞에 !를 넣어주고 로그인을 못하게 하는 기능이라고 함   
다른 내용이기는 한 듯함)


## 다시 로그인 가능하게 하려면    
위의 usermod로 shell을 지정해준다 /bin/bash (-s 옵션 넣어주기)   

```
$sudo usermod -s /bin/bash ftpuser
```


## 마지막으로 유저삭제
유저를 삭제하려면 userdel을 사용하면 된다 -r 옵션 (man 보기)