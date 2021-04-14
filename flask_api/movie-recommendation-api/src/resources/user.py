from flask import request
from flask_restful import Resource
from http import HTTPStatus

from db.db import get_mysql_connection
from email_validator import validate_email, EmailNotValidError

from mysql.connector import Error

from utils.validations import val_empty, passwd_length, val_pass_char
from utils.passwd_utils import hash_password, check_password

# JWT 라이브러리
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt

# 로그아웃 기능 구현
from flask_jwt_extended import get_jti
jwt_blocklist = set()  #app.py에서 import


class UserResourceRegister(Resource) :
    def post(self) :
        data = request.get_json()

        # 데이터가 전부 다 있는지 체크
        if 'email' not in data or 'password' not in data or 'name' not in data or 'gender' not in data :
            return {'err_code': 1}, HTTPStatus.BAD_REQUEST
            #err_code : 1 데이터가 없을 때 

        # 공백 오류 찾아내기
        temp_list = []
        for requestedData in data.values():
            # 공백 있으면 False 리턴
            val_result = val_empty(requestedData)
            if val_result == False:
                return {'err_code': 2}, HTTPStatus.BAD_REQUEST
                # err_code : 2 빈 값이 있을 때

        # 변수에 저장 (공백 제거)
        email = data['email'].strip(' ')
        password = data['password'].strip(' ')
        name = data['name'].strip(' ')
        gender = data['gender'].strip(' ')
        
        # 이메일 검증
        try:
            validate_email(email)
        except EmailNotValidError as e:
            print(str(e))
            return {'err_code': 3}, HTTPStatus.BAD_REQUEST
            # err_code : 3 이메일 검증 실패

        # 비밀번호 길이 체크 및 암호화
        if passwd_length(password) == False:
            return {'err_code': 4}, HTTPStatus.BAD_REQUEST
            # err_code : 4 비밀번호 길이 오류
        
        # 비밀번호 특수기호 포함
        if val_pass_char(password) == False:
            return {'err_code': 5}, HTTPStatus.BAD_REQUEST
            # err_code : 4 특수기호 1개 이상 포함

        hashed_password = hash_password(password)

        # 데이터베이스에 저장
        try:
            connection = get_mysql_connection()
            cursor = connection.cursor()
            query = """ INSERT INTO user (email, password, name, gender)
                        VALUES (%s, %s, %s, %s);
                    """
            param = (email, hashed_password, name, gender)
            cursor.execute(query, param)
            connection.commit()

            # db입력 후 마지막 id값 받아오기
            user_id = cursor.lastrowid
            access_token = create_access_token(identity=user_id) # 토큰 만들기
            cursor.close()
            connection.close()
            # 성공 토큰 응답하기, 201 # 바로 로그인 가능하게 토큰 응답
            return {'token' : access_token }, 201

        except Error as e :
            print(str(e))
            return {'err_code': 20}, HTTPStatus.NOT_ACCEPTABLE


# 로그인

class UserResourceLogin (Resource):
    # 로그인 post방식 API
    def post(self):
        data = request.get_json()
        if 'email' not in data or 'password' not in data:
            # 데이터가 없는 경우
            return {'err_code': 1}, HTTPStatus.BAD_REQUEST
            #err_code : 1 데이터가 없을 때 

        # 요청받은 데이터 저장    
        email = data['email'].strip(' ')
        password = data['password'].strip(' ')

        # 이메일 검증
        try:
            validate_email(email)
        except EmailNotValidError as e:
            print(str(e))
            return {'err_code': 3}, HTTPStatus.BAD_REQUEST
            # err_code : 3 이메일 검증 실패

        #DB연결
        connection = get_mysql_connection()
        cursor = connection.cursor()
        query = """ 
                    SELECT id, password FROM user
                    WHERE email = %s;
                """
        param = (email,)

        try :
            # db에서 가져오기
            cursor.execute(query, param)
            result = cursor.fetchone()
            
            #연결 종료
            cursor.close()
            connection.close()
        except Error as e :
            print(str(e))
            return {'err_code': 20}, HTTPStatus.NOT_ACCEPTABLE
            # err_code : 20 db 에러
        
        # 등록된 이메일이 없을 경우
        if result is None :
            print ('no user')
            return {"err_code" : 6 }, HTTPStatus.NOT_ACCEPTABLE
            # err_code : 6 email 유저가 없을 시 에러
        else:
            # 암호화된 패스워드와 다르면 에러코드 리턴
            res = check_password(password, result[1])  #[1]이 password
            if res == False: 
                return {"err_code" : 7 }, HTTPStatus.NOT_ACCEPTABLE
                # err_code : 7 패스워드 틀림
            else:
                # 유저 토큰을 만들어 준다
                user_id = result[0] #[0] id
                #print(user_id)
                access_token = create_access_token(identity=user_id)
                return {'token': access_token }, HTTPStatus.OK



# 로그아웃 API 만들기

class UserResourceLogout (Resource):
    @jwt_required()
    def post(self):
        # 매뉴얼상 나와있는 것 로그아웃시 
        jti = get_jwt()['jti']
        jwt_blocklist.add(jti)

        return { }, 200


class UserMeInfo (Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity() # 토큰 변환

        query = """
                SELECT u.email, u.name, u.gender, m.title, r.rating
                FROM movie m
                JOIN rating r
                ON m.id = r.item_id
                JOIN user u
                ON u.id = r.user_id
                WHERE u.id = %s; """
        try:
            param = (user_id,)
            connection = get_mysql_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, param)
            result = cursor.fetchall()
                    
            if (len(result) == 0 ) :
                query = """
                SELECT email, name, gender  
                FROM user u
                WHERE id = %s; """
                
                param = (user_id,)
                connection = get_mysql_connection()
                cursor = connection.cursor(dictionary=True)
                cursor.execute(query, param)
                result = cursor.fetchall()
                return { 'review' : 0, 'ret' : result }, HTTPStatus.OK
                # return {'err_code': 5}, HTTPStatus.NOT_ACCEPTABLE
                # 결과 없음 리뷰 없음에서 회원정보만 보여주는 것으로 변경
            else:
                return { 'count' : len(result), 'ret': result }, 200
            
        except Error as e :
            print(str(e))
            return {'err_code': 20}, HTTPStatus.NOT_ACCEPTABLE
            # err_code : 20 db 에러, 일치하는 회원없음
