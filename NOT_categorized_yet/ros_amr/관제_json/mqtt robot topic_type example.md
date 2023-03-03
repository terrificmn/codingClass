
## json 형식
- header, body로 구성
- header 의 version은 0으로 고정, type 은 변경
- body 안에 실제 데이터를 넣어준다
예
```js
{
	"header": 
	{
		"version": 0,
		"type": 0
	},
	"body":
	{
		"key1": "value1",
		"key2": "value2"
	}
}
```



## 토픽 및 타입에 따른 json data 예 

> json 내의 type 생략하고 우선 body만 기술함

### 1. topic | 공통 | al.common

#### type 0
 Robot -> Server : 주기적으로 로봇 상태 전송 (pose data, status, etc...)
```js
{
	"header": 
	{
		"version": 0,
		"type": 0
	},
	"body":
	{
		"robot_id": 1,
		"x": 10.123456,
		"y": -5.123456,
		"yaw": 1.123456,
		"status": "active",
		"recipe": 2,
		"sequence": 1,
		"task": "none",
		"battery": 85.5,
		"order_state": "readyToLoad",
		"basket_state": "empty"
	}
}
```

| 이름     | 타입   |
| -------- | ------ |
| robot_id | int    |
| x        | double |
| y        | double |
| yaw      | double |
| status   | string |
| recipe   | int    |
| sequence | int    |
| task     | string       |
| battery      | double |
| order_state  | string |
| basket_state | string |


이 중 status, order_state, basket_state는 value의 예
- status : "Charging", "Standby", "Active", "Stuck",  or "Lost"
- order_state : "ReadyToOrder", "ReadyToLoad", or "ReadyToUnload"
- basket_state : "Empty", or "InUse" 
- task : "move_to_goal", order", "stations", "none"


#### type 1
Server -> Robot : 특정 로봇에 응답 요청
```js
{
	"header": 
	{
		"version": 0,
		"type": 1
	},
	"body":
	{
		"robot_id": 1
	}
}
```

| 이름 | 타입 |
| ---- | ---- |
| robot_id   | int  |


#### type 2
Robot -> Server : type1로 받은 로봇이 서버에 응답
```js
{
	"header": 
	{
		"version": 0,
		"type": 2
	},
	"body":
	{
		"robot_id": 1,
		"status": "active"
	}
}
```

| 이름   | 타입   |
| ------ | ------ |
| robot_id     | int    |
| status | string |



#### Type 10
Server -> Robot: 주변 로봇 정보를 broadcasting
```js
{
	"header":
	{
		"version":0,
		"type":10
	},
	"body":
	{
		"robots": 
		[
			{
				"robot_id":1,
				"x":11.1235,
				"site_id":2,
				"y":-11.1235
			},
			{
				"robot_id":2,
				"x":-0.730176,
				"site_id":2,
				"y":0.227345
			},
			{
				"robot_id":3,
				"x":0.0,
				"site_id":2,
				"y":0.0},
			{
				"robot_id":4,
				"x":0.0,
				"site_id":2,
				"y":0.0
			}
		]
	}
}
```



*추가 타입*

#### type 3
Server -> Robot : 이동 명령
```js
{
	"header": 
	{
		"version": 0,
		"type": 3
	},
	"body":
	{
		"robot_id": 1,
		"goal_x": 10.123456,
		"goal_y": -5.123456
	}
}
```

| 이름     | 타입   |
| -------- | ------ |
| robot_id | int    |
| goal_x   | double |
| goal_y   | double |


#### type 4
Robot -> Server : 이동 명령에 대한 응답  
```js
{
	"header": 
	{
		"version": 0,
		"type": 4
	},
	"body":
	{
		"robot_id": 1,
		"status": "Moving",
		"goal_x": 10.123456,
		"goal_y": -5.123456
	}
}
```

| 이름     | 타입   |
| -------- | ------ |
| robot_id | int    |
| status   | string |
| goal_x   | double | 
| goal_y   | double |




#### type 5
Server -> Robot : 개별 로봇 멈춤 명령
```js
{
	"header": 
	{
		"version": 0,
		"type": 5
	},
	"body":
	{
		"robot_id": 1
	}
}
```

| 이름     | 타입   |
| -------- | ------ |
| robot_id | int    |





#### type 6
~~Robot -> Server : (type5) 에대한 멈춤 명령에 대한 응답  - status 변경 ~~
**응답 안하기로 함**

