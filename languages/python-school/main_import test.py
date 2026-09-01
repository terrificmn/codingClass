#같은 디렉토리에 있으면 파일명만 적어주면 되고, 확장자 .py는 적지 않는다.
'''
import square2

print(square2.base)
print(square2.square(10))
'''

# from 모듈명(파이썬파일 이름(확장자 빼고)) import 메소드1, 메소드2, ...
from square2_func import base, square
print(base)
print(square(10))

#import personcls
#james = personcls.Person('홍길동', 39, '인천')
#james.personcls.greeting()


#클래스 파일 import하기 
#from 모듈명(파일명 자체) import 클래스명 
from person_cls import Person
james = Person('홍길동', 39, '인천')
james.greeting()


