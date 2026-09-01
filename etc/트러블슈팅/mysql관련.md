# mysql 에러 해결하기
몇몇의 에러 발생했던 것을 모음

## Can't connect to local MySQL server through socket '/var/lib/mysql/mysql.sock'
```
 Can't connect to local MySQL server through socket '/var/lib/mysql/mysql.sock' (2)
(base) [sgtocta@localhost ~]$ systemctl status mariadb
● mariadb.service - MariaDB 10.5.9 database server
   Loaded: loaded (/usr/lib/systemd/system/mariadb.service; disabled; vendor pr>
  Drop-In: /etc/systemd/system/mariadb.service.d
           └─migrated-from-my.cnf-settings.conf
   Active: inactive (dead)
     Docs: man:mariadbd(8)
           https://mariadb.com/kb/en/library/systemd/
```
사실 작동하고 있는지 여부먼저 확인해야함   

```
$systemctl start mariadb  
```

```
Are you connecting to "localhost" or "127.0.0.1" ? I noticed that when you connect to "localhost" the socket connector is used, but when you connect to "127.0.0.1" the TCP/IP connector is used. You could try using "127.0.0.1" if the socket connector is not enabled/working.
```
이게 답인데 

그 다음 로그인 한 다음에 
```
$mysql -uroot -p
```

DB 프롬프트에서 아래 처럼 나오면 성공
```
MariaDB [(none)]> show databases;   
```

## 데비안 계열에서 라즈베리파이 에서 오류 - mariadb (mysql) 로그인시 접근 거부
데비안 계열에서 라즈베리파이 에서 오류 - mariadb (mysql) 로그인시 접근 거부

설치를 마치고 mysql_secure_installation을 해주면 root 권한 및 첫 보안 설정을 해 줄 수가 있다.
```
mysql_secure_installation
```
우분투나 CentOS에서는 그렇게만 해주면 설정은 끝이였는데  
첫 셋팅을 해주었음에도  
라즈베리파이에서는 root로 로그인할 때 비번을 넣고 로그인을 하면 접근에러가 난다.  

root (mysql)로 로그인 하려고 하면 에러발생
```
$mariadb -u root -p
```
mysql명령어로 해도 같음 ㅋㅋㅋ

```
ERROR 1698 (28000): Access denied for user 'root'@'localhost
```

이럴 때는 원래 테이블에 있는 것을 다시 초기화 시키고 다시 넣어줘야하는 것 같다

먼저 sudo로 로그인한다 -p 없이
```
$ sudo mysql -u root
```
하지만 이렇게 해도 안 될 수도 있다  
이러면 조금 곤란해지는데 왜냐하면 mysql root로 뭘해도 들어갈 수가 없어서이다.  
이럴때는 /var/lib/mysql 디렉토리를 통째로 날려버리는 방법을 택할 수도 있다.   
이면 해결책 아래를 참고하자~   

어쨋든.. 위처럼 하면 비번 없이 들어가진다.    
root 의 plugin 컬럼을 업데이트 그리고 Flush    
*flush privileges은 grant 테이블을 읽어서 mysql을 재시작하거나 reload 없이   
특정유저에게 권한을 바꿀 수 있게 해준다  

```
MariaDB> USE mysql;
MariaDB> UPDATE user SET plugin='mysql_native_password' WHERE User='root';
MariaDB> FLUSH PRIVILEGES;
```

그리고 루트의 비번을 다시 만들어 준다.
```
MariaDB> ALTER USER 'root'@'localhost' IDENTIFIED BY '뉴패스워드-입력';
MariaDB> exit;
```

그리고 재시작해준다
```
sudo systemctl restart apache2
```

이제 로그인하면 잘 됨
```
$mysql -u root -p
```
바뀐 비번 입력 후 
테스트겸.. 데이타베이스나 확인..
```
MariaDB [(none)]> show databases;

```

잘 나오면 성공!


## mysql에서 mysql.user 테이블이 없다는 식으로 나오는 경우
mysql에서 mysql.user 테이블이 없다는 식으로 나오는 경우 (정확하게 기억이;;;)

참고- 기억나는대로 메모를 해놓은 것이라.. 다소 정확하지 않을 수 있다    
안되면 다시 검색하는 수 밖에;; ㅠㅠㅠ

흠.. 라즈비안 기준으로 sudo apt remove mariadb-server --purge   
까지 해주고 다시 설치를 해도 (sudo apt update 후 다시 apt install mariadb-server)  
뭔가 에러가 발생했던 것으로 똑같이 발생한다..;;   
지웠다가 깔았으면 처음부터 시작해야하는데 그렇지 못한거 같다..   
어쨋든.. 정확한 에러 메시지는 기억이 않나지만..  

mysql.user doesn't exist 이런식으로 나왔던거 같다...   
즉, mysql 데이터베이스가 없다는 것..

mariadb error log 에러 로그 보는 법   
/var/log/mysql/mariadb.err  에 있는데..  
```
tail -50 /var/log/mysql/mariadb.err
```
로 확인해서 메세지를 확인해 본다.

만약 지웠다 깔았다는 반복하거나, /var/lib/mysql을 지워버렸을 경우   
(지우고 하면 된다는 구글 글에... 지웠다면 ㅠㅠ)

또는 sudo mysql -u root 를 비번없이 해도   
```
ERROR 1698 (28000): Access denied for user 'root'@'localhost  
```
처럼 나온다. 액세스 거부가 될 때 하는 두 번재 방법 

먼저 /var/lib/mysql 디렉토리를 지워준다   
```
$cd /var/lib
$sudo rm -rf mysql
```

그리고 해당 디렉토리에 다시 mysql db를 설치해준다
```
mysql_install_db --user=mysql --datadir=/var/lib/mysql --auth-root-authentication-method=normal
```
그리고 나서 
```
$li -l mysql
```
을 해서 사용자:그룹 권한이 mysql로 되어 있는지 확인   
만약 root로 되어 있거나 할 때에는 권한 바꿔주기

어쨋든 이러면 mysql db가 만들어 지는것 같다   
root로 (mysql계정 root)가 아닌 진짜 root 만들어 지기 때문에

먼저 소유권을 다시 셋팅! (만약 디렉토리가 지운게 아니라면 mysql_install_db 를 하기전에 변경한다)
```
sudo chown -R mysql:mysql /var/lib/mysql
```

그리고 나서 다시 (몇몇 파일 생성하는데 권한이 필요하므로 sudo 사용)
```
sudo mysql_secure_installation
```

이제 root비번을 다시 정해주면 잘 들어가 진다. 처음에 root 비번을 물어볼 때 엔터를 치고   
root 비번을 만들겠냐고 물어볼 때 yes 를 누르고 root비번을 다시 입력해주면 된다.

##