대신 type6번은 resume 으로 사용
Server -> Robot : (type5) 이후 재개 명령
```js
{
	"header": 
	{
		"version": 0,
		"type": 6
	},
	"body":
	{
		"robot_id": 1
	}
}
```

| 이름     | 타입   |
| -------- | ------ |
| robot_id | int    |

~~| status   | string |
| ack   | int | ~~


#### type 998
Server -> Robot : 긴급 상황 시 작업 중지 명령
```js
{
	"header": 
	{
		"version": 0,
		"type": 998
	}
	
}
```

| 이름 | 타입 |
| ---- | ---- |
|      |      |

바디 없음


#### type 999
Server -> Robot : 모든(?) 로봇에게 작업 재개 명령
```js
{
	"header": 
	{
		"version": 0,
		"type": 999
	}

}
```

| 이름   | 타입   |
| ------ | ------ |

바디 없음




### 2. topic | 등록/조회 | al.register

#### type 100
Robot -> Server: 로봇 최초 등록 시 신규 등록 요청
```js
{
	"header": 
	{
		"version": 0,
		"type": 100
	},
	"body":
	{
		"mac_address": "99-2E-93E-19E-30-15"
	}
}
```

| 이름        | 타입   |
| ----------- | ------ |
| mac_address | string |


#### type 101
Server -> Robot : 로봇 등록에 대한 서버쪽의 요청, ID 발급
```js
{
	"header": 
	{
		"version": 0,
		"type": 101
	},
	"body":
	{
		"id_status": 1,
		"robot_id": 5,
		"error": 0
	}
}
```

| 이름      | 타입    |
| --------- | ------- |
| id_status | int     |
| robot_id | int     |
| error     | unknown |


#### type 102
Robot -> Server : 로봇쪽에서 로봇 ID 조회
```js
{
	"header": 
	{
		"version": 0,
		"type": 102
	},
	"body":
	{
		"mac_address": "99-2E-93E-19E-30-15"
	}
}
```

| 이름        | 타입   |
| ----------- | ------ |
| mac_address | string |


#### type 103
Server -> Robot : 서버에서 로봇 ID 응답
```js
{
	"header": 
	{
		"version": 0,
		"type": 103
	},
	"body":
	{
		"robot_id": 3,
		"mac_address": "02:7c:15:03:e9:25"
	}
}
```

| 이름   | 타입    |
| ------ | ------- |
| robot_id     | int     |
| mac_address  | string |



### 3. topic | 주문 | al.order

#### type 200
Server -> Robot: 새로운 주문 할당
```js
{
	"header": 
	{
		"version": 0,
		"type": 200
	},
	"body":
	{
		"robot_id": 3,
		"order_id":  10,
		"basket": [
			{
				"id": 1,
				"depository_x": -1.029711,
				"depository_y": -4.020630
			},
			{
				"id": 2,
				"depository_x": 1.252728,
				"depository_y": -2.293799
			}
		]
	}
}
```

| 이름                  | 타입   |
| --------------------- | ------ |
| robot_id              | int    |
| order_id              | int    |
| basket                | array  |
| (basket).id           | int    |
| (basket).depository_x | double |
| (basket).depository_y | double |



#### type 201
Robot -> Server: 주문을 확인하고 주행 시작 
```js
{
	"header": 
	{
		"version": 0,
		"type": 201
	},
	"body":
	{
		"robot_id": 2,
		"order_id":  10,
		"error": 0
	}
}
```

| 이름     | 타입 |
| -------- | ---- |
| robot_id | int  |
| order_id | int  |
| error    | int  | 

order_state 변경 후 이동


#### type 202
Robot -> Server: 주문을 현황을 수시로 전송
```js
{
	"header": 
	{
		"version": 0,
		"type": 202
	},
	"body":
	{
		"robot_id": 2,
		"order_id":  10,
		"progress_rate": 40.5
		"order_state": "ReadyToLoad",
		"sequence": 4
	}
}
```

| 이름          | 타입   |
| ------------- | ------ |
| robot_id      | int    |
| order_id      | int    |
| progress_rate | float  |
| order_state   | string |
| sequence      | int    |

해당 스테이션에 도착하게 되면 order_state "ReadyToLoad" 로 변경되어 전송
바코드 인식 후 order_state "ReadyToMove"


#### type 203
Robot -> Server: 주문 완료 시, 주문 현황 전송 (전체 완료)
```js
{
	"header": 
	{
		"version": 0,
		"type": 203
	},
	"body":
	{
		"robot_id": 2,
		"order_id":  10,
		"res_status": 0/1,
		"error": 0/1,
		"order_state": "OrderCompleted"
	}
}
```

