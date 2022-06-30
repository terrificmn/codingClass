
웹서버가 깔려 있어야 함

먼저 domain name이 있어야 한다. 구입 또는 공짜로 얻어야 함
freenom

A DNS A Record 가 내 서버의 public IP 주소로 지정이 되어 있어야 함

그리고 방화벽에서 https를 허용해준다


Certbot Let’s Encrypt Client 설치
먼저 certbot 설치한다
centos 버전으로 설치
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

광고수신은 No를 해줌

Http traffic to https 로 해주는 것을 2번 Redirect로 해줌

이제 certificate files 이 생성이 되는데 /etc/letsencrypt/live/내도메인이름 경로에 pem 파일이 생성이 된다


검증하기
https://www.ssllabs.com/ssltest/analyze.html?d=example.com


## renew
Let's Encrypt certificates 는 90일 동안 유효하다  
그래서 90일 후에 renew를 해줘야하는데 자동으로 할 수 있게 할 수 있다

30일도 채 안남았을 경우 다시 생성해주는 명령어가 있다
```
certbot renew 
```

> --dry-run 옵션을 넣어주면 갱신을 시뮬레이션 하듯이 테스트 한 후 저장은 하지 않는다.


## cron
cron job으로 자동으로 할 수 있게 해주자. 하루에 2번 실행할 수 있게 하는 것이 공식 추천이라고 한다

```
echo "0 0,12 * * * root python3 -c 'import random; import time; time.sleep(random.random() * 3600)' && certbot renew -q" | sudo tee -a /etc/crontab > /dev/null
```
위 명령은 noon, midnight, 매일 실행이 되는 것이고 파이썬 스크립트가 실행이 되고 
잠깐 멈추게 되는데 0부터 60분 가량 랜덤으로 멈추게 됨. (Let's Encrypt의 서버의 로드를 줄이기 위한 방법이라고 함)

그리고 나서 certbot renew가 진행된다고 함




