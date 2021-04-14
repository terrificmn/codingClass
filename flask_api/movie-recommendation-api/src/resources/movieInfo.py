from flask import request
from flask_restful import Resource
from http import HTTPStatus
from mysql.connector import Error

from db.db import get_mysql_connection
from utils.validations import val_number, val_pass_char

import pandas as pd
import numpy as np
import json 

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
        try:
            connection = get_mysql_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            # 카운트 수와  결과 리턴해 주기
            return { "count" : len(result),  "ret" : result }, HTTPStatus.OK

        except Error as e :
            print(str(e))
            return {'err_code': 20}, HTTPStatus.NOT_ACCEPTABLE
            # err_code : 20 db 에러, 또는 일치하는 회원없음


class MovieShow (Resource):
    # 내용 보여주기
    #@jwt_required()
    def get(self, title_id) :
        
        # title_id가 0번으로 들어오면 1로 표시해주기에서 에러 리턴으로 바꿈
        if title_id == 0 :
            #title_id = 1
            return { 'err_code' : 10 }, HTTPStatus.FORBIDDEN
            #err_code :10  0 입력 안됨 (영화 0번 없음) 

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

        try:
            connection = get_mysql_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, param)
            result = cursor.fetchall()
            cursor.close()
            connection.close()
        
            # 카운트 수와  결과 리턴해 주기
            return { "count" : len(result),  "ret" : result }, HTTPStatus.OK
        
        except Error as e :
            print(str(e))
            return {'err_code': 20}, HTTPStatus.NOT_ACCEPTABLE
            # err_code : 20 db 에러, 또는 일치하는 회원없음



class MovieFind (Resource):
    # 영화 검색
    #@jwt_required()
    def get(self, title):
        # 공백제거 및 소문자 변환
        title = title.strip(' ')
        title = title.lower()

        # offset/limit query param은 설정은 안했지만 디폴트값으로 설정
        offset = request.args.get('offset', default='0')
        limit = request.args.get('limit', default='25')

        query = """SELECT m.id, m.title, count(r.user_id) as cnt, CONVERT(CAST(avg(r.rating) AS DECIMAL (10,2)), CHAR) as average
                    FROM movie m
                    JOIN rating r
                    ON m.id = r.item_id
                    WHERE m.title like CONCAT('%', %s ,'%')
                    GROUP BY m.id
                    ORDER BY cnt DESC"""
        
        # offset, limit 붙이기, 쿼리 완성
        query += ' LIMIT ' + offset + ', ' + limit + ';'
        
        try:
            connection = get_mysql_connection()
            cursor = connection.cursor(dictionary=True)
            #print(query)
            param = (title, )
            cursor.execute(query, param)

            result = cursor.fetchall()
            cursor.close()
            connection.close()

            return { "count" : len(result),  "ret" : result }, HTTPStatus.OK
        
        except Error as e :
            print(str(e))
            return {'err_code': 20}, HTTPStatus.NOT_ACCEPTABLE
            # err_code : 20 db 에러, 또는 일치하는 회원없음



