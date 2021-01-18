#중복loop은 i * j(n) 만큼 반복하게 된다 
for i in range(5):
    for j in range(5):
        print("$", end='')
    print() #print()함수만 사용하면 줄바꿈이 일어남

for i in range(5):
    for j in range(5):
        if i == j:
            print("$" * (j+1), end='') #j가 0부터 시작하므로 j+1해서 +1부터 나올 수 있게 함
    print()

#? 위의 코드를 더 간단하게 range를 이용해서 바꿀 수 있음
for i in range(1, 6):
    #i 값을 주게 되면 i값 만큼만 반복하게 됨
    for j in range(i): #즉, i가 1이면 j는 1번, i가 3이면, j는 3번 반복
        print ("$", end='') #?위의 코드와는 다르게 if문을 사용안해도 됨
    print()

#? for문 반대로 반복하기
for i in range(5, 0, -1):
    for j in range(i):
        print ("$", end='')
    print()

# 별(*) 
'''
*****
 ****
  ***
   **
    *
위의 모양으로 출력''' 
for i in range(5):
    for j in range(5):
        if j < i:
            print(' ', end='')
        else:
            print("*", end='')
    print()

