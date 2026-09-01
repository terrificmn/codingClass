```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:jXHYehJy8QpP1y9yX8sjaxTqDZB+/IOZy9IYfj/udWc.
Please contact your system administrator.
Add correct host key in /home/sgtubunamr/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /home/sgtubunamr/.ssh/known_hosts:4
  remove with:
  ssh-keygen -f "/home/sgtubunamr/.ssh/known_hosts" -R "192.168.10.100"
ECDSA host key for 192.168.10.100 has changed and you have requested strict checking.
Host key verification failed.
```
이런식으로 ssh로 같은 ip를 등록할 때 생긴다.  

같은 ip이지만 리눅스 버전이 다른 상황이었는데 그래서 위의 에러가 나오고 verification에 실패    
다행히 known_hosts 파일에서 지우라고 나오므로 그대로 해주면 됨


```
ssh-keygen -f "/home/user/.ssh/known_hosts" -R "192.168.10.100"
```
중간의 user는 자신의 계정

knwon_hosts에서 지우고 다시 접속한 후 

```
ECDSA key fingerprint is SHA256:jXHYefJy8QswdfasfsjaxTqDB+/IOyIfj/udWc.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.10.100' (ECDSA) to the list of known hosts.
```

다시 yes를 눌러 등록





ssh: connect to host 192.168.10.100 port 22: Connection refused

systemctl status ssh 를 해서 확인해본다  
서버쪽이든 클라이언트 쪽이든 설치가 되어 있는지 확인  

없다면 설치
```
sudo apt install openssh-server
```
