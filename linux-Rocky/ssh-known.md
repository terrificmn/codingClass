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