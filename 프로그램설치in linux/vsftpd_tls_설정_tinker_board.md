# vsftpd 정리
오랜만에 ftp를 다시 설치해보았다. 한 2년도 더 된 거 같은데, 예전 자료를 가지고 했으나   
역시나 잘 안된다. 물론 우분투, Rocky도 아닌 데비안이어서?? (그럴확률은 낮을 듯...)   

아마도 버전이 달라졌겠지 하고 생각해본다.  

> 사실 vsftpd 말고 그냥 22번 포트를 사용하는 sftp 를 사용하는 방법도 있다.

기본적으로 ftp 관련해서 사용할 유저를 만들고 그 유저만 ftp를 접속할 수 있게 진행함  

현재 다른 md파일도 있는데 여기 내용을 주로 참고하자. 정리 및 테스트 완료 (On Nov11, 2023)


##  vsftp.conf 정리버전
먼저 21번 포트를 사용하는 기본 방식이다. 아무런 보안이 되지 않는 방식   
*Plain FTP (insecure)*   

설치 후에 설정 파일은 /etc/vsftpd.conf 이다.   
우분투와 마찬가지로 따로 디렉토리가 생기지 않는다... (RHEL 계열은 vsftpd 디렉토리가 생김)

vsftpd.conf 을 열어서 수정한다(없으면 만들어 준다.)
```
sudo vi /etc/vsftpd.conf
```

아래는 확인이 된 버전. 그냥 다 지우고 아래 내용으로 만들어도 된다. (테스트완료)
```
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022
dirmessage_enable=YES
xferlog_enable=YES
connect_from_port_20=YES
xferlog_std_format=YES
listen=NO
listen_ipv6=YES
pam_service_name=vsftpd
userlist_enable=YES
userlist_file=/etc/vsftpd.userlist
userlist_deny=NO
chroot_local_user=YES
allow_writeable_chroot=YES
user_sub_token=$USER
local_root=/home/$USER
```

- write_enable 쓰기 가능하게 해줌   
- conect_from_port_20 은 필요 없을 듯 하기도 하다   
- userlist_enable 관련해서는, 파일을 따로 만들어 준다. (userlist_file)  
- user_sub_token은 해당 접속하는 유저의 환경변수를 사용해서 루트를 고정해주는 것 인데   
글쎄.. 고정이 되지 않고 상위 디렉토리로 이동을 할 수가 있다.   
- 결국 chroot_local_user와 같이 사용해야함.  
- local_root 는 홈 유저의 디렉토리를 다 사용하거나, 아니면 특정 디렉토리를 만들어 고정  
- chroot_local_user 와 같이 사용하면 해당 유저 디렉토리를 ftp상에서 /로 고정할 수가 있다.  
- allow_writeable_chroot가 없다면 접속 시 에러가 난다.(chroot_local_user와 세트)   

### 방화벽 포트 허용
ufw 를 사용해서 허용해준다

없다면 설치 `sudo apt install ufw`

```
sudo ufw enable
sudo ufw allow OpenSSH
sudo ufw allow 21/tcp 
```
`sudo ufw allow 20/tcp`도 할 수 있으나 사용 안 할 것 같아서 안함.


### vsftpd 재실행
설정 파일 및 파이어월 설정 이후  
```
systemctl restart vsftpd
```
그리고 status check를 해보면 
```
systemctl status vsftpd
```
에러 없이 잘 실행이 되어야 한다. 

예를 들어 녹색으로 active 표시가 되면 ok
```
Loaded: loaded (/lib/systemd/system/vsftpd.service; enabled; 
Active: active (running)
```

만약 active 상태가 아니라면 설정 파일에서 오타나, 띄어쓰기 등을 확인해본다.  

> vsftpd가 조금 불편한게 뭔가 틀리면 기본 설정 파일로 사용하게 하면 좋을 듯 하지만,  
엄격하게 조금이라도 틀리면 아예 실행이 안된다. 안될 경우 잘 체크해보자


#### filezile 로 접속할 경우
해당 ip와 포트 21, Encryption 에서는 plain ftp 모드로 접속한다.  

> 아, 회사 ftp도 plain ftp 모드였다..ㅠㅠ  

즉, 그냥 21번 포트로 가볍게 사용할 것 이라면 여기 까지 설정해도 무방하다


## TLS 를 이용한 방식
SSL/TLS 인증서를 이용해서 key, pem 파일을 만들어서 data 전송의 보안을 강화 시켜준다.  

먼저 RSA 라는 키를 만들기 위한 명령어   
> 참고로 원래 /etc/vsftp.pem  이런식으로 경로를 만들었는데, Debian Buster 10 에서는 이게 오히려 문제가 됨   
물론 리눅스에 상관 없이 vsftpd가 버전이 달라져서 그럴 수도 있다.  

