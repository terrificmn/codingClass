from flask import Flask
from flask_restful import Api

from config.config import Config
from resources.user import UserResourceRegister, UserResourceLogin, UserResourceLogout, jwt_blocklist, UserMeInfo

from resources.movieInfo import MovieIndex, MovieShow, MovieFind, MovieCreate, MovieRecommend
from resources.favorites import Favorite

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

VER = '/v1'

# 회원가입 (post)
api.add_resource(UserResourceRegister, VER+'/users/register')

# 로그인 (post)
api.add_resource(UserResourceLogin, VER+'/users/login')
# 로그아웃 (post)
api.add_resource(UserResourceLogout, VER+'/users/logout')

# 벌졈이나 리뷰순으로 보여주기
api.add_resource(MovieIndex, VER+'/movies/index/<type>', VER+'/movies/index/<type>/<order>')

# 영화 리뷰정보 보여주기
api.add_resource(MovieShow, VER+'/movies/show/<int:title_id>')

# 영화 검색
api.add_resource(MovieFind, VER+'/movies/find/<title>')

# 영화 별점 포스팅
api.add_resource(MovieCreate, VER+'/movies/create')

# 영화 추천받기
api.add_resource(MovieRecommend, VER+'/movies/recommend')


# 내 정보 가져오기
api.add_resource(UserMeInfo, VER+'/users/me')

# 즐겨찾기 추가 / 삭제
api.add_resource(Favorite, VER+'/favorites', VER+'/favorites/<int:title_id>')


if __name__ == "__main__" :
    app.run()
