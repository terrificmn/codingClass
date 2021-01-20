x, y = map(int, input().split())
#x = 10
#y = 20

def calc(x, y):
    #리턴은 여러개로 ()로 묶어서 리턴 가능하다
    return (x+y, x-y, x*y, float(x/y))

#함수를 호출하고 리턴받은 값을 각 변수에 할당 해준다
a, s, m, d = calc(x, y)

#format()메소드를 이용해서 각 변수의 값을 변환? 매칭해준다
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))

