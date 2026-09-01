import random

#print(random.random()) #소수점 이하 랜덤으로 받음
#randint(시작, 끝) 2개의 arguments에서 1, 6 사이의 숫자에서만 랜덤으로 만들어준다
#print(random.randint(1, 6)) 


i = 0 
#i가 3이 아니면 true, 3이면 false
while i != 3:
    #i에 랜덤으로 수 생성해서 넣어준다
    i = random.randint(1, 6)
    print(i)


lotto = [11, 23, 35, 43, 53, 67, 83]
# random.choice()는  리스트에서 랜덤으로 선택해서 반환
print(random.choice(lotto))

#로또 번호 만들기 while문 사용
i = 6 #6번 만들기 위해서 변수에 넣어줌
while i:
    #random.randint(시작숫자, 끝숫자) 2개 아큐먼트 사이에서 랜덤으로 숫자 만듬
    print(random.randint(1, 45), end= " ")
    i -= 1 #-1을 해줘서 6번만 반복되서 0이면 되면 false로 빠져나갈 수 있게 함

