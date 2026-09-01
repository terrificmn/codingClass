# 계단식 별 출력
'''
for i in range(1, 6):
    print("*" * i)

'''
'''대각선 별
for i in range(5):
    for j in range(5):
        if i == j:
            print("*", end='')
        else:
            print(" ", end='')
    print(' ')
'''
# 1시간 반 ㅠ
star = int(input())
space = star
numhol = 1

for i in range(star):
    # print(i)
    # space 띄울 변수 정의(입력받은 값에서 -1 씩 감소시켜준다, 즉 for i가 돌때 쓸 스페이스바 수 정의)
    space -= 1
    print(' ' * space, end='')
    for j in range(1, star*2):  # j의 반복은 입력된 것은 2배만큼 해준다
        if j % 2 != 0:  # 홀수 구하기
            print("*" * numhol)
            numhol += 2  # 출력할 별의 홀수를 맞추기 위해 +2해줌 (홀수가 된다, 3, 5, 7등...)
            break  # 홀수이면 for j 빠져나감 (홀수 별을 출력하는게 목적)
