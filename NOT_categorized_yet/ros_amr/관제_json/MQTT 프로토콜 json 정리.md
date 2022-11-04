
## 공통

평상시 주기적으로 로봇 상태 전송
```json
{
	"header": {
		"version": 0,
		"type": 0
	},
	"body": {
		"robotId": 1,
		"x": 10.123456,
		"y": 1.123456,
		"battery": 70.5,
		"status": "Active",
		"orderState": "ReadyToOrder",
		"basketState": "Empty"
	}
}
```



## 로봇 ID 등록

최초 Mac Address 전송 
```json
{
	"header": {
		"version": 0,
		"type": 100
	},
	"body": {
		"MacAddress": "02:3c:14:03:e8:12",
	}
}
```


로봇 등록 요청 결과 (Subscribe)
```json
{
	"header": {
		"version": 0,
		"type": 101
	},
	"body": {
		"status": 0,
		"robotId": 2
		"error": ?
	}
}
```


## 주문 

주문할당 (Subscribe)
```json
{
	"header": {
		"version": 0,
		"type": 200
	},
	"body": {
		"robotId": 2,
		"orderId": 
		"error": ?
	}
}
```


