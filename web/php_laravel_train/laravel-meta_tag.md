title 태그안에 변수로 controller에서 넘겨주면 그걸 사용
예
```
<title>{{ $metaTitle ?? '' }}</title>
```
없으면 '' 출력


```
<title>{{ $metaTitle ?? config('app.name') }}</title>
```

app.name 은 프로젝트명
config/app.php 에 보면 'name' => env('APP_NAME', 'Laravel') Laravel로 지정이 되어 있다
그래서 위 처럼 하면 기본적으로 Laravel로 나오게 됨 (없다면 )


이거의 단점은 모든 컨트롤러 메소드에서 메타 타이틀을 위해서 보내야한다는 점

### View::share() 사용하기
app/Providers/AppServiceProvider.php 에 

use Illuminate\Support\Facades\View; 추가
boot() 메소드 안에 
View::share('key', 'value'); 넣어주면  
모든 view 페이지에서 key 변수를 공유를 할 수 있다. 





## ServiceProvider를 이용하기 위해서 만들어주기
app/Providers 디렉토리에 ViewServiceProvider.php 를 만들어준다 

내용은 기존의   
Providers/AppServiceProvider.php 를 복사해서 만들 수도 있지만

확인해보기
```
 docker-compose run --rm artisan make:provider --help
```

artisan 으로 만들어준다  
아규먼트로 클래스 이름만 지정해주면 된다
```
docker-compose run --rm artisan make:provider ViewServiceProvider
```

이제 생긴 ViewServiceProvider.php 파일에 boot() 메소드에 정의

이 작업은 어떤 view에서 사용할지를 정해준다.  
일단 layouts 등에서 사용하니 layouts.app 으로 정해줌

네임스페이스쪽에 use로 선언해주고, boot()메소드에 추가
```php
use App\View\Composers\MetaComposer; //추가
use Illuminate\Support\Facades\View;  // 추가하기

public function boot()
    {
        // view에서 composer를 사용할 수 있게 해줌
        // Using class based composers... // register MetaComposer 등록
        View::composer('layouts.app', MetaComposer::class);
    }
```


### ViewProvider에서 지정한 composer 클래스를 만들어서 사용하기
app/View/Composers/Matacomposer.php 를 만들어준다
app 디렉토리 내에 View 디렉토리 자체가 없으므로 만들어 줘야 하고   

> 저장할 때 권한 문제 발생하면 chown chmod 로 바꿔준다

namespace 로 디렉토리 지정해주고, 이름으로 씀, View 클래스를 사용한다
```php
<?php

namespace App\View\Composers;

use Illuminate\View\View;

class MetaComposer 
{
    /**
     * Bind data to the view.
     *
     * @param  \Illuminate\View\View  $view
     * @return void
     */
    public function compose(View $view)
    {
        dd(echo request()->segment(1));

    }
}
```

request()->segment(int) 로 사용한다음에 $metaTitle을 만들어 준다음에 ->with()메소드로 보내준다 




### cofin에 추가 (중요)
config의 app.php 파일을 수정안하면 ViewServiceProvider만들어 놓은 것이 작동을 안함
그래서 중요한 것은 ServiceProvider를 ViewServiceProvider라고 추가해줬으니  
providers 배열에 추가를 해줘야 한다. config/app.php  
```php
/*
* Application Service Providers...
*/
//아래줄에 추가
App\Providers\ViewServiceProvider::class,
```

App\View\Composers\MetaComposer class는 
이제 compose 메소드는 view 페이지가 (layouts.app) 계속 렌더가 될 때 마다 실행이 되게 된다 

> 주의할 점은 블레이드 페이지까지 지정을 해줘야지 되는 것 같다. layouts 만 해주면 (view의 layouts 디렉토리 통채는 안됨)


## segment() 메소드를 이용해서 URL
URL에서 정보를 받아와서 사용
segment(int) 아규먼트 int 값은 1이 URL의 첫번째 / 뒤에 나오는 내용
http://localhost/blog 주소 일 때 blog를 반환하게 된다 

이를 이용해서 메타 데이터를 보내줄 수 있다. 예를 들어
```php
public function compose(View $view)
    {
        if (request()->segment(1) != '') {
            $metaTitle = request()->segment(1);
        };

        $view->with('metaTitle', $metaTitle);
    }
```

이제 여기에서 로직을 좀 더 만들어서 $metaTitle을 보내주고  
이것을 layouts.app 블레이드파일에서 헤드의 title 태그안에서 잘 처리해준다

