# NGINX 설치

[참고사이트: https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-centos-8](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-centos-8)

dnf로 설치하기
```
$sudo dnf install nginx
```

스타트. enbale은 시키고 싶으면 enable시키면 됨(자동시작)
```
$sudo systemctl start nginx
$sudo systemctl enable nginx
```

방화벽 포트열어주기, 포트를 직접 지정하는것이 아니라 서비스 이름을 지정하게 됨   
(여태껏 포트번호로만 주로 넣어봄)
```
$sudo firewall-cmd --permanent --add-service=http
```

방화벽 리스트 확인하기
```
$sudo firewall-cmd --permanent --list-all
```
services부분에 보면 추가가 되었다면 ok!

적용시키기
```
$sudo firewall-cmd --reload
```

읽어보기 환경설정 파일들
Content
    /usr/share/nginx/html: The actual web content, which by default only consists of the default Nginx page you saw earlier,   
    is served out of the /usr/share/nginx/html directory. This can be changed by altering Nginx configuration files.  

Server Configuration
    /etc/nginx: The Nginx configuration directory. All of the Nginx configuration files reside here.   
    /etc/nginx/nginx.conf: The main Nginx configuration file. This can be modified to make changes to the Nginx global configuration.   
    /etc/nginx/conf.d/: This directory contains server block configuration files, where you can define the websites that are hosted within Nginx. 
    A typical approach is to have each website in a separate file that is named after the website’s domain name, such as your_domain.conf.   

Server Logs
    /var/log/nginx/access.log: Every request to your web server is recorded in this log file unless Nginx is configured to do otherwise.   
    /var/log/nginx/error.log: Any Nginx errors will be recorded in this log.


## 멀티플 환경에서 사용할 수 있게 하기
아파치의 virtual hosts와 비슷한 기능인데, 서버한개로 여러개의 도메인이름으로 서비스할 수 있게 해줌    
그거를 Server Blocks라고 한다   
관련된 환경파일은 /etc/nginx/conf.d    

기본으로는 /usr/share/nginx/html 이 기본으로 작동하는 디렉토리라고 보면됨   
여러개에서 작동할 수 있게 하려면   
/var/www 디렉토리를 만들어줘야하는데    
이제 여기에서 your_domain자리는 각 도메인 이름이 되면 된다 (즉 프로젝트 디렉토리명이 될 듯)  
```
$sudo mkdir -p /var/www/your_domain/html 
```
그리고 그 디렉토리의 권한을 현재 user로 주는데 환경변수를 사용 (environment variable)
```
$sudo chown -R $USER:$USER /var/www/your_domain/html 
```

vi편집기로 간단한 html파일을 만든다   
또는 vscode로 ! (Emmet)기능으로 간단하게 html페이지 만들어주기  

이제 Server Block이 잘 작동하기 위해 디렉토리를 맞춰주기 위해 .conf 파일을 만들어 줘야함   
vi 나 nano 편집기로 만들어 준다

```
$ sudo vi /etc/nginx/conf.d/your_domain.conf
```

파일에 아래 내용을 추가해준다
```
server {
        listen 80;
        listen [::]:80;

        root /var/www/your_domain/html;
        index index.html index.htm index.nginx-debian.html;

        server_name your_domain www.your_domain;

        location / {
                try_files $uri $uri/ =404;
        }
}
```

listen은 말그대도 80번 포트로 http 로 듣고 있는 것   
root 경로를 설정해주고 (도메인(프로젝트) 디렉토리 위치)  
그 다음줄은 index.html 기본 파일들 정해줌   
그 다음은 server_name 이름을 정해주는 것인데, 이부분에서 localhost로 잘 될지 모르겠음   

에러가 없는지 확인은 
```
sudo nginx -t
```
ok, successful이라고 나오면 성공

재시작
```
$systemctl restart nginx
```

custom document root 로 http 컨텐츠 가능하게 만들어주기    
chcon 은 Selinux 보안관련 파일을 바꾸는 명령어
```
$ chcon -vR system_u:object_r:httpd_sys_content_t:s0 /var/www/your_domain/
```

