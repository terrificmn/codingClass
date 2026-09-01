# while문 형태 
# while (조건True/Fa;se): # * true이면 반복, false면 반복하지 않는다
#* while문은 조건이 True이면 무한반복을 하기 때문에 
#* 비교할 변수를 +1 해주어야함 (그래서 결국 조건이 false가 될 수 있게..)
#* 또는 if문을 사용해서 break등을 사용

'''
i = 0
while i < 10:
    print('hello world', i)
    i += 1  #조건으로 비교할 변수를 증가 시켜주기 

#반대로 반복문 실행
for i in reversed('PYTHON'):
    print(i, end=' ')

num = int(input())
while num < 10:
    print('hello world')
    num += 1  #조건으로 비교할 변수를 증가 시켜주기 

#braek문 사용해서 빠져나가기
x = 0
while True:
    print(x)
    x += 1
    if x == 10:
        break #조건에 맞으면 빠져나감

#continue 사용: continue키워드 아래코드를 실행안하고 다시 for문 반복
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
'''


#while문 continue 사용 
i = 10 
while i:
    i -= 1 #i값을 -1해줘서 반복할 수 있게..
    if i % 2 == 0: #i가 처음에 10이므로 처음부터 짝수 이므로 
        continue #짝수면 코드 실행을 안하기 위해서 continue
    print(i)

'''
#* tip: pass키워드를 넣어서 아무런 실행을 안하면 for문 반복되는 만큼 딜레이 시킬 수 있음
for i in range(1000): 
    pass
print(10)
'''