```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/vsftpd.key -out /etc/ssl/certs/vsftpd.pem
```

> -days 는 더 늘려도 될 듯 하다.  
또한 여기에서 파일 경로는 각각, /etc/ssl/private/vsftpd.key, /etc/ssl/certs/vsftpd.pem 으로 생성  
key, pem 자체가 디렉토리 자체가 달라진다.  
그 전에는 /etc 디렉토리 안에 만들어서 지정해도 문제가 없었지만 (ubuntu 20이후에서는 확인 못해봄)   
어쨋든 위의 커맨드로 해당 디렉토리에 만들고 지정하면 문제 없이 잘 된다. (보안 때문에 해당 디렉토리 허용되는지는 잘 모르겠지만...)   

이제 위의 vsftpd.conf 파일에(without ssl 내용) ssl 관련해서 파라미터가 더 추가 된다 

테스트완료된 파일 내용은 아래
```
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022
dirmessage_enable=YES
xferlog_enable=YES
connect_from_port_20=YES
xferlog_std_format=YES
listen=NO
listen_ipv6=YES
pam_service_name=vsftpd
userlist_enable=YES
userlist_file=/etc/vsftpd.userlist
userlist_deny=NO
chroot_local_user=YES
allow_writeable_chroot=YES
user_sub_token=$USER
local_root=/home/$USER
rsa_cert_file=/etc/ssl/certs/vsftpd.pem
rsa_private_key_file=/etc/ssl/private/vsftpd.key
pasv_min_port=30000
pasv_max_port=31000
ssl_enable=YES
ssl_sslv2=NO
ssl_sslv3=NO
ssl_tlsv1=YES
require_ssl_reuse=NO
ssl_ciphers=HIGH
allow_anon_ssl=NO
force_local_data_ssl=YES
force_local_logins_ssl=YES
```

- rsa_cert_file, rsa_private_key_file 경로를 각각 잘 넣어준다   
- pasv_min/max_port 는 임의로 변경 가능하다. 인터넷에서 잘 설명해주는곳에서는 40000, 50000 으로 사용한 곳도 있음  
- 나머지는 그대로 사용하면 됨

> 새로 만들어서 복붙해서 사용하자 (기존 파일이 있다면 백업파일로 만들어놓은 후에..)   
vsftpd가 조금 불편한게 파라미터의 글자가 조금 틀리거나, 또는 파일 경로가 안맞는 경우  
무시하고 기본값으로 실행되는 것이 없는 듯 하다. 그냥 vsftpd가 실행이 안 되게 된다.


### 방화벽 허용
없다면 설치 `sudo apt install ufw`

```
sudo ufw enable
sudo ufw allow OpenSSH
sudo ufw allow 21/tcp 
sudo ufw allow 990/tcp
sudo ufw allow 30000:31000/tcp
```

당연히 21번 포트는 ftp 주 포트이고, 30000-31000은 패시브 포트로 사용이 된다.  
990번 포트는 TLS가 enable일 경우 사용 된다.  

확인은 
```
sudo ufw status
```

