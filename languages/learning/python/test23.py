# 연습문제
# 3차원 리스트 만들기
# a = [[[0 for i in range(3)] for j in range(4)] for k in range(2)]

''' #?이런 느낌
[k
    [j
        [i][i][i], [i][i][i], [i][i][i], [i][i][i]
    ],
    [j
        [i][i][i], [i][i][i], [i][i][i], [i][i][i]
    ]
]
'''
# print(a)

# 퀴즈
# ? *은 지뢰 , .은 지뢰 아님
# ? 2차원 리스트
# import copy
# dlist = copy.deepcopy(dlist)

# row, col = map(int, input().split())
row = 3
col = 3

dlist = []
# 입력 받아서 dlist 2차원 배열 만들어주기
'''
for i in range(row):
    dlist.append(list(input()))
    second = []
    for j in range(col):
        second.append(0)
    dlist.append(second)
'''
for i in range(row):
    dlist.append(list(input()))
    for j in range(col):
        if dlist[i][j] == "*":
            continue
        else:  # 지뢰(*)이 아니면 0 넣어주기
            dlist[i][j] = 0

# print(dlist)
# print('---')
# print(dlist)

# 검증 시작
for i in range(row):
    for j in range(col):
        if dlist[i][j] != "*":  # '*' 이 아닌 경우
            if j == 0:
                # 오른쪽
                if dlist[i][j+1] == "*":
                    dlist[i][j] += 1
                    # print("오른쪽지뢰1추가")
            elif j < col-1:
                # 양쪽
                if dlist[i][j-1] == "*":
                    dlist[i][j] += 1
                    # print("센터왼쪽지뢰없음")
                if dlist[i][j+1] == "*":
                    dlist[i][j] += 1
                    # print("센터오른쪽지뢰1추가")
            elif j == col-1:  # j반복의 마지막 이면
                if dlist[i][j-1] == "*":
                    dlist[i][j] += 1
                    # print("왼쪽지뢰1추가")

            #! i번째로 비교
            if i == 0:
                # 아래쪽만
                if dlist[i+1][j] == "*":
                    dlist[i][j] += 1
                    # print("아래쪽지뢰1추가")
            elif i < row-1:
                # i번째의 중간대 검증 (위, 아래)
                if dlist[i-1][j] == "*":
                    dlist[i][j] += 1
                    # print("위쪽지뢰1추가")
                if dlist[i+1][j] == "*":
                    dlist[i][j] += 1
                    # print("아래쪽지뢰1추가")
            elif i == row-1:
                # i번째의 마지막일 경우 위에만
                if dlist[i-1][j] == "*":
                    dlist[i][j] += 1
                    # print("위쪽지뢰1추가")

            # ? 모서리 부분 검증
            if i == 0 and j == 0:  # 위쪽 왼쪽 끝
                if dlist[i+1][j+1] == "*":
                    dlist[i][j] += 1
            elif i == 0 and j < col-1:  # 맨 위 중간
                if dlist[i+1][j-1] == "*":
                    dlist[i][j] += 1
                if dlist[i+1][j+1] == "*":
                    dlist[i][j] += 1
            elif i == 0 and j == col-1:  # 위쪽 오른쪽 끝
                if dlist[i+1][j-1] == "*":
                    dlist[i][j] += 1

            elif i < row-1 and j < col-1:  # 중간
                if dlist[i-1][j-1] == "*":
                    dlist[i][j] += 1
                if dlist[i-1][j+1] == "*":
                    dlist[i][j] += 1
                if dlist[i+1][j+1] == "*":
                    dlist[i][j] += 1
                if dlist[i+1][j-1] == "*":
                    dlist[i][j] += 1

            elif i < row-1 and j == 0:  # i번째는 중간 j번째 왼쪽 끝
                if dlist[i-1][j+1] == "*":
                    dlist[i][j] += 1
                if dlist[i+1][j+1] == "*":
                    dlist[i][j] += 1

            elif i < row-1 and j == col-1:  # i번째는 중간 j번째 오른쪽 끝
                if dlist[i-1][j-1] == "*":
                    dlist[i][j] += 1
                if dlist[i+1][j-1] == "*":
                    dlist[i][j] += 1

            elif i == row-1 and j == 0:  # 맨아래 왼쪽
                if dlist[i-1][j+1] == "*":
                    dlist[i][j] += 1
            elif i == row-1 and j < col-1:  # 맨아래 중간
                if dlist[i-1][j-1] == "*":  # ?
                    dlist[i][j] += 1
                if dlist[i-1][j+1] == "*":
                    dlist[i][j] += 1
            elif i == row-1 and j == col-1:  # 맨아래 오른쪽 끝
                if dlist[i-1][j-1] == "*":
                    dlist[i][j] += 1

        print(dlist[i][j], end='')
    print()
