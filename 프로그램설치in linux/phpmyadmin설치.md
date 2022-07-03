# phpmyadmin 설치

[phpmyadmin에서 다운로드하기](https://www.phpmyadmin.net/downloads/)

압축풀기 ({VER} 부분은 버전에 맞는 파일명으로 바꿔준다, tab으로 하면 편함)  
```
$ tar xvf phpMyAdmin-${VER}-all-languages.tar.gz
```

압축푼 폴더채로 /usr/share/phpmyadmin 디렉토리로 이동해주기   
```
$ sudo mv phpMyAdmin-{버전}/ /usr/share/phpmyadmin
```

tmp 디렉토리 만들어주기   
그리고 이어서 사용자:그룹 지정   
```
$sudo mkdir -p /var/lib/phpmyadmin/tmp
$sudo chown -R apache:apache /var/lib/phpmyadmin
```

데비안계열 (우분투, 라즈베리파이의 경우에 해당)  
유저와 그룹명이 apache가 아니고 www-data:www-data 로 조금 다르다    
```
$sudo chown -R www-data:www-data /var/lib/phpmyadmin
```

어떤 블로그에는  /usr/share/phpmyadmin/tmp 로 만드는 방법도 있던데   
딱히 경로는 중요하지 않은것 같다.. 나중에 한번 지워보고 어떻게 되나 해봐야겠다

이제 옮겨진 경로로 이동하자
```
$ cd /usr/share/phpmyadmin 
```
로 가보면 config.sample.inc.php 파일이 있는데    
파일명을 바꾸거나 복사한다음에 config.inc.php 로 만든다

샘플은 남겨두고 복사하기
```
$sudo cp /usr/share/phpmyadmin/config.sample.inc.php  /usr/share/phpmyadmin/config.inc.php
```

에디터로 vi나 vim 편집기로 열어서 내용 수정
```
$sudo vim /usr/share/phpmyadmin/config.inc.php
```

이제 열린 config.inc.php 파일의 내용 중에 수정할 부분이 있는데    
```
$cfg['blowfish_secret']
```
이 부분의 내용을 32 글자(32개) 이상으로 써 준다   

이건 매뉴얼 홈피에 나와있는 방식대로 그대로 써줌   
```
$cfg['blowfish_secret'] = '1{dd0`<Q),5XP_:R9UK%%8\"EEcyH#{o';
```
그리고 sql계정으로 (mariadb mysql:현재 사용하는 것)    
phpmyadmin으로 들어올 떄마다 매번 로그인해야하는데 그게 귀찮은 사람은   
아래 처럼 설정해도 된다고 함
**중요** 보안상 좋지 않으므로 참고만 하자  

매뉴얼홈피에 보면 Warning! 이 있다   
> Storing passwords in the configuration is insecure as anybody can then manipulate your database.

어쨋든 방법은 이런식이라고 한다
```
$cfg['Servers'][$i]['user']          = 'root';
$cfg['Servers'][$i]['password']      = 'changeme'; // 여기에 mysql 비번 적기
$cfg['Servers'][$i]['auth_type']     = 'config';
```

그래서 비번은 저장안하고 skip함   

그리고 temp 디렉토리 설정하기 위해서 아래의 변수를 찾는다.    
```
cfg['TempDir']
```
근데 없을 경우에는 그냥 하나 추가해주기     
아래 코드를 입력해준다   
```
$cfg['TempDir'] = '/var/lib/phpmyadmin/tmp';   
```
그리고 : 누르고 wq 를 눌러 저장하고 빠져나오기   

일단, config파일에는 넣어줬으나 실제로는 디렉토리가 없다    
없다면 만들어야한다 (아마 처음에 먼저 만들었을 것임(위에서 설명))   

그리고 temp디렉토리가 없으면 phpmyadmin을 실행하게 되면    
Permission denied 와 함께 아래와 같은 에러가 발생   
Backtrace

```
./libraries/classes/Config.php#1285: mkdir(
string '/usr/share/phpmyadmin//var/lib/phpmyadmin/tmp/twig',
integer 504,
boolean true,
)
```

temp 안만들면 어떻게 되나 봤더니, warning 메세지!   

이제는 아파치 웹 서버 설정파일 만들어주기   
아마 없을 것이다.. 그래서 어차피 빈 파일로 만들면서    
저장될 듯  

```
$sudo vim /etc/httpd/conf.d/phpmyadmin.conf
```

우분투/라즈베리파이  sudo vim /etc/apache2/conf-available/phpmyadmin.conf 여기에 만든다

아래내용을 copy & paste
```
# Apache configuration for phpMyAdmin
Alias /phpMyAdmin /usr/share/phpmyadmin/
Alias /phpmyadmin /usr/share/phpmyadmin/
 
