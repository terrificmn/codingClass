docker_ngnix_php 디렉토리에 만들어둔 copy파일 참고할 것
projects/docker_nginx_php/nginx_php_mysql_phpmydamin_docker-compose copy

httpd 서버와 거의 비슷함
다만, ngnix 용 conf파일 설정만 다름
ngix의 ports  8000 이나 80으로 설정 
만약 로컬에서 httpd가 돌아가거나 다른 서비스가 하고 있으면 안될 수 있으니 적절히 열어주자

디렉토리는 app 으로 연결함, 즉 app 디렉토리도 만들어 주기
Dockerfile은 이름은 PHP.Dockerfile 로 해놈 
당황하지말고 최상단 경로에 복사해 만들어 놓으면 됨

mysql은 mysqldata와 연결시킴
mysqldata 디렉토리 만들어주기

서버 테스트는 app/public/index.html or index.php 를 만든 후 
localhost 를 브라우저에 쳐본다 (포트번호 설정한 것에 주의)

phpmyadmin은 localhost:8080 를 브라우저에 쳐본다
비번은 yml파일에 mysql 부분의 environment에 정의된 것을 참고


그리고 잘 되는 거 확인했으면 이제 app 디렉토리를 지우고 
그 자리에 즉 최상단에 app으로 라라벨 new 프로젝트를 생성
그리고 다시 localhost로 가면
처음 라라벨 home이 나오면 완성!
