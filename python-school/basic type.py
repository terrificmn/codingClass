# print('hello world')
# print('Hello world,again')

a = 10
if a == 10:
    print(a)
    print(a + 1)

print(1+1)
print(2-1)
print(2*5)
print(a//2) #몫
print(a%2)
print(3**3) #제곱

print(int(3.3))
print(5/2)
print(int(5/2))

print(type(a))
print(type(10))
print(type(10.0))
print(type('10'))

print(type(divmod(5,2))) #몫, 나머지를 튜플로 만들어줌

#print(float(3))

print('소음이 가장 큰 층수:', int(0.2467 * 12 + 4.159), "층 입니다")

#왜곡 스킬은 ap = 102 에 따라 (ap*0.6) +255 데미지
print(102 * 0.6 + 225)

x = 2
print(x)

x = 1
y = 2
z = 3
#x,y,z = 1,2,3 한번에 각각 할당
print(x,y,z)

x=y=z=10
print(x, y, z)
del x # x변수를 지움 (이후 출력하면 정의가 안되어있다고 나옴)
x = None
print(x)

a = 10
b = 20
c = a + b
print(c)

a = 30
print(a + b)

name = '고길동'
print(name)
name = 20
print(name)

#X = input() #키보드로 입력 받음
#X = input('정수를 입력하세요: ')
#print(X)

# a = int(input('첫번재 정수를 입력하세요:'))
# b = int(input('두번째 정수를 입력하세요:'))
#print(a+b)

#a, b = input('정수 2개를 입력하세요:').split()
# #split fn. 구분자로(기본: 스페이스)로 문자열을 나눔, 특정문자를 파라미터로 넘겨주면됨

#a, b = input('정수 2개를 입력하세요:').split(',')
#print(int(a)+int(b))

x = 10
y = 20
print(x, y)
# 변수의 값을 바꿔서 할당 (파이썬에서는 쉽게 작동)
x, y = y, x
print(x, y)

a = 10
print(a)
a += 20
print(a)

#map()fn.은 결과를 int로 변환, float은 float로 변환 , int는 괄호로 처리하지 않고 int, 로만 씀
#a, b = map(int, input('정수 두 개를 입력해 주세요:').split(','))
#print(a+b)

#a, b, c = map(int, input().split())
#print(a+b+c)


#a, b, c, d = map(int, input().split())
#print(int((a+b+c+d)/4))
#또는 #print((a+b+c+d)//4)

#sep 값 넣어주기 (separate로 \t \n등을 넣는다)
print(10, 20, 30, sep='\n')
#end 값 넣어주기 end='' 지정하면 출력물 마지막에서 한칸 내리지 않음 (다음출력시에 영향)
print(1, end=' ')
print(2, end='')
print(3)

