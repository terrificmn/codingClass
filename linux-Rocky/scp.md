# scp

```shell
scp /home/myuser/Donwloads/my_file remote_user@192.168.0.10:/home/remote_user/Donwloads/
```
만약 이미 같은 파일이 있다면 `Text file busy` 라는 에러가 발생

문제가 없다면 remote_user 의 비밀번호를 물어본 후 진행하게 된다.   


## 디렉토리 복사
-r 옵션을 사용

```shell
scp -r /path/to/local/my_dir remote_user@192.168.0.10:/path/to/remote
```

