# SSL 인증을 하기 위해서는 
웹브라우저에 http로 접속을 하게 되면 대게는 보안관련해서 워닝이 뜬다  
물론 접속하는 것에는 문제가 전혀 없지만~ 나는 괜찮지만 다른 사람(유저) 입장은 그게 아닐꺼라는 생각이 든다  

<img src=0>

그래서 https를 사용해서 연결이 암호화 되어서 사용할 수 있게 해야한다

- Secure Socktes Layer (SSL)  
서버와 클라이언트 사이에 암호화된 link를 만들어서 통신하는 표준 보안 기술

> SSL certificates create an encrypted connection and establish trust.

서버에 private key 와 public key를 암호화 해서 만들어야 하는데  
도메인 가입했던 곳에서도 ssl 서비스가 있었는데 년 4달러 정도 했었던 것 같다.   

하지만 무료로 가능하다. 서버에서 인증서를 받을 수 가 있는데   
그게 **Certbot Let’s Encrypt Client** 이다.

<br/>

## 먼저 있어야 하는 것 
1. 웹서버가 깔려 있어야 함
nginx 기준으로 작성됨  

2. domain name이 있어야 한다. 구입 또는 공짜로 얻어야 함.   
namecheap, GoDaddy 와 같은 도메인 업체   
freenom 같은 공짜 도메인   
처음에는 도메인도 그냥 VPS (Virtual Private Server) 웹 호스팅 업체에 가입을 하면 도메인도 주는 줄 알았다.  
"도메인 관리도 공짜? 가능" 뭐 이런식으로 되어 있어서  
그런데 관리를 할 수 있게 되는 것일 뿐, 도메인 네임은 따로 사야 하는 것이였다.(몰랐었음 ㅠ)

3. 도메인 가입을 한 후 서버의 A DNS A Record 가 서버 public IP 주소로 지정이 되어 있어야 함   
웹 브라우저에 ip주소를 입력하지 않고 http:// 내도메인.com 해서 웹페이지가 되는 상태   
도메인을 가입/구입 했다면 여기는 금방 해결된다

4. 방화벽에서 https를 허용해줘야 한다.  
http는 80번 포트, https는 443번 포트  

> firewalld 를 확인한다. 우분투라면 ufw 관련 내용을 확인한다.   
docker를 사용한다면 (port를 연결을 했다면) firewall관계없이 오픈이 되는 점 참고한다  

그리고 현재 포스팅 내용은 docker, docker-compose를 활용한 내용이고  
나중에 기억하기 위해서 하는 포스팅이기도 하기 때문에   
중간중간 내용이 생략이 되어 있을 수도 있어서 깃허브를 참고하면 좀 더 나을 듯 합니다.  

> docker로 구성, php, 라라벨에 특화된 내용임에 주의

<br/>

## certbot을 직접 설치 후 실행할 때  
사실 이번 포스팅은 docker 컨테이너인 certbot 으로 진행한 내용을 정리하려고 했지만  
그 전에 직접 certbot을 설치해본게 있어서 정리한 내용도 남겨본다  

