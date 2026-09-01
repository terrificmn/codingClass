# ssh ECDSA key 변경
리눅스를 다시 설치해서 유저가 바뀐 경우에 ..

`ssh new_user@192.168.21.111` 했을 경우에 이미 등록되어 있는 경우에는 아래와 같은 워닝이 나온다  

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:tfvrq4wPieesisOpe8qgse7wKBHo4HqyFRkjOQeBQDb3d.
Please contact your system administrator.
Add correct host key in /home/user/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /home/user/.ssh/known_hosts:1
  remove with:
  ssh-keygen -f "/home/user/.ssh/known_hosts" -R "192.168.21.111"
ECDSA host key for 192.168.21.111 has changed and you have requested strict checking.
Host key verification failed.
```

다행히 지우는 방법도 알려준다 
```
ssh-keygen -f "/home/user/.ssh/known_hosts" -R "192.168.21.111"
```

지운후에 다시 ssh 접속을 하면 ECDSA key fingerprint를 다시 등록할 수가 있다  



