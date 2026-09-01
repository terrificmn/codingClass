# parameter 하나만 써서 여러개 받기
# 파라미터가 몇개가 들어올지 확실치 않는 경우에는 parameter변수앞에 *을 붙여준다
def avg(*param):
    return sum(param)/len(param)


kor, eng, com = 100, 90, 80
print(avg(kor, eng, com))

# 몇개가 args로 인수로 넘어올 지 모르는 상황에서 파라미터와 아규먼트 갯수를 맞춰주지 않으면
# 에러가 발생하므로 아규먼트를 많이 넘겨줄 때 함수를 정의할 때 파라미터 앞에 *을 넣기


def printf(*param):
    # 넘겨받은 인수 만큼 반복시키면서 출력하기
    for i in param:
        print(i, end=' ')
    print()


# 함수를 호출하면서 인수를 맞춰주지 못하는 경우 (모르거나, 아무 많을 때(무한정 파라미터를 만들 수 없기 때문에))
# 몇개든 ok, 단 함수의 파라미터는 *을 붙여야 한다
printf(1, 3, 4, 5, 6)  # 인수가 5
printf(1, 2)  # 인수 2
printf(1, 3, 4, 5, 6, 7, 8, 0)  # 인수 8

# unpacking 하기 , 파라미터에서 몇개가 넘어올지 모르는 위의 상황이랑은 반대로
# arguments에서 몇개를 넘겨줄지 모르는 상황에 변수앞에 *을 붙여서 함수를 호출한다


def calc(a, b, c):
    return (a+b+c, a*b*c)


# 이때 calc()함수는 3개의 파라미터가 있으므로 a,b,c 이렇게 3개를 넘겨야하는데
# 아래처럼 리스트에 요소가 3개 담겨 있는데 이거를 x변수만 넘길 때 가변인수를 사용한다
x = [1, 2, 3]
# 그냥 함수 호출하면서 인수를 넘기면 에러발생
# ? print(calc(x))
# 이런식의 에러가 발생 calc() missing 2 required positional arguments: 'b' and 'c'
# 즉, 2개의 인수가 필요하다는 것 b, c를 넘겨라
# 하지만 x리스트 변수에 3개의 요소가 들어가 있을 때 x변수 앞에 *을 붙여서 함수를 호출하는 것이
# 가변인수 임
print(calc(*x))

# 가변파라미터와 unpacking을 딕셔너리 변수일 때는
# 함수와 함수호출에서도 (**변수)가 되어야한다.
# 즉, 함수에서는 몇개가 넘어올 지 모르니깐 가변파라미터를
# 함수호출시에 인수를 딕셔너리로 넘기므로 unpacking을 하기위해 *을 붙여주는데
# 딕셔너리는  **을 두번 붙여야지 딕셔너리 변수로 넘어온 값의 key, value를 잘 넘겨받을 수 있음


def printout(**paramDict):
    for key, value in paramDict.items():
        print("key이름: ", key, ", value값: ", value)


p = {'name': '홍길동', 'age': 20, 'address': '인천'}

# 함수 호출 (가변인수)
printout(**p)
