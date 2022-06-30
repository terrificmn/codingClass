laravel 프로젝트 디렉토리에 보면 .env 파일이 위치 함

항상 .gitignore 에 포함이 되어 있기 때문에 파일 자체가 없으므로   
.env.example 로 카피를 해서 사용  

APP_KEY 는 encryption key 인데 이게 없을 경우 app이 보여지지 않는다.  
없을 경우 php artisan key:generate 를 해야함   
docker를 사용하는 경우는 docker-comopse run 으로 실행할 수 있음

```
APP_DEBUG=true
```
대신 local에서 개발을 하고 있을 때만 true로 해서 에러 표시가 페이지에 표시될 수 있게 한다   
하지만 서버에서 배포 했을 경우에는 반드시 `false` 로 해줘야한다   
false로 되어 잇을 경우는 **500 | SERVER ERROR** 만 표시한다  

```
DB_HOST=127.0.0.1
```

docker 컨테이너로 mysql이 사용되는 경우에는 컨테이너 이름으로 해줘야한다  
```
DB_HOST=mysql
```

## config
config/services.php 파일을 열어 보면 Third Party Sevices 에 대해서 정의를 할 수 있는데   
이를 config() 함수를 이용해서 리턴을 받을 수 있다

services 파일에는 예를 들어
```php
'mailgun' => [
        'domain' => env('MAILGUN_DOMAIN'),
        'secret' => env('MAILGUN_SECRET'),
        'endpoint' => env('MAILGUN_ENDPOINT', 'api.mailgun.net'),
    ],
```
이런식으로 지정이 되어 있고, env 함수(helper function)로 `env('MAILGUN_DOMAIN', 'test")` 식으로 2번째 인자를 넘겨주면   
디폴트 값이 된다.   
.env 파일에서 값을 읽어오는 것임. 아마 .env파일에도 정의를 해줘야하는 듯 하다

web.php 에서 접근해서 확인할 수가 있다.
```php
dd(config('services.mailgun.domain'));
```

또는 env() 도 사용할 수 가 있다. .env 파일에 설정되어 있는 내용을 리턴해준다
```php
dd(env('DB_HOST'));
```

> env 관련 변수를 정의할 때는 대문자로 만들어준다


