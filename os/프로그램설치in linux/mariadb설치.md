# mariadb 설치

## dnf로 설치하기
mariadb 설치 (10.3.10.3-27 버전 /2021년 2월 13일 확인)   

```
  $ sudo dnf install mariadb-server
```

참고:   
https://fedoraproject.org/wiki/MariaDB

> raspberry pi에서는 그냥 sudo apt로 설치하자.     
버전도 10.3 이다. 이게 속편하다.    
아래의 공식사이트에는 debian은 있지만 10 buster인가 있는데 raspbian버전을 못찾는 거 같다   

centOS repo는 보수적으로 안정적으로 접근하기 때문에 최신버전은 없음   
그래서 최신버전으로 받으려면 (안정화 버전 10.5.9)   
먼저 사이트 방문  
https://downloads.mariadb.org/mariadb/repositories/#distro=CentOS&distro_release=centos8-amd64--centos8&mirror=yongbok&version=10.5

> 버전이 계속 업데이트 될 것이므로 상황에 따라서 다른 버전을 받을 수도 있고 그에 따른 메뉴얼 참고하자

>우분투 일 경우에는 위의 사이트에서 우분투로 바꿔주면 됨  
그리고 하나씩 실행 시키면 됨 . 먼저 레포지터리 추가, 마리아디비 설치  
오히려 레포지터리 추가 및 바로 sudo apt-get install mariadb 여서 편함     
이하 mysql_secure_installation은 CentOS와 같음 (아래 참고)  

아래의 목록을 파일로 만들어 준다   
centOS 전용 YUM repository 라고 함   
/etc/yum.repos.d/ 안에 넣어주는데 파일명은 MariaDB.repo 로 하면 됨   

```
# MariaDB 10.5 CentOS repository list - created 2021-02-22 23:03 UTC
# http://downloads.mariadb.org/mariadb/repositories/
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.5/centos8-amd64
module_hotfixes=1
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
```

위의 내용을 복사 붙여넣기 한다   
```
$ sudo vi /etc/yum.repos.d/MariaDB.repo
```
파일이 없었으므로 저장하고 빠져나오면 repo파일 생성됨

리포지토리 리스트 보기 (dnf명령어로 해도 됨)
```
$ yum repolist
```
목록에서 MariaDB가 나오면 ok   

그 다음은 설치  
```
$sudo yum install MariaDB-server
```

시작 및 enable (자동시작) 만들기
```
$ systemctl start mariadb
$ systemctl enable mariadb
```
mariadb 잘 작동하는지 확인
```
$ systemctl status mariadb 
```

firewall 이 작동하고 있으면 firewall 규칙에 추가해 주기, 그리고 다시 시작
```
$ sudo firewall-cmd --permanent --add-service=mysql
$ sudo firewall-cmd --reload
```

마지막 마리아DB 셋팅
```
$ sudo mysql_secure_installation
```
맨 처음 Yes /No 에서 그냥 엔터누르고 진행
그 다음부터는 사이트 참고 (거의 yes)

참고 사이트 https://www.tecmint.com/install-mariadb-on-centos-8/

마리아DB 테스트   
마리아DB의 root 로 로그인 (시스템 root아님, 위에서 처음 installation에서 설정했던 비번 입력하면 됨)   
```
$ mysql -u root -p
```

로그인을 하게 되면 MairaDB [(none)]>  처럼 바뀌는데 
```
select version();
```

그러면 version 정보가 뜸. 그러면 오키