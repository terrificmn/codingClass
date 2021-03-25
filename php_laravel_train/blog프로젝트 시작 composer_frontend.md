tailwindcss 설치 및 활용

참고 버전
php artisan --version
8.32.1
php -v
8.0.2
node -v
14.16.0
중요 npm 버전도 확인해야함 (왜냐하면 npm 버전이 낮게 설치되어 있으면 호환문제가 발생)
npm만 따로 설치할 수 있어서 따로따로 하기보다는 nodejs 리포지터리 추가해서 설치하는게 좋다. (nodejs 셋팅npm트러블슈팅 참고할 것)


install
composer require laravel-frontend-presets/tailwindcss --dev

php artisan ui tailwindcss --auth

그 다음 라라벨믹스를 지웠다가 다시 깜 
npm remove laravel-mix
npm install laravel-mix --save-dev

cross-env 설치
npm install cross-env --save-dev 

tailwindcss를 매번 사용할 때마다 컴파일해서 사용하게 해줌
npm run watch

----------------
webpack compiled successfully 이렇게 나오면 끝

이제 public/css 디렉토리의 app.css 파일을 열어보면
Tailwind 가 적용되어 있음

-------------
처음 간단한 env 파일 데이터베이스 설정
laravelblog db이름

사실 아래것들은 완전 처음 시작할 때하는 것이므로
깃허브에서 받아서 하는데,, 처음에는 잘 되었는데 뭔가 문제인지 새로 프로젝트를 만든다음에 pull 하면 에러가 난다.. 
아예 다른곳에서  init을 하지말고 clone으로 해보면 프로젝트가 통으로 받아지는데 
물론 php artisan serve를 하면 에러가 남 (이유는 gitignore로 일부파일은 없기때문에 ㅠ)

일단 git 하는 것이 되면 (아직 해결은 못함)
아예 처음에 한쪽에는 새로운 프로젝트를 만들어서 초기 설치할 것들 설치하고
그래서 그 상태에서 위에 필요한 npm mix부터 처음부터 해보기
그 다음에 다른 디렉토리에 git pull로 다운을 받은 후에 
거기에서 필요한 파일들만 카피하자 (무식한 방법이지만 사실 컨트롤러 모델, 뷰 등 그렇게 파일이 많지는 않다 ㅋ)


그 다음에 필요한 라이브러리 composer로 추가하기

php artisan make model with migration
php artisan make:controller PageController
php artisan make:model Post -m
php artisan make:controller PostController --resource



일단  sluggable은 설치안하기 . 이유는 Str클래스에서 slug 기능을 할 수 있음
use Illuminate\Support\Str; 위에 사용한다고 정의하고 사용하면 됨
사용은 아래와 같은 식으로
$slug = Str::slug($request->title)

<!-- cviebrock/eloquent-sluggable 컴포저 설치
composer require cviebrock/eloquent-sluggable -->


___

그리고 PostController에 넣어주는데 참고로만 알고 있자, 왜냐하면 이미 위에서 복사했기 때문에 넣어줄 필요는 없다
```php
use Cviebrock\EloquentSluggable\Services\SlugService;
```
그리고 컨트롤러의 store()메소드에
```php
// SlugService로 slug를 만듬 (1@param: Post모델, 2param: 컬럼명, 3param: 입력받은 title)
$slug = SlugService::createSlug(Post::class, 'slug', $request->title);
```


Home 관련된 페이지를 사용안하기 때문에 
관련해서 Home 디렉토리 바꾸기
app/Http/Auth/LoginController.php >> 에서 
RouteServiceProvide::HOME을 리다이렉트하고 있는데 

app/Providers/RouteServiceProvider.php 에서 
public const HOME = '/home'; 이라고 정해져있어서 home 지우고 '/' 만 남기면 됨
