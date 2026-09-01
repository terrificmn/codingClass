'''
for i in range(10):
    print('hello', i)

for i in range(0, 10, 2): #? 시작, 끝, 스텝값
    print('hello', i)

for i in range(10, 0, -1): #역으로 반복
    print('hello', i)

for i in reversed(range(10)): #reversed()는 반대로 바꿔줌
    print('hello', i)

num = int(input())
for i in range(num):
    print(i, end=' ')

a = [10,20,30,40,50] #list
for i in a:   #? for i in [1,2,...list형태]도 가능
    print(i)
'''

#문자열을 넣고 반복도 가능
for i in 'python':  
    print(i)

#** reversed()메소드 사용해서 간단하게 반대로 반복가능
for i in reversed('python'):
    print(i)

