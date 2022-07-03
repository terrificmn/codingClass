# postman 에서 post방식 처리

웹브라우저 상에서는 get방식으로만 처리를 하기 때문에   
post방식으로 접근할 수가 없어서 postman 프로그램을 이용한다.  

postman을 실행시켜서 
방식은 POST로 바꾸고 
주소는 
localhost:5000/add_two_nums  

중요한 것은 body를 선택해주고, raw데이터 JSON을 선택해준다.   
(참고 JSON에서는 "" 쌍따옴표로 묶는다)
그리고 딕셔너리 형태의 (Python의 경우), json 형태로 적어준다 

app.py 에서 코드는 
```py
@app.route('/add_two_nums', methods= ['POST'])
def add_two_nums() :
    data = request.get_json()
    # 웹url로 /add_two_nums가 실행이 되면  { "x": 10, "y": 20} 이런식으로 넘어오게된다
    if 'x' not in data or 'y' not in data :
        return {'message' : '파라미터가 잘못되었습니다.'}
        # 이렇게 요청이 잘못되면 응답을 해주게 만든다.
        
    x = data['x']
    y = data['y']

    z = x + y
    ret = {'sum' : z}
    return ret

if __name__ == "__main__" :
    app.run()  
```

postman 에서  { "x": 10, "y": 20}  이런식으로 전송을 하면
합계가 리턴되어 리스폰스로 보여지게 된다

만약 { "x": 10 } 요렇게만 요청을 했다면,   
if문으로 에러 처리를 할 수 있게 만드는데, 이렇게 하면 응답 요청으로 
'message' : '파라미터가 잘못되었습니다.' 이렇게 해줄 수 있으나,   
대신 이렇게 하면
HTTP status가 200로 정상으로 나온다.   

정상이 아니므로 다른 식으로 보내줘야함

먼저 import를 해준다
```py
# HTTP의 상태코드를 전송할 수 있는 라이브러리
from http import HTTPStatus
```

그 다음에 리턴을 해줄 때 .HTTPStatus를 사용해서 적절한 상태를 바꿔줘서 응답해 줄 수 있다
```py
return {'message' : '파라미터가 잘못되었습니다.'}, HTTPStatus.BAD_REQUEST
```