참고로 -R 은 recursive -v는 verbose (작업을 보이게 해주는 것)


## ubuntu에서 NGINX 설치 ubuntu 18.04 우분투

업데이트 한 후 nginx 인스톨하기
```
sudo apt-get update
sudo apt-get install nginx
```

방화벽 설정하기, nginx 어플리케이션으로 등록할 수 있는 것을 보여준다
```
sudo ufw app list
```
그러면 결과가
Nginx Full  Nginx HTTP Nginx HTTPS 나오는데

```
  Nginx Full: This profile opens both port 80 (normal, unencrypted web traffic) and port 443 (TLS/SSL encrypted traffic)
  Nginx HTTP: This profile opens only port 80 (normal, unencrypted web traffic)
  Nginx HTTPS: This profile opens only port 443 (TLS/SSL encrypted traffic)
```

위의 것 중에서 일단  HTTP를 허용해보기   
```
$sudo ufw allow 'Nginx HTTP'
```

참고, http 또는 80 식으로 허용해줄 수 있다
```
$sudo ufw allow 80
$sudo ufw allow http
```
그리고 처음에 ufw를 enable 시키면 ssh가 방화벽에 막힐 수 있으므로 ssh를 사용하는 경우면   
ssh를 확인 후 열어주자

상태확인
```
$sudo ufw status
```
inactive 상태라면 
```
$sudo ufw enable
$sudo ufw status
```
이제 브라우저에 가서 localhost 나 ip를 입력해주면 NGINX 서버 웹컴 페이지를 볼 수 있다.   

이제는 설정만이 남음

먼저 디렉토리를 만들어준다   
기본디렉토리는 /var/www/html 인데   
여기에서 www 하위디렉토리로 만들어준다 일단 id_testsite 로 만들어 보자  
그래서 sgtubun_testsite 로 만듬  
```
$cd /var/www
$sudo mkdir -p sgtubun_testsite/html
``` 
이제 여기 경로에 html파일들이 있는 경로가 되겠음   
아예 절대경로로 전체경로를 만들어도 결과는 같음 (mkdir -p /var/www/sgtubun_testsite/html)

디렉토리의 소유권을 변경해준다 -> 유저   
이것도 경로는 편한대로 , user이름을 직접적어도 되고 변수를 사용해도 됨
```
$sudo chown -R $USER:$USER /var/www/sgtubun_testsite/html
```

퍼미션도 변경해준다. 
```
$sudo chmod -R 755 /var/www/sgtubun_testsite
```

이제 테스트 페이지를 만들어 준다. vscode, nano 맘에드는 걸로   
html까지 적을필요도 없을 듯 하고 hello world 정도면.. 
```
cd /var/www/sgtubun_testsite/html
vim ./index.html
```

## Virtual Host 셋팅하기
이제 설정파일을 열어서 수정해준다   
/etc/nginx/sites-available 에 가면 default  파일이 있는데 참고하면 된다   
일단 파일을 하나 만들자   
/var/www/ 이하가 sgtubun_testsite으로 만들었기때문에 sgtubun_testsite으로 만든다   
```
cd /etc/nginx/sites-available
sudo vim sgtubun_testsite 
```

default 파일을 열어보면 맨 아래 부분에 설명이 되어 있다   
```
Virtual Host configuration for example.com
You can move that to a different file under sites-available / and symlink that to sites-enabled/ to 
enable it
```
심볼릭 링크를 먼저 만든다음에 수정하자. 사실 순서는 상관없음   
먼저 여기 sites-available 디렉토리에 있는 내용은 원본 소스파일이 된다.    
심볼릭링크파일은 /etc/nginx/site-enable/  안에 만들어 준다  
절대경로로 만들어주는 것에 주의!
```
$ sudo ln -s /etc/nginx/sites-available/ubun_testsite /etc/nginx/site-enable/
```

