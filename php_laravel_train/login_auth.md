아예 프로젝트를 다시 만듬
```
laravel new sample-project-for-login
```
만들어지면 프로젝트로 이동
```
cd sample-project-for-login/
```

로그인 관련 설치를 해준다 (composer dependency 패키지 이용)

```
composer require laravel/ui
```

이제 설치가 되면
php artisan 입력 해보면
ui명령어가 생긴것을 알 수 있고

```
php artisan ui:auth
```
하면 

Authentication scaffolding generated successfully.
고 나옴

```
php artisan serve
```

페이지를 해보면 log in 과 Register가 생김
css등이 적용은 안되어 있지만 사용가능

이제 데이터베이스가 없으므로 
만들어준다

새로만들어도 되고, 기존에 쓰던것에 써도 됨

CREATE DATABASE sample_project_for_login;
그냥 프르젝트명과 같은 이름으로 만듬

env파일 db 정보 수정해주기
새로운 프로젝트이니 비번까지 다 다시 입력
(다른 프로젝트가 열려있다면 새로 열고 시작, 헛낄 수 있음)

그리고 migrate해준다
```
php artisan migrate
```

이제 회원가입을 해보면
회원가입이 되고
비번찾기 이메일보내기, 로그인 다 됨

구~웃!




