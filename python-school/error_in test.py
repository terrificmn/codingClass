import random
'''
a = [1, 2, 3]
#예1
i = 0
while i < len(a):
    print(a[i])
    i += 1

#예2
# for i in range(len(a)):
    print(a[i])

#예3
for i in a:
    print(i)

a = [1, 2, 3]
#예4
for i in a:   # 리스트를 반복시키는 for문 위의 다른 반복문 처럼 될 것 같지만, 인덱스 에러가 남
    print(a[i])

    # 이유는 그냥 a리스트 변수를 가지고 와서 하나씩 요소를 꺼내게 되면
    # i 변수에는 요소값이 1, 2, 3 (반복 할때 마다) 들어가지는데
    # print(a[i])이런식으로 인덱스로 접근하면 인덱스는 0부터 시작하므로
    # a[1], a[2], a[3] 요렇게 반복이 작동하게 되고, 마지막 i는 리스트의 3인데, 인덱스로 접근하면
    # a[3]은 없기 때문에 IndexError: list index out of range 가 발생하게 됨
    # 오히려 예3번 처럼, i변수만 출력해주면 
    # 출력을 print(i)라고 하면 오히려 하나씩 요소를 꺼낸 온 것이기 때문에 실행에 문제가 없다

# a.append()
# a.extend()

'''
# import zipfile #압축관련 모듈
# import time #시간관련 모듈


'''
# 틀린문제
# 기본 //연산자는 나눈 후 소수점 이하를 버리는 연산자 임
print(10 / 2)  # 결과는 5.0 소수점 표시 됨
print(10 // 2)  # 결과는 5 소수점 버림


# * 틀린문제 1. txt 파일 읽어오기

# 【문제12】단어가 줄 단위로 저장된 words.txt 파일이 주어집니다.
# words.txt 파일에서 회문인 단어를 각 줄에 출력하는 프로그램을 만드세요.
# 단어를 출력할 때는 등장한 순서대로 출력해야 합니다.
# 그리고 파일에서 읽은 단어는 \n이 붙어있으므로 \n을 제외한 뒤
# 회문인지 판단해야 하며 단어를 출력할 때도 \n이 출력되면 안 됩니다. *회문은 거꾸로 뒤집어도 똑같은 단어 인것. 예: mom --> mom
# (단어 사이에 줄바꿈이 두 번 일어나면 안 됨).

with open('python-school/words.txt', 'r') as f:
    # print(line)  # 그냥 라인 한 줄만 읽어오면 문자열에 |n이 포함되어 있어서 출력했을 때 1칸 더 줄바꿈됨
    while True:  # 참고로 line은 문자열 임 (아무것도 없으면 whlie문 반복 끝)
        line = f.readline()  # 한줄을 읽어 옴
        striped = line.strip('\n')

        # reversed = striped.reverse()
        # 위 처럼 하면 AttributeError: 'str' object has no attribute 'reverse'
        # reverse()메소드는 리스트의 순서만 바꿀 수 있다. 리스트로 바꾼다음에 join을 이용할 수 있다
        # 문자열이라서 에러가 나는 듯 함

        # 아니면 reversed() 함수 이용 reverse아님
        # print(reversed(striped)) #메모리에 위치되어 있음 (객체가 리턴된다고 함(리스트가 아닌 경우))  내용이 표시되지 않음
        # join 함수를 사용하면 받아올 수 있다 앞에 ''는 붙여야 한다
        # 아래처럼 join을 이용해서 print 하는 것은 문제가 안되는데
        # print(''.join(reversed(striped)))
        # 하지만 if문으로 비교가 안되는 문제가 있음 (type 에러가 남)

        # 거꾸로 하려면 슬라이싱 하기 (가장 쉽고 정확함!!!)
        # print(striped[::-1])
        reversed = striped[::-1]
        if striped == reversed:
            print(striped)
        if not line:  # *중요 line으로 받은 데이터가 없으면 break 하게 해줌
            # readline()은 한줄씩 오픈한 파일의 한줄씩 받아오는데 while문으로 돌리면 무한반복하기 때문에 유의
            break
#####################################################################

'''

'''
# for문으로 작성  with open으로 연 후에 직접 파일을 반복시켜도 됨
# with 로 열때에도 마지막에 :붙이고, 들여쓰기 해야함
# 프로젝트가 열린 디렉토리가 상위 디렉토리로 열려있는것에 유의
# * 1번째 for문 방법 그냥 for문 반복하기
with open('python-school/words.txt', 'r') as f:
    for i in f:  # readlines()를 사용한 효과
        i.strip('\n')
        reversed = i[len(i)::-1]  # 거꾸로 표시
        if i.strip('\n') == reversed.strip('\n'):
            # print(i.strip('\n'), reversed)
            print(i, end='')


# * 2번째 for문 readlines이용 (파일전체 내용을 받아와서 for문으로 한줄씩 실행)
print('2번째 for문 readlines')
with open('python-school/words.txt', 'r') as f:
    # 또는 간단하게 readlines()를 이용하면 편함. (readlines가 EOF end of file 파일끝까지 읽고 끝내므로 file close가 필요없음)
    for line in f.readlines():
        striped = line.strip('\n')
        reversed = striped[::-1]
        if striped == reversed:
            print(striped)


###########################################################################
print('---while으로 반복하기---')
with open('python-school/words.txt', 'r') as f:
    while True:  # 참고로 line 이 없다면
        line = f.readline()  # 한줄을 읽어 옴 (다음반복 때 다음줄을 읽어옴)
        striped = line.strip('\n')
        reversed = striped[::-1]
        if striped == reversed:
            print(striped)
        if not line:  # 중요 빠져나올 포인트
            break
'''

# 원래 틀린코드 완전 틀림 ㅡㅡ
#file = open('words.txt', 'w')
# file.write("apache\ndecal\ndid\nneep\nnoon\nrefer\nriver\n")
# file.close

# with open('words.txt', 'r') as f

# for i in f:
#    line = f.readline()
#    reversed = line.strip('\n').reverse()
#    if line.strip('\n') == reversed:
#        print(i.strip('\n'))


'''
# * 틀린문제 2
# -----

# ranList = list(range(1, 101)) 필요없음
# ranTest = ranList.random.random()  틀린코드
# print(random.random()) #실수 타입으로 랜덤으로 만들어 줌
ranTest = random.randint(1, 100)  # 고친 코드 randint()

count = 0
print(ranTest)  # 추가 랜덤이 몇인지 알기 위해
while True:
    inputUser = int(input('1 ~ 100사이의 정수를 입력하시오.'))
    if inputUser != ranTest:
        count += 1  # 틀릴 경우, 무한반복
        quitY = input("그만두기는 y, 계속 도전은 n 누르세요:")
        if quitY == "y":
            break

    else:
        count += 1  # 맞을 경우도 일단 카운트 +1 하고 빠져나가기
        break

print("{0}번 시도에 정답 {1}을 맞췄습니다." .format(count, ranTest))


# * 틀린문제 3 - class: @classmethod, @staticmethod (다행히 단순 syntax 에러)

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, (time_string.split(':')))
        return cls(hour, minute, secocnd)  # todo: 변수 이름 오류

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, (time_string.split(':')))
        return hour <= 24 and minute <= 59 and second <= 60


time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')
'''
