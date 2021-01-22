'''
a = [1, 2, 3]
for i in a:
	print(i)


i =0
while i < len(a):
	print(a[i])
	i += 1



for i in range(len(a)):
	print(a[i])

for i in a:
	print(a[i])


import zipfile
import time
a.append()
a.extend()


'''

#【문제12】단어가 줄 단위로 저장된 words.txt 파일이 주어집니다. 
# words.txt 파일에서 회문인 단어를 각 줄에 출력하는 프로그램을 만드세요. 
# 단어를 출력할 때는 등장한 순서대로 출력해야 합니다. 
# 그리고 파일에서 읽은 단어는 \n이 붙어있으므로 \n을 제외한 뒤 
# 회문인지 판단해야 하며 단어를 출력할 때도 \n이 출력되면 안 됩니다
# (단어 사이에 줄바꿈이 두 번 일어나면 안 됨).

# todo: readline()으로 할 수 있는 방법 연구하기
with open('words.txt', 'r') as f:
	line = f.readline()
	while line != -1:
		line.strip('\n')
		reversed = line.reverse()
		if line.strip('\n') == reversed.strip('\n'):
			#print(i.strip('\n'), reversed)
			print(line, end='')

#이코드는 안되는 듯





'''
#with 로 열때에도 마지막에 :붙이고, 들여쓰기 해야함
with open('words.txt', 'r') as f:
	for i in f:
		#line = f.readline()
		i.strip('\n')
		reversed = i[len(i)::-1] #거꾸로 표시
		if i.strip('\n') == reversed.strip('\n'):
			#print(i.strip('\n'), reversed)
			print(i, end='')

#todo: 작동은 되나 readline()을 이용해서 할 수 있는 방법 찾아보기
'''

'''
원래 틀린코드
file = open('words.txt', 'w')
file.write("apache\ndecal\ndid\nneep\nnoon\nrefer\nriver\n")
file.close

with open('words.txt', 'r') as f

for i in f:
    line = f.readline()
	reversed = line.strip('\n').reverse()
	if line.strip('\n') == reversed:
		print(i.strip('\n'))


#-----------------------
#틀린코드 고치기
import random

#ranList = list(range(1, 101)) 필요없음
#ranTest = ranList.random.random()  틀린코드 
ranTest = random.randint(1, 100)

count = 0
print(ranTest) #추가 랜덤이 몇인지 알기 위해
while True:
	inputUser = int(input('1 ~ 100사이의 정수를 입력하시오.'))
	if inputUser != ranTest:
		count += 1 #틀릴 경우, 무한반복
		quitY = input("그만두기는 y, 계속 도전은 n 누르세요:")
		if quitY == "y":
			break
	
	else:
		count += 1 #맞을 경우도 일단 카운트 +1 하고 빠져나가기
		break		

print("{0}번 시도에 정답 {1}을 맞췄습니다." .format(count, ranTest)) 
'''


'''
#-----------------------

class Time:
	def __init__(self, hour, minute, second):
		self.hour = hour
		self.minute = minute
		self.second = second
	
	@classmethod
	def from_string (cls, time_string):
		hour, minute, second = map(int, (time_string.split(':')))
		return cls(hour, minute, secocnd) #todo: 변수 이름 오류
	
	@staticmethod
	def is_time_valid (time_string):
		hour, minute, second = map(int, (time_string.split(':')))
		return hour <= 24 and minute <=59 and second <= 60

time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')

'''