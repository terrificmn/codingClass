QuestionController
Question 모델
Answer 모델
2개의 모델에 대한 migration 이 필요 (create_table)

Question 과 Answer 모델의 두 관계는 
questions의 테이블의 questionnaries의 테이블의 id를 가져오고 -=-> questionnaire_id
answers 테이블은 questions 테이블의 id를 가져오게됨 --> question_id

그리고 Question모델은 Questionnaire 모델에 속하게 됨


class Questionnaire extends Model
{
    use HasFactory;
    protected $fillable = ['title', 'purpose', 'user_id'];
    //protected $guarded = [];

    public function user() {
        return $this->belongsTo(\App\Models\User::class);
    }

    public function question() {
        return $this->hasMany(Question::class);
    }
}


class Question extends Model
{
    use HasFactory;
    //protected $fillable = [];
    protected $guarded = [];

    public function questionnaire()
    {
        return $this->belongsTo(Questionnarire::class);
    }

    public function answer()
    {
        return $this->hasMany(Answer::class);
    }
}




class Answer extends Model
{
    use HasFactory;
    protected $guarded = [];

    public function question()
    {
        return $this->belongsTo(Answer::class);
    }
}


관계를 input태그에도 적용할 수 있는데
<div class="form-group">
    <label for="question">Question</label>
    <input name="question[question]" type="text" class="form-control" id="question" aria-describedby="questionHelp" placeholder="Enter Question">
    <small id="questionHelp" class="form-text text-muted">Ask simple and to-the-point questions for best results.</small>

    @error('guestion.question')
        <small class="text-danger">{{ $message }}</small>
    @enderror
</div>

여기에서 주목할 점은 input의 name이 "question[question]" 으로 쓰였다는 것
이름안에 배열을 넣어준것인데 여기에서 배열의 question은 questions 테이블의 db에도 question컬럼이 있다는 것

@error 블레이드 방식으로는 question.question 점으로 표시


이것도 반복시키면 많이 숫자를 늘려줌
<input name="answers[][answer]" type="text" 
    class="form-control" id="answer1" aria-describedby="choiceHelp" placeholder="Enter choice 1">

<input name="answers[][answer]" type="text" 
    class="form-control" id="answer2" aria-describedby="choiceHelp" placeholder="Enter choice 2">


<input name="answers[][answer]" type="text" 
    class="form-control" id="answer3" aria-describedby="choiceHelp" placeholder="Enter choice 3">



@error('answers.0.answer')
    <small class="text-danger">{{ $message }}</small>
@enderror

이제 이 형식을 반복하면서 숫자를 늘려준다

@error('answers.1.answer')
    <small class="text-danger">{{ $message }}</small>
@enderror

@error('answers.2.answer')
    <small class="text-danger">{{ $message }}</small>
@enderror
..
..
..


데이터를 전송을 하게 되면 submit 버튼을 눌러서 store 메소드가 작동하게 될 때 
dd()헬퍼함수를 써서  dump and die
이런 결과가 나온다 
```json
array:3 [▼
  "_token" => "07Ptwq753McW21mJqIwzOPv0KAOz5DUWLNVa0JQx"
  "question" => array:1 [▼
    "question" => "What should we do?"
  ]
  "answers" => array:4 [▼
    0 => array:1 [▼
      "answer" => "Stay the same"
    ]
    1 => array:1 [▼
      "answer" => "change"
    ]
    2 => array:1 [▼
      "answer" => "do something"
    ]
    3 => array:1 [▼
      "answer" => "do else"
    ]
  ]
]
```

위에서 사용한 결과로 이렇게 됨

위의 과정을  QuestionController에서 적용하는 방법
```php

 public function store(\App\Models\Questionnaire $questionnaire) {
        
        dd(request()->all());
        $data = request()->validate([
            'question.question' => 'required',  //question.question 은 question디렉토리의 create.blade.php 에서 
            // input name="question[question]" 인풋 태그의 이름
            'answers.*.answer' => 'required'  // 이것 역시 같은 블레이드 페이지의 input의 이름
            // input name="answers[][answer]" // answers[] 배열을 행을(row) *로 처리 와이들카드로 모든것을 의미,  열은 다시 또 answer
        ]);
        return view('question.create', compact('questionnaire'));
    }

```

validation 확인해서 메세지 보여주려면
```php
@error('answers.1.answer')
    <small class="text-danger">{{ $message }}</small>
@enderror
```

@error 블레이드형식 넣어주면 되고, 
input tag에 value= old() 함수 이용해서 예전 메세지를 기억하게 한다

```php
value="{{ old('question.question')}}"

<input ....  value="{{ old('answers.3.answer')}}"> 
```


검증된 데이터가 validate()를 거친 것을 dd()해보면
json형태를 볼 수 있는데 
아래와 같음 참고
```json
array:2 [▼
  "question" => array:1 [▼
    "question" => "test"
  ]
  "answers" => array:4 [▼
    0 => array:1 [▶]
    1 => array:1 [▶]
    2 => array:1 [▶]
    3 => array:1 [▶]
  ]
]
```
즉 질문지 input question 에는 배열 하나
질문지의 input answers 에는 배열 4개

form 자체가 그렇게 설계되어 있었음
그래서 request()로 데이터가 넘어가는 것도 그러함

QuestionController에서 store()메소드 정의
```php
public function store(\App\Models\Questionnaire $questionnaire) {
        
        //dd(request()->all());
        $data = request()->validate([
            'question.question' => 'required',  //question.question 은 question디렉토리의 create.blade.php 에서 ( nested values를 처리하는 방법)
            // input name="question[question]" 인풋 태그의 이름
            'answers.*.answer' => 'required'  // 이것 역시 같은 블레이드 페이지의 input의 이름
            // input name="answers[][answer]" // answers[] 배열을 행을(row) *로 처리 와이들카드로 모든것을 의미,  열은 다시 또 answer
        ]);

        //dd($data); // validated data  확인
        $question = $questionnaire->question()->create($data['question']);
        // 넘어온 questionnaire 모델을 이용해서 question 메소드로 (서로 관계정의할 떄 사용)
        // 검증처리된 $data의 question 부분. 즉, 질문에 대한것을 db로 create 해라. 그래서 Question 모델을 반환
        $question->answer()->createMany($data['answers']);
        // 다시 relationship을 이용한 answer()메소드를 불러서 이번에는 create이 아닌 createMany 로 생성
        // 왜냐하면 데이터가 많이 있기 때문(배열로 들어가 있음) : answers 키에는 values가 배열로 4개가 되어 있음 
        return redirect('/questionnaire/'.$questionnaire->id);
        
    }

```

아 최종적으로 반영하려면
migrate를 해야함
db를 먼저 만들어 줘야함

```
$php artisan migrate
```


