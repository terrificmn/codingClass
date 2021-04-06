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

# @app.route('/recipes', methods= ['POST'])
# def recipes() :
#     #data = request.get_json()

#     parser = reqparse.RequestParser() 
#     #print(parser)
#     parser.add_argument('name', type=str, help="name is required.", required=True)
#     #about(404, message="not found")
#     # required=True로 하지 않으면 해당 키가 없으면 None으로 리턴
#     parser.add_argument('description', type=str, help="name is required.")
#     parser.add_argument('num_of_servings', type=str, help="name is required.")
#     parser.add_argument('cook_time', type=str, help="name is required.")
#     parser.add_argument('directions', type=str, help="name is required.")
    
#     args = parser.parse_args()
    
#     if args['name'] not in args:
#         abort('invaild')
#     else:
#         print("wrong")
#     # recipes[likes] = args
#     # return recipes[likes], 201

# { 
# "name": "계란국", 
# "description": "계란를 풀어 만든 국", 
# "num_of_servings": 2, 
# "cook_time": 30, 
# "directions": "1. 물을 끓인다. 2. 물이 끓으면 계란을 넣는다. 3. 파를 넣는다."
# }
    
    # return {}

if __name__ == "__main__" :
    app.run()