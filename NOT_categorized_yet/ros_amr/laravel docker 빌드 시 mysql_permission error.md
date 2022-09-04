# No permission to read from ...
```
error checking context: 'no permission to read from '/home/sgtocta/Workspace/docker-laravel-blog/mysqldata/performance_schema/db.opt''.
```
빌드 실패  

평상시에 하던것 처럼 chown 명령어를 이용해서 33:33 또는 root:root 바꾸면 바로 퍼미션 에러가 해결이 되었는데..  

좀 더 파일을 열어서 확인을 해보니 
-rw-rw---- 로 되어 있다. mysqldata 디렉토리를 권한을 넣어주면서 -R 옵션을 잘 못 준것 같다. 안의 서브 디렉토리에 모두 같은 상황. 완전히 꼬여버렸다 ㅠ

그래서 other에도 r 로 넣어줘야 한다. 디렉토리에 들어가서 일일이 바꿔야 할 듯 하다
```
sudo chmod 664 ./*
```
물론 디렉토리 자체는 바꾸면 안됨 6을 주면 디렉토리 자체에 들어갈 수가 없다

이제 docker-compose build를 하면 잘 됨

