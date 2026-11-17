# ssh known_host 실패

퍼미션이 소유권이 root로 변경되어 있다.  
이것 때문에 계속 known_host 변경에 실패해서 매번 yes 를 눌러줘야 한다.

```
Failed to add the host to the list of known hosts (/home/myuser/.ssh/known_hosts).
```

간단하게 소유권을 내 유저로 바꿔준다. 

```
sudo chown $USER:$USER ~/.ssh
```

이후 ssh 소유권 정리

```
chmod 700 ~/.ssh
chmod 600 ~/.ssh/known_hosts 2>/dev/null
chmod 600 ~/.ssh/id_* 2>/dev/null
chmod 644 ~/.ssh/*.pub 2>/dev/null
```


## ssh public key 등록
*ssh-copy-id* 를 해서 key auth 가 될 수 있게 해준다.  

```
ssh-copy-id myuser@192.168.11.10
```
이후 비번을 입력하고 로그인을 하게 되면  다음번 로그인 때부터는 자동으로 로그인이 된다.  


~/.ssh 디렉토리 이하에 id_ed25519.pub or id_rsa.pub 퍼블릭 키임  

SSH connection 이 비번을 입력해서 성공하면  현재 내 컴퓨터의 .pub 파일을 카피해서 remote 접속하려는 ip의 해당 user (myuser)  
에 ~/.ssh/authorized_keys 에 한줄이 입력되게 된다.  

> ssh-copy-id 는 해당 remote 의 .ssh 디렉토리는 700, 이하의 authorized_keys 파일은 700 으로 변경해서  
해당 유저만 권한을 얻게 됨  

> 내 로컬의 id_ed25519.pub 는 public key, id_ed25519 (확장자 없음)은 private key  , ssh-keygen 를 한 날짜가 기록되고  
ssh-copy-id 는 생성하지는 않고, 이동만 시켜준다.  
remote 접속하는 pc 의 authorized_keys 는 ssh-copy-id 를 한 날짜로 변경  

다음번 로그인할 때에는 remote 에서는 authorized_keys 에서 등록된 public 키를 (remote 에 등록됨)  
local의 내 private key 와 비교해서 로그인을 하게 된다. 
