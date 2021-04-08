# JSON 형식으로 메세지 처리하기
from flask import Flask, request
# HTTP의 상태코드를 전송할 수 있는 라이브러리
from http import HTTPStatus

app = Flask(__name__)  # flask 기본구조

# 두개의 숫자를 클라이언트에게 받는다. #파라미터 x, y로 받기
# 받은 두 숫자를 더해서, 클라이언트에 response

@app.route('/add_two_nums', methods= ['POST'])
def add_two_nums() :
    data = request.get_json()
    # 웹url로 /add_two_nums가 실행이 되면  { "x": 10, "y": 20} 이런식으로 넘어오게된다
    if 'x' not in data or 'y' not in data :
        return {'message' : '파라미터가 잘못되었습니다.'}, HTTPStatus.BAD_REQUEST

    x = data['x']
    y = data['y']

    z = x + y
    ret = {'sum' : z}
    return ret

if __name__ == "__main__" :
    app.run()  
