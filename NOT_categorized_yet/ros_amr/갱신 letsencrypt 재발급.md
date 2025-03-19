## let's encrypt 갱신
90일 기간 후에 바로 갱신을 했어야 하는데... 날짜도 등록을 해놓고  
이메일도 와서 알고 있었는데... 귀찮니즘에.. 망했다. ㅋㅋ

처음에 갱신을 하려고 했는데 실패했다  
원래는 renew 한방이면 되는 줄 알았는데.. ~~에러 발생해서 유효기간 만료라서 안되는 줄 알고~~    
결국은 지우고 다시 발급 받음. 

~~다음에 다시 발급 받는다면 아래 명령어로 다시 도전 해보자..~~

갱신하려면 renew-ssl.md 파일을 참고하자

재발급
```
docker-compose run --rm certbot renew
```

> ㅋㅋ 이런;; 다시 유효기간을 넘겨버렸다;; on Dec2 2023  

아예 새로 발급 받을 필요없이 새로 renew 명령어가 통한다.  
먼저 `docker-compose stop` 을 이용해서 서비스를 중단 시킨다음에  

설정파일에서 dev로 변경한 후에 다시 `docker-compose up` 해 주고  
위의 명령어를 실행해주면 된다.  

이후 
```
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Congratulations, all renewals succeeded: 
  /etc/letsencrypt/live/qsp****.com/fullchain.pem (success)
```

이렇게 나오면 성공!

다시 서비스 중단 해준다음에 환경 설정을 prod 로 변경 후에   
다시 docker up (옵션 -d 와 함께) 해주자. 그럼 끝


## 아예 새로 발급 받는 방법
위의 방법이 안될 경우 아예 처음 부터 새로 발급 받는 과정   

> renew 명령어가 작동할 것이므로 아래 내용은 참고만 하자..   

```
docker-compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ -d example.com
```

> example.com 은 내 도메인 이름으로..

그랬으나.. 아마도 발급 받으면서 다시 http로 접속을 할 때 실패를 한 것인지..
아니면 퍼미션 에러가 난 것인지 정확히 모르겠다..   
일단 .well-know/acme-challenge 에서 404 에러가 발생한 것으로 봐서는   
nginx 설정 파일을 dev 전용으로 바꾸고서 했는데 이 부분이 없어서 에러 발생한 듯 하다

 
## dev로 변경
일단 결론을 말하면  
local에서 개발 할 경우에만 .env파일에서 dev로 사용하게 만들었으므로..   
서버에서 prod으로 되어 있는 변수값을 변경을 해줘야 한다.  
물론 이 방법은 certbot을 이용해서 아예 인증서를 **새로 발급** 받는 경우이다.   

> 이미 commit을 했으므로 다음에는 .env 파일만 변경해서 사용하면 됨   
> 아래의 새로 발급 내용은 참고만 하자. localhost로 작업할 때에도 문제가 없는 것 확인

요약 정리하자면.. 
1. .env 파일의 CONF_STATUS=dev 로 변경
2. docker-compose build && docker-compose up
3. docker-compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ -d example.com
4. 발급 성공 후 다시 .env 파일 CONF_STATUS=prod 로 변경
6. docker-compose build && docker-compose up

커맨드 정리
```
##먼저 디렉토리 이동 후에 
docker compose stop
vi ./.env
## dev 로 변경

docker compose up -d
docker-compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ -d 내blog주소.com
docker compose stop
vi ./.env
## 다시 prod 으로 변경
docker compose up -d
```

다음에는 새로 발급 받는 일이 없게 renew로 진행해보자   
키포인트는 아무래도 default_prod.conf 상태에서도 발급이 되는지 이다.   
그래도 안되면 default_dev.conf 파일로 도전  
그래도 안되면 아래처럼 다시 재발급?   


## 이후는 사용법만 참고하자~~  
## 가장 먼저 stop시키자
백그라운드에서 실행되고 있는 docker를 정지해주자
```
docker-compose stop
```
> down은 삭제되니 사용 금지

## 처음 다시 받는 것 처럼 진행 (새로 발급)
일단은 변경했던 내용을 바탕으로 적었으므로 참고만 하자

