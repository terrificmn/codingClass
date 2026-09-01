'''
for i in range(10):  # 10까지 반복 0~9까지
    print(i, end=' ')
    i = 10  # i 변수는 (다른 언어랑 다른 듯, for문 반복되는것에서 영향을 주지 못함)

# 문자열 문자열 시퀸스 객체 (문자열 반복)
for letter in 'Who said Python is easy!': #letter 대신 i도 됨
    print(letter, end=' ')
'''

'''
# 시작, 끝 지정 (0번째가 아님에 주의!, 시작이 4이면 4부터)
# range(10) 이런식으로 할 경우에는 0부터 9까지 (10개)
for i in range(4, 10):
    print(i)
'''

'''
# 연습문제
x = [49, -17, 25, 102, 8, 62, 21]

for i in x:
    print(i * 10, end=" ")

'''

# 퀴즈

goo = int(input())
for i in range(1, 10):  # 마지막은 포함 안함
    print(goo, '*', i, '=', goo * i)
