Questionnaire store() method
```php
public function store() {
    $data = request()->validate([
        'title' => 'required',
        'purpose' => 'required'
    ]);

    $data['user_id'] = auth()->user()->id; //이 방법은 아주 좋은 방법은 아니라고 함
    // 아래서 코드 수정할 예정

    $questionnaire = \App\Models\Questionnaire::create($data);

    return redirect('/questionnaires/'.$questionnaire->id);
}
```

Questionnaire show() method
```php
public function show(\App\Models\Questionnaire $questionnaire) {
    return view('questionnaire.show', compact('questionnaire'));
}
```


convention 방법! 컨트롤러의 이름을 이용해서 디렉토리를 만들고 그 안에 메소드 이름으로 만든다
resources/view에 
questionnaire 디렉토리 만들고 안에 메소드 이름으로 blade 파일 만들기

예: resources/view/questionnaire/show.blade.php


User 모델과 Questionnaire 모델간의 one to many?? relationship 정의해주면 
위에서 코드를 더 쉽게 할 수 있다고 함

User모델 에 method questionnaire()로 만들어주기
```php
public function questionnaire() {
    return $this->hasMany(\App\Models\Questionnaire::class)
}
```

반대로 Questionnaire 모델에 user()이름으로 메소드 만들어주기
```php
public function user() {
    return $this->belongsTo(\App\Models\User::class)
}
```
E17 16:53 볼 차례