| 이름        | 타입   |
| ----------- | ------ |
| robot_id    | int    |
| order_id    | int    |
| res_status       | int    |
|error       | int    |
| order_state | string |

res_status는 성공여부
완료시 order_state "OrderCompleted" 변경 전송


#### type 204
Sever -> Robot: 주문 취소 시 특정 로봇에게 전송
```js
{
	"header": 
	{
		"version": 0,
		"type": 204
	},
	"body":
	{
		"robot_id": 3,
		"order_id":  10
	}
}
```

| 이름        | 타입 |
| ----------- | ---- |
| robot_id    | int  |
| order_id    | int  |



#### type 205
Robot -> Server: 주문 취소 확인 전송
```js
{
	"header": 
	{
		"version": 0,
		"type": 205
	},
	"body":
	{
		"robot_id": 3,
		"order_id":  10,
		"order_state": "OrderCancelled",
		"error": 
	}
}
```

| 이름        | 타입   |
| ----------- | ------ |
| robot_id    | int    |
| order_id    | int    |
| order_state | string |
| error            |        |

order_state 는 "OrderCancelled"로 변경 전송


#### type 206
Server -> Robot: 하나의 스테이션에서 픽킹 완료 (자체, 태블릿에서 전송)
```js
{
	"header": 
	{
		"version": 0,
		"type": 206
	},
	"body":
	{
		"robot_id": 3,
		"sequence": 1
	}
}
```

 header의 type과 , body의 robot id  

| 이름     | 타입 |
| -------- | ---- |
| robot_id | int  |
| sequence | int     |

sequence는 수행하고 있는 order의 순서 (wp), miss match 확인




### 4. topic | 웨이포인트 | al.stations

#### type 300
Server -> Robot: 웨이포인트 순회

```js
{
	"header": 
	{
		"version": 0,
		"type": 300
	},
	"body":
	{
		"robot_id": 22,
		"stations": [
			{
				"id": 1,
				"x": -1.029711,
				"y": -4.020630
			},
			{
				"id": 2,
				"x": 1.252728,
				"y": -2.293799
			}
		]
	}
}
```

| 이름       | 타입          |
| ---------- | ------------- |
| robot_id   | int           |
| stations   | array         |
| --- 아래는 | stations 배열 |
| id         | int              |
| x          | double        |
| y          | double        |



#### type 301
Server -> Robot: 다음 목적지 출발 명령
```json
{
	"header": 
	{
		"version": 0,
		"type": 301
	},
	"body":
	{
		"robot_id": 22,
		"sequence": 3
	}
}
```

| 이름     | 타입 |
| -------- | ---- |
| robot_id | int  |
| sequence         | int      |




### 5. topic | 서버 | al.server

#### type 400
Server -> Robot: 다른 로봇들의 pose 정보 제공

```js
{
	"header": 
	{
		"version": 0,
		"type": 400
	},
	"body":
	{
		"tick-count": 1111,
		"locations": [
			{
				"id": 1,
				"locationX": -1.029711,
				"locationY": -4.020630,
				"yaw": 0.0,
				"status: "LOST",
				"site_id": 2
			},
			{
				"id": 2,
				"locationX": 10.029711,
				"locationY": 5.020630,
				"yaw": 0.0,
				"status: "LOST",
				"site_id": 2
			}
		]
	}
}
```

| 이름       | 타입           |
| ---------- | -------------- |
| tick-count | int            |
| locations  | array          |
| --- 아래는 | locations 배열 |
| id         | int            |
| locationX  | double         |
| locationY  | double         |
| yaw        | double         |
| status     | string         |
| site_id    | int            |







## order 테스트

같은 장소. type 200
```json
{
	"header": 
	{
		"version": 0,
		"type": 200
	},
	"body":
	{
		"robot_id": 22,
		"order_id":  10,
		"basket": [
			{
				"id": 1,
				"depository_x": -1.029711,
				"depository_y": -4.020630
			},
			{
				"id": 2,
				"depository_x": -1.029711,
				"depository_y": -4.020630
			},
			{
				"id": 3,
				"depository_x": -1.029711,
				"depository_y": -4.020630
			}
		]
	}
}
```

픽업 완료 type 206
```json
{
	"header": 
	{
		"version": 0,
		"type": 206
	},
	"body":
	{
		"robot_id": 22
	}
}
```



