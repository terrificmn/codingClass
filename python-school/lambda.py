#람다 표현식

#보통 함수는 이름이 있고 아래와 같은 형식으로 사용되는데 람다 함수는 이름없는 함수 정의가 가능하다
def plus(x):
    return x + 10

print(plus(10))

#람다 함수는 바로 변수에 할당해서 사용하면 된다
#lambda라고 쓰고 리턴할 값을 써줌 
'''
plusLambda = lambda x: x + 10
print(plusLambda)
'''

# 변수에 람다함수로 정의해서 만들었기 때문에 바로 사용할 수 있으며
# map()함수로 묶어주는데 람다함수로 호출해서 뒤의 리스트값을 넘겨줘서 결과를 받게 된다
'''
list = list(map(plusLambda,[1,2,3]))
print(list)
'''

'''
#위의 것과 같은 것, 람다표현식으로 바로 사용함
list = list(map(lambda x: x + 10, [1, 2, 3]))
print(list)
'''
'''
a = [1,2,3,4,5,6,7,8,9,10]
list = list(map(lambda x: str(x) if x % 3 == 0 else x,a))
print(list)
'''

#람다를 이용해서 리스트로 만들기
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
#각 a,b리스트에서 x, y로 넘기고 x+y를 람다함수가 리턴해준것을 리스트로 만들어 준다
l1 = list(map(lambda x,y: x+y, a, b))
print(l1)

#filter함수와 람다함수 이용해서 조건에 맞는 수만 뽑아오기
# 람다함수만 사용하면 원래 if문도 넣어줘야하는데 
# filter()함수를 사용하면 if문이 없이 가능해진다
a = [4, 5, 6, 7, 8, 9, 3, 4, 2, 10]
list = list(filter(lambda x: x > 5 and x < 10, a))
print(list)

#reduce 모듈 불러와서 reduce를 람다함수와 같이 사용해서 
# 리스트내의 모든 수를 더하는 연산을 할 수 있음
from functools import reduce
a = [1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda x, y: x+y, a))

