참고 사이트: 부트스트랩 example
https://getbootstrap.com/docs/5.0/components/list-group/

먼저 Survey 모델과  마이그레이션 준비
Survey 모델과 SurveyResponse 필요 

php artisan make:model Survey -m
php artisan make:model SurveyResponse -m

db 테이블을 복수형으로 만들어짐에 주의 (surveys) 이런식으로 그래서 모델명을 정할 때 단수로 만들어줘야한다 Survey
그리고 SurveyResponse는 survey_responses db테이블이 만들어짐

모델끼리 관계를 형성해준다

많은 관계를 가지면 복수형으로 메소드를 만든다. 속해있으면 단수형으로 메소드를 만듬

**Survey**모델은 questionnaire() 로 
return $this->belongsTo(Questionnaire::class); 이렇게 됨

그리고 surveyresponses() 를 가지는데 많이 가질 수 있음
return $this->hasMany(SurveyResponse::class); 이렇게 됨

**Questionnaire** 모델은 surveys()를 많이 가질 수 있음
return $this->hasMany(Question::class);

이번에는 
**SurveyResponse** 모델은 survey() 에 속해있는 메소드를 만듬
return $this->belongsTo(Survey::class);


서베이랑 서베이응답을 만든 것이므로 서베이에 대한 응답을 한 유저의 정보를 받기 위해서 name과 email을 입력받는다 input태그

show.blade.php에서 

```html
<div class="card mt-4">
    <div class="card-header">Your Information</div>

        <div class="card-body">
            <div class="form-group">
                    <label for="name">Your name</label>
                    <input name="survey[name]" type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Enter name">
                    <small id="nameHelp" class="form-text text-muted">Hello~ What's your name?</small>

                    @error('name')
                        <small class="text-danger">{{ $message }}</small>
                    @enderror
                </div>

                <div class="form-group">
                    <label for="email">Your email</label>
                    <input name="survey[email]" type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Enter email">
                    <small id="emailHelp" class="form-text text-muted">Your email, please</small>

                    @error('email')
                        <small class="text-danger">{{ $message }}</small>
                    @enderror
                </div>

                <div>
                    <button type="submit" class="btn btn-primary">Complete Survey</button>
                </div>

    </div>
```

중요한것이 이번에도 입력받은 것을 넘길 때 form에서 input태그의 name이 배열로 해서 넘겨준다 survey[name] , survey[email] 이렇게 넘겨주면
**SurveyController** 컨트롤러에서 validate()를 하는데
```php
'survey.name' => 'required',
'survey.email' => 'required|email' 
```
요렇게 추가해줄 수 있게 된다.

그리고 이렇게 마무리 되게 됨
```php
public function store(Questionnaire $questionnaire) {
    ... $data = request()->validate([....]) ..생략
    //위의 Questionnaire모델을 가지고 와서 surveys()관계를 이용해서 메소드 호출(hasMany relationship) ->create($data[키])

    $survey = $questionnaire->surveys()->create($data['survey']);
    $survey->surveyresponses()->createMany($data['responses']); //surveyresponses 관계 이용
  }
```

request()로 넘어온 데이타는 dd()를 찍어보면 dd(request()->all()) 들어온 데이터를 보여주는데, 
위의 html input 태그로 넘긴 survey[name] 온 걸 알 수 있고 
이것을 $data로 받아서 진행 여기에서는 키(값) 만 사용하면 dB에 넣어주면 됨
결국 (키의 value가 db에 들어가짐 )

surveyresponses 도 마찬가지로 진행되지만, survey는 많은 responses를 가지기 때문에 (hasMany relationship) creteMany() 메소드로 db를 생성한다



이제 마이그레이션 준비
DB 스키마
```php
  Schema::create('surveys', function (Blueprint $table) {
            $table->bigIncrements('id');
            $table->unsignedBigInteger('questionnaire_id'); //relationship with questionnaire (belongsTo)
            $table->string('name');
            $table->string('email');
            $table->timestamps();
        });
```

```php
 Schema::create('survey_responses', function (Blueprint $table) {
            $table->bigIncrements('id');
            $table->unsignedBigInteger('survey_id');  //SurveyResponses (survey_responses)는 belongsTo Survey(surveys id를 가지고 온다)
            $table->unsignedBigInteger('question_id'); 
            $table->unsignedBigInteger('answer_id'); // question 과 answer id를 통해서 passing throgh my form 했기 때문에 
            $table->timestamps();
        });
```

그리고 마이그레이션
```
php artisan migrate
```