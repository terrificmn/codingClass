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
> mariadb-dump  

## sql dump파일 복원시키기
그전에 database를 하나 먼저 만든다음에.. pf2010이라고 만듬 (pf2010은 dbname)  
```
mysql -u root -p pf2010 < /저장된장소/DB_backup_Feb_10_2010.dump  
```

> mariadb

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

반대로 Host 에서 contiainer 로 카피할 경우에도 docker cp를 사용  
예:  
```
docker cp docker-backup_2026-02-11.sql my_mysql:/
```
> docker cp copy-filename.sql container_name:/
일단 유저가 root로 되어 있기 때문에 / 부터 원하는 path로 지정하면 된다.  
(편의상 / 바로 아래로 지정해서 사용)  


### docker로 restore 하기
```
mariadb -u sql_user -p myDbName < ./docker-backup_2026-02-11.sql 
```

에러
```
ERROR 1005 (HY000) at line 449: Can't create table `robotSoftware`.`released_pack_package` (errno: 121 "Duplicate key on write or update")
```

CONSTRAINT 중복이 되어서 진행이 안된다. 위의 에러 메세지 처럼 449 번째 줄   
sql 파일을 열어서  

```
  CONSTRAINT `1` FOREIGN KEY (`released_pack_id`) REFERENCES `released_pack` (`id`),
  CONSTRAINT `2` FOREIGN KEY (`package_id`) REFERENCES `package` (`id`)
```
위 내용에서 CONSTRAINT 를 unique 하게 해주게 변경해주면 된다.  
```
  CONSTRAINT `fk_released_pack_1` FOREIGN KEY (`released_pack_id`) REFERENCES `released_pack` (`id`),
  CONSTRAINT `fk_package_2` FOREIGN KEY (`package_id`) REFERENCES `package` (`id`)
```

다만 sql dump를 했을 때 위 처럼 CONSTRAINT 가 1, 2 정도로 셋팅이 된게 많아서    
여러번 에러가 발생한다. 겹치지 않게 다르게 만들어서 수정 한 후 시도 하면 성공 한다.  
  
> docker cp 한 다음에 계속 복구를 시도한다. 

