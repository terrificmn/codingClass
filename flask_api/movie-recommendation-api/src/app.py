from flask import Flask
from flask_restful import Api

from config.config import Config
from resources.user import UserResourceRegister, UserResourceLogin, UserResourceLogout, jwt_blocklist

from resources.movieInfo import MovieIndex, MovieShow, MovieFind

#JWT용 라이브러리
from flask_jwt_extended import JWTManager

app = Flask(__name__)  # flask 기본구조

# 1. 환경 변수 설정
app.config.from_object(Config) #Config 클래스 불러오기

# JWT 환경설정 / 로그인/로그아웃을 위함
jwt = JWTManager(app)
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload) :
    jti = jwt_payload['jti']
    return jti in jwt_blocklist  #blocklist가 없으므로 user.py에 만들어 준다


# 2. api 설정
api = Api(app)

# 회원가입 (post)
api.add_resource(UserResourceRegister, '/v1/users/register')

# 로그인 (post)
api.add_resource(UserResourceLogin, '/v1/users/login')
# 로그아웃 (post)
api.add_resource(UserResourceLogout, '/v1/users/logout')

# 벌졈이나 리뷰순으로 보여주기
api.add_resource(MovieIndex, '/v1/movies/index/<type>', '/v1/movies/index/<type>/<order>')

# 영화 리뷰정보 보여주기
api.add_resource(MovieShow, '/v1/movies/show/<int:title_id>')

# 영화 검색
api.add_resource(MovieFind, '/v1/movies/find/<title>')
if __name__ == "__main__" :
    app.run()
