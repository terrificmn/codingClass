from flask import request
from flask_restful import Resource
from http import HTTPStatus

from db.db import get_mysql_connection

# JWT 라이브러리
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt



class MovieIndex(Resource) :

    # movie 별점 / 조회수 보여주기
    #@jwt_required()
    def get(self, type, order='DESC') :

        offset = request.args.get('offset', default='0')
        limit = request.args.get('limit', default='25')

        # 에러 처리
        # type 파라미터가 지정된 값이 아니면 false로 에러 리턴하기
        if type.lower() != "review_cnt" and type.lower() != "star_cnt" :
            return { 'err_code' : 8 }, HTTPStatus.BAD_REQUEST
            # err_code : 8 get 방식 패스 파라미터 확인 : review_cnt or star_cnt 만 가능
        
        # order파라미터는 기본값이 있으므로 desc 나 asc가 아닌 값이 들어오면 에러발생
        if order.lower() != "desc" and order.lower() != "asc" :
            return { 'err_code' : 9 }, HTTPStatus.BAD_REQUEST
            # err_code : 9 get 방식 패스 파라미터 확인 : 생략가능하나 다른값은 안됨

        # 기본 쿼리
        query = """SELECT m.title, count(r.user_id) as cnt, CONVERT(CAST(avg(r.rating) AS DECIMAL (10,2)), CHAR) as average
                    FROM movie m
                    JOIN rating r
                    ON m.id = r.item_id
                    GROUP BY m.id """

        # type 리뷰 카운트 기준 order asc일때 오름차순 정렬
        if type == 'review_cnt' :
            if order == 'asc' :
                query += 'ORDER BY cnt ' + order 
            else :
                query += 'ORDER BY cnt ' + order #아니면 기본값 DESC

        # type 별점 카운트 기준 order asc일때 오름차순
        if type == 'star_cnt' : 
            if order == 'asc':
                query += 'ORDER BY average ' + order 
            else :
                query += 'ORDER BY average ' + order #아니면 기본값 DESC
        
        
        # offset, limit 붙이기, 쿼리 완성
        query += ' LIMIT ' + offset + ', ' + limit + ';'
                
        # #print(query)
        connection = get_mysql_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        
        # 카운트 수와  결과 리턴해 주기
        return { "count" : len(result),  "ret" : result }, HTTPStatus.OK


class MovieShow (Resource):
    
    #@jwt_required()
    def get(self, title_id) :
        print('안녕')

        # title_id가 0번으로 들어오면 1로 표시해주기
        if title_id == 0 :
            title_id = 1

        offset = request.args.get('offset', default='0')
        limit = request.args.get('limit', default='25')

        query = """SELECT m.title, u.name, u.gender, r.rating
                    FROM movie m
                    JOIN rating r
                    ON m.id = r.item_id
                    JOIN user u
                    ON u.id = r.user_id
                    WHERE m.id = %s"""

        # offset, limit 붙이기, 쿼리 완성
        query += ' LIMIT ' + offset + ', ' + limit + ';'
        param = (title_id,)

        #print(query)
        connection = get_mysql_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, param)
        result = cursor.fetchall()
        
        # 카운트 수와  결과 리턴해 주기
        return { "count" : len(result),  "ret" : result }, HTTPStatus.OK


class MovieFind (Resource):
    def get(self, title):
        
        query = """SELECT * 
                    FROM movie m
                    JOIN rating r
                    ON m.id = r.item_id
                    WHERE m.title like '%%s%'"""

        connection = get_mysql_connection()
        cursor = connection.cursor(dictionary=True)
        
        파라미터 %s 해결하기
        param = (title, )
        cursor.execute(query, param)

        result = cursor.fetchall()

        return { "count" : len(result),  "ret" : result }, HTTPStatus.OK