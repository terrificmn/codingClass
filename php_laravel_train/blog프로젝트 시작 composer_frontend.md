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

처음에 라라벨 뉴 프로젝트를 만들고 
만약 학교에서 작업을 하는경우에 git reset을 한 경우는  (install linux 참고)
다행히 원격과 싱크는 맞출 수 있었지만 깔린게 없으므로 설치해줘야한다
예로 바로 php artisan serve를 하면
 In order to use the Auth::routes() method, please install the laravel/ui package.
라고 나온다
그럼 아래 처럼 필요한 것 깔아주기

참고: 우분투에서 npm없다고 할 시에 apt-get nodejs 만 설치하면 
버전도 낮고 심지어 npm도 안깔린다..;; 
centos는 npm은 깔리지만 nodejs 버전이 낮아서 문제가 된다
어쨌든 우분투도 리포지터리 추가 확인해야할 듯

`nodejs 셋팅npm트러블슈팅.md`파일 확인 




예전 기록들.... docker_nginx 관련 파일 참고할 것

처음 laravel new project명  한 이후 설치할 것들...

install
composer require laravel-frontend-presets/tailwindcss --dev
(도커버전)docker-compose run --rm composer require laravel-frontend-presets/tailwindcss --dev 



php artisan ui tailwindcss --auth
(도커버전)docker-compose run --rm artisan ui tailwindcss --auth


그 다음 라라벨믹스를 지웠다가 다시 깜 
npm remove laravel-mix
(도커버전)docker-compose run --rm npm remove laravel-mix

npm install laravel-mix --save-dev
(도커버전)docker-compose run --rm npm install laravel-mix --save-dev

cross-env 설치
npm install cross-env --save-dev 
(도커버전)docker-compose run --rm npm install cross-env --save-dev


tailwindcss를 매번 사용할 때마다 컴파일해서 사용하게 해줌
npm run watch
(도커버전)docker-compose run --rm npm run watch

----------------
webpack compiled successfully 이렇게 나오면 끝

이제 public/css 디렉토리의 app.css 파일을 열어보면
Tailwind 가 적용되어 있음

-------------
처음 간단한 env 파일 데이터베이스 설정
laravelblog db이름





예전 기록들 ----
충돌 해결할 수 있음;;; (docker-ngnix정리버전.md파일 참고)

일단 git 하는 것이 되면 (아직 해결은 못함)
아예 처음에 한쪽에는 새로운 프로젝트를 만들어서 초기 설치할 것들 설치하고
그래서 그 상태에서 위에 필요한 npm mix부터 처음부터 해보기
그 다음에 다른 디렉토리에 git pull로 다운을 받은 후에 
거기에서 필요한 파일들만 카피하자 (무식한 방법이지만 사실 컨트롤러 모델, 뷰 등 그렇게 파일이 많지는 않다 ㅋ)
--> 이제는 깃으로는 pull만 받아서 사용한다 
--> 충돌이 나기때문에 push는 안하고 로컬에서 파일을 수정하고 push하고 서버에서는 pull만 한다
05apr 2021








예전 기록들...

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
