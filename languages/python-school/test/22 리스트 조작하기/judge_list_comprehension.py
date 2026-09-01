'''
#연습문제
#리스트 표현식으로 특정요소 길이가 5인것만 출력
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]
print(b)
'''

#표준 입력으로 정수 두 개가 입력됩니다
# (첫 번째 입력 값의 범위는 1~20, 두 번째 입력 값의 범위는 10~30이며 
# 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 
# 첫 번째 정수부터 두 번째 정수까지를 지수로 하는 
# 2의 거듭제곱 리스트를 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다). 
# 단, 리스트의 두 번째 요소와 뒤에서 두 번째 요소는 삭제한 뒤 출력하세요. 
# 출력 결과는 리스트 형태라야 합니다.

#firstIn = 1
#lastIn = 10
firstIn, lastIn = map(int, input().split()) 
listA = []

for i in range(firstIn, lastIn+1): #최종의 값의 실제 마지막까지 반복하기 위해 +1
    listA.append(2 ** i) #2의 거듭제곱 만들기
del listA[1] #지우기
del listA[-2]
print(listA)


''' 리스트 표현식으로 코딩
firstIn, lastIn = map(int, input().split()) 
A = [2 ** i for in range(firstIn, lastIn +1)]
del a[1]
del a[-2]
print(a)
'''