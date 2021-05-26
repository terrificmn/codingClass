[sgtocta@localhost Projects]$ ssh pi@222.235.121.84 -p 10200
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:nxpP89o8LxcL60N5I3X/9VjL6gzNDWlhym/3IEAZWSY.
Please contact your system administrator.
Add correct host key in /home/sgtocta/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /home/sgtocta/.ssh/known_hosts:3
ECDSA host key for [222.xxx.xxx.xx] has changed and you have requested strict checking.
Host key verification failed.

이렇게 나오면서 접속이 안될 때


```
vi ~/.ssh/known_hosts 
```
파일을 열어서 해당 아이피로 등록되어있는 키를 지워주고 저장 시키고 빠져나온다

그리고 다시 ssh로 접속 하면 잘 접속이 된다
