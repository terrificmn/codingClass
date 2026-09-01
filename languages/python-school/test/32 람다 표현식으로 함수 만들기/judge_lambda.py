'''
#연습문제
# 이미지 파일만 .jpg .png 파일만 가져오게 만들기

files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
# 람다함수를 사용, find()메소드를 사용해서 찾은 값만 리턴한다
print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files)))
'''

files = input().split()

#포맷팅 {0}{1}로 하나씩 매칭해준다, {0은 0:03d}[0]번째는 파일명이고 .split('.')으로  '.'기준으로 나눠 준다
#{0}{1}.format(0번 바꿀내용, 1번 바꿀내용)메소드로 각각 0, 1로 매칭이 되서 바뀜
#{0}에서 {0:03} 은 처음 0은 포맷팅 할 0번 순서 :(콜론)이후는 숫자 자리수 
# 03은 3자리수이고 앞은 0으로 채워짐 예: 05이면 5자리안에 숫자를 채우고 나머지는 0으로 채움의 뜻
print(list(map(lambda x: '{0:03d}.{1}'.format(int(x.split('.')[0]), x.split('.')[1]), files)))