<Directory /usr/share/phpmyadmin/>
   AddDefaultCharset UTF-8
 
   <IfModule mod_authz_core.c>
     # Apache 2.4
     Require all granted
   </IfModule>
   <IfModule !mod_authz_core.c>
     # Apache 2.2
     Order Deny,Allow
     Deny from All
     Allow from 127.0.0.1
     Allow from ::1
   </IfModule>
</Directory>
```

대충 내용은 디렉토리 설정해주는 것이고   
127.0.0.1 localhost만 승인하고 나머지는 거부하게 해놓는 설정인듯하다   

완벽히는 잘 모름   
위의  
Alias 는 맨앞을 /phpmyadmin 과 /phpmyAdmin으로 되어 있는데 (중간에 대문자 A)   
별칭을 자기 맘대로 해주면 됨   
예를 들어 Alias /mydb /usr/share/phpmyadmin/ 로 하면   
phpmyadmin 접속할 때 localhost/mydb 이런식으로 하면 접속이 됨   
아마도 phpmyadmin 이라는 것은 다 알기때문에 별칭으로 하면 보안상 좋다고 하는 것   
같다고 다른 블로그에서 봤는데, 흠.. 어차피 다른아이피는 못들어오게 되있어서   
상관없지 않나 싶다.. 잘 모르겠음. 아니면 짧게 /php 라고 해도 좋을 듯  
어쨌든 저것도 그대로 skip ㅋㅋ 그대로 복붙 함  

이건 확인용인데 아파치 설정 validate 라고 함  
```
$ sudo apachectl configtest
```
맞게 설정했으면 Syntax OK 라고 나옴 

그리고 httpd 재시작 
```
$sudo systemctl restart httpd
```

데비안 계열
```
sudo systemctl restart apache2
```


마지막 중요한 SELinux 설정   
이거 무시했다가 계속 에러가 남   
아마 SELinux를 관련 설정안하면 phpmyadmin 들어가면 Access Denied 라고 접속이 안될 것임   
처음에 에러 메세지가 안나오고 하얀화면만 나오면   
/etc/php.ini 파일을 설정해서 에러가 표시되게 해야함    

대개 centos는 enforcing 인가로 모드가 설정되어 있다고 함   
그래서 퍼미션 거부 에러가 계속 난다. (접속 시도시에) 이것을 몰라서 포기했다가   
여담으로 dbeaver로 깔았다가 설치 쉽고 좋았는데,   
그러다가 다시 한번 시도해봤는데 이게 문제였다는것을 알게되었음   

어쨌든...  
/usr/share/phpmyadmin 를 httpd에 허용하게 끔 해주는 것이라고 함;;   
```
$sudo semanage fcontext -a -t httpd_sys_content_t "/usr/share/phpmyadmin(/.*)?"
```

그리고 적용
```
$sudo restorecon -Rv /usr/share/phpmyadmin
```

방화벽도 허용해주기
```
$sudo firewall-cmd --add-service=http --permanent
```
그리고 이어서 리로드
```
$sudo firewall-cmd --reload
```

>default zone도 확인해야함 아마 firewalld 관련  찾아보기

이제 접속하기    
브라우저에서 본인의 ip주소/phpmyadmin 하면 접속이 됨    
그러면 db로 계정으로 로그인하면 완료!
