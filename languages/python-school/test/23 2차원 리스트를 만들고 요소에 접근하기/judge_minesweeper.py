#표준 입력으로 2차원 리스트의 가로(col)와 세로(row)가 입력되고
# 그 다음 줄부터 리스트의 요소로 들어갈 문자가 입력됩니다. 
# 이때 2차원 리스트 안에서 *는 지뢰이고 .은 지뢰가 아닙니다. 
# 지뢰가 아닌 요소에는 인접한 지뢰의 개수를 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).
#여러 줄을 입력 받으려면 다음과 같이 for 반복문에서 
# input을 호출한 뒤 append로 각 줄을 추가하면 됩니다
# (list 안에 문자열을 넣으면 문자열이 문자 리스트로 변환됩니다).

row, col = map(int,(input().split()))
matrix = [] #리스트 1차원배열 셋팅

for i in range(row):
    matrix.append(list(input()))

for i in range(row):
    for j in range(col):
        if matrix[i][j] == ".": #지뢰가 아닌경우, 즉 지뢰(*)이면 아무것도 안함
            nbr = 0  #카운트를 담당할 변수 초기화 0
            #현재 위치에서 한번 더 for문을 돌린다 
            #즉, 현재 위치 기준으로 위, 아래, -1씩, +1씩 해서 주변
            #반복할 범위를 지정(range()함수이용)
            #끝 값은 포함하지 않으므로 +1을 더해야해서 결과적으로 +2임
            #인덱스 참조할 범위가 벗어나면 에러가 나므로 z for문에서 if문으로 제어한다
            for x in range(i-1, i+2):
                for z in range(j-1, j+2):
                    #인덱스 에러가 나지 않게 0보다 적으면 안되고 입력받은 row, col값 보다 크지 않게 해줌
                    #예: row가 3이면 x는 3보다 최소 같거나 크면 안됨(실제 인덱스로 돌아갈때는 0, 1, 2 만큼 돌아가므로)
                    if x < 0 or z < 0 or x >= row or z >= col:
                        continue #에러가 안나게 다시 for문 위로 올라가서 실행 (아래부분 실행 안함)

                    #범위가 현재 위치의 i값에서 -1부터 시작하므로 위의 row부터 시작하게 됨
                    #여기에서 지뢰인지 확인, 주의할 점은 검증하는 대상은 x,z 임에 주의
                    #현재[i][j]배열은 . 인 상태 (즉, 지뢰가 아님)
                    elif matrix[x][z] == "*":
                        #count를 해줄 변수에 1을 더해서 올려준다
                        nbr += 1
            matrix[i][j] = nbr

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end='') #줄바꿈 없이 요소 출력
    print()



''' 똑같은 반복코드 연습
for i in range(row):
    for j in range(col): 
        if matrix[i][j] == ".":
            nbr = 0
            #**현재[i][j]로 포인트가 되어 있는것에 주목! 현재값으로 비교
            #시작범위가 현재i에서 위의 i인덱스까지 반복해야하고
            #아래로는 +1만큼 더 반복해야하는데, 끝 범위는 range()에서 포함하지 않으므로
            #i+1에서 +1을 더 시켜준다, 결과적으로 i+2가 됨
            #z로 반복시키는 부분도 i와 같은 의미로 j-1 부터 j+1까지 해줘야함
            for x in range(i-1, i+2): 
                for z in range(j-1, j+2): #1~3          
                    #! 현재포인트에서 x와 z값이 0작아지거나, row/col 값 보다 크면 인덱스를 벗어나므로 
                    #! 실행을 안하게 한다
                    if x < 0 or z < 0 or x >= row or z >= col:
                        continue
                    elif matrix[x][z] == "*":
                        nbr += 1
            matrix[i][j] = nbr


for i in range(row):
    for j in range(col):
        print(matrix[i][j], end='')
    print()
'''

