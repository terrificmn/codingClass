# 연습 및 테스트 용

f = open('test1.txt', 'w')
f.write('테스트 입니다')
f.close()

#inputFile = input('입력하세요.: ').split()


# {0}{1}.format(0번 바꿀내용, 1번 바꿀내용)메소드로 각각 0, 1로 매칭이 되서 바뀜
# {0}에서 {0:03} 은 처음 0은 포맷팅 할 0번 순서 :(콜론)이후는 숫자 자리수
# 03은 3자리수이고 앞은 0으로 채워짐 예: 05이면 5자리안에 숫자를 채우고 나머지는 0으로 채움의 뜻
inputFile = ["1.jpg", "2.jpg", "3.png", "44.png"]
a = list(map(lambda ff: "{0:05}.{1}".format(
    int(ff.split('.')[0]), ff.split('.')[1]), inputFile))
print(a)

# 문자열 앞에 f 로 포맷팅 그 이후 {}중괄호에 변수 이름 넣기
name = "홍길동"
print(f'안녕 {name}')

# 정렬  f 쓰고 {}중괄호로 묶고
print(f'{"Hello":>10}')

# count 메소드, 문자열 몇개 인지 반환

# find 메소드 찾는 문자열의 인덱스 반환, 없으면 -1 반환
# index 메소드는 문자열 인덱스 반환, 없으면 에러
t = "hello"
print(t.find('e'))

# join 문자열 삽입 (인덱스 사이사이에 해당 문자를 넣어줌)
print(','.join(t))

#lstrip, rstrip, strip (왼쪽, 오른쪽, 양쪽)
# 공백 지움
t = "      space.      "
print(t.rstrip())
# 해당 문자열도 같이 제거 가능 (공백과 같이)
print(t.strip(' . '))

# replace 메소드 ("찾기", "대상")
print(t.replace("e", 'E'))
