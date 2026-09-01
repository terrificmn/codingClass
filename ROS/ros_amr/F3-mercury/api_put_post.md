# api
[slamtec API 주소 여기 클릭](https://docs.slamtec.com/#/)   

postman, insomnia 등의 테스트 프로그램으로 api를 request해볼 수가 있다   

> Postman 프로그램에서는 PUT, POST 방식으로 할 경우에   
Body 탭의 raw로 지정해서 Json 형태로 만들어 주면 된다   
raw로 지정하면 text, Json 폼으로 변경 시킬 수 있다 

> Insomnia 프로그램은 아예 Json 탭이 나와 있어서 쉽게 찾을 수 있다

주소 지정시에는 포트번호 1448을 확인한다  


## PUT example
put 방식도 post 방식처럼 json을 선택해서 넣어준다  

- 위치 작동하게 하기 
method: PUT
주소: /api/core/slam/v1/localization/:enable

body  부분에 json으로 넣어준다 
```json
{
  "enable": true
}
```

다른 PUT 방식을 사용하는 API 라면 위와 같은 형식으로 json으로 맞춰주면 된다   
나머지 필요한 Key: Value 는 API 문서를 참고한다 



## POST example
- 특정 좌표로 이동 시킬 수 있다   
method: POST   
주소: /api/core/motion/v1/actions   

body 부분에 json을 선택해서 아래 json 형식으로 맞춰준다 
```json
{
	"action_name": "slamtec.agent.actions.MoveToAction",
	"options": {
		"target": {
			"x": -0.2,
			"y": 0.0,
			"z": 0
		},
		"move_options": {
			"mode": 0,
			"flags": [],
			"yaw": 0,
			"acceptable_precision": 0,
			"fail_retry_count": 0
		}
	}
}
```

- 특정 task 지정하기   
일단 robostudion에서는 task display 이름으로 지정할 수가 있고, task id 는 랜덤으로 할당되는 아이디 처럼 보인다    
그래서 pos_name, 과 task_points 를 넣어주게 되어있는데 task_points가 등록이 안되어 있다.   
task_points는 태블릿 앱과 연동 되는 것일 수도 있다?

mothod: POST   
주소: /api/delivery/v1/tasks  

```json
{
  "location": {
    "poi_name": "101",
    "task_points": [
      "A01"
    ]
  },
  "type": "TAKEOUT",
  "cargos": [
    {
      "cargo_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "boxes": [
        "000"
      ]
    }
  ]
}
```

