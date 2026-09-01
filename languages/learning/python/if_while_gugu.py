a = 1
if (a > 0):
    msg = "a는 양수 입니다"
else:
    msg = "a는 음수 입니다"

print(msg)

if (a == 0):
    msg2 = "ai is 0"
else:
    msg2 = 'a is not 0'

print(msg2)

msg = 'a is positive numbers' if a < 0 else 'a is negative'
print(msg)

l = ['a', 9, [1, 2, 3], ('a', 'b')]
for i in range(len(l)):
    print(l[i])

for i in [1, 2, 3]:
    for j in (10, 20):
        print(j)
    print(i)

num = 10
while (num > 0):
    if(num == 6):
        print("--this is the end--")
        break
    print(num)
    num -= 1

a = 5
while a > 0:
    print(a)
    a -= 1

print([i+j for i in range(3) for j in range(3)])


# 구구단
for i in range(2, 10):
    if (i == 4):
        continue  # 조건에 맞으면 다시 현재 for문 진행 (아래 코드는 실행 안함)
    for j in range(1, 9):
        #print("%d x %d = %d" % (i, j, i*j))
        print("{} x {} = {}".format(i, j, i*j))  # format함수로 출력 위의 코드와 같은 결과
