Centos/RHEL Fedora

먼저 업데이트 
```
dnf upgrade
```

시간 설정하기
```
timedatectl list-timezones
```
스크롤을 내려서 Asia/Seoul 를 찾아도 되지만  

아래 명령어를 수행한다
```
timedatectl set-timezone 'Asia/Seoul'
```

이제 `date` 를 입력해보면 시간이 잘 맞게 나온다



## 호스트 네임 정하기

    Descriptive and/or Structured: web, staging, blog, or something more structured like [purpose]-[number]-[environment] (ex: web-01-prod).

    Generic/Series: Such as the name of a fruit (apple, watermelon), a planet (mercury, venus), or animal (leopard, sloth).

이런 방식을 사용한다고 한다
```
sudo hostnamectl set-hostname example-hostname
```

> 여기서 설정한 hostname은 FQDN (fully qualified domain name)에 사용이 될 수가 있다고 한다   
(ex: web-01-prod.example.com)

그러면 `cat /etc/hostname` 이라고 치면 설정한 이름이 나온다
```
webblog-01-prod
```

hosts 파일 수정하기
```
vi /etc/hosts
```

Linode의 public IP주소 FQDN hostname 순으로 적어준다

```
203.0.113.10 webblog-01-prod.example.com webblog-01-prod
```
> example.com 은 도메인이  없는데 될라나 모르겠다 일단 저장

마지막줄은 IPv6 주소를 적어준다

```
2600:3c01::a123:b456:c789:d012 example-hostname.example.com example-hostname
```
위 처럼 IPv6주소는 리노드 관리자 페이지에서 알 수 있다


## user 추가하기 
(기존에 작성했던 adduser 등을 참고)

sudo privileges를 갖기 위해서 wheel group에 등록해준다
```
usermod -aG wheel username
```

> -a옵션 수정하기 -G 옵션과 같이 쓰여서 다른 그룹에서 user를 지우지 않고 대체 그룹으로 들어가게 해준다   
-G 새로운 대체할 그룹

```
sudo usermod -aG wheel username
```

`cat /etc/group` 을 쳐보면 
```
wheel:x:10:myusername
```


## SSH Key Pair 만들어서 접속제한하기 
ssh key pair를 만들어서 private 키를 가지고 있고, 서버에 public key를 둬서  
그것만으로 로그인이 가능하게 하는 방법임   
물론 A cryptographic key-pair (암호화가 되어 있음) 만들어서 보안을 강화시킬 수가 있다

자신의 desktop 등, local에서 실행을 하면 된다.   
아래의 명령어를 실행하면 SSH Key를 만들어 준다
```
ssh-keygen -b 4096
```
> -b 옵션은 키 pair를 만들게 되는데 4096-bit RSA key-pair를 만듬   
만약 RSA키가 있었다면 덮어씌우므로 주의한다

위의 ssh-keygen 명령으로 home/.ssh 디렉토리에 키가 만들어진다.

권한 때문에 안 만들어진다면 권한을 확인해준다  
.ssh 디렉토리가 root로 되어 있는지 확인  

```
cd ~
ls -la 
```
root root 로 되어 있다면 
```
sudo chown -R $USER:$USER .ssh
```

다시 돌아와서 위의 ssh-keygen 명령어를 쳤을 때 파일위치 물어보면 엔터 한번 치고   
passphrase를 입력해준다~ 생략할 수도 있으나 하는 것을 추천

```
Generating public/private rsa key pair.
Enter file in which to save the key (/home/your_username/.ssh/id_rsa):
```

> 추후 ssh로 서버에 접속할 때 여기에서 설정한 passphrase를 물어본다

이제 ~/.ssh 디렉토리 안에 id_rsa, id_rsa.pub 이 있다. 만들어진 키를 서버로 보내야 한다

A private key는 id_rsa란 파일이름으로 만들어지고 다른 사람, 그룹이 볼 수 없게 해야한다   
A publick key는 id_rsa.pub 파일로 만들어진다. 로그인을 할 서버에 있으면 되고 공개된 키다

encryption과 decryption이 이루어지는데   

- Signed Communication: 으로 로컬에서 private key를 통해서 메세지가 나가게 되고   
- Verification of Communicaiton: 은 서버에서 public키를 가지고 있어서 private key를 통해 보낸
메시지를 해독하게 된다