먼저 nginx/default_dev.conf 에 파일 추가해야함. 요렇게 변경 (이미 변경함 참고만 할 것)
```
location /.well-known/acme-challenge/ {
	root /var/www/certbot;
}
```
server 블럭 안에 추가

먼저 .env 파일에서 dev로 수정한 후 
```
vi .env
```

```
CONF_STATUS=dev
```

상위 디렉토리로 이동한 후에  
혹시 몰라서 certbot 디렉토리를 백업 (또는 삭제) 후에 진행함.   
물론 삭제를 안해도 될 것 같다는 생각은 든다..~~한번 스킵 한 후에 그래도 안되면 지워보자~~   
> 삭제 안해도 된다  
```
cd docker-laravel-blog
rm -rf certbot
```

그리고 빌드 진행 (build는 안 해도 된다)
```
docker-compose up -d
```

~이 상태에서 다른 터미널로 로그인하고  ~ 다른 터미널로 할 필요 없이 위에서 -d 옵션으로 백그라운드에서 돌아가게 해준다

```
cd docker-laravel-blog

docker-compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ -d example.com
```
**중요**   
> 역시 example.com 부분은 내 도메인으로 수정  
> 그리고 중요한 부분은 **http에서 letsencrypt.org 쪽에서 요청이 들어오므로**  
> http에서 응답 할 수 있어야 한다

이제 성공적으로 받았다면. 만료 기간등 안내가 나오고 

```
Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/******.com/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/******.com/privkey.pem
This certificate expires on 2022-**-**.
These files will be updated when the certificate renews.
```

다행히 다시 재발급을 받음

-d 모드로 실행했다면 `docker compose stop` 으로 종료 시킨 후에 
```
vi .env
```

다시 prod_default.conf 파일을 읽을 수 있게 변경.  
.env 파일을 열어서 다시 CONF_STATUS를 바꾸고 build 진행
```
CONF_STATUS=prod
```

그리고 build는 안해도 된다 (도커 버전에 따라 안될 시 build할 것. 상관없이 up만해도 환경변수 잘 읽는 듯 하다)
``` 
docker-compose up
```

이제 확인을 해보면 다시 잘 http로 입력해도 https로 잘 넘어가지고 
connection secure -> verified by Let's Encypt

이제 다 잘 되었다면 ^c 로 종료한 후에 
```
docker-compose up -d
```

휴~ 원래는 renew 인가 명령어만 하면 되는 것으로 알고 있었는데   
만료도 되었고 뭔가 처음부터 꼬여서 지우고 다시 하느라고 시간만 오래걸렸다...;;   
거진 2시간 소비 ㅠㅠ

마지막으로 git 상태는 defulat_prod만 servername 등이 바뀌어 있으므로  

	modified:   nginx_conf/default_prod.conf
이렇게 나오면 정상 





### 만약 nginx 컨테이너 exec나 run으로 접근해서
letsencrypt 부분까지 다시 지우고 다시 할려고 해도 docker-compose.yaml 파일에서  
ro (read only)로 해놓아서 지울 수가 없다.. 
chmod, chown으로도 해결이 안됨. 지울려고 하면 docker-comopse.yaml 파일에서 :rw 옵션을 주고 다시 docker-compose build를 하면 지울 수 있다.

```
rm: cannot remove 'letsencrypt/renewal': Read-only file system
rm: cannot remove 'letsencrypt/csr/0000_csr-certbot.pem': Read-only file system
rm: cannot remove 'letsencrypt/csr/0001_csr-certbot.pem': Read-only file system
rm: cannot remove 'letsencrypt/renewal-hooks/pre': Read-only file system
rm: cannot remove 'letsencrypt/renewal-hooks/post': Read-only file system
rm: cannot remove 'letsencrypt/renewal-hooks/deploy': Read-only file system
rm: cannot remove 'letsencrypt/keys/0000_key-certbot.pem': Read-only file system
rm: cannot remove 'letsencrypt/keys/0001_key-certbot.pem': Read-only file system
```

**하지만** 어차피 발급은 certbot 컨테이너에서 진행하고 거기에는 :rw 옵션이 들어가 있으므로  
위에서 certbot 컨테이너서는 읽고 쓰고  
nginx에서는 읽기만 하고 하는게 맞는거 같다. 결국 괜히 지울려고 노력하지 말자.   



