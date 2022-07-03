# TLS 인증하기
기존 ftp 는 암호화를 하지 않기 때문에 보안에 취약했다고 하는데 이는 기본 텍스트를 사용했다고 함  
sftp는 secuire FTP는 ftp 서버와 클라이언트 간의 통신을 암호화 해준다고 함     
그래서 TLS (Transport Layer Security)를 생성한다   
-days 365  1년으로 만듬 
키는 -keyout에 설정한 경로로 만들어진다   

일반 우분투 18.04에는 /etc/vsftpd 디렉토리가 없고  바로 /etc/vsftpd.conf로 되어 있음    
디렉토리를 만들어도 괜찮을것 같지만, 일단 디렉토리 안만들고 해봄   
(우분투인 경우)

~~정확하지는 않지만 /etc 경로로 이동해서 openssl로 키를 만들면 중간에 처리가 진행이 안되는데   
그냥 home디렉토리로 와서 하니 진행이 잘 됨 (검증은 안됨 ㅋ)~~   
나중에 보니 .rnd파일을 생성을 못해서 에러가 난듯하다   
설치되어 있어야하는것이 openssl 있으면 됨, centos는 확인이 가능한데 우분투를 검색은 잘 모르겠음   
```
$sudo openssl req -x509 -nodes -keyout /etc/vsftpd/vsftpd.key -out /etc/vsftpd/vsftpd.pem -days 365 -newkey rsa:2048
```
우분투에서는  vsftpd.key 와 .pem 위치를 따로 지정해주니, 디렉토리를 만들던가  
vsftpd.conf에서 경로를 잘 설정해주면 됨 (사실 또 에러날까봐 그냥 디렉토리 안만들고 함)


## 트러블슈팅 
키 생성할 때   
```
Can't load /home/ubun/.rnd into RNG
140121868997056:error:2406F079:random number generator:RAND_load_file:Cannot open
```

이런 에러가 나면 
.rnd 파일을 생성을 못하는 것인데 
```
You can manually create the file with openssl rand -out <randFile> -hex 256.
In your case sudo openssl rand -out /root/.rnd -hex 256 (훌륭하신 분 답변)
```

```
$sudo openssl rand -out $HOME/.rnd -hex
```
아마도 .rnd 파일을 있어야 뭔가 키 만든느데 베이스? 정도가 되는 듯한 느낌적인 느낌인데 아닐 수도 있음

이제 에러가 없다면..위의 TLS키 만드는것 이어서...  
그러면 생성하기위한 정보를 입력해준다

```
writing new private key to '/etc/vsftpd/vsftpd.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [XX]:KR
State or Province Name (full name) []:Incheon
Locality Name (eg, city) [Default City]:Incheon
Organization Name (eg, company) [Default Company Ltd]:test
Organizational Unit Name (eg, section) []:test lab
Common Name (eg, your name or your server's hostname) []:ftp-server.testlab.com
Email Address []:root@ftp-server.testlab.com
```

이렇게 하면 /etc/vsftpd/ 디렉토리안에 vsftpd.key vsftpd.pem 파일이 생긴다   
그리고 나서 다시 vsftpd.conf 파일을 다시 설정하는데 맨 아래에 아래 코드를 복사하기
```
ssl_enable=YES
ssl_sslv2=NO
ssl_sslv3=NO
ssl_tlsv1_2=YES
rsa_cert_file=/etc/vsftpd/vsftpd.pem
rsa_private_key_file=/etc/vsftpd/vsftpd.keyof
allow_anon_ssl=NO
force_local_data_ssl=YES
force_local_logins_ssl=YES
require_ssl_reuse=NO
ssl_ciphers=HIGHmin_port=30000
pasv_max_port=31000
debug_ssl=YES
```

위의 내용의 설명이다
```
ssl_enable=YES       # Enable vsftpd Secure connections
ssl_sslv2=NO      # Disallow SSL v2 protocol connections
ssl_sslv3=NO      # Disallow SSL v3 protocol connections
ssl_tlsv1_2=YES      # Allow TLS v1.2 protocol connections
rsa_cert_file=/etc/vsftpd/vsftpd.pem   # Location of TLS certificate
rsa_private_key_file=/etc/vsftpd/vsftpd.key  # Location of Private Key
allow_anon_ssl=NO     # Disallow Anonymous Access
force_local_data_ssl=YES    # Force users to use SSL connection for data transfer
force_local_logins_ssl=YES    # Force users to use SSL connection for credentials
require_ssl_reuse=NO     # Disable SSL session reuse
ssl_ciphers=HIGH       
pasv_min_port=30000     # Min port number to define a range for PASV connections
pasv_max_port=31000     # Max port number to define a range for PASV connections
debug_ssl=YES      # Dump OpenSSL diagnostics in vsftpd log file
```


## 클라이언트에서 사용할 lftp 설치하기
근데 vsftp를 이용해서 자체TLS를 만든것이기 때문에 실행을 하면 Not trusted라고 에러가 발생   
그래서 lftp 설정파일을 수정해준다   
```
$ echo "set ssl:verify-certificate no" >> /etc/lftp.conf
```
이것역시 안되면 vi편집기로 입력해준다

