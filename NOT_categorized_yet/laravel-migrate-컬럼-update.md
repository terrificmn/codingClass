# 컬럼 update하기
기존 data가 필요없다면 database/migrations 에서 해당하는 migration 테이블을 찾아서   
추가 또는 수정을 (컬럼) 한 뒤에 migrate를 해버리면 쉽게 되겠지만   

```
php artisan migrate:refresh
```
하지만 데이터가 다 지워진다는 것이다. 기존에 data가 없을 때는 위의 방식처럼 하면 된다


## 관계형? 그냥 테이블 alter
테이블을 더 만들어서 관계형으로 설정해서 하는 방식도 있을 듯 하다.  
하지만 foreign key 설정으로 기존의 테이블에도 추가해줘야하고   
새로운 테이블도 만들고   기존 코드도 수정을 많이 해야할 것 같아서   

기존의 테이블을 업데이트를 수정하기로 결정!  

하지만 이미 기존 data가 있는 경우이기 때문에서 migration 파일을 만든다음에   
특정 컬럼을 추가해서 다시 migrate를 하는 방식으로 진행해야한다  

파일을 한 개 더 만들어 준다음에 그걸로 migration을 진행한다.

> 어떻게 생각하면 sql로 alter table 하는 방법도 있을 듯 하다.  
하지만 다음에 rollback하거나 할 때에는 문제가 발생할 수도?? 

## 새로 migration 만들기
도커버전, make:migration 뒤 아규먼트에 알아볼 수 있게 아래같은 방식으로 만들어준다. 
```
docker-compose run --rm artisan make:migration update_and_addstatus_to_posts_table
```

> 위에서 지정한 파일이름으로 만들어진다   
년_월_일_시간_update_and_addstatus_to_posts_table.php


이제 function up()에 추가해준다
```php
public function up()
{
    Schema::table('posts', function (Blueprint $table) {
        $table->string('category')->after('image_path');   //추가할 컬럼
    });
}
```

기존의 Schema facade에서는 create()메소드를 사용했는데 이번에는 **table()메소드**를 사용한다   
맨 뒤의 after() 함수는 기존의 어떤 컬럼 뒤에 만들겠다는 의미

이번에는 function down()에도 추가해줘야한다
```php
public function down()
{
    Schema::table('posts', function (Blueprint $table) {
        $table->dropColumn('category');
    });
}
```

rollback을 수행할 떄 추가한 컬럼을 지울 수 있게 해준다.  
중간에 추가한 것 이기 때문에 migration을 진행할 때 기존의 테이블 (원래 migration)  
에서 에러 발생할 수 있다.   


migrate 하기   
도커버전
```
docker-compose run --rm artisan migrate
```

다행히 migration이 잘 된다.
```
Migrating: 2022_06_12_224327_update_and_addstatus_to_posts_table
Migrated:  2022_06_12_224327_update_and_addstatus_to_posts_table (68.95ms)
```

기존 데이터는 그대로 있는 상태에서 컬럼이 하나 추가가 되었음



## 다른 예
새로 migration 만들기 예:
```
php artisan make:migration update_and_addstatus_to_employees_table
```

up() method에 바꿀 컬럼 만들어주기  

> table 메소드를 사용하는 것으므로 create로 만든 테이블이 있어야 함

```php
public function up()
{
       Schema::table('employees', function (Blueprint $table) {
               $table->renameColumn('emp_name', 'employee_name');// Renaming "emp_name" to "employee_name"
               $table->string('gender',10)->change(); // Change Datatype length
               $table->dropColumn('active'); // Remove "active" field
               $table->smallInteger('status')->after('email'); // Add "status" column
       });
}
```

> renameColumn(from, to) 컬럼 이름 바꾸기   
gender column type의 길이 바꾸기   
dropColumn(컬럼) 지우기   
new column 추가, email 컬럼 뒤에 추가하게 됨   

rollback을 위해서 down에도 넣어주기

```php
public function down()
{
        Schema::table('employees', function (Blueprint $table) {
               $table->renameColumn('employee_name', 'emp_name');
               $table->string('gender')->change(); 
               $table->smallInteger('active');
               $table->dropColumn('status');
        });
}
```

migration 실행
```
php artisan migrate
```


## renaming, dropping tables
테이블을 이름을 바꿀 경우에는 migration 파일안에서  
Schema::rename($from, $to); 이런 방식으로 사용   
예  
```php
use Illuminate\Support\Facades\Schema;
 
Schema::rename($users, $user_info);
```

drop은 아래의 메소드 사용
```php
Schema::drop('users');
 
Schema::dropIfExists('users');
```







