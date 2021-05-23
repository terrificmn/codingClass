# 라즈베리파이에 워드 프레스 설치 준비
준비는 php8.0과 mariadb 등이 설치되어야한다

라즈베리 php8.0 참고
마리아디비 설치 참고

주의할점은 php8.0을 설치할 때 아파치와 연동되는 라이브러리도 설치 해줘야 아파치서버에서 php를 잘 읽는것 같음

## wordpress 설치
먼저 홈페이지에서 다운을 받거나 zip파일과 tar.gz 형태를 제공
wget으로 받아도 된다. (wget으로 받으면 현재 경로에 받아지므로 주의)


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

## wordpress 관련 db설정하기
마리아db를 들어간다. 
```
$mariadb -u root -p
```
비번 입력한 후 데이터베이스를 만들어 준다

```
MariaDB> CREATE database wordpress;
```

아래는 확인해봐야함. root래서 딱히 권한 설정은 필요해 보이지 않는데.. 테스트 필요할 듯 함;;
```
MariaDB> GRANT ALL PRIVILEGES ON wordpress.* TO 'root'@'localhost' IDENTIFIED BY '비번';
MariaDB> FLUSH PRIVILEGES;
```

이제 설치 및 database까지 만들었으므로 워드프레스 실행을 한다
브라우저에 localhost/wordpress 를 입력한다

혹시라도 문제가 있을 경우 
[워드프레스 how to install WordPress 참고하기](https://wordpress.org/support/article/how-to-install-wordpress/)

이제 워드프레스 페이지가 로딩이 되면서 기본 설정 및 
그리고 db관련해서 설정도 해준다
워드프레스로 사용할 아이디/비번을 등록하게 된다

이제 로그인을 해서 원하는 테마로 바꿔주면 된다



