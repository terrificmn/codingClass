'''
#연습문제: 공배수 처리하기 
for i in range(1, 101):
    if i % 22 == 0: #또는 i % 2 == 0 and i % 11 = 0 도 됨
        print('FizzBuzz')
    elif i % 2 == 0:
        print('Fizz')
    elif i % 11 == 0:
        print('Buzz')
    else:
        print(i)
'''

# 퀴즈
#first, second = map(int, input().split())
first = 35
second = 40

for i in range(first, second+1): #범위의 마지막을 +1을 해서 마지막 최대치까지 반복
    if i % 35 == 0: 
    #if i % 5 == 0 and i % 7 ==0: #?(5와 7의 최소 공배수는 두개 5*7)
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Fizz")
    elif i % 7 == 0:
        print("Buzz")
    else:
        print(i)





