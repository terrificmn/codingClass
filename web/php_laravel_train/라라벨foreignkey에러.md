# 라라벨 foreign key 관련해서 에러  트러블 슈팅

에러메세지:
> general error 1005 can't create table foreign key constraint is incorrectly formed

foreign key 설정을 잘 못했을 경우에 mysql에서 에러를 발생시키는데, 
구글링을 해본 결과 에러가 발생하는데에는 몇가지 이유가 있었음, 이것도 몇시간을 붙들고 헤맴

1. 외부키는 foreign key는 참조하려는 키와 타입이 같아야 한다
2. 참조하는 원래 테이블은 먼저 만들어져야 한다
3. 디비의 종류가  InnoDB 여야 한다   

이었던것 같다..

일단 모든 조건을 다 검토해도 계속 같은 에러가 발생해서;; 알 수 없는 다른 이유인 줄 알았지만, 
아래처럼 직접 테이블을 만들어 보니 라라벨에서 발생하는 에러가 아닌  mysql에서 발생시키는 에러임에는 확실!
결국은 내가 원인이지;;; ㅋ

원래 직접 sql을 입력할 경우에는 아래처럼 하는데
post_id는 foreign key이므로 참조하는 posts테이블의 id를 담아야하는데 
그래서 타입이 같아야하는데 이부분에서 타입이 서로 맞다고 착각한 것이 문제였음

에러가 나는 경우, 아래와 같은 에러가 남
```
ERROR 1005 (HY000): Can't create table `laravelblog`.`tags` (errno: 150 "Foreign key constraint is incorrectly formed")
```

그래서 라라벨로 안 만들고 직접 mysql에 로그인해서 쿼리를 작성했더니 만들어졌다
```sql
MariaDB [laravelblog]>  create table tags (
    ->      id int not null primary key auto_increment,
    ->      tag_name varchar(255) not null,
    ->      post_id int(10) unsigned not null,
    ->      foreign key (post_id) references posts(id)
    ->  );
Query OK, 0 rows affected (0.026 sec)
```

___
결국 내가 타입을 안맞춰서 에러가 발생했구나~   

먼저 관계 설정을 해놨던   
users 테이블의 id를 참조하는 posts테이블의 user_id를 보고 착각을 한 것인데..  

이거를 라라벨에서 코드로 보면  
일단 users의 id는   
`$table->id();` 이렇게 되어 있었고 이렇게 id()메소드를 사용하면 bigint(20) unsigned가 됨  

posts의 user_id(foreign key)는   
`$table->unsignedBigInteger('user_id');`말그대로 언사인드 빅인티저  
위처럼 되어 있어서 
posts와 tags테이블도 같은 방식으로 하면 되는 거라고 착각을 함

결론은
posts테이블의 id는
`$table->increments('id');` 요렇게 이놈은 int(10) unsigned 타입이 된다  
이렇게 되면   
tags테이블의 post_id(foreign key)는   
~~`$table->unsignedBigInteger('user_id');`~~ 이렇게 하면 안되고  
`$table->integer('post_id')->unsigned();` 이렇게 되어야한다  
그리고   
foreign key 까지 넣어주면   
`$table->foreign('post_id')->references('id')->on('posts')->onDelete('cascade');`  
저장 한 후

CLI로 다시 입력을 하면   
`php artisan migrate`  
테이블이 에러 없이 잘 만들어 진다!