docker를 사용하고 있다면 스킵하고 아래 부분으로 넘어가자  
[docker에서 certbot을 실행 내용보려면 점프](#certbot-도커-컨테이너)

> 당연하겠지만 docker 컨테이너로 nginx가 돌아가고 있다면   
직접 설치한 certbot에서 nginx를 인식하지 못한다. 그래서 docker로 구성했다면  
certbot도 docker 컨테이너로 구성하는게 편할 듯 하다.  

- CentOS / RHEL 계열 기준   
먼저 Certbot Let’s Encrypt Client 설치   
```
sudo dnf install epel-release
```

설치
```
sudo dnf install certbot python3-certbot-nginx mod_ssl
```

> apache를 사용한다면 python3-certbot-apache 를 설치

설치 후 `which certbot` 를 실행해보면 잘 설치되어 있는 것을 알 수 있다
```
/usr/bin/certbot
```
잘 설치가 되었다

이제 `certbot --nginx -d domain_name` 입력해서 실행. 자신의 도메인이름을 넣는다
```
sudo certbot --nginx -d domain_name@com
```

email 주소를 물어보는데 주소를 넣어준다   
광고수신은 No를 해주면 (선택)   

이제 certificate files 이 생성이 되는데 /etc/letsencrypt/live/내도메인이름   
경로에 pem 파일이 생성이 된다

<br/>


## certbot 도커 컨테이너
먼저 깃허브에서 클론을 받는데  
업데이트가 되어 있기 때문에 여기에서는 현재 추가했던 내용 위주로 정리함  

[docker-laravel 관련해서 깃허브에서 클론해서 사용](https://github.com/terrificmn/docker-laravel.git)

나중에 다시 한번 참고하려고 포스팅, 자세한 내용은 깃허브 README 확인하세요  

<br/>

## docker-compose파일 
nginx 컨테이너에 volumes 추가 지정하는데 이는 certbot 관련 파일들을 인식하기 위해서이다   
```
- ./certbot/www:/var/www/certbot/:ro
- ./certbot/conf/:/etc/letsencrypt/:ro 
```
:ro read-only를 해줘서 컨테이너에서 파일을 업데이트 하지 못하게 해준다   
혹시 모를 에러를 줄일 수 있다  

certbot 컨테이너를 추가해준다. 아래와 같은 모습   
```
certbot:
  image: certbot/certbot:latest
    volumes:
      - ./certbot/www/:/var/www/certbot/:rw
      - ./certbot/conf/:/etc/letsencrypt/:rw
```
certbot 컨테이를 실행할 때 certificates를 /etc/letsencrpyt 디렉토리에 만들어준다. 컨테이너와 파일들을 공유 연결 해준다

<br/>

## nginx 설정파일 default.conf 파일에 location 수정
default_dev.conf와 default_prod.conf 2개가 있는데   
default_dev는 로컬에서 개발할 때 사용하기 위해서 만들었고     
로컬에서 https로 할 필요가 없기 때문에 https로 돌려보내지 않고 사용

> 깃허브의 소스코드 참고 

default_prod.conf 파일에서 설정 내용은    
이제 server {} 블럭에 80번을 listen을 하고 있는데 (http:// 식으로 입력했을 때)  
모두 https로 돌려보내기 위해서 아래와 같은 예로 바꿔준다  

```
server {
    listen 80 default_server;
    listen [::]:80;
    index index.php index.html index.htm;
    server_name example.com www.example.com;   ## server에서 적용시 도메인이름 바꾸기

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }
    ## 80번 포트 http로 들어온 것은 https로 return 시킴
    return 301 https://$host$request_uri;
}
```
example.com 은 **자신의 도메인 이름**으로 맞게 바꿔준다
location / 블락에서 80번 포트로 들어온다면 443포트로 redirect를 시켜준다

그리고 바로 아래줄에 https에 443 포트 부분에 대한 새로운 server {} 블럭을 추가해준다   

라라벨을 사용하므로 root 부분에 /var/www/html 에서 한번 더 /public 까지 지정  
코드는 아래처럼 참고
```
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;

    server_name example.com;
    root /var/www/html/public;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;  
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem; 
    
    location / {
      try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        try_files $uri =404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass php:9000;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
    }
}
```
역시 *example.com* 은 **자신의 도메인 이름**으로 변경해준다   
ssl_certificate, ssl_certificate_key 관련해서 certbot에서 만들어준 것을   
nginx 역시 볼륨으로 연결을 했고 이를 인증할 수 있게 파일 위치를 지정  

<br/>

## docker-compose build
docker-compose build를 할 때 권한 문제가 발생하면 
```
cd storage/app
sudo chmod -R 775 images
```

이제 빌드가 끝나면 docker-compose up을 해줘야 하는데   
.env 파일의 CONF_STATUS를 dev로 먼저 해놓은 상태에서 docker-compose up을 해준다

> nginx의 설정파일을 다른 것을 사용해서 (http에서만 잘 돌아갈 수 있게..)   
먼저 http 상태에서 certificates를 성공적으로 발급을 받아야 하기 때문   

<br/>

## certbot 으로 인증서 발급
이제 docker-compose up을 해준다 
```
docker-compose up
```

그리고 certbot 컨테이너를 통해서 certificates를 발급 받자   
-d example.com 옵션에서는 **자신의 도메인 이름**으로 수정해준다
```
docker-compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ -d example.com
```

> 옵션 certonly는 인스톨 없이 인증서를 생성  
webroot 은 nginx의 웹서버를 이용   
webroot-path 는 challenges를 위한 certbot의 루트 디렉토리
마지막으로 d 옵션은 도메인 이름 (인증을 받은 대상)

email 주소와 동의를 Y해서 입력한다면 발급을 시작한다.

발급이 성공적으로 끝났다면. 
web (nginx) 컨테이너에서 volumes 부분에서 default_dev.conf 에서  
default_prod.conf로 바꿔주기 위해서 .env 파일을 다시 한번 수정해준다

.env 파일 중
```
CONF_STATUS=prod
```

이제 docker를 stop 시킨 후에 (^C 컨트롤+C) 다시 docker-compose up

이제 nginx 설정 파일에서 http는 https로 돌려보내고  
443포트로 들어온 요청에서 ssl_certificate, serificate_key를 통해서 인증이 이루어질 수 있게 된다.

그래서 실제 웹브라우저에서 블로그 주소를 입력하면  

<img src=1>

접속도 잘 되고 보안도 👍👍 (connection secure)