이제 다시 vsftpd 를 재 실행한다.   
[위의 내용을 vsftpd-재실행 부분을 참고](#vsftpd-재실행)  


## 포트 포워딩
내부 private 망을 외부에서 접속할 수 있게 하려면 포트포워딩을 해줘야 한다.  

보통 웹브라우저에 192.168.10.1 로 접속해서 공유기 설정 화면으로 들어간다  

공유기 제품(회사) 마다 추가 방법은 다르겠지만 추가할 포트는, 즉 최소한으로 필요한 포트는   
**21**, **990**, **30000~31000(범위)** 포트이다   

먼저 ftp로 사용할 pc/sigle board pc 등의 아이피를 예약을 해주면 계속 해당 ip를 사용할 수가 있다.  
이때에는 mac address로 매칭을 시켜주므로 mac address로 특정 아이피를 예약(고정) 하면 된다. 

이후 포트 포워딩을 찾아서 추가해준다.  
외부 포트 (임의의 포트), 내부 포트, 아이피 등을 지정해준다.

예를 들면.. (외부포트도 내부 포트와 같은 값을 지정해도 상관 없다. )
```
외부포트 10021, 내부포트 21, 아이피 192.168.10.100
```

tplink 공유기 같은 경우에는 외부 포트에서만 30000-31000 로 지정해주고    
내부 포트는 빈칸으로 지정하면 외부 포트와 같은 번호 내부포트를 지정해줘서 사용할 수가 있다.   
(30000, 31000 따로 지정이 아닌 범위로 지정해줘야한다. min/max로 설정했으므로..)  

> 단, 외부 포트를 임의의 다른 번호로 지정할 수는 없을 듯 하다. 왜냐하면 외부포트를 범위로 지정하면   
내부포트로 같은 범위의 포트번호로 지정되기 때문  
물론 다른 iptime 등의 다른 회사의 공유기들은 설정이 조금 다를 수 있다.

여기까지 하면 이제 외부에서 연결이 잘 되게 된다.  

> 참고로 30000~31000 패시스 min/max 포트는 다른 포트로 지정이 가능하다.  
vsftpd.conf 파일과 방화벽을 해당 임의의 포트로 지정 후 allow 시켜준다. 물론 포트포워딩도..  

### filezilla 사용
Encryption 방식을 *Require explicit FTP over TLS* 로 지정 후 사용하고   
아이피는 포트포워딩한 실제 ip를 적어준다(192.168....아님)   
포트 번호는 포트포워딩한 포트 (예를 들어 10021)

예전에는 ftp가 잘 되는 것을 확인한 후에 /bin/bash도 로그인을 못하게 막았는데   
보안상 ftp만 가능하게 하고 실제 쉘 로그인은 막는 것인데,  
로그인을 못하게 했더니 **ftp 로그인도 안 되는 현상이 발생**  
그래서 다시 로그인 가능하게 변경해서 사용하는 중..  

이제 TLS 방식을 사용하므로 server의 certicate 를 신뢰하냐는 창이 뜨게 된다. ok   

## lftp 설정 (클라이언트 쪽 설정)
lftp 프로그램을 이용해서 사용하려고 할 때 
```
sudo dnf install lftp
```

우분투/데비안
```
sudo apt install lftp
```

plain ftp로 접속을 할 경우에는 문제가 없으나,   

SSL/TLS 인증을 해서 접속하는 경우에는 문제가 생긴다. 물론 ftp에 제대로 접근이 안되서  
다운로드 및 파일 목록 조차 볼 수 없다.
```
Fatal error: Certificate verification: Not trusted 
```

전에는 `set ssl:verify-certificate no` 로 설정해서 사용했는데,   
꼭 추천 방법은 아니다. 
물론 no 로 설정 후 사용해도 ftp가 되어서 이전에는 그렇게 사용을 했었다. (본인)  

하지만 인증서 관련 certificates의 내용으로 인증을 진행 한 후 사용할 수있다.  

openssl 명령을 이용해서 그 내용을 crt 파일로 만든 후에 사용하는 방법을 사용한다.  
먼저 디렉토리 및 파일들을 만들어 준다.
```
mkdir ~/.lftp
cd ~/.lftp
touch my-certificate.crt rc
```

이후 openssl 명령어로 certicate 내용을 출력할 수가 있다.
```
openssl s_client -connect 43.12.122.35:10021 -starttls ftp -showcerts
```
> 아이피 또는 도메인 이름, 포트는 21 또는 포트포워딩한 포트번호

이제 꽤 긴 내용이 출력이 되는데, 이 중 필요한 것은 
*-----BEGIN CERTIFICATE-----* 부터 *-----END CERTIFICATE-----* 이다.  
나머지는 필요가 없다.  

예를 들어서 
```
-----BEGIN CERTIFICATE-----
CCAegAwIBAgUOofKE+1M8mZ4aQP8rwpCC5Sv0wDQYJKoZIhvcNAQEL
BQAwTELMAGA1UEBhMCS1IHhcNMjMxMTxMTExNTI2WhNMjQxMTEwMExNTI2
WjAQswQYDVQEwJLUjCASIwDQYJKoIhvcNAQEBQADggEPCCAQoCggEB
....생략...
-----END CERTIFICATE-----
```
이 부분만 my-certificate.crt 파일에 복사 후 저장.  

그리고 rc 파일을 열어준다. 이는 lftp 환경설정 파일이 된다. 
아래 내용을 복사 후 파일 경로를 잘 지정해준다.   
```
set ssl:check-hostname no
set ssl:ca-file "/home/myuser/.lftp/my-certificate.crt"
```

> .lftp/rc 파일까지는 기본으로 설정된 파일들 경로 인 듯하고, crt 파일명은 바뀌어도 괜찮다.  
즉 .lftp 디렉토리 및 rc 파일까지는 같아야 한다.    
> 또한 시스템 전역으로 설정을 하려면 rc 파일이 아닌, /etc/lftp.conf 로 파일을 만들고   
위의 설정 내용을 넣어주면 된다.  

이제 lftp 로 접속을 하면 잘 에러 없이 잘 실행이 된다. 파일 전송 / 다운로드 ok!

그리고 추가로 `set ssl:check-hostname no` 를 안해주면 hostname을 체크를 해서  
아래와 같은 오류가 발생하게 된다. 참고

```
Fatal error: Certificate verification: certificate common name doesn't match requested host name ‘43.23.21.33’ 
```