class MovieCreate (Resource):
    # 무비 별점
    @jwt_required()
    def post(self) :
        data = request.get_json()
        
        if 'rating' not in data or 'item_id' not in data :
            return {'err_code': 1}, HTTPStatus.BAD_REQUEST
            #err_code : 1 데이터가 없을 때 
        
        # 원래 json으로 숫자만 보내야하지만, 문자열 상태로 요청했을 때도 처리해줌
        for requestedData in data.values():
            # 숫자가 아니면 False 리턴
            if val_number(requestedData) == False:
                return {'err_code': 2}, HTTPStatus.BAD_REQUEST
                # err_code : 2 빈 값이 있을 때, # -1 도 숫자로 처리안함

        # 위에서 문자열로 들어왔을 경우 처리가 끝났으므로 int로 바꾸고 진행
        item_id = int(data['item_id'])
        rating = int(data['rating'])
        user_id = get_jwt_identity() # 토큰 변환

        # rating 숫자 limit 설정
        if rating < 0 or rating > 5 :
            return {'err_code': 11}, HTTPStatus.BAD_REQUEST

        # 해당 영화가 없음
        if item_id == 0:
            return {'err_code': 12}, HTTPStatus.BAD_REQUEST
            # 해당 영화가 없음

        query = """
                SELECT * FROM rating WHERE user_id = %s and item_id = %s;
                """
        try:
            param = (user_id, item_id)
            connection = get_mysql_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, param)
            result = cursor.fetchall()
            
            if (len(result) > 0 ) :
                return {'err_code': 13}, HTTPStatus.NOT_ACCEPTABLE
                # 이미 해당영화를 레이팅 함
                
        except Error as e :
            print(str(e))
            return {'err_code': 20}, HTTPStatus.NOT_ACCEPTABLE
            # err_code : 20 db 에러
        
        # 토큰으로 user_id 확인
        # titld_id 입력 (검색 후 title_id를 알고있다고 가정)
        # 본격 입력 부분!
        query = """
                INSERT INTO rating (user_id, item_id, rating) 
                VALUES (%s, %s, %s);
                """
        try:
            param = (user_id, item_id, rating) 
            cursor.execute(query, param)
            connection.commit()

            cursor.close()
            connection.close()
            return {}, 200

        except Error as e :
            print(str(e))
            return {'err_code': 20}, HTTPStatus.NOT_ACCEPTABLE
            # err_code : 20 db 에러



class MovieRecommend (Resource) :
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity() # 토큰 변환
        
        #일단 유저가 레이팅한게 있는지 확인
        query = """
                SELECT * FROM rating WHERE user_id = %s;
                """
        try:
            param = (user_id,)
            connection = get_mysql_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, param)
            result = cursor.fetchall()
                    
            if (len(result) == 0 ) :
                return {'err_code': 5}, HTTPStatus.NOT_ACCEPTABLE
                # 결과 없음 레이팅을 안함
        except Error as e :
            print(str(e))
            return {'err_code': 11}, HTTPStatus.NOT_ACCEPTABLE
            # err_code : 11 db 에러

        # 문제가 없을 시(별점 있을 시 진행)
        
        query = """SELECT m.title, r.rating
                FROM movie m
                JOIN rating r
                ON m.id = r.item_id
                WHERE user_id = {}""".format(user_id)
        
        # 판다스 df만들기
        user_ratings_df = pd.read_sql(query, connection)

        # movie_correlations.csv 불러오기, 불러오기에서 index_col=파라미터를 안주면 기본값 0,1,2....으로 나오는것에 주의!!
        movie_correlations_df = pd.read_csv('movie_correlations.csv', index_col='title')
        
        #데이터 프레임으로 만들어 주기
        recommended_movies_list = pd.DataFrame()
        #user의 df: user_ratings_df로 correlation 만들기
        for i in np.arange(0, len(user_ratings_df)):
            user_movie_title = user_ratings_df['title'][i]
            recommended_movies = movie_correlations_df[ user_movie_title ].dropna().sort_values(ascending=False).to_frame()
            recommended_movies.columns = ['correlation'] #컬럼명 바꾸기
            recommended_movies['weight'] = recommended_movies['correlation'] * user_ratings_df['rating'][i] # 가중치 계산
            recommended_movies_list = recommended_movies_list.append(recommended_movies)
        
        
        # # weight가 높은 것으로 정렬
        final_recommend = recommended_movies_list.sort_values(by='weight', ascending=False).head(10)
        result_json = final_recommend.to_json(orient="table")
        parsed = json.loads(result_json)
        # json_data = json.dumps(parsed, indent=4) # str로 되서 리턴하기 어려움
        
        return { "count" : len(parsed['data']) , "ret" : parsed['data'] }



