# 3으로 끝나는 것만 출력 안되게 하기


start, stop = map(int, input().split())

i = start

while True:
    if i % 10 == 3:  # 10으로 나눴을 때 나머지가 3이면 3으로 끝난 상태
        i += 1
        continue  # 아래 코드 실행안하고 다시 반복문 실행
    if i > stop:
        break
    print(i, end=' ')
    i += 1
