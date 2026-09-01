질문응답에 대한 % 표시하기

Answer 모델에 SurveyResponses 관계를 설정해준다
```php
public function responses() {
        return $this->hasMany(SurveyResponse::class);
    }
}
```

그리고 

Question 모델에 SurveyResponses 관계를 설정해준다
위와 똑같음
```php
public function responses() {
        return $this->hasMany(SurveyResponse::class);
    }
}
```

위의 relationship을 이용해서 화면에 %를 표시해줄 수 있다
```php
<div class="card-body">
<ul class="list-group">
    
    @forelse($question->answers as $answer)
        <li class="list-group-item d-flex justify-content-between">
            <div>{{ $answer->answer }}</div>
                        
                <div>{{ intval(($answer->responses->count() / $question->responses->count() ) *100) }}%</div>
            @endif
        </li>
    
    @empty
        <li class="list-group-item">답변이 없습니다.</li>
    @endforelse
</ul>
```
count()를 이용해서 수를 구한 다음에 
한개의 질문에는 여러개의 option (answer모델)이 있는데 이 수를 구함
$answer->responses->count()

그리고 그 질문에 달린 총 응답 수를 구한다
$question->responses->count()

그리고 나눈 다음에 100 하면 되는데, intval() 함수를 사용해서 float로 표시가 안되게 해줌


DivisionByZeroError
바로 Division by zero 0으로 나눌 수 없는 에러가 발생~ 즉 아무도 응답을 안한 경우 0으로 나누게 되면 에러가 발생
그러면 간단하게 if를 넣어줘서 true일때만 실행하도록 고친다
```php
@if ($question->responses->count())
    <div>{{ intval(($answer->responses->count() / $question->responses->count() ) *100) }}%</div>
@endif
```

위의 관계 테이블   
| 모델 |User |Quationnaire | Question | Answer | Survey | SurveyResponse |
|-- |-- |-- | -- | -- | -- | -- |
| 테이블 | users | questionnaires | questions | answers | surveys | surveyresponses |
| 컬럼 | id, ..등 | user_id, title, purpose.. | questionnaire_id, question ..| question_id, answer.. | questionnaire_id, name, email ..| id, survey_id, question_id, answer_id ..|  



<br />
survey는 설문 페이지를 완료한 사람의 데이터가 들어감(name, email)
테이블마다 id는 생략..     
questionnarie는 설문지 자체이고
question은 하나의 질문 문항
answer는 question 질문의 여러 옵션들

예를 들어서...   

첫번째 사람 
| question: 당신은 행복합니까? | answer: 3개 | response |
| -- | --| --|
|question_id : 1 | 많이행복하다 answer_id : 1 | 응답함 response, question_id :1 , answer_id: 1 |
|question_id : 1 | 행복하다 answer_id : 2 | 응답안함 |
|question_id : 1 | 행복하지않다 answer_id : 3 | 응답안함  |

두번째 사람 
| question: 당신은 행복합니까? | answer: 3개 | response |
| -- | --| --|
|question_id : 1 | 많이행복하다 answer_id : 1 | 응답안함 response |
|question_id : 1 | 행복하다 answer_id : 2 | 응답함 response, question_id :1 , answer_id: 2 |
|question_id : 1 | 행복하지않다 answer_id : 3 | 응답안함 response |

세번째 사람 
| question: 당신은 행복합니까? | answer: 3개 | response |
| -- | --| --|
|question_id : 1 | 많이행복하다 answer_id : 1 | 응답함 response, question_id :1 , answer_id: 1 |
|question_id : 1 | 행복하다 answer_id : 2 | 응답안함   |
|question_id : 1 | 행복하지않다 answer_id : 3 | 응답안함  |

네번째 사람 
| question: 당신은 행복합니까? | answer: 3개 | response |
| -- | --| --|
|question_id : 1 | 많이행복하다 answer_id : 1 | 응답함 response, question_id :1 , answer_id: 1 |
|question_id : 1 | 행복하다 answer_id : 2 | 응답안함   |
|question_id : 1 | 행복하지않다 answer_id : 3 | 응답안함  |

다섯번째 사람 
| question: 당신은 행복합니까? | answer: 3개 | response |
| -- | --| --|
|question_id : 1 | 많이행복하다 answer_id : 1 | 응답안함  |
|question_id : 1 | 행복하다 answer_id : 2 | 응답안함   |
|question_id : 1 | 행복하지않다 answer_id : 3 | 응답  response, question_id :1 , answer_id: 3 |



surveyresponse(테이블)에는 question_id, answer_id 등이 들어가는데 

위의 표로 이렇게 해서 추려보면
question_id =1인 당신은 행복합니까?의 answer 항목은 3개이고   
그 answer_id를 가져가서 response 테이블에 저장된 것을 합쳐보면   
answer_id= 1 이 2개,  
answer_id=2 가 1개,   
answer_id= 3 가 1개  
각 count()를 하면 같은 question_id 1은 4번 나왔고, 
각 answer_id 수 나온 것을 계산 할 수 있음
(3 / 5) * 100 ---> 60%
(1 / 5) * 100 ---> 20%
(1 / 5) * 100 ---> 20%

관계가 헛깔리구먼 ;;




