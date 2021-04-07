from flask import request
from flask_restful import Resource
from http import HTTPStatus
from utils import hash_password, check_password
from db.db import get_mysql_connection
#from email_validator import validate_email, EmailNotValidError
from reg_email import validation
from mysql.connector import Error

class UserListResource(Resource) :
    def post(self) :
        data = request.get_json()

        # 0. 데이터가 전부 다 있는지 체크
        if 'username' not in data or 'email' not in data or 'password' not in data :
            return {'err_code': 1}, HTTPStatus.BAD_REQUEST
            # err_code는 회사마다 다름, 여기에서는 임의로 줌
        
        # 1. 이메일 유효한지 체크
        #라이브러리 email-validator
        val_result = validation(data['email'])
        if val_result == False:
            return {'err_code': 3}, HTTPStatus.BAD_REQUEST
        
        # try:
        #     # Validate.
        #     validate_email(data['email'])

        # except EmailNotValidError as e:
        #     # email is not valid, exception message is human-readable
        #     print(str(e))
        #     return {'err_code': 3}, HTTPStatus.BAD_REQUEST

        # 2. 비밀번호 길이 체크 및 암호화
        if len(data['password']) < 4 or len(data['password']) > 16 :
            return {'err_code': 2}, HTTPStatus.BAD_REQUEST

        hashed_password = hash_password(data['password'])

        # 3. 데이터베이스에 저장
        try:
            connection = get_mysql_connection()
            cursor = connection.cursor()
            query = """ INSERT INTO user (username, email, password)
                        VALUES (%s, %s, %s);
                    """
            param = (data['username'], data['email'], hashed_password)
            cursor.execute(query, param)
            
        except Error as e :
            return {'err_code': str(e)}, HTTPStatus.NOT_ACCEPTABLE
            # 실제로는 에러코드 자체를 클라이언트한테 보여주면 안됨, 숫자코드만 보여주기
            # 악용될 수 있음, print(e)로만 처리하는게 좋을 수 있음

        connection.commit()

        cursor.close()
        connection.close()

        return {}, 200

class UserResource (Resource):
    def post(self):
        # 요청받은 데이터 저장
        data = request.get_json()
        email = data['email']
        password = data['password']

        try:
            #이메일 검증
            val_result = validation(email)
            if val_result == False:
                return {'err_code': 3}, HTTPStatus.BAD_REQUEST

            #DB연결
            connection = get_mysql_connection()
            cursor = connection.cursor()
            query = """ 
                        SELECT password FROM user 
                        WHERE email = %s;
                    """
            param = (email,)

            # db에서 가져오기
            cursor.execute(query, param)
            result = cursor.fetchone()
            if result is None :
                print ('no user')
                return {"err_code" : 5 }, HTTPStatus.NOT_ACCEPTABLE
            else:
                # 암호화된 패스워드와 다르면 에러코드 리턴
                res = check_password(password, result[0])
                if res == False: 
                    return {"err_code" : 6 }, HTTPStatus.NOT_ACCEPTABLE
                else:
                    return {'login': 'successful' }
            
            
        except Error as e :
            return {'err_code': str(e)}, HTTPStatus.NOT_ACCEPTABLE

        #연결 종료
        cursor.close()
        connection.close()