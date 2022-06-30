# mysql 직접 사용하기

> 잠깐 또는 phpmyadmin을 사용해도 된다.    
웹 브라우저에서 웹주소 뒤에 :포트 번호를 넣으면 됨 (docker-compose.yml 파일에서 설정)   
(만약 안되면 http:// 를 붙여서하면 됨)

`docker-compose up` 을 해서 컨테이너들이 실행이 되고 있는 상황에서 
일단 up을 시킨 후에 다른 터미널을 띄운다
```
docker exec -it mysql /bin/bash
```

그러면

root@158b8d66c70f:/# 처럼 프롬프트가 바뀐 것을 확인하고  

mysql에 들어갈 수가 있다 
```
mysql -u db유저아이디 -p
```

이제 비번을 물어보는데 로그인을 해준다 

```
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 8
Server version: 10.8.3-MariaDB-1:10.8.3+maria~jammy mariadb.org binary distribution
```
👍👍

`use Database이름;` 을 사용해서 DB을 선택해준다 

```
Database changed
MariaDB [mydatabase]> 
```
이렇게 잘 바뀌면 이제 부터 SELECT 부터 해서 쿼리를 진행할 수 있다

```
SELECT * FROM `users` 
```

id 이름 변경
```
UPDATE `users` SET `name` = '바꿀것적어주기' WHERE `users`.`id` = 1; 
```





