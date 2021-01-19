'''
#** 2차원 리스트는 [대괄호]안에 또 [대괄호]를 넣어준다
a = [[10, 20],
    [30, 40],
    [50, 60]]
print(a)
print(a[0][0]) #?0번째 배열의(1차원의 첫번째) 2차원의 0번째 값(2차원의 1번째값)
print(a[0][1]) #?0번째 배열의(1차원의 첫번째) 2차원의 1번째 값(2차원의 2번째값)

#pprint import해서 사용 
#import를 해야함
#pprint(a, indent = 4, width=20)

#*2가지 변수로 2개요소를 접근할 수 있다
#*a리스트에서 x는 1차원배열 y는 2차원배열에 대입해서 사용할 수 있다
for x, y in a:
    print(x, y) #즉 [0][0]과 같은 결과

#? 위의 결과랑 같은 결과를 냄
for i in a:
    for j in i: #a list의 i의 값이 jdp에 넣어주면 값이 2차원의 내용이 됨
        print(j, end=" ")
    print()

#? 위의 결과랑 같은 결과를 냄
for i in range(len(a)): #a list의 길이는 3
    for j in range(len(a[i])): #다시 a의 1차원배열에는 2차원배열이 들어가 있으므로 2
        print(a[i][j], end='')
    print()

print('-----------------')

i = 0
while len(a) > i:
    #! 파이썬에서는 2개의 변수에 (혹은 여러개) 한번에 넣어줄 수 있다
    x, y = a[i] #! a i번째 배열에는 2차원 배열 2개가 들어가 있음, x와 y에 각각 넣어줄 수 있다
    print(x, y, end=' ')
    i += 1
    print()

print()
#? 위의 while문과 같은 결과 
i = 0
while i < len(a):
    j = 0 #초기 값 설정에 주의!!
    while j < len(a[i]):
        print(a[i][j], end=' ')
        j += 1
    i += 1
    print()


#* 1차원 리스트 만들기
a1 = [] #list 만들기
for i in range(10):
    a1.append(i)

print(a)

#* 2차원 리스트 만들기
a2 = [] #? 1차원배열 사용할 리스트 변수 만들기
for i in range(3):
    b = [] #? 2차원배열로 사용할 리스트 정의
    for j in range(2):
        b.append(j) #? 단순하게 j가 반복되는 동안 b리스트에 append()메소드를 이용해서 추가해 준다
    a2.append(b) #? 1차원 배열에 다시 b 리스트를 넣어준다, 그러면 2차원배열 완성!

print(a2)

print("--------------------------------------")
#[대괄호]안에 다시 [대괄호]를 넣어주면 바로 2차원 배열로 만들어 진다
a = [[i, i] for i in range(3)]
print(a)
# 이중 for문으로 2차원리스트 만들기
# 0은 들어갈 데이터를 의미 [첫번쨰 대괄호 [2번째 대괄호안에 두번째 j for문을 써준다]
# 첫번째 대괄호 나머지 부분은 i for문을 써 준다
a = [[0 for j in range(2)] for i in range(3)]
print(a)

# for문 한번으로 2차원 배열 만들기 (들어갈 값을 *2 해줌)
a = [[0] * 2 for i in range(3)]

'''

a = [[10, 20],
    [30, 40],
    [50, 60]]

b = a #주소만 복사 됨, b변수에 a를 넣어주면 복사가 되나 주소만 가지고 있음
print(id(a))
print(id(b))
import copy #copy모듈 
b = a.copy() # copy()메소드를 사용하면 b를 새롭게 만들어서 복사해줌
print(id(a))
print(id(b)) #서로 다른 주소를 가지게 됨





