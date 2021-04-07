from flask import Flask
from flask_restful import Resource, reqparse, request
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
        data = request.get_json()  #post값의 body부분 작성될 것을 받아온다
        
        if 'name' not in data:
            return {'message': 'name is required'}, HTTPStatus.BAD_REQUEST
        
        #1. 클라이언트가 요청한 request의 body에 있는 json 데이터를 가져오기
        #2. 필수 항목이 있는지 체크
        #3. 데이터베이스 커넥션 연결
        #4. 커서 가져오기
        #5. 쿼리문 만들기
        #6. 쿼리문 실행
        #7. 커서와 커넥션 닫기
        #8. 클라이언트에 reponse하기

        connection = get_mysql_connection()

        cursor = connection.cursor(dictionary=True)
        
        query = """insert into recipe (name, description, num_of_servings, cook_time, directions, is_publish)
                    values (%s, %s, %s, %s, %s, %s);"""

        param = ( 
                data['name'], data['description'], data['num_of_servings'], 
                data['cook_time'], data['directions'], data['is_publish'] 
        )
        
        result = cursor.execute(query, param)
        print(result)

        cursor.close()
        connection.close()

        return {}, HTTPStatus.CREATED
        # parser = reqparse.RequestParser() 
        
        # parser.add_argument('name', type=str, help="name is required.")
        # #abort(404, message="not found")
        # # required=True로 하지 않으면 해당 키가 없으면 None으로 리턴
        # parser.add_argument('description', type=str, help="name is required.")
        # parser.add_argument('num_of_servings', type=str, help="name is required.")
        # parser.add_argument('cook_time', type=str, help="name is required.")
        # parser.add_argument('directions', type=str, help="name is required.")
        
        # args = parser.parse_args()
        # if args['name'] is None:
        #     return {'message' : 'name이 잘못되었습니다.'}, HTTPStatus.BAD_REQUEST
        # else:
        #     print('몰라')


    # def put(self, likes):
    #     recipes = {}
        
    #     put_args = reqparse.RequestParser()
    #     put_args.add_argument("name", type=str, help="name of the recipe is required", required=True)
    #     put_args.add_argument("likes", type=int, help="likes on the video")

    #     args = put_args.parse_args()
    #     recipes[likes] = args
    #     return recipes[likes], 201

class RecipeResource (Resource):
    def get(self, recipe_id):
        #1. 경로에 붙어있는 값(레시피 테이블의 아이디)을 가져와야 한다. 

        #URL에서 ?뒤에 있는 get방식을 쿼리를 받을 때 사용
        #예: localhost:5000?id=3&name=mike
        #recipe_id = request.args

        #get 으로 아디값만 받으므로 get 메소드 파라미터로 받으면 됨
        print(recipe_id)

        #2. 디비 커넥션 가져온다
        connection = get_mysql_connection()

        #3. 커서 가져오고 
        cursor = connection.cursor(dictionary=True)

        #4. 쿼리문 만들고
        #dateform = ""
        query = """select name, description, num_of_servings, cook_time, directions, is_publish,
                DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%S') as created_at, 
                DATE_FORMAT(updated_at, '%Y-%m-%d %H:%i:%S') as updated_at
                from recipe Where id = %s;"""
        # DATE_FORMAT 을 사용할 때 시 분 초에서 %s 로 하지말고 %S 대문자로 해줘야지
        # mysql_connector 가 %s로 param 변수로 바꿀 때 에러가 나는 버그라고 함
        
        # It is a bug in the parser of MySQL Connector Python, 
        # which tries to substitute the %s in date_format function with a parameter. 
        # Due to this bug it expects 3 parameters in total
        # while only one parameter was specified in the parameter tuple.

        # As a work around you could specify the format parameter for seconds 
        # in date_format function in uppercase which should solve the problem: 
        # DATE_FORMAT(time, '%H:%i:%S')

        param = (recipe_id,)
        
        #5. 쿼리 실행
        cursor.execute(query, param)
        records = cursor.fetchall()
        
        #6. 커서, 커넥션 닫기
        cursor.close()
        connection.close()
        
        print(records)   
        #7. 실행 결과를 클라이언트에 보내준다 
        if len(records) == 0:
            return {'message': '해당 id가 없습니다.'}, 400

        # sql에서 쿼리로 DATE_FORMAT으로 변경 안한 경우는 for loop를 진행해서 json형태로 날짜를 변환해 준다
        # result = []
        # for row in records :
        #     row['created_at'] = row['created_at'].isoformat()
        #     row['updated_at'] = row['updated_at'].isoformat()
        #     result.append(row)
        
        #return {'count' : len(result), 'ret' : result[0]}
        return {'count' : len(records), 'ret' : records[0]}

    # put 메소드는 put은 postman에서 body부분에 보내야한다 raw-json형태로 보냄
    def put(self, recipe_id) :
        #업데이트 함수 작성
        #요리시간과 direction만 업데이트 할 수 있도록 해 주세요
        #요리시간과 direction은 필수값입니다.
        data = request.get_json()
        
        print(recipe_id)
        
    
        if len(data) <= 1 :
            return {'message': 'cook_time and directions are required'}, 400
        #또는
        # if 'cook_time' not in data or 'directions' not in data: 로 처리해도 됨
        
        else:
            connection = get_mysql_connection()
            cursor = connection.cursor(dictionary=True)
            query = """
                    UPDATE recipe SET cook_time=%s, directions=%s
                    WHERE id=%s;
                    """
            param = (data['cook_time'], data['directions'], recipe_id)
            cursor.execute(query, param)
            connection.commit()

            cursor.close()
            connection.close()
            
            if cursor.rowcount > 0:
                return {'cook_time': data['cook_time'],  
                        'directions': data['directions'],
                        'message': "성공적으로 변경되었습니다."
                        }, HTTPStatus.OK
            else :
                print ('오류가 발생하였습니다.')

    # delete는 postman에서 delete를 선택
    def delete(self, recipe_id) :
        connection = get_mysql_connection()
        cursor = connection.cursor()
        
        # 해당 id가 없을 경우 (이미 지워졌거나 없는 경우)
        query = """
                SELECT * FROM recipe WHERE id=%s;
                """
        param = (recipe_id, )
        cursor.execute(query, param)
        result = cursor.fetchall()
        if len(result) == 0:
            cursor.close()
            connection.close()
            return { 'message': "{} 에 해당하는 게시물이 없습니다.".format(recipe_id)}, HTTPStatus.NOT_FOUND

        query = """
                DELETE FROM recipe WHERE id=%s;
                """
        param = (recipe_id, )
        cursor.execute(query, param)
        connection.commit()

        cursor.close()
        connection.close()

        return { 'message': "성공적으로 지워졌습니다." }, 200



class RecipePublishResource (Resource):
    # is_publish를 1로 변경해주는 함수
    def put (self, recipe_id):
        connection = get_mysql_connection()
        cursor = connection.cursor()
        query = """
                UPDATE recipe SET is_publish = 1
                WHERE id = %s;
                """
        param = (recipe_id, )

        cursor.execute(query, param)
        connection.commit()
        cursor.close()
        connection.close()

        return {}, 200


    # is_publish를 0으로 셋팅 (db에서 지우는 것이 아님)
    def delete(self, recipe_id):
        connection = get_mysql_connection()
        cursor = connection.cursor()
        query = """
                UPDATE recipe SET is_publish = 0
                WHERE id = %s;
                """
        param = (recipe_id,)

        cursor.execute(query, param)
        connection.commit()
        cursor.close()
        connection.close()

        return {}, 200
