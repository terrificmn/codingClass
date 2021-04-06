from flask import Flask, request
from flask_restful import Api, reqparse

from db.db import get_mysql_connection
from config.config import Config
from resources.recipe import RecipeListResource

app = Flask(__name__)  # flask 기본구조

# 1. 환경 변수 설정
app.config.from_object(Config) #Config 클래스 불러오기




# 2. api 설정
api = Api(app)
api.add_resource(RecipeListResource, '/recipes')

#api.add_resource(RecipeListResource, "/recipes/<int:likes>")



# { 
# "name": "계란국", 
# "description": "계란를 풀어 만든 국", 
# "num_of_servings": 2, 
# "cook_time": 30, 
# "directions": "1. 물을 끓인다. 2. 물이 끓으면 계란을 넣는다. 3. 파를 넣는다.", 
# "is_publish": ""
# }

# 3. 경로(path) URL랑 리소스(resource)를 연결한다.
# 리소스는 클래스로 만든다 (실무에서 class로 사용)
if __name__ == "__main__" :
    #app.run(port=Config.PORT)  # Config클래스를 이용해서 포트번호 지정하려면 #아니면 port=5002 이런식으로 주면 됨
    app.run()  



