#모듈은 py확장자를 가진 파이썬 파일들
#내장 모듈

#수학관련 모듈
'''
import math
#파이 
print(math.pi)
print(math.sqrt(4))
'''

'''
#모듈 별칭을 주기 as 별칭
import math as m 
print(m.pi) #원래는 math.pi 입력해야하지만 별칭으로 m.pi 

#특정 모듈 중에서 특정 기능만 사용할 경우
from math import pi, sqrt
print(pi) #바로 pi 라고만 입력해도 가능해짐
print(sqrt(3))

#특정 모듈에서 특정 기능만 사용하는데 그것도 별칭으로 사용할 경우
#오히려 축약으로 사용하는 것이 안좋을 수 있다
from math import sqrt as s
print(s(4))

#여러개 완전 별칭으로 사용
from math import pi as p, sqrt as s
print(s(4))
print(p)
'''

''' 안됨 이유 찾아볼 것
#특정 디렉토리에 들어가 있는 경우에 import사용
#urllib 는 디렉토리명이 됨 (urllib 디렉토리가 있음 .(점) 이후에는 파일명 request)
import urllib.request as url
#rep = urllib.request.urlopen('http://www.google.com')
rep = url.request.urlopen('http://www.google.com')
print(rep.status)
'''

'''
from urllib.request import Request, urlopen
req = Request('http://www.google.com')
response = urlopen(req)
response.status
'''

# requests는 외부모듈이어서 No module named 'requests'라고 못 찾음
# 터미널에서 설치를 해줘야지 사용할 수 있음
# pip install 모듈명 
# 위의 방식으로 설치해야함
#todo: 모듈 설치 공부해보기 vscode 버젼
import requests
r = requests.get('http://www.google.com')
print(r.status_code)
