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


class Favorite (Resource) :
    @jwt_required()
    def post(self):
        data = request.get_json()
        if 'movie_id' not in data: 
            return {'err_code': 1}, HTTPStatus.BAD_REQUEST
            #err_code : 1 데이터가 없을 때 
        
        try:
            user_id = get_jwt_identity()

            connection = get_mysql_connection()
            cursor = connection.cursor()
            query = """ INSERT into favorites 
                        (liked_movie, user_id)
                        VALUES (%s, %s);
                    """
            param = (data['movie_id'], user_id)
            cursor.execute(query, param)
            connection.commit()

            cursor.close()
            connection.close()
            # 성공 토큰 응답하기, 201 # 바로 로그인 가능하게 토큰 응답
            return {}, 201

        except Error as e :
            print(str(e))
            return {'err_code': 10}, HTTPStatus.NOT_ACCEPTABLE


    # 즐겨찾기 지우기
    @jwt_required()
    def delete(self, title_id):
        try:
            user_id = get_jwt_identity()
            connection = get_mysql_connection()
            cursor = connection.cursor()

            query = """ SELECT * FROM favorites 
                        WHERE liked_movie = %s and user_id = %s;"""
            param = (title_id, user_id)
            cursor.execute(query, param)
            result = cursor.fetchall()

            if len(result) == 0 :
                return {'err_code': 10}, HTTPStatus.NOT_ACCEPTABLE
                #err_code :10 일치하는 데이터 없음

            # 조건에 맞는게 없더라도 에러가 발생하지를 않는다;;; 그래서 위에서 select추가
            # 이제 조건에 맞으면 아래 수행
            query = """ DELETE FROM favorites 
                        WHERE liked_movie = %s and user_id = %s;"""

            param = (title_id, user_id)
            cursor.execute(query, param)
            connection.commit()

            cursor.close()
            connection.close()
            # 성공 토큰 응답하기, 201 # 바로 로그인 가능하게 토큰 응답
            return {}, HTTPStatus.ACCEPTED

        except Error as e :
            print(str(e))
            return {'err_code': 10}, HTTPStatus.NOT_ACCEPTABLE


    # 즐겨찾기 불러오기
    @jwt_required()
    def get(self):
        #헤더 토큰으로 아이디 파악
        user_id = get_jwt_identity()
        offset = request.args.get('offset', default='0')
        limit = request.args.get('limit', default='25')

        try:
            connection = get_mysql_connection()
            cursor = connection.cursor(dictionary=True)

            query = """ SELECT m.title, u.name 
                        FROM favorites f
                        JOIN movie m
                        ON f.liked_movie = m.id
                        JOIN user u
                        ON u.id = f.user_id
                        WHERE u.id = %s;"""
            # offset, limit 붙이기, 쿼리 완성
            query += ' ORDER BY m.title ASC LIMIT ' + offset + ', ' + limit + ';'
            
            param = (user_id, )
            cursor.execute(query, param)
            result = cursor.fetchall()
            return { 'count': len(result), 'ret': result }, 200

        except Error as e :
            print(str(e))
            return {'err_code': 10}, HTTPStatus.NOT_ACCEPTABLE
