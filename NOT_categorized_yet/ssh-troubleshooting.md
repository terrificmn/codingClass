# ssh 관련 트러블 슈팅
linode 서버 관련

`ssh: connect to host (ip주소) port 22: Connection refused`

ssh로 public 키를 통해서 로그인을 하는데 아예 연결이 안되면 곤란하다;   

이럴 때에는 리노드 사이트 홈페이지에서 콘손을 직접 연결해서 사용하는   
Launch LISH Console 을 이용한다.  

비밀번호를 잃어 버렸다면.. power off를 한 후 
root 비번을 바꿀 수 있으며, 다시 root 로 로그인 하는 방법


서버의 .ssh/authorized_keys   
에 public 키가 등록되어 있고 마지막에 요청하는 쪽(클라이언트)의 유저명이 들어가 있는데   
유저명이 달라도 public키가 맞으면 잘 작동한다.


## 확인 방법
systemctl restart / status 확인
`sudo netstat -anp | grep sshd`

tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      21324/sshd        
이런식이면 정상

방화벽 확인   
```
sudo firewall-cmd --list-all
```

services에 ssh 가 들어가 있는지, active 인지 확인

마지막으로 다시 reload 를 해봄

```sudo firewall-cmd --reload```

success

라고 나오면 성공이며, 

다시 ssh를 시도해 본다


