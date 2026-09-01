# 경로를 안 쓰면 현재 경로에 만들어짐 (경로를 쓸 때는 \\ 2번 써야함)
# f = open("a.txt", 'w')  # w write , 이후 또 w를 사용하면 덮어쓰기함에 주의
#f.write("test 12345678910")
# f.close()
# f = open("a.txt", 'a')  # 기존파일에 새로운 내용을 추가할 떄는 a
# f.write("\ncontents")  # \n \t 등이 가능 """ 쓰고 내용쓰고 """ 도 가능(free form같은 느낌)
# f.close()

# f = open("a.txt", 'x')  # x는 w처럼 파일을 만들지만 같은파일이 존재하면 만들어 지지 않는다
# f.write("\n1234")
# f.close()

import os  # os 모듈 사용
# os 모듈을 사용함 - 시스템의 환경 변수, 디렉토리, 파일 등을 제어할 수 있다고 함
f = open("a.txt", 'r')
print(f.readline())  # f.readline() 한줄씩 읽음
print(f.readlines())  # f.readlines() 리스트 형태로 받아와서 보여줌
f.close()

# 표준 출력 전환 하기 (콘솔에서 print 하는게 아닌 파일창을 열어줌)
# import sys #작동안함 이유는 알아봐야할 듯
#f = open("b.txt", 'w')
# sys.stdout = f  # print()로 생성한 내용이 파일로 출력됨
# print("test")
# f.close()

print(os.listdir('.'))  # . 현재 경로
print(os.path.exists('a.txt'))  # 해당 파일 존재 유무 -True, False로 반환
# path.abspath() 파일 존재 상관 없이, 해당 파일의 절대 경로 반환
# print(os.path.basename('C:\\Users\\a.txt'))  # 파일명 반환
# print(os.path.dirname('C:\\Users\\a.txt'))  # 디렉토리 반환

print(os.getcwd())  # 현재 디렉토리 위치 확인 Current Working Directory
print(os.chdir())  # 경로 변경
os.mkdir('temp')  # 디렉토리 생성
print(os.path.exists('temp'))
