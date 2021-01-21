a = 'Life is too short, you need Python'
print(a[:])

a = "20210111Sunny"
date = a[:8] # : 이후 (마지막 숫자는 포함안함) //
year = a[0:4]
weather = a[8:]
print(weather)
print(year)

#%d 는 int로 formatting
print ('I eat %d apples' % 3)
#%s 는 str로 formatting
print ("I eat %s apples" % "five")

#여러개 포맷팅 (n1, n2)여러개 표현 가능
# %s=string , %c=one character, %d=integer, %f=float, 등등..
# 문자열에 %가 포함되어 있다면 %% 두번 사용
num = 10
day = "three"
string = "I ate %d apple. so I was sick for %s days."
print (string % (num, day))

# %f 사용시 소수점 아래 표현 %0.(갯수)f 로 표현 (예: %0.4f)
print ("%0.5f" % 3.14233241234) #소숫점 5째자리까지 표시

# {} 로 대입하고 %d 대신에 사용
# format함수에서 첫번째 변수, 두번재 변수가 각각 {0} {1}로 바뀜
print ("I have {0} apples. but I ate {1} apples.".format(num, day))
# {} 인덱스가 아닌 {name}형태를 사용 가능
# 대신 파라미터로 value를 직접 넣어줘야함 예: format(num=10, howMany=3)
print ("I have {num} apples. but I ate {howMany} apples.".format(num=10, howMany=3))

#f 문자열 포맷팅
#문자열 앞에 f만 붙이면 되고, 나머지는 변수에 할당
name = '고길동'
age = 50
print(f'나의 이름은 {name} 이고, 나이는 {age}입니다.')
print(f'나의 이름은 {name} 이고, 내년 나이는 {age+1}입니다.')

#f 정렬
print(f'{"Hello":<10}') #<10 작은면 왼쪽정렬
print(f'{"Hello":>10}') #>10 크면 오른쪽 정렬
print(f'{"Hello":^10}') #^10이면 가운데 정렬

#count 해당 문자열에 몇개 인지 반환
string = "hobby"
print(string.count('b')) #b가 2개이므로 2반환

#find, index 함수 // 각각 문자열 인덱스 반환
string = "Python is the best choice."
print(string.find('b'))
#단, find함수는 찾는 문자열이 없다면 -1 값을 리턴
print(string.index('b'))
#단, index함수는 찾는 문자열이 없다면 오류를 발생

#join 문자열 삽입 (함수내에서 넘기지 않음
print(",".join(string))

#대문자 upper 반대로 소문자는 lower()함수
print(string.upper())

#공백 지우기 lstrip, rstrip, strip (왼쪽, 오른쪽, 양쪽)
string = "         spaces           "
print(string.lstrip())
print(string.rstrip())
print(string.strip())

#replace
#특정문자열 바꿈 (첫번째,2번째 서로 바꿈)
a = "Life is short, you need Python!"
print(a.replace("short", "long"))

