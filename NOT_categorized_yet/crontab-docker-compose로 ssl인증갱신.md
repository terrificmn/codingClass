# certbot 인증하기
certbot으로 받은 certificate은 유효기간이 90일이어서 대충 한달에서 두달사이에 갱신을 해줘야하는데   

docker-compose 로 한번 실행해주면 간편하게 가능하다
```
docker-compose run --rm certbot renew
```

갱신된 것 확인하기
```
docker-compose run --rm certbot certificates
```


## crontab 아직 실행 안해봄
테스트 전 

이를 crontab으로 해보자

먼저
```
crontab -e
```

그리고 나서 아래줄을 입력
```
0 5 1 */2 *  /usr/local/bin/docker-compose up -f /var/docker/docker-compose.yml certbot
```

5 am 에 매 2개월 마다 실행을 함
docker-compose up 명령어의 절대경로를 확인 후 입력해주고   
-f 옵션 이하의 docker-compose.yml 파일의 위치도 현재 프로젝트의 절대경로로 적어준다

> crontab에 대해서 좀 더 알아봐야할 듯 하다