al.common 으로 이동 명령
```json
{
	"header": 
	{
		"version": 0,
		"type": 3
	},
	"body":
	{
		"robot_id": 22,
		"goal_x": -1.029711,
		"goal_y": -4.020630
	}
}
```





### cancle 테스트

취소
```json

{
	"header": 
	{
		"version": 0,
		"type": 204
	},
	"body":
	{
		"robot_id": 2,
		"order_id":  1
	}
}

```

이동
```json

{
	"header": 
	{
		"version": 0,
		"type": 206
	},
	"body":
	{
		"robot_id": 2,
		"sequence": 2
	}
}

```

주문
```json

{
  "header": {
    "version": 0,
    "type": 200
  },
  "body": {
    "robot_id": 2,
    "order_id": 1,
    "basket": [
      {
        "id": 1,
        "depository": 1,
        "code": "98271",
        "name": "orange",
        "quantity": 1,
        "description": "",
        "depository_x": -0.555683,
        "depository_y": 2.37623
      },
      {
        "id": 2,
        "depository": 2,
        "code": "98272",
        "name": "apple",
        "quantity": 1,
        "description": "",
        "depository_x": -0.636509,
        "depository_y": 2.43215
      },
      {
        "id": 3,
        "depository": 3,
        "code": "98273",
        "name": "banana",
        "quantity": 1,
        "description": "",
        "depository_x": -1.61573,
        "depository_y": 2.41207
      },
      {
        "id": 4,
        "depository": 4,
        "code": "98274",
        "name": "grape",
        "quantity": 1,
        "description": "",
        "depository_x": -1.72959,
        "depository_y": 0.409578
      },
      {
        "id": 5,
        "depository": 5,
        "code": "98275",
        "name": "speaker",
        "quantity": 1,
        "description": "",
        "depository_x": -0.366691,
        "depository_y": 0.253385
      },
      {
        "id": 6,
        "depository": 6,
        "code": "98276",
        "name": "mouse",
        "quantity": 1,
        "description": "",
        "depository_x": -1.60292,
        "depository_y": 0.438153
      },
      {
        "id": 7,
        "depository": 7,
        "code": "98277",
        "name": "iphone",
        "quantity": 1,
        "description": "",
        "depository_x": -0.430206,
        "depository_y": 0.242123
      }
    ]
  }
}

```


order 테스트 -gazebo경로 type 200
```json
{
  "header": {
    "version": 0,
    "type": 200
  },
  "body": {
    "robot_id": 3,
    "order_id": 1,
    "basket": [
      {
        "id": 1,
        "depository": 1,
        "code": "98271",
        "name": "orange",
        "quantity": 1,
        "description": "",
        "depository_x": 4.507804,
        "depository_y": -1.926179
      },
      {
        "id": 2,
        "depository": 2,
        "code": "98272",
        "name": "apple",
        "quantity": 1,
        "description": "",
        "depository_x": 0.209795,
        "depository_y": -1.019812
      }
      
    ]
  }
}

```


stations 테스트 - gazebo경로  type 300
```json
{
  "header" : 
  {
    "version": 0, "type": 300 
  },
  "body" :
  {
    "robot_id": 3,
    "recipe": 2,
    "stations": [
        {
          "id": 2,
          "x": 4.507804,
          "y": -1.926179
        },
        {
          "id": 3,
          "x": 0.209795,
          "y": -1.019812
        }
      ]
  }
}
```



stations 테스트 - type 301
```json
{
  "header" : 
  {
    "version": 0, "type": 301 
  },
  "body" :
  {
    "robot_id": 3,
    "sequence": 1
  }
}
```


stations 테스트 sorting 테스트 (for office)
```json
{
  "header" : 
  {
    "version": 0, "type": 300 
  },
  "body" :
  {
    "robot_id": 2,
    "recipe": 10,
    "stations": [
        {
          "id": 2,
          "x": 3.0446906,
          "y": 0.1253185
        },
        {
          "id": 3,
          "x": 6.151103,
          "y": -0.896063
        },
        {
          "id": 4,
          "x": 3.33870,
          "y": -2.63941
        },
        {
          "id": 5,
          "x": 2.0804343,
          "y": 0.079382
        },
        {
          "id": 6,
          "x": 3.996640,
          "y": 1.749974
        },
        {
          "id": 7,
          "x": 4.952727,
          "y": -1.173892
        },
        {
          "id": 8,
          "x": -0.956039,
          "y": 1.633952
        }
      ]
  }
}
```