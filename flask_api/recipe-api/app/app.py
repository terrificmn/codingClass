from flask import Flask, request
from flask_restful import Api

from db.db import get_mysql_connection
#from config.config import Config
from resources.recipe import RecipeListResource, RecipeResource, RecipePublishResource
from resources.user import UserListResource, UserResource

app = Flask(__name__)  # flask 기본구조

# 1. 환경 변수 설정
#app.config.from_object(Config) #Config 클래스 불러오기

# 2. api 설정
api = Api(app)
# recipe.py에 있는 클래스들은 import 해준다  # GET / POST 방식에 대응한다
api.add_resource(RecipeListResource, '/recipes')

# put, delete 까지 처리함
api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')  # URL get으로 받아오는 값을 변수로 처리

# publish 관련 처리하는 클래스 추가 (publish가 0이면 비공개)
api.add_resource(RecipePublishResource, '/recipes/<int:recipe_id>/publish')


# post 회원가입
api.add_resource(UserListResource, '/users')

# post 로그인
api.add_resource(UserResource, '/users/login')

if __name__ == "__main__" :
    app.run()
