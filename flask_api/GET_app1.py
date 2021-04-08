from flask import Flask

app = Flask(__name__)  # flask 기본구조

# get  localhost:포트번호   경로 /

@app.route('/', methods = ['GET'])  # 'url의 루트경로 /'
def hello_world() :
    return 'Hello World from Flask'

@app.route('/act', methods = ['GET'])
def act() :
    ret = {  #json 형식인 딕셔너리로 만들어준다
        'count' : 2, 
        'students' : [
            {'name' : '홍길동',     'age' : 30},
            {'name' : '김나나',     'age' : 25},
            {'name' : '이바다',     'age' : 20},
            {'name' : '박강',     'age' : 30}
        ]
    }
    return ret


if __name__ == "__main__" :
    app.run()  
