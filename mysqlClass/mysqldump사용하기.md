## mysqldump 이용 백업하기
mysqldump 명령어로 해당db을 파일로 백업
```
#mysqldump -u root -p 디비이름 > 파일명.sql
```

만약 sudo로는 permission denied 되면 root 로 로그인
```
$su -  
```

위 커맨드를 실행하면 mariadb 암호를 물어본다. 암호입력 후 현재 디렉토리에 생성이 된다   
pwd 명령어를 실행한 후 현재 디렉토리를 확인한 후 하는 것이 좋다  
실행 예:  
```
  #mysqldump -u root -p phplesson > backup_php2020-12-30.sql  
```


## sql dump파일 복원시키기
그전에 database를 하나 먼저 만든다음에.. pf2010이라고 만듬 (pf2010은 dbname)  
```
mysql -u root -p pf2010 < /저장된장소/DB_backup_Feb_10_2010.dump  
```

### docker 에서 백업
docker exec -it mysql /bin/bash

컨테이너로 접근 후에  위에 방식으로 sqldump 를 해준다.  

이제 해당 파일을 host 컴퓨터로 넘기기 위해서는 `docker cp` 명령어를 사용할 수 있다.  
우선 exit 로 해당 컨테이너의 bash 쉘을 빠져나온다.

이후 복사를 할 수가 있는데, 컨테이너에서 host 로는 이런 형식으로 복사할 수 있다.  
`docker cp container_name_or_id:/path/in/container/file_or_dir /path/to/local/destination`

예 mysql 컨테이너에서 해당 / (root)이하의 파일을  호스트컴쪽의 현재 디렉토리로 복사
```
 docker cp mysql:/aug12-backup-laravelblog.sql ./
```
