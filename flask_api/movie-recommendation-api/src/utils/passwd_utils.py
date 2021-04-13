from passlib.hash import pbkdf2_sha256
from config.config import salt  # 비밀번호 암호화에 추가로 문자열을 추가

# 회원가입 유저의 비밀번호를 암호화
def hash_password(password):
    #암호화를 솥트 SALT 로 추가로 더 문자열을 추가해준다
    return pbkdf2_sha256.hash(password + salt)

# 로그인 할 때 유저의 비번과 db의 비번 확인
def check_password(password, hashed_password):
    return pbkdf2_sha256.verify(password + salt, hashed_password)
