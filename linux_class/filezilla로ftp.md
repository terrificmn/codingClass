# host 컴 또는 외부에서 Ftp 접속/전송 확인하기

windows 호스트 컴으로 Ftps접속을 할 때에는   
리눅스에서는 lftp 를 설치해서 (클라이언트)로 접속할 수가 있었는데   
윈도우용으로도 lftp버전이 있기는 한데; 설치가 잘 안되서   
그냥 filezilla로 설치해서 테스트 해봄   

일단 사이트 관리자에서 ftp서버를 주소 및 아이디 등을 등록을 하는데..

여기에서 호스트에는 가상머신 혹시 리눅스머신 아이피를 입력해주고   
프로토콜은 FTP로 선택    
vsftpd로 (very secured ftp)해서 sftp인줄 알았으나 아니였음 ㅋㅋ   
FTPS라고 보면 됨 (21번 포트)   

그래서 프로토콜을 ftp - 파일 전송 프로토콜 로 선택을 해주고   
포트번호는 빈칸으로 남겨놓아도 됨   

# FTPS 와 SFTP 
먼저 ftp에서 발전된 형태인 FTPS는 FTP Secure 또는 FTP-SSL 이라고 불림  
FTPS는 방식에 따라 (21번 포트만 사용하거나 다른 포트 990번포트와 같이 사용)  

SFTP 는 22번 포트만 사용하며   
SFTP는 SSH FTP로 명령어와 데이터를 암호화해서 전송  
SSH SSH(프로토콜)채널을 통해 파일을 전송하는 확장방식으로 만들어졌다고 함  


# FTPS에서 Implicit vs Explicit 방식
암호화는 묵시적 FTPS와 명시적 FTPS 방법이 있는데

먼저 나온 암호화 방법이 묵시적 FTP 방법인 Implicit FTP 방법이라고 한다   
다른 포트번호를 사용 990번 포트를 사용한다.. 아...그래서 990번 포트를 개방했군;;;      
로그인을 하기전이나 파일전송전에는 990번 포트를 이용해서 SSL을 연결을 한다고 함.   
그리고 전체 FTP 세션이 암호화 되지만 현재는 deprecated 프로토콜이라고 여겨진다고 함   

두번째 방법은 Explicit FTP 방식이다. 로그인을 하기전에 같은 FTP 포트번호인    
21번 포트로 이루어지고 SSL 접속도 21번 포트를 통해 함   
데이터 전송을 시작하기전에 어떤 데이터를 보호해야하는지 선택할 수 있는데, 선택을 안했으면   
접속이 거부되거나 예전 긱본 FTP방식으로 데이터 전송이 이루어진다.   


# TLS?
TLS 란?   
- Transport Layer Security    
- 해커등이 데이터 전송중에 개인 정보(비번, 신용카드번호 등..)을 가로챌 수 있는 것을 못하게    
암호화 시키는 것   
- SSL (Secure Socket Layers)로 부터 발전된 방식    
- 키 페어(한쌍)을 이용하는데, public (다른사람들이 알 수 있음) 와 private (소유자만 알 수 있음) 키 2개로 사용해서    
- asymmetric cryptography 이라고 하는데,, 어렵다.. 이런게 있구나;;   
- 키의 길이가 중요한데  2048 bits가 선호된다고 함   
- 데이터를 보낼 때 secret key를 통해 보내는 쪽에서 암호화하고 받는 쪽에서 암호를 푸는 방식   
- 여러가지 키를 생성하는 방식중에 RSA, Diffie-Hellman 등등... 암튼 여러가지가 있음    
- X.509를 사용해서 서드 파티인 Certificate Authority(CA)로 인증받은 public key를 사용하는 것이 안전한 방법이라고 함   
- X.509 standard for Public Key Infrastructures (PKIs)   


어쨋든 그래서 vsftpd를 설치하고 셋팅할 때 TLS 관련해서 key, pem파일을 만드는데    
```shell
$sudo openssl req -x509 -nodes -keyout /etc/vsftpd/vsftpd.key -out /etc/vsftpd/vsftpd.pem -days 365 -newkey rsa:2048
```
여기에 보면 -x509 로 public키를 만드는 것 같고, rsa방식 2048bits로 만드는 것을 대충 알 것 같다;;




# 참고 FTPS와 SFTP의 장단점

참고한 사이트 보기  
[Pros vs Cons](https://exavault.medium.com/the-difference-between-ftp-ftps-and-sftp-5f80a33a7838)   

[Explicit FTPS vs Implicit FTPS](https://www.ftptoday.com/blog/explicit-ftps-vs-implicit-ftps-what-you-need-to-know)


