from flask import Flask
from flask_restful import reqparse
from flask_restful import Resource
from http import HTTPStatus
from db.db import get_mysql_connection
import json

# 이 RecipeListResource 클래스는 
# Flask 프레임워크에서 경로랑 연결시킬 클래스인데 
# 그래서 Resource클래스를 상속받아야함
# Flask 프레임워크 레퍼런스 사용법에 나와 있음

class RecipeListResource (Resource):
    def get(self):
        # recipe 테이블에 저장되어 있는 모든 레시피 정보를 가져오는 함수
        
        connection = get_mysql_connection()
        cursor = connection.cursor(dictionary=True)
        query = """select * from recipe;"""
        cursor.execute(query)
        records = cursor.fetchall()

        print(records)
        ret = []
        for row in records :
            row['created_at'] = row['created_at'].isoformat()
            row['updated_at'] = row['updated_at'].isoformat()
            ret.append(row)
        
        # 커서와 커넥션을 닫아준다
        cursor.close
        connection.close

        # 클라이언트에 리스판스 한다 
        return { 'ret': ret}, HTTPStatus.OK #200코드

    def post(self):
        parser = reqparse.RequestParser() 
        
        parser.add_argument('name', type=str, help="name is required.")
        #abort(404, message="not found")
        # required=True로 하지 않으면 해당 키가 없으면 None으로 리턴
        parser.add_argument('description', type=str, help="name is required.")
        parser.add_argument('num_of_servings', type=str, help="name is required.")
        parser.add_argument('cook_time', type=str, help="name is required.")
        parser.add_argument('directions', type=str, help="name is required.")
        
        args = parser.parse_args()
        if args['name'] is None:
            return {'message' : 'name이 잘못되었습니다.'}, HTTPStatus.BAD_REQUEST
        else:
            print('몰라')
                            # "name": args['name'], 
                            # "description": args['description'], 
                            # "num_of_servings": args['num_of_servings'], 
                            # "cook_time": args['cook_time'], 
                            # "directions": args['directions']
                            

            
            return {}
        #1. 클라이언트가 요청한 request의 body에 있는 json 데이터를 가져오기
        #2. 필수 항목이 있는지 체크
        #3. 데이터베이스 커넥션 연결
        #4. 커서 가져오기
        #5. 쿼리문 만들기
        #6. 쿼리문 실행
        #7. 커서와 커넥션 닫기
        #8. 클라이언트에 reponse하기

    def put(self, likes):
        recipes = {}
                
        put_args = reqparse.RequestParser()
        put_args.add_argument("name", type=str, help="name of the recipe is required", required=True)
        put_args.add_argument("likes", type=int, help="likes on the video")

        args = put_args.parse_args()
        recipes[likes] = args
        return recipes[likes], 201