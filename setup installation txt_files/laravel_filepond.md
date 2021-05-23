# 이미지 업로드 filepond 사용하기
먼저 filepond를 사용하려면 filepond를 설치해야하는데..
먼저 공식 사이트를 참고한다.

[공식사이트 가기-인스톨 살펴보기](https://pqina.nl/filepond/docs/patterns/installation/)

npm으로 설치하거나 CDN으로 할 수가 있는데, CDN이 간단하고 편하므로 CDN 방식으로 했다.

>CDN? Content delivery network (콘텐츠 전송 네트워크) : 콘텐츠를 사용자에게 좋은 성능으로 빠르게 제공하는 것을 말한다. 
CDN nodes를 다양한 지역, 장소에 둬서 페이지 로딩 시간/ 트래픽을 줄여주고, 컨탠츠를 전세계적으로 가능하게 해주는 일을 한다.
소프트웨어 다운로드, 음악/비디오 스트리밍, 웹 오브젝트 등을 하게 해준다

정확히는 설명할 수 없지만.. ㅠ   
즉 내 프로젝트에는 npm으로 직접 설치할 수도 있고 그러면 내 서버에 사용자가 직접 요청했을 때 filepond가 응답하겠지만, 
CDN 방식으로 연동하면 다른 서버에 (사용자한테 가까운)로 처리가 되는 것을 말하는 것 같다.

어쨋든 위의 공식사이트를 이용하면 된다.

CDN방식은, 각각 2개의 코드를 html head부분에 넣어주고, 
여기는 라라벨에서 대개 layout에 넣어주면 모든 페이지에서 잘 들어가지게 됨. 

```
<!-- add to document <head> -->
<link href="https://unpkg.com/filepond/dist/filepond.css" rel="stylesheet" />
```

그리고 아래코드는 <body>코드 끝나기 전에 넣어준다.. 거의 마지막에 넣어주면 되는 듯..
```
<!-- add before </body> -->
<script src="https://unpkg.com/filepond/dist/filepond.js"></script>

```

이제 filepond를 사용하려면 파일 업로드를 사용할 페이지에 넣어주면 되는데 
```html
<input type="file" name="image" id="image">
```
이러면 보통의 파일 업로드 박스(?)가 생기게 된다.

복수로 가능하게 하려면 name을 배열로 만들어준다
```html
<input type="file" name="image[]" id="image" multiple data-max-file-size="20MB"/>
```

현재 내 상태에서는 data-max-file-size="20MB"는 작동을 안 함. 왜냐하면 ngink를 웹서버로 사용하는데 
default값이 1mb 업로드 제한이 걸려있다고 함. 근데 다른 이미지 올리는 것은 상관없었던 거 같은데;; 확인해봐야겠음

그리고 해당 input "file"이 들어간 페이지 밑에 스크립트를 넣어줘야한다
그냥 페이지라고 하면 script태그 부분을 넣어주면 되는데, 나는 현재 레이아웃으로 공통으로 사용하기 때문에 
라라벨 블레이드를 이용해서 @섹션을 만들어준다.

먼저 레이아웃되는 메인 페이지에서는, 마지막 부분에 위에서 스크립트를 바로 그 부분 밑에
@yeild를 해준다
```php
<script src="https://unpkg.com/filepond/dist/filepond.js"></script>
@yield('scripts')
```

이제 파일 업로드를 할 페이지에서 @yield('scripts')라고 해준 부분을 만들어주고 아래 내용을 넣는다.
```php
@section('scripts')
    <script>
        const inputElement = document.querySelector('input[id="image"]');
        const pond = FilePond.create( inputElement );

        FilePond.setOptions({
            server: {
                url: '/upload',
                headers: {
                    'X-CSRF-TOKEN': '{{ csrf_token() }}' //java script varible로 만듬
                }
            }
        });
    </script>
@endsection
```
이 부분은 javascript가 작동하는데, 중요한 부분은 input[id=]부분을 file input을 만들어 준 부분의 id를 적어주고
아래의 server: { } 부분의 API를 설계해준다. 즉 업로드 버튼을 눌러서 이미지 파일을 선택하게 되면  
서버의 /upload 부분으로 POST방식으로 요청이 되는 구조가 된다.
그리고 라라벨에서는 포스트 방식으로 요청할 때 csrf token이 없으면 에러가 발생, 자바스크립트 변수로 처리해 주게 된다


이렇게 되면 이렇게 깔끔하게 바뀌게 된다.
(포스팅 할 때 넣어주기: 사진 비교)
<img src=0>
<img src=1>

이제 /upload에 대응해야하므로 컨트롤러를 하나 만들어 준다.
그리고 임시테이블을 사용할 것이므로 모델과 migrations를 준비
```
$php artisan make:controller UploadController
$php artisan make:model TemporaryFile -m
```
도커를 사용하는 경우 (artisan포함)
```
$docker-compose run --rm artisan make:controller UploadController
$docker-compose run --rm artisan make:model TemporaryFile -m
```

이제 UploadController에 store 메소드를 만들자
```php
public function store(Request $request) {
        
    if ($request->hasFile('imageFile')) {
       $file = $request->file('imageFile'); //파일 하나일 때

        // dirName으로 uniqid로 하나만 만들기 위해서 설정, temporary_files(table)에 하나만 넣어주고 리턴도 하나만 할려고함        
        $dirName = uniqid() . '-' . now()->timestamp;
        
        $filename = $file->getClientOriginalName(); //파일의 원래 이름을 저장
        $file->storeAs('images/tmp/' . $dirName, $filename); // images/tmp에 파일 저장
        
        //temporary_files 테이블에 upload된 이미지 저장
        TemporaryFile::create([
            'dirname' => $dirName,
            'filename' => $filename
        ]);

        return $dirName;

    } else {
        return '';
    }
}
```

$dirname 변수에는 유니크한 문자열(13자)과 시간으로 조합해서 만들어준다 
TemporaryFile 모델을 이용해서 저장해주게 되는데, 임시로 table을 만든 이유는
보통이미지만 올리면 상관없겠지만 
내 경우에는 post를 올리는 곳에서 사용하는데, filepond를 이용해서 사진을 올린다음에 사진이 다 올라가고 나면
그 후에 포스트를 마무리하고 저장(submit)을 하면 posts 테이블에 내용이 저장되게 만들어져 있는데
위의 store 메소드에서는 $dirname을 반환해주게 된다

임시 테이블에서 저장했다가 추후 최종 submit이 되면 리턴받은 $dirname과 비교해서 임시테이블에 있으면
파일을 옮겨는주는 작업을 좀 더 수월하게 할 수 있다.

변수로 넘겨주는 방식은 한계가 있는 것 같다. 정확하지는 않지만 filepond 의 Server에서 작동하는 방식을 보게되면
unique id인 즉 php에서 $dirname으로 반환하게 해준 것을 hidden input field에 갖고 있는다고 하는 것 같다.
뭐 그렇다.. 지금 생각해보니 임시테이블이 없으면 최종 $dirname 즉 unique id인 12345를 비교할 때 어려울 것 같기도 하다.;


이제 TemporaryFile 모델 내용을 작성하고, migrations도 만들어 준다
```
protected $fillable = ['dirname', 'filename'];
protected $table = 'temporary_files';
```
별거 없다. 컬럼 2개를 사용할 수 있게 해주고, 중요한 포인트인 table명을 새로 지정해준다.
Eloquent Model에서는 네이밍 convention이 모델 클래스명을 따라가게 셋팅이 되는데,
예를 들어 Post 라고 하면 posts(복수형)가 되는 것, 그런데 Model에서 아무런 정의가 없으면
temporaryfiles 처럼 (복수형)으로 해서 찾는데 이렇게 되면 테이블이 없다고 하는 에러가 발생

왜냐하면 모델명을 TemporaryFile 즉 카멜case 식으로 만들면
실제 테이블은 temporary_files으로 만들어지기 때문이다. 그래서 위에서 $table property를 정의해주는 것!

아래는 DB table 스키마
```
Schema::create('temporary_files', function (Blueprint $table) {
    $table->id();
    $table->string('dirname');
    $table->string('filename');
    $table->timestamps();
        });
```

이제 php artisan을 이용해서 migration을 해준다.
```
$php artisan migrate
```

이제 최종 submit이 되었을 때를 작업하기 위해서 내 경우에는 PostController의 store()메소드에 추가
```php
    $temporaryFile = TemporaryFile::where('dirname', $request->image)->first();
// //싱글 파일 일 때
    if ($temporaryFile) {
        $from_path = storage_path('app/images/tmp/' . $request->image . '/' . $temporaryFile->filename);
        //디렉토리가 없으므로 만들기
        mkdir(storage_path('app/public/images/post_images/'). $request->image);
        $to_path = storage_path('app/public/images/post_images/' . $request->image. '/' . $temporaryFile->filename);

        // tmp 디렉토리에 업로드된 파일 이동시켜주기
        File::move($from_path, $to_path);

        // db에서 delete // ( 싱글파일일때는 $temporaryFile->delete()가 됨)
        $temporaryFile->delete();
    }
```
$request->image 로 넘어온 것은 UploadController store()메소드에서 리턴해준 값인데 유니크 id 즉, 디렉토리명이 넘어온다.
신기하게도 filepond에서 처리를 해서 파일이 많을 경우에는 배열 상태로 넘어오게 된다.

그래서 임시테이블에서 위의 값을 비교해서 있다면, 임시로 저장한 파일을 public 디렉토리로 옮겨주게 된다.

왜냐하면 라라벨로 웹에서 이미지를 보여주려면 public 디렉토리에 있어야 하는데, storage 디렉토리 같은 경우에는 
그렇게 할 수가 없다. public디렉토리가 아니여서 접근이 안되는데, 이를 심볼릭 링크로 걸어서 해줄 수가 있다.
아래서 설명...
그래서 파일을 File을 이용해서 이동시켜준다.
참고로 File 클래스(?)를 사용하려면 컨트롤러 맨 위에 use로 정의해준다
```
use File;
```

사진을 여러장을 처리하려면 배열로 리턴되는 것을 활용해야하는데
일단 배열로 받은 $dirname을 처리하려면 쿼리빌더를 whereIn()메소드를 사용
```php
if (isset($request->image)) {
            $temporaryFile = TemporaryFile::whereIn('dirname', $request->image)->get();
        }   

// 임시db에서 있는 데이터 만큼 파일 이동시켜주기
    foreach($temporaryFile as $imageDirFile) {
        $from_path = storage_path('app/images/tmp/' . $imageDirFile->dirname . '/' . $imageDirFile->filename); //템프에서는 각 디렉토리가 만들어져서 하나씩 다 가져와야함
        // array로 넘어온 것의 첫번째만 사용해서 디렉토리는 하나로 통일
        $to_path = $storageToDir. '/' . $imageDirFile->filename;
        // tmp 디렉토리에 업로드된 파일 이동시켜주기
        File::move($from_path, $to_path);
    }
```
그리고 foreach문을 사용해서 임시 디비로 셀렉트된 놈들로만 반복을 시켜서 파일을 이동시켜준다.
그리고 실제 포스트를 저장해주게 된다.
```php
$post = Post::create([
    'title' => $request->input('title'),
    # ... 생략
]);
```

그리고 나서 이미지 경로는 다른 테이블에 다시 저장해준다.
```php
    $PostImages = new \App\Http\Controllers\PostImageController;
    // temporaryFile로 결과, 마지막 post에서 마지막 id값 넘겨주기
    $PostImages->store($temporaryFile, $post->id); 
            
    // $temporaryFile->delete(); 싱글파일일 때는 작동
    // collection이라서 그런지 다시 쿼리 빌드해서 지워주기 (변수로 하면 안됨)
    TemporaryFile::whereIn('dirname', $request->imageFile)->delete();
```
새로운 디비테이블을 만들고 거기에 저장을 해준다. 
PostImageController, Postimage모델, migrations 등을 만들어 준다.
아래는 각각의 내용

모델에는 post()메소드를 정의해서 belongsTo()를 정의해준다. Postimage 클래스는 Post모델에 속해있다. 
그래서 한 포스트에는 여러장의 사진이 들어가게 해줌

```php
 protected $fillable = ['dirname', 'filename', 'post_id'];
    // Eloquent Model 클래스명과 테이블명이 다를 때 property 정의 해주기 (대개 클래스명의 복수가 db table명임)

    // relationship
    public function post() {
        return $this->belongsTo(\App\Models\Post::class);
    }
```

그리고 실제 Post 모델 class에는 반대로 Postimage가 여러개가 있다고 hasMany()릴레이션을 해준다.
```php
public function postimage() {
        return $this->hasMany(\App\Models\Postimage::class);
    }
```
이렇게 되면 실제로 이미지를 표시할 때 엘로컨트로 Post 모델로 쿼리해서 내용을 가져왔을 때, 
postimage()메소드를 불러서 Postimage클래스 모델에 접근해서 데이터를 받아올 수 있게 된다.

그리고 마이그레이션 태이블 스키마 셋팅

```php
Schema::create('postimages', function (Blueprint $table) {
    $table->id();
    $table->string('dirname');
    $table->string('filename');
    $table->integer('post_id')->unsigned();
    $table->timestamps();
    $table->foreign('post_id')->references('id')->on('posts')->onDelete('cascade');;
});
```

그리고 마지막 이미지컨트롤러에는 
```php
public function store($temporaryFile, $post_id) {

    //임시db에 저장된 첫번쨰 디렉토리로 통일
    $firstDir = $temporaryFile[0]->dirname;
    foreach($temporaryFile as $imageDirFile) {
        Postimage::create([
            // dir은 첫번째로 고정 //하나의 디렉토리로 몰아주기 위해서: 임시로 업로드 되었을 시에는 파일 하나당 디렉토리하나씩 만들어짐
            'dirname' => $firstDir, 
            'filename' => $imageDirFile->filename,
            'post_id' => $post_id
        ]);
    }
}
```
넘겨받은 temporaryFile 엘로컨트 모델과 마지막 포스트한 id를 받아서, 저장을 해주게 된다.
post_id를 넘겨받은 것은 마지막 포스트한 id를 받은 것인데.. 흠.. 혼자하는 포스팅에는 문제가 없어보이는데
다른 곳에서 사용될 경우 (예를 들어 동시다발적으로 디비에 인서트 되는 것이라면 좋은 아이디어가 아닐 수 있어 보인다.)

그리고 마지막으로 ... 라라벨에서 웹에서 이미지를 표시하려면 
위에서 언급한대로, 
public 디렉토리에 있어하는데 storage디렉토리에 있는 내용은 보여줄 수가 없어서 
public 디렉토리에 sotrage심볼릭 링크를 만들어서 보여주게 된다.

라라벨 앱이 설치된 곳의 public으로 이동, 내 경우는 src가 라라벨 앱 
그 다음에 public 디렉토리 안에,
즉, storage로 심볼릭 링크를 만드는데 이 심볼릭디렉토리는 -> /var/www/html/storage/app/public 를 가리키게 된다

```shell
cd src/public 
sudo ln -sf /var/www/html/storage/app/public ./storage
```

다행히 더 쉬운 방법은 라라벨 아티잔이 있다.
```
artisan storage:link
```
이러면 끝

도커라면 (artisan까지 포함된 경우)
```
docker-compose run --rm artisan storage:link 
```

The [/var/www/html/public/storage] link has been connected to [/var/www/html/storage/app/public]. The links have been created.

요렇게 나오면 굿!
하지만 ls -l을 해보면 링크가 깨질때 나오는 빨간색으로 표시된다. 원본파일인 실제에 /var/www/html/에는 storage가 없기 때문
하지만 웹서버가 알아서 잘 처리해준다. 그래서 무시하고 넘어가면 된다.

(포스팅 할 때 넣어주기: 사진 비교)
<img src=2>


# 트러블슈팅
uniqid() 함수로 만든 게 리눅스에서 mkdir로 만들어지는 것과 db table로 들어가는 문자열이 조금 다르다.
테스트를 해보니 5번 중에 한 2~3번은 에러가 난다. 디렉토리명이 다른다.. 
리눅스에서 같은 데이터로 표기하는 방법이 달라서 다르게 디렉토리명이 만들어지고, 이를 DB에서 가져온 데이터로 찾을려고 하니
이미지가 없다고 한다.

(포스팅 할 때 넣어주기: 사진 비교)
<img src=3>

UploadContorller에서 
그래서 해결책은 uniqid()를 한 것을 기본이 13개의 문자열인데 8자로 자름
```php
$dirName = substr(uniqid(),0, 8) . '-' . now()->timestamp;
```

그랬더니 다행히 이미지를 못찾는 현상은 아직까지는 없다..

