## vsftp 설치
ftp (vsftp) 설치 :요새는 보안 때문에 ~~비추천!!~~이라고 생각했었는데 ㅋㅋ    
예전에는 비추천이라고 잘못 알았지만 ~~sftp기능을~~ 이용해서 사용하면 더 안전하게 사용할 수 있다고 함  
그리고 vsftp 이름자체가 very secured ftp라고 함   

> sftp 는 22번 (ssh포트)를 사용하는 것을 의미, 딱히 ftp가 필요없이, ssh로 접속하듯이 ftp도 사용할 수가 있다.

~~업데이트된 기록 (29MAR 2021)~~   
업데이트 (Nov11 2023)

먼저 vsftpd 설치   
```
$ dnf install vsftpd
```

설치는 /etc/vsftd/ 에 설치되는데    
설정파일을 백업을 해두자  먼저 이동
```
$cd /etc/vsftd
$cp vsftpd.conf vsftpd.conf.backup
```

참고로 우분투 경우에는 vsftd 디렉토리가 따로 없고   
/etc/vsftpd.conf가 바로 있음    
그리고 우분투에서는 설치는 아래 처럼
```
$ sudo apt install vsftpd
```

이제 vsftpd.conf 파일을 열어서 환경설정 파일을 수정하는데, 사실 바꿀 부분은 딱히 없다.

기본파일에서 `write_enable=YES`, `chroot_local_user=YES` 정도를 주석해제 해주는데   

아래는 환경설정 설명
```
anonymous_enable=NO   # disable anonymous users #그대로
local_enable=YES   # allow local users  #그대로
write_enable=YES   # allow ftp write commands  # 주석제거
local_umask=022    # set default umask  # 주석제거
dirmessage_enable=YES   # enable messages on change directory
xferlog_enable=YES   # enable logging of uploads and downloads
connect_from_port_20=YES  # ensure PORT transfer connections from port 20 (ftp-data)
xferlog_std_format=YES   # keep standard log format  # 주석제거/ 안해도 됨(선택)
listen=NO    # prevent vsftpd run in stand alone mode
listen_ipv6=YES    # allow vsftpd to listen on IPv6 socket
pam_service_name=vsftpd   # set PAM Service name to vsftpd  #그대로
```

# AWS ftp 등록하기 (이 부분만 따로 정리하기)
서버에서는  
```
sudo apt install vsftpd
```
로 설치하고   
위의 설정 몇개만 건들여 주고 vsfptd 을 restart 시켜주면 된다   

그리고 클라이언트에서 filezila 를 깔아주고     
Site Manager 상단 왼쪽끝의 아이콘을 눌러서 
사이트를 추가할 때 Protocol은 SFTP - SSH File Transfer Protocol 선택해 준다

Host는 서버 아이피주소   
Port 번호는 빈칸   
logon Type을 Key file 로 해주고 pem키를 지정해주면 된다   
유저만 ubuntu로 한다

> 여기에서 User는 ftp로 로그인을 할 수 있는 유저이름을 적어주면 된다. 따로 만들어도 되고 현재 쓰고있는 계정으로 해도 됨

> 참고로 AWS 키로 로그인을 하는 경우에는 22포트 ssh를 사용하므로 서버에 vsftpd가 필요가 없다

## 유저 등록
이제 특정유저만  ftp를 사용할 수 있게 특정 유저를 등록해준다  
마찬가지로 같은 경로에 위치하는 user_list 파일에 유저를 등록해주면 된다   

이제는 ftp를 사용할 유저를 추가해주고 비번도 설정한다   

```
$ sudo useradd ftpuser
$ sudo passwd ftpuser
```

디폴트는 user_list에 들어가있는 유저들을 ftp접근이 거부가 되게 되어 있는데   
일단 특정 유저만 접근할 수 있게 허용해줘야한다   
일단 userlist_enable=YES 는 되어 있을텐데 userlist_deny=NO를 추가해준다   
(우분투에서는 user_list파일이 없음, 못찾은 것일지도.. 어쨋든 그냥 만들면 되기는 함)   
먼저 vsftpd.conf   

우분투에는 /etc/ftpusers 에 파일이 있는데 금지 유저 목록이 들어가 있으므로    
그냥 userlist로 하나 만들어 주자

새로 추가 (우분투 기준으로는 없음)    
```
userlist_enable=YES   # enable vsftpd to load usernames
userlist_deny=NO   # allow access to users in userlist
```
저장 그리고 나서   
리다이렉트 기능으로 user_list에 내용 추가해주기    
```
$sudo echo ftpuser >> ./user_list 
```
근데 퍼미션때문에 안된다면 그냥 편집기 열어서 추가해주자   

우분투는 
```
sudo vi /etc/vsftpd.userlist 로 만들고 
```
user를 추가해주자

ec2는 ubuntu 이므로 ubuntu 유저를 등록
```
userlist_enable=YES
userlist_file=/etc/vsftpd.userlist
userlist_deny=NO
```
centos에서는 userlist 파일이 있어서 등록이 되는 거 같은데 우분투는 따로 없으므로 
userlist_file에 해당경로를 써준다. 

예제 파일 복사해서 사용해도 무방..  
아래 주석에서 설명이 되어 있는 것 처럼, userlist_deny를 어떻게 설정하냐에 따라서 쓰임이 달라진다.  

