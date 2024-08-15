
업데이트 필요!!!!!!!!!

실패할 경우 아래 처럼 나오게 됨
```
Certbot failed to authenticate some domains (authenticator: webroot). The Certificate Authority reported these problems:
  Domain: qs**log.com
  Type:   unauthorized
  Detail: 2400:8902::f03c:93ff:febc:9c54: Invalid response from https://qs****.com/.well-known/acme-challenge/XY4XjjZb_Up_8Je3ju3Sm_qNx0Vs-oyuWOeTrqhhxuE: 404

Hint: The Certificate Authority failed to download the temporary challenge files created by Certbot. Ensure that the listed domains serve their content from the provided --webroot-path/-w and that files created there can be downloaded from the internet.

Cleaning up challenges
Failed to renew certificate qs****.com with error: Some challenges have failed.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
All renewals failed. The following certificates could not be renewed:
  /etc/letsencrypt/live/qs****.com/fullchain.pem (failure)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1 renew failure(s), 0 parse failure(s)
Ask for help or search for solutions at https://community.letsencrypt.org. See the logfile /var/log/letsencrypt/letsencrypt.log or re-run Certbot with -v for more details.
```

이는 docker 컨테이너가 실행되고 있을 때 http로 응답을 해야하는데 응답을 못해줘서? 그럴 것임  
먼저 docker를 내리고 설정파일을 바꾼다

```
docker-compose stop
```
> 아마도 docker-compose file이 있는 곳으로 이동을 먼저 해야할 수도 있음

환경 설정파일을 열어 변경
```
$ vi .env
```
prod 에서 dev로 바꿔준다

그리고 다시 docker 실행. 이번에는 detach 모드로 실행해서 background에서 돌아가게 해준다   
```
docker-compose up -d
```

certbot 컨테이너를 실행해줘야 하게 때문이고, run 명령으로 실행시켜준 후에   
종료 후 컨테이너 자동 삭제하게 해준다

```
docker-compose run --rm certbot renew -v
```

그러면 아래처럼 나오면 성공
```
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Processing /etc/letsencrypt/renewal/qs****.com.conf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Certificate is due for renewal, auto-renewing...
Plugins selected: Authenticator webroot, Installer None
Renewing an existing certificate for qs***g.com
Performing the following challenges:
http-01 challenge for qs****.com
Using the webroot path /var/www/certbot for all unmatched domains.
Waiting for verification...
Cleaning up challenges

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Congratulations, all renewals succeeded: 
  /etc/letsencrypt/live/qs****g.com/fullchain.pem (success)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```

만약 기간내에 재발급을 하지 못했다면, 좀 더 복잡하게 된다.   
새로 발급을 받아야한다.  다른 md파일 참고하기

> 기간이 지났더라도 위의 방법으로 다시 하면 재발급이 잘 된다.