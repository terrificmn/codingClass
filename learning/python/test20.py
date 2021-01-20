'''
for i in range(1, 10):  # 마지막 범위(?)의 숫자까지는 포함안함에 유의 (9까지만 출력)
    print(i)
'''

'''
for i in range(1, 21):
    if i % 3 == 0:  # 3으로 나누어서 나머지가 0이면 3의 배수
        print(i, ': 3의 배수')
    elif i % 5 == 0:  # 5으로 나누어서 나머지가 0이면 5의 배수
        print(i, ': 5의 배수')
    else:
        print(i)
'''
#first, second = 35, 40
first, second = map(int, (input().split()))
for i in range(first, second+1):
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Fizz")
    elif i % 7 == 0:
        print("Buzz")
    else:
        print(i)
