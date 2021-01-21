f = open('test1.txt', 'w')
f.write('테스트 입니다')
f.close()

#inputFile = input('입력하세요.: ').split()


#{0}{1}.format(0번 바꿀내용, 1번 바꿀내용)메소드로 각각 0, 1로 매칭이 되서 바뀜
#{0}에서 {0:03} 은 처음 0은 포맷팅 할 0번 순서 :(콜론)이후는 숫자 자리수 
# 03은 3자리수이고 앞은 0으로 채워짐 예: 05이면 5자리안에 숫자를 채우고 나머지는 0으로 채움의 뜻
inputFile = ["1.jpg", "2.jpg", "3.png", "44.png"]
a = list(map(lambda ff: "{0:05}.{1}".format(int(ff.split('.')[0]), ff.split('.')[1]), inputFile))
print(a)

