# sshd root 접근 막기
서버의 sshd_config 파일을 수정한다

```
sudo vi /etc/ssh/sshd_config
```

yes에서 no 바꿔준다. 
```
PermitRootLogin no
``` 

> 또는 데비안 버스터 경우에는 `PermitRootLogin prohibit-password` 로 되어 있는데  
비밀번호 패스워드 접근을 막고 Key 파일로만 로그인이 될 수 있게 하는 옵션

일단 no로만 해도 될 듯하고   
ssh keygen을 이용해서 할 경우에는 *server강화_기본부터_ssh_key만들기.md* 파일 참고하기

그래서 key로만 접근하려고 할 때에는 아래 파라미터도 설정한다   
ssh password authentication도 yes에서 no 로 바꿔서 패스워드 로그인이 안되게 한다
```
PasswordAuthentication no
```

`#AddressFamily any` 를 찾아보자. 주석을 해제하고 inet 으로 바꿔준다
```
AddressFamily inet
```

## sshd 재시작
```
systemctl restart sshd
```

그런데 만약 다시 재 접속이 안되는 경우가 생긴다  
```
kex_exchange_identification: read: Connection reset by peer
Connection reset by 192.111.234.123 
```
이럴 때에는 방법이 없다. 서버를 직접 다시 재부팅 해주자


### 현재는 PermitRootLogin no 로만 해둠.    
단, 서버쪽은 다 적용함


## ssh 퍼미션 permission 에러
```
hostfile_replace_entries: mkstemp: Permission denied
update_known_hosts: hostfile_replace_entries failed for /home/user/.ssh/known_hosts: Permission denied
```

권한 문제이다. 일단 root로 되어 있는지 확인하자  
```
cd ~/.ssh
ls -l
```

root 나, 권한이 rw-rw-rw- 등으로 되어 있다면 보안을 위해서 변경
```
cd
sudo chown $USER:$USER -R .ssh
sudo chmod 700 .ssh
sudo chmod 600 .ssh/*
```
