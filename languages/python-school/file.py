#file 생성하기 open()함수로 만들기
# open()의 첫번재 arg는 파일명, 두번째 'w'는 wirte
#** w write , 이후 또 w를 사용하면 덮어쓰기함에 주의
f = open('hello.txt', 'w')
#write()메소드에는 내용을 입력한다
f.write('hello world\nhello world')
#메모리에 계속 남아있는 것을 방지하기 위해 close를 꼭 한다
f.close() #close() 파일 닫음

# open()의 첫번재 arg는 파일명, 두번째 'r'는 읽기모드
f = open('hello.txt', 'r')
#read()메소드로 file변수를 불어와서 s변수에 넘김
s = f.read()
print(s)
f.close()

f = open("hello.txt", 'a')  # 기존파일에 새로운 내용을 추가할 때는 'a'모드
f.write("\ncontents: 테스트 테스트")  # \n \t 등이 가능 """ 쓰고 내용쓰고 """ 도 가능(free form같은 느낌)
f.close()

# close()을 이용 안해도 되는 with 키워드를 이용해서 open()하고 
# 변수에 할당은 as 변수명
# 좋은점은 close()메소드를 안 사용해도 됨
'''
with open('hello.txt', 'r') as f:
    s = f.read()
    print(s)
'''
'''
# with로 파일을 열고 for문으로 입력하기 
with open('hello.txt', 'w') as f:
    for i in range(3):
        f.write('hello world {0}\n'.format(i))
'''
'''
#입력하기
lines = ['안녕하세용\n', '파이썬\n', '코딩도장 입니다\n']
with open('hello.txt', 'w') as f:
    #wirtelines()메소드를 이용해서 입력
    f.writelines(lines)
'''
'''
print("------------------------------")
#리스트 형태로 받아오기
# 참고: lines의 문자열은 위의 주석 처리 때문에 다를 수 있음 
# 일단 w모드로 생성이 안되어 있음 참고 (복습할 때)
lines = ['안녕하세용\n', '파이썬\n', '코딩도장 입니다\n']
with open('hello.txt', 'r') as f:
    #readlines 는 리스트 여러줄 형태로 받아온다
    #lines = f.readlines()
    
    #readline()은 리스트로 한줄만 받아옴
    lines = f.readline()
    print(lines)
'''

#readline()을 이용해서 한줄씩 while문 이용해서 반복 처리 (한줄씩)
#readline()은 리스트로 반환
# 참고: lines의 문자열은 위의 주석 처리 때문에 다를 수 있음 
# 일단 w모드로 생성이 안되어 있음 참고 (복습할 때)
lines = ['안녕하세용\n', '파이썬\n', '코딩도장 입니다\n']
with open('hello.txt', 'r') as f:
    while lines != '':
        #readline()은 리스트로 한줄만 받아옴
        lines = f.readline()
        print(lines.strip('\n'))
    


# f = open("a.txt", 'x')  # x는 w처럼 파일을 만들지만 같은파일이 존재하면 만들어 지지 않는다
# f.write("\n1234")
# f.close()