그리고 나서 접속 테스트   
```
$lftp ftpuser@127.0.0.1    
```
비번을 입력하면 로그인이 되는데    
처음에 ls 명령어를 치면 아무것도 안나옴    
exit를 한 후 새로 gui상태에서 새로 로그인을 해주면 환경설정이 되면서   
디렉토리등이 만들어 지는데 다시 로그아웃을 하고 원래 계정으로 로그인을 해준다   

다시~
```
$lftp ftpuser@127.0.0.1
```
비번 입력 후 다시 ls를 해보면 이제 디렉토리들이 보이는 것을 확인

ltfp 사용방법 (이제 접속을 했으므로 remote가 됨)   
파입 업로드는 put 명령어     
다운로드는 get , 여러개 다운로드 mget   
이동은 cd, 뒤로 가기 cd -    


트러블 슈팅 
```
failed (Result: exit-code) since Tue 2021-03-30 15:57:24 KST; 4s ago
  Process: 15171 ExecStart=/usr/sbin/vsftpd /etc/vsftpd.conf (code=exited, status=2)
```

위의 결과는 
```
$systemctl status vsftpd
```
를 해서 나온것인데 따로 에러가 발생하지를 않는다. centos 8에서는 뭔가 에러가 있으면 start를 시키면    
에러가 발생하면서 진행이 안됨   
하지만 우분투에서는 restart를 해도 에러메세지가 안나오고    
status를 봐야함 (아마도 설정 어딘가가 disable되있거나...) 이런식으로 에러가 나는데 어디서 에러인지 잘 모름. 물론 구글링을 하지만 그것도 명확하지 않은 듯   

확실하게 에러메세지를 보려면, 직접 수동으로 실행을 직접해보면 됨   
```
$sudo /usr/sbin/vsftpd /etc/vsftpd.conf 
```

이렇게 직접 실행을 시키면 에러 메세지가 나옴    
500 OOPS: config file not owned by correct user, or not a file

그래서 확인해보니
```
 ls -l /etc/vsftpd*
-rw-r--r-- 1 ubun ubun  495 Mar 30 15:57 /etc/vsftpd.conf
-rw------- 1 root    root    1708 Mar 30 14:13 /etc/vsftpd.key
-rw-r--r-- 1 root    root    1403 Mar 30 14:14 /etc/vsftpd.pem
-rw-r--r-- 1 root    root       8 Mar 30 12:54 /etc/vsftpd.userlist
```
이런결과가 ...  
일단 소유자를 root로 바꿔보자    
```
sudo chown -R root:root /etc/vsftpd.conf
```

다시 ls로 확인해보면 root로 바뀌어 있고, 
```
$systemctl restart vsftpd
$systemctl status vsftpd
```

해보면 Active: active( running) 초록색 글씨가 나를 반김 ㅠㅠ   


## 이제 ftp접속
lftp로 접속을 한 후에 lftp 아이디@127.0.0.1  
```
$lftp ftpuser@127.0.0.1
```
를 한 후에 패스워드 입력 후    
ls를 입력해보면 디렉토리가 보이면 성공   

접속상태에서 ftp를 통해 업로드 해보기 ftp에서는 put 임
```
lftp ftpuser@127.0.0.1:/> put ~/Downloads/image.jpg
```
이렇게 하면 파일이 업로드? 가 되면 성공!

그리고 exit으로 빠져나온 뒤에   
현재유저로 (다른계정)으로 로그인하고 ls명령어를 치면 permission denied로 나오는것을 봐서는    
특정유저 로그인이 잘작동하는 것 같음   


## 로그인 못하게 막기 nologin
이제 테스트는 끝났으니.. nologin으로 바꾸기. 이렇게 되면 셀에 접속할 수 없게 된다   
```
$sudo usermod /sbin/nologin ftpuser
```
혹시 안되면 -s 옵션을 붙인다. (인자)   

아무튼 이렇게 되면 유저는 그대로 남아있지만 로그인은 할 수 없는 상태가 된다     
(로그인화면도 안나옴)

그 다음에 cat /etc/passwd 를 확인해보면   
ftpuser:x:1001:1001::/home/ftpuser:/sbin/nologin 요렇게 바뀌어 있음   
이렇게 되면 처음로그인 화면에도 안나오고, ftp로도 접속을 못하게 된다  
(-L 옵션도 있기는 함, lock the user account 기능인데    
암호화 시킨 패스워드 앞에 !를 넣어주고 로그인을 못하게 하는 기능이라고 함   
다른 내용이기는 한 듯함)

다시 로그인 가능하게 하려면    
위의 usermod로 shell을 지정해준다 /bin/bash (-s 옵션 넣어주기)   

```
$sudo usermod -s /bin/bash ftpuser
```

마지막으로   
유저를 삭제하려면 userdel을 사용하면 된다 -r 옵션 (man 보기)

참고 사이트   
https://www.centlinux.com/2020/01/how-to-install-secure-ftp-server-centos-8.html


