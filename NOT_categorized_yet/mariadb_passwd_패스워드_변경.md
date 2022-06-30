`docker-compose run --rm mysql` 직접 실행하지 말고 

주의 에러가 발생한다 

`docker-compose up` 으로 실행시킨 후에 
컨테이너에 접속을 해서 직접 명령을 실행하자

일단 up을 시킨 후에 다른 터미널을 띄운다
```
docker exec -it mysql /bin/bash
```

그러면 새롭게 도커 컨테이너에 들어가지는데 
프롬포트가 `root@cab84105e111` 이런식으로 바뀐다

이제 mariadb에 접속하자

mysql -u root -p 로 접속

```
mysql -u root -p
```
그러면 비번입력을 할 수 있다. 로그인

이제 비번을 바꾸자. 아래 명령은 MariaDB 10.2.0 이상 가능하다
```
MariaDB [mysql]> ALTER USER 'root'@'localhost' IDENTIFIED BY '바꿀비번';
```
```
MariaDB [mysql]> flush privileges;
```

그리고

일반계정도 바꾸기
```
ALTER USER larablog IDENTIFIED by 'new_password';
```

그리고 빠져나오기
```
exit
```

> UPDATE user SET password=PASSWORD('lara418MB_DB') WHERE user='larablog' AND Host = 'localhost';   
참고 이건 예전 버전인 듯 하다


docker디렉토리의 .env 파일에 비번을 바꿔주자   
라라벨프로젝트 내에도 .env 비번을 바꿔주자

