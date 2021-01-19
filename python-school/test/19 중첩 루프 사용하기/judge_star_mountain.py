# 표준 입력으로 삼각형의 높이가 입력됩니다. 
# 입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다). 
# 이때 출력 결과는 예제와 정확히 일치해야 합니다. 
# 모양이 같더라도 공백이나 빈 줄이 더 들어가면 틀린 것으로 처리됩니다.

inputNbr = int(input())
#inputNbr = 5
num = 1 #홀수를 만들기 위함
space = inputNbr #space에 입력받은 만큼 넣어줌
for i in range(inputNbr):
    space -= 1 #처음띄워줄 스페이스는 입력받은 수의 -1만큼임
    if space != 0:
        print(" " *space, end="") #space만큼 띄워준다, 처음스페이스바는 입력받은 수
    for j in range(inputNbr*2): #일단 입력받은거의 2배로 한다(어차피 break할 것임)
        if j % 2 != 0: #짝수가 아니면
            print("$" *num) #j가 홀수번째면 num만큼 곱해서 출력
            num += 2 #다음번 출력을 위해서 +2해서 계속 홀수를 유지해준다
            break
        
        #else는 j가 0이거나 짝수이면 아무것도 안함
'''
#* 다른방법
#height = int(input())
height = 3
for i in range(height):
    for j in reversed(range(height)): #거꾸로 반복
        if j > i:
            print(' ', end='')
        else:
            print("*", end='')
    for j in range(height): #위의 j 반복이 (거꾸로) 되어서 입력이 끝난 후 그 뒤에 이어서 다시 j반복 함
        if j < i:
            print("*", end='')
    print()
'''
