# while문의 기본 구조
'''
i = 0
while i < 100:
    print('Hello, world!')
    i += 1
'''
'''
# whlie문에서  input 받은 수 만큼 반복하기
# 중간에 혹시 모를 에러에 대비 break 넣기
count = int(input('횟수를 입력하세요: '))
i = 0
while i < count:
    if count > 100:
        break #for문 빠져나가기 
    print('Hello, world!', i)
    i += 1
'''
'''
# import random random 함수를 사용하기 위해서  random 모듈 불러오기

import random
ran = random.randint(1, 6)  # randint()는 시작, 끝의 파라미터 사이의 랜덤으로 수 생성
print(ran)  # 실행할 때 마다 다른 수가 출력됨

# random.choice()를 사용하면 리스트, 튜플, range, 문자열 등의 시퀸스 객체에서 무작위 숫자를 선택함
ran2 = list([1, 2, 3, 4, 5])  # list
ran_str = "Hello, friend!"
print(random.choice(ran2))  # 리스트에서 랜덤
print(random.choice(ran_str))  # 문자열에서 랜덤으로 출력
'''

# 퀴즈
#bal = 13500
bal = int(input())
while bal >= 1350:
    bal -= 1350
    print(bal)
