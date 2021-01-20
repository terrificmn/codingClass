#function 정의
def hello():
    print('hello world')

hello()

'''
#parameter 변수1, 변수2로 정의하면 됨
#파라미터로 받은 값과 아규먼트로 넘겨준 인수 각 변수의 이름은 같으나 서로 다르다
#? 함수에서 정의된 변수는 함수내에서만 사용할 수 있다
def add(a, b):
    print(a + b)

#입력 받아서 함수 호출
a ,b = map(int,input().split())
add(a, b)
'''

# return하기 
def add(a, b):
    sum = a + b
    return sum

# 함수 호출한 후에 리턴 받은 값을 출력
print(add(10, 20))

# *상황에 따라 return으로 아무값도 반환안할 수도 있다 (break 처럼 함수의 실행이 끝남)
def ten(a):
    if a == 10:
        return  #? 그냥 return을 하게되면 None값을 리턴한다
    print(a)

ten(5)

#* 함수에서 리턴을 2개 이상 할 수 있음
#? 여기에서 리턴은 ()나 []로 묶어서 여러개 리턴 가능
#? 예: return (1, 2, 3) 또는 return [1, 2, 3]
def add_sub(a,b):
    return a+b, a-b

# 함수 호출 후 리턴값 2개 받아서 각 변수에 할당
x, y = add_sub(20, 10)
print('더하기: ', x)
print('빼기: ', y)

def number(a, b, c):
    print(a)
    print(b)
    print(c)

number(1, 2, 3)


x = [1, 2, 3]
#*unpacking 하기 
# 함수 호출 할 때는 arguments의 갯수 맞춰서 호출해야하는데 한개의 변수만 넘길 때는 
#* 변수 앞에 *을 넣은 후에 호출하면 함수의 파라미터에 맞춰서 넘겨준다
# 단, argument로 넘길 변수의 요소가 함수 파라미터와 같아야 한다
#number(x)  이렇게 하면 에러
number(*x)

#가변인수의 예 print함수, args가 몇개를 받을지 모르지만 가변으로 넘길 수 있음
print(1,2,3,4,5,6,7,8,9,10)

#* 가변인수는 몇개를 넘길 지 모르기 때문에
#* 함수의 파라미터를 무한대로 만들 수 는 없기 때문에 
#* 파라미터 변수 앞에 *을 넣어준 후에 함수 내에서 for문으로 반복하면서 처리함
# 함수를 호출할 때는 가변으로 arguments를 넘겨도 된다
def number2(*args):
    for i in args:
        print(i)

#가변인수로 호출 // 함수 내에서는 파라미터가 *변수로 정의되어 있어서 가능하다
number2(1, 2, 3, 4, 5, 6, 8)

print("------------------------------")

#가변인수롤 넘기기, 원래는 unpacking한 요소 개수와 함수의 파라미터 개수가 같아야 하지만
# (별) *을 붙여서 args를 넘기게 되면 문제 없이 처리가 된다 (함수내에서 파라미터도 *을 넣어 정의되 있음)
x = [10, 20, 30, 40, 50]
number2(*x)


def per(name, age, address):
    print(name)
    print(age)
    print(address)

per('홍길동', 30, '서울')

print()
#? 딕셔너리를 구조를 이용해서 함수를 호출할 수도 있다
#? 딕셔너리 변수를 넘길 때 앞에 **을 두번 쓴다
#? **을 써야지 함수의 파라미터에 받는 변수랑 딕셔너리의 key값의 이름이 가변인수로 넘어가게 된다
p = {'name':'홍길동', 'age': 20, 'address': '인천'}
per(**p)

#* 딕셔너리에서 가변파라미터로 받으려면 ** (2번) 적어준다 
#* 딕셔너리로 받을 경우
def per2(**kwargs):
    for key, value in kwargs.items():
        print(key, " ", value)

#언패킹을 2번 해줘야지 딕셔너리의 키로 넘어감
p = {'name':'홍길동', 'age': 20, 'address': '인천'}
per2(**p)

#함수의 파라미터 기본값 설정하기 
#변수에 값을 넣어주면된다 
# 그리고 함수를 호출할 때 args를 안 넘기면 기본값으로 넣은 값이 처리된다
def per3(name, age, addr='비공개'):
    print(name)
    print(age)
    print(addr)
#인수를 넘길 때는 기본값으로 설정된 파라미터에 해당하는 args는 안 넘기면 됨
per3('둘리', 10000)