[여기에서 ssh_key 만들기 확인할 수 있다 참고 사이트](https://www.linode.com/docs/guides/use-public-key-authentication-with-ssh/)

<br/> 

## ssh 키 보내기
이제 만들어진 키를 복사해서 서버에서 사용할 수 있게 보낼 수 있다   
서버에서 내가 사용할 특정 유저의 home 디렉토리의 .ssh 디렉토리 안으로 보내게 되는데   
authorized_keys 파일로 생성이 되고 여기에는 public 키가 추가가 된다.

서버의user@서버아이피 형식으로 입력한다
```
ssh-copy-id server_user@172.10.24.10
```
이제 server_user@172.10.24.10's password 하고 비번을 물어보면   
서버쪽 user의 비번을 넣어주면 key 추가된다

좀더 보안을 강화하는 차원에서 권한 변경해준다
```
sudo chmod 700 ~/.ssh/
cd .ssh
sudo chmod 600 authorized_keys 
```

> 디렉토리에 group, other 권한이 없으므로 접근할 수 없다   
authorized_keys 파일은 읽고 쓰기만 가능하게 해준다

이렇게 authorized_keys에는 public키가 포함되게 되었지만   
로컬에서 보관중인 id_rsa는 유출되지 않게 잘 보관해야한다~  public키와 짝꿍이기 때문에   

local 내 컴에서도 
```
sudo chmod 700 ~/.ssh/
cd .ssh
sudo chmod 600 ./*
```

> private key인 id_rsa 는 공개키가 아님에 주의해야한다고 함

<br/>

## 이제 서버 접속하기
서버의 sshd_config 파일을 수정한다

```
sudo vi /etc/ssh/sshd_config
```

yes에서 no 바꿔준다. (저번 포스팅에서 했던)
```
PermitRootLogin no
``` 

ssh password authentication도 yes에서 no 로 바꿔서 패스워드 로그인이 안되게 한다
```
PasswordAuthentication no
```

`#AddressFamily any` 를 찾아보자. 주석을 해제하고 inet 으로 바꿔준다
```
AddressFamily inet
```

> inet은 listen only on IPv4, inet6은 listen only on IPv6   
그리고 system-wide로 적용되는 것이 아니고 sshd에 한함

이제 wq를 눌러서 저장을 한 후 sshd를 재시작 해준다
```
sudo systemctl restart sshd
```

<br/>

## ssh로 로그인 하자
이제 로그인을 해보자   
내 로컬 컴에서 터미널을 열고 ssh 자신의서버_유저아이디@서버주소를 입력해서 늘 하던대로 접속을 하면   
```
ssh server_user_id@72.10.24.10
```

passpharase 로 입력을 했던 비번을 요구한다. 해당 비번을 넣고 엔터를 치게 되면 접속이 되게 되고   
그 다음부터는 exit 을 하고 다시 로그인을 할 때에는  
그냥 뿅 하고 로그인이 된다

> 한번 passphrase를 입력하면 logout이나 재부팅을 하기 전까지는 다른 세션 터미널을 열더라도   
비번을 묻지 않고 접속을 한다. 물론 묻지말라고 unlock 해달라는 체크박스도 보인다

바로 직전에 했던 ssh-copy-id 명령을 통해서 키가 복사되었기 때문에 ssh 로그인 접속이 잘 된다.

그리고 이번에는 저번과 마찬가지로 root로 ssh 접속을 하려고 하면   
(현재 root, password로 로그인이 다 막혀 있는 상태)  
예를 들어 root@192.72.10.24 이런식으로 로그인을 시도하게 되면
```
root@192.72.10.24: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
```

하고 차단되는 것이 확인 된다. 👍👍

> 하지만 이거는 딱 로컬 내 컴퓨터에서 rsa key가 있어야만 작동하는 것 같다   
이제 다른곳에서는 아마 접속을 못 할 것.   
아마도 멀티로 더 추가 할 수 있을 거 같다. 좀 더 알아봐야겠다


[블로그에 올림](https://qspblog.com/blog/sshd-%EA%B4%80%EB%A0%A8-SSH-Key-pair-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-2%ED%83%84)



## 이후 서버 보안은 
- firewall 설치 및 실행 참고

- fail2ban 설치 및 실행 관련 참고 할 것


