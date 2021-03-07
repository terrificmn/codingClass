# factory 기능 활용 하기
- db table에 들어갈 데이터 자동으로 넣어준다
- 테스트용으로 좋다

tinker에서 사용해볼 수 있음
```
$php artisan tinker
```

Article::factory(5)->create();  
하면 만들어 준다 (랜덤으로 db 데이터 생성)  

또는   
App\Models\Article::factory(5)->create();  -- 5개 row데이터 생성  

유저 똑같이 가능  
App\Models\User::factory(5)->create();


처음에는 기본으로 User factory만 있음

다른 클래스도 만들고 싶으면
artisan을 사용

먼저 헬프로 보기
```
$ php artisan help make:factory
```

생성
```
$php artisan make:factory ArticleFactory -m "App\Models\Article"
```
여기서 -m 플래그는 어떤 모델을 사용할지 정해주는 것

그리고 8버전 이후에는 
코드 윗부분에 `use App\Models\User;`
를 사용한다고 써주기

왜냐하면 User 모델 클래스를 사용할 것인데  
user_id는 User모델로부터 받아와야하는데  
이때 User를 이해를 못하기때문에 네임스페이스를 지정해준다, 또는 직접 적어준다  
App\Models\User::factory();


사용 예:  
함수 definition() 부분에 적어준다
```php
public function definition()
    {
        return [
            'user_id' => User::factory(), //위에서 명시 //use App\Models\User;
            'title' => $this->faker->sentence,
            'excerpt' => $this->faker->sentence,
            'body' => $this->faker->paragraph
        ];
    }
```
다시 artisan 실행
```
$php artisan tinker
```

```
>>> App\Models\Article::factory(3)->create();
```
*참고 >>> 표시는 tinker 프로그램안에 들어온 것 임

factory()에는 만들고 싶은 데이터 갯수를 입력해준다,  
 위의 예는 3개의 더미데이터가 만들어짐

이제는 
mysql로 돌어와서
```
$mysql -u root -p
```
로그인 후 (아,, phpmyadmin 깔아야하는데;;)

```
>select * from articles;
```

```
MariaDB [myblog]> select * from articles;
```
데이터가 자동으로 생성되어 있는 것 확인


create()메소드에 특정 파라미터로 
특정컬럼만 바꿔주기 
컬럼이름으로 해서 => value값을 바꿔주면 된다

```
>>> App\Models\Article::factory(3)->create(['title'=> 'overrided title']);
```

바뀐 것을 확인
```
생략...
App\Models\Article {#4338
user_id: 16,
title: "overrided title",
excerpt: .....
...생략 ..
```


## articles 테이블의 user_id foreign_key 설정

먼저 Articledml migration을 바꿔준다
database/migrations 디렉토리에 가서
날짜_년_월_일_create_articles_table.php
에 

함수 up 안에 적어준다
```php
// 만약 user테이블에서 해당아이디로 참조하는데 그 해당아이디가 지워졌거나 없다면(탈퇴 등으로..)
// 그러면 문제가 생긴다. 왜냐하면 users 테이블에서는 아이디가 없는데
// 이미 참조해서 만들어진 articles 테이블에는 해당아이디가 남아있으므로
// 이때 사용할 수 있는 것이 아래 코드 
// foreign('user_id')를 지정 이것은 users테이블의 id이고 id가 지워졌으면 'cascade' 해라
// DB에 가보면 Articles테이블에 user_id에 foreign_key가 설정되어 있게 됨
$table->foreign('user_id')->references('id')->on('users')->onDelete('cascade');

```

이후 중간에 넣어준것이라면 다시 migration해주는데 데이터가 다 지워지므로 주의

마이그레이션
```
$php artisan migrate:fresh

```

테이블 컬럼을 봐보면
이제 Articles의 user_id를 보면 forien_key가 설정되어 있음

이렇게 되면 user의 특정 id가 지워지면
articles의 해당 id로 되어 있던 글들도 모두 지워지게 된다


