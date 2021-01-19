'''
#연습문제: 3으로 끝나는 숫자만 출력하기
i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > 73:
        break
    print(i, end=' ')
    i += 1
'''

'''
표준 입력으로 정수 두 개가 입력됩니다
(첫 번째 입력 값의 범위는 1~200, 두 번째 입력 값의 범위는 10~200이며
첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 
다음 소스 코드를 완성하여 첫 번째 정수와 두 번째 정수 사이의
숫자 중 3으로 끝나지 않는 숫자가 출력되게 만드세요. 
정답에 코드를 작성할 때는 while True:에 맞춰서 들여쓰기를 해주세요.
'''

start, stop = map(int,input().split())
#start = 1
#stop = 20
i = start

while True:
    #! 10으로 나눠서 나머지가 3과 같다면 i는 3으로 끝나는 수!! 
    if i % 10 == 3: 
        i += 1
        continue # continue를 해서 아래코드가 실행안되게, 결과적으로 3은 빼고 출력
    if i > stop:
        break
    print(i, end=' ')
    i += 1







