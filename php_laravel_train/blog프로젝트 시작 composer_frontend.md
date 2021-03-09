tailwindcss 설치 및 활용

참고 버전
php artisan --version
8.32.1
php -v
8.0.2
node -v
14.16.0



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

php artisan make model with migration
php artisan make:controller PageController
php artisan make:model Post -m
php artisan make:controller PostController --resource



