# ManyToMany relationship
Article모델과 Tag모델 관계

## Tag 모델
모델만들기 -m은 migration용
php artisan make:model Tag -m

tag 모델에 메소드 정의
```php
    public function tags() {
        return $this->belongsToMany('App\Models\Tag', 'article_tag');
    }
```

database/migrations 
에 새로 생긴 create_tag_table.php (Tag 용)
스키마 추가

 Schema::create('tags', function (Blueprint $table) {
            $table->bigIncrements('id');
            $table->string('name');
            $table->timestamps();
        });

        // convention: 아티클_태그 언더스코어로 연결
        Schema::create('article_tag', function (Blueprint $table) {
            $table->bigIncrements('id');
            $table->unsignedBigInteger('article_id'); // article table과 연결
            $table->unsignedBigInteger('tag_id');
            $table->timestamps();

            $table->unique( ['article_id', 'tag_id' ]); //중복을 방지하기 위해서 unique

            // foreign키 설정: article_id 레퍼렌스 aritcles테이블의 id를 참조 id가 지워지면 여기도 article_id 지워지게 설정
            $table->foreign('article_id')->references('id')->on('articles')->onDelete('cascade');
            // tag_id 에도 같은 설정 (tags 테이블의 id 참조)
            $table->foreign('tag_id')->references('id')->on('tags')->onDelete('cascade');
            
        });
    

그 다음 마이그레이션
php artisan migrate

이렇게 하고 DB table에서 더미 데이터를 넣어본다

Aritcles 테이블에 1번 글이 title이 Laravel 으로 하고

tags 테이블에 태그 내용을 적어준다
1 laravel
2 php
3 education
이런식으로..

그리고 이 둘 테이블의 관계를 정한 linking table인 article_tag 테이블에서
(참고:이렇게 2개의 테이블이 관계가 있을 때는 테이블1이름_테이블2이름 로 하는게 좋다)

article_id 는 1번
tag_id는 1 , 2, 3 각 이렇게 대응되게 됨


이제 Tag 모델 파일로 돌아가서 마찬가지로 
article 메소드를 만들어 준다, 
```php
    // 반대로 생각해보면 tag모델에서는 artcle과 서로 관계에 있음
    public function article() {
        return $this->belongsToMany('App\Models\Article', 'article_tag'
);
    }
```
에러 참고: 예전 코드 방식으로는 에러 발생  
모델을 못 찾음, 잘 모르겠음 ㅠ, 파라미터를 더 지정해야하는 지도 모름
```php
return $this->belongsToMany(App\Models\Aritcle::class);
```




tinker
$article = App\Models\Article::find(5);
// id=5로 되어 있는 글 찾기
$article->tags()->attach(1);
// article에서 tags() 메소드를 호출하면 tag는 Tag모델로 이어지고 article_tag 테이블에 참조하게 되는데  attach(1)을 하면 1로 추가가 됨
tag_id 컬럼에 1이 추가됨, 그리고 아티클은 5번이었으니 article_id는 5번이 들어감
$article->tags()->detach(1);
tag_id 1 지우기 == article_id도 지워짐
 $article->tags()->attach([1, 2]);

$article->tags()->detach([1, 2]);


반대로 ManyToMany 로 연결되어 있으므로 

tinker에서 
$tag = App\Models\Tag::find(1);
tag 테이블의 id 1을 찾고 
$article->tags()->attach($tag); 을 하면 같은 결과가 처리됨


또는  배열로도 찾아서
$tag = App\Models\Tag::findMany([1, 2] );
$article->tags()->attach($tag);



