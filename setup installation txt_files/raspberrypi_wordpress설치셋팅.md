# 라즈베리파이에 워드 프레스 설치하기
준비는 php8.0과 mariadb, phpmyadmin 등이 설치되어야한다. 

라즈베리 php8.0 참고  

마리아디비 설치 참고

주의할점은 php8.0을 설치할 때 아파치와 연동되는 라이브러리도 설치 해줘야 아파치서버에서 php와 연동이 된다.

<br>

## wordpress 설치
먼저 홈페이지에서 다운을 받거나 zip파일과 tar.gz 형태를 제공합니다.  
wget으로 받아도 된다. (wget으로 받으면 현재 있는 경로에 받아짐)


```shell
$wget https://wordpress.org/latest.tar.gz
```
압축을 해제해준다
```
$cd ~/Downloads
$tar -zxvf wordpress-5.7.2.tar.gz
```
그리고 나서 파일을 아파치 서버의 디폴트 디렉토리(?)로 이동 시킨다

```
$sudo mv wordpress /var/www/html/
```
이러면 압축이 풀린 디렉토리의 파일 전체가 이동된다

그리고 나서, 권한 관련해서 소유자와 소유그룹을 apache2로 바꿔줘야한다
```
$cd /var/www/html
$sudo chown -R www-data:www-data wordpress
```
-R 옵션을 넣었기 때문에 wordpress 이하의 소유권도 바뀐다 

<br>

## wordpress 관련 db설정하기
마리아db를 들어간다. 
```
$mariadb -u root -p
```
비번 입력한 후 데이터베이스를 만들어 준다

```
MariaDB> CREATE database wordpress;
```

이제 워드 프레스를 처음으로 실행하면 DB를 셋팅하게 되는데   
여기서 root를 사용하게 되는데,

>검증되지는 않았지만.. 워드프레스를 root로 로그인할 수 있게 셋팅하니깐
mariadb에 root로 로그인을 하는 것이 막혔다. 바로 전까지는 root로 로그인시 에러가 없었는데 다시한번 root로 로그인이 안됨


그래서 root 권한을 이용하기 보다는 다른 유저를 만들어서 그 유저에게 위에서 만든 wordpress 데이터베이스를
사용할 수 있게 권한을 주자~

어차피 wordpress 데이터베이스 하나 밖에 없지만 root로 하기보다는 일반 유저를 만들어서  
그 유저에게 wordpress만 사용할 수 있는 권한을 주자  

>이는 실무에서도 많이 쓰는 방식이라고 함!

마리아db에 로그인이 되어 있는 상태에서 
```
MariaDB> CREATE USER 'wp_admin'@'%' identified by 'wordpress1234';
MariaDB> grant all on wordpress.* to 'wp_admin'@'%';
```
새로운 유저인 wp_admin을 만들고 (뒤에 identified 이하는 비번을 정해준다)   

wordpress 데이터베이스의 테이블을 사용할 수 있는 모든 (all) 권한을 줌 to 'wp_admin'유저에게

이제 설치 및 database까지 만들었으므로 워드프레스 실행을 한다.  
브라우저에 localhost/wordpress 를 입력한다

혹시라도 문제가 있을 경우 
[워드프레스 how to install WordPress 참고하기](https://wordpress.org/support/article/how-to-install-wordpress/)  
  
이제 워드프레스 페이지가 로딩이 되면서 기본 설정 및 그리고 db관련해서 설정도 해준다  
워드프레스로 사용할 아이디/비번을 등록하게 된다.


위에서 만들어준 mariadb 유저인 wp_admin 및 데이터베이스는 wordpress 비번 등을 입력해주게 되면 된다.

이제 로그인을 해서 원하는 테마로 바꿔주면 된다