좀 더 쉽게 하는 방법이 명령어를 인식할 수 있게 해서 실행하면 좀 더 편하게 할 수 있음   
먼저 해당 디렉토리로 이동한 후에 pwd를 실행해서 링크 파일 만들기 (``백틱으로 묶어줌)
```
$cd /etc/nginx/site-enable/
$sudo ln -s /etc/nginx/sites-available/ubun_testsite `pwd`
```
위 처럼하면 현재경로 (pwd명령어로 수행) 이하에 링크파일을 (같은 이름으로) 생성해준다 

그리고 심볼릭링크가 잘 되었는지확인
```
cd /etc/nginx/site-enable/
ls -li
```

```
ubun_testsite -> /etc/nginx/sites-available/ubun_testsite
```
이렇게 하늘색 표시가 되면 잘 된 것임   
만약 결과가 빨간색으로 나오면 -sf 옵션으로 다시 링크를 이어주고,아니면 심볼릭링크를 지우고 다시만든다   

링크파일을 열어서 내용을 써준다.    
(구지 처음파일을 만들었을 때 수정을 안하고 심볼릭링크를 먼저 만들고 수정한 이유는   
심볼릭링크에 좀 더 익술해질려고 ㅋㅋㅋ 뭔가 헛깔리니깐   
어쨋든 여기 심볼릭링크를 수정하면 참조하고 있는 원본 파일도 바뀐다)   

```
server {
    listen 81;
    listen [::]:81;

    server_name stgubun_testsite.com www.stgubun_testsite.com;

    root /var/www/stgubun_testsite/html;
    
    index index.html index.htm;

    location / {
            try_files $uri $uri/ =404;
    }
}
```
server_name 내가 주고 싶은것을 적어준다. stgubun_testsite.com 으로 만들어봄   
왜냐하면 서버이름은 내가 주고 싶은 것을 주는 것은 실제 도메인을 가리키고 있는 것이 아니기 때문이라고 함.   
어느 이름도 상관없음   
여기서 중요한 것은 root 부분의 경로를 내가 만든 디렉토리를 적어주면 된다. 최종 html파일 위치가    
index.html 파일을 읽어들이는 위치가 됨

root /var/www/stgubun_testsite/html;

포트번호는 80번이 기본인데, 81번으로 바꿔줌 80번으로 하고 테스트를 하면 기존의 원래 도메인들이    
많아서 그런 사이트들도 이동하게 되고 나만 알 수있는 이름으로 만들어도 작동이 제대로 안됨   
아마 제대로 서비스를 할려고 할 때나 가능한 듯 하다...   


추가 설정   
그리고 hash bucket memory problem 을 막기 위해서   
/etc/nginx/nginx.conf 파일의 주석처리되어 있는 것을 제거해준다   
찾아서 주석해제한다
```
server_names_hash_bucket_size 64;
```

에러는 없는지 확인 (syntax error)
```
$sudo nginx -t
```

```
$ systemctl restart nginx
```

그리고 접속을 해본다   
브라우저에 localhost:81 으로 입력하면 html 디렉토리에 입력했던 내용이 나오는 것을 알 수 있음   
이제 /var/www/sgtubun_testsite/html 로 이동해서 index.html 파일을 수정해보자   
아무런 말을 적으면 됨
```
<h2> Nginx works! great!! </h2>
```
그리고 저장한 후 다시 브라우저에서 새로고침해서 잘 나오면 성공

여기까지는 잘 됐지만, site_name에서 적어준 것으로는 작동이 안된다   

http://sgtubun_testsite.com
실제 도메인이 아니여서 작동을 안하는 듯 한데, 추후 더 공부가 필요할 듯 하다;;

일단 포트번호를 달리해서 했지만 일단 2개의 사이트를(?) 만드는데 성공했다   
브라우저에 localhost 라고만 치면 기본 서버 디렉토리 경로인    
/var/www/html 에서 index파일을 읽어서 웰컴 페이지가 뜨고    
localhost:81 이라고 하면 내가 만든 사이트가 나온다~   

오 끝!  
참고사이트:   
https://ubuntu.com/tutorials/install-and-configure-nginx#5-activating-virtual-host-and-testing-results   

https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04

