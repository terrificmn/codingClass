# docker 만들기
- 서버를 apache로 할지 ngnix로 할지 결정
- 결정한 dockerfile , docker-compose.yml, default.conf 파일 등을 깃허브에 올리기

## 준비
깃허브로부터 서버에 다운을 받으면
디렉토리부터 일단 만든다 
만들이름은 아무거나 상관없고
이제 Dockerfile, docker-compose.yml 은 최상위디렉토리에 준비하게 놓고
그리고 3개의 디렉토리를 만드는데 httpd, mysqldata, app
mkdir로 디렉토리를 만든다. 이제 httpd 디렉토리 안에 default.conf파일을 넣어 준다. 이렇게 되면 일단 준비는 끝


파일트리는 이렇게 됨
상위경로
docker_deploy
   |. Dockerfile
   |. docker-compose.yml
   |------- httpd (디렉토리)
   |------- mysqldata (디렉토리)
   |------- app (디렉토리)

만약 깃허브에 다 올린다면 만들어진것을 토대로 올려야 할 듯 한데 흠...
좀 더 연구가 필요



## 먼저 서버에 docker, docker-compose 설치

docker설치하기.md 파일 참고