먼저 NO로 설정하면 deny모드가 아닌, allow 모드가 되어서 특정 user만 넣어주면 다른 유저는 들어올 수가 없다.  
반대로 YES로 설정하면 deny모드가 되어서, 아래 리스트에 있는 유저는 모두 접속할 수가 없다.

아무래도 NO 로 설정하고 사용하면 더 좋은 듯 하다.

*NO 로 설정한 예 : 리스트에 있는 유저만 접속할 수가 있다.*
```
# vsftpd userlist
# If userlist_deny=NO, only allow users in this file
# If userlist_deny=YES (default), never allow users in this file, and
# do not even prompt for a password.
# Note that the default vsftpd pam config also checks /etc/vsftpd/ftpusers
# for users that are denied.
ftpuser
```


*YES 로 설정한 예 : 리스트 외에는 모두 접속할 수가 있다.*
```
# vsftpd userlist
# If userlist_deny=NO, only allow users in this file
# If userlist_deny=YES (default), never allow users in this file, and
# do not even prompt for a password.
# Note that the default vsftpd pam config also checks /etc/vsftpd/ftpusers
# for users that are denied.
root
bin
daemon
adm
lp
sync
shutdown
halt
mail
news
uucp
operator
games
nobody
```
파일 예.. centOS 같은 경우에는 /etc/vsftpd/ 디렉토리가 있어서 그 안에 user_list 파일이 있는데    
우분투는 아예 vsftpd 디렉토리가 없고 /etc/vsftpd.conf 만 있기 때문에   

위의 설명처럼 userlist_deny를 NO로 하게되면 파일에 있는 유저 목록만 로그인 할 수 있게 한다고 하니깐   
다른 유저 리스트는 지우고 내 계정만 추가해준다. 그러면 아예 오픈이 되어 버리는 것이니깐   
먼저 /etc/ftpusers 가 있는데 centos는 /etc/vsftpd/ftpusers   
에는 유저 목록이 잘 있는지를 확인하다. 아마도 여기에 있는 ftpusers에 있는 유저들은 금지   


## 홈 디렉토리만 개방
그리고 여기에서 유저의 디렉토리 허용하는 방식이 2가지 있음  
다시 vsftpd.conf 를 열어서 내용을 추가해준다  

먼저 첫 번째 방법은 홈디렉토리를 개방해주는 것   
chroot jail 이라고 불리는 것인데, 아래처럼 하면 특정유저의 홈디렉토리를  ftp 디렉토리로 사용하게 된다   
특정유저의 가장 root경로가 되는 셈 (home디렉토리로, 다른데는 접근할 수 없다)  
```
$ chroot_local_user=YES   # Create chrooted environment for users
$ allow_writeable_chroot=YES  # Allow write permission to user on chroot jail directory
```
chroot_local_user=YES 도 기본으로 되어 있고 (주석 되어있는 거 제거 )   
allow_writeable_chroot=YES 가 없어서 넣어줘야한다

```
You may restrict local users to their home directories.  See the FAQ for
# the possible risks in this before using chroot_local_user or
# chroot_list_enable below.
chroot_local_user=YES
```
이렇게 설명이 되어 있다.

이제 유저의 홈디렉토리 전체가 ftp에 사용될 수 있게 한다   

두 번째 방법은 ftp업로드 시에 홈 디렉토리가 아닌 특정 다른 디렉토리만 사용하게 할 수 있는 방법   
vsftpd.conf 파일에 추가해준다. 그리고 이때에는 allow_writeable_chroot 옵션은 입력하지 않는다  
```
user_sub_token=$USER
local_root=/home/$USER/ftp
```
특정 디렉토리를 만들고 (예: ftp 라고 만듬)
유저 환경 변수를 사용해서 ftp 디렉토리만 사용하게 하는 방법이 있다

(두 개 다 해보자 ㅋㅋ)


## 트러블슈팅
```
VSFTPD chroot_local_user problem - an unexpected TLS packet was received
```
lftp에서 접속해서 유저 로그인을 한 후에 명령어를 쳤을 때   
위와 같은 에러가 발생하면

> lftp 클라이언트에서 사용하는 프로그램 cli모드에서 

/etc/vsftpd.conf 파일에   
```
chroot_local_user=YES 
allow_writeable_chroot=YES
```
이 둘다 되어 있는지 확인해야함   
allow_writeable_chroot을 빼먹어서 에러가 난것임;;   
이것저것 하다보니 빼먹음 ;; 정신없음

> 500 OOPS: vsftpd: refusing to run with writable root inside chroot()

2개다 넣어주니 ftp 접속 및 명령어 성공   

방화벽 포트 열어주기
```
$ sudo firewall-cmd --permanent --add-port=30000-31000/tcp
$ firewall-cmd --permanent --add-port=990/tcp 
$ firewall-cmd --permanent --reload
```

vsftpd 시작
```
$systemctl start vsftpd
```

만약 이때 
```
500 oops bad bool value in config file for anonymous_enable
```
이런 에러가 발생하면 설정파일에 빈칸이 있어서 그러는 것이라고 함   

각각 마지막 줄에 띄어쓰기 되어 있는지 확인 후 빈칸을 다 지워준다  
그래도 안되면 아래 명령어 실행

```
$ cd /etc/vsftpd
$ sed -i 's,\r,,;s, *$,,' ./vsftpd.conf
```
빈칸이랑 CR 캐릭터를 지워주는 명령어임

