''' #* 리스트에 요소 추가하기 
a = [10, 20, 30]
print(a)
a.append(500) #리스트에 추가 (마지막에)
print(a)
#리스트에 추가 마지막에 (배열로 넣어주더라도 원래 배열에서 확장되는 것
a.extend([600, 700]) 
print(a)
#위의 방식과 다르게 리스트[]형태로 append추가하게 되면 2차원 배열로 들어가짐
a.append([800, 900])
print(a)
# insert(인덱스, 값) 은 해당인덱스에 값을 추가해준다. 
a.insert(2, 1000) 
print(a)
#insert() 인덱스 부분을 len()으로 길이를 받아와서 값을 넘기면 마지막에 넣어짐(2차원)
#2차원으로 넣으면 2차원 배열로 추가됨
a.insert(len(a), [900, 1000])
print(a)
'''
'''
#* 리스트에 요소 삭제
# pop()은 리스트의 마지막 요소를 지워준다 
a = [10, 20, 30]
a.pop()
print(a)

#del([인덱스]) 해당 인덱스를 지움
a = [10, 20, 30]
del a[1]
print(a)

#remove()해당 값을 찾아서 지워줌 
a = [10, 20, 30]
a.remove(20)
print(a)
'''

a = [10, 20, 30, 40, 20, 50]
print(a.index(20)) #index(값)을 반환
print(a.count(20)) #count(값) 리스트 내의 값을 찾아 몇개인지 반환

#반대로 값을 바꿈
a.reverse()
print(a)

#sort() 는 정렬 (기본 오름차순 reverse=false임, 생략가능)
a.sort()
print(a)

#sort(reverse=True)는 내림차순으로 정렬되게 함(반대로)
a.sort(reverse=True)
print(a)

#리스트 지우기
a.clear()
print(a)

a = [10, 20, 30]
#len()길이로 슬라이싱으로 마지막이후부터 추가 가능
a[len(a):] = [500, 600]
print(a)

#b에다가 a값을 넣어줌 
#!여기서는 주소값만 넣어주는 것이므로 서로 다른놈이 아님 
b = a 

b[2] = 90 #? b변수를 바꾸었지만 a변수의 주소값을 가지고 있으므로 b를 바꾸면
#? a의 실제 value가 바뀜
print(a)
print(b) #* a와 b가 같은 결과가 나옴: b바꾸었지만 주소지의 값을 바꾸기 때문

#! copy()메소드를 이용하면 다른 주소를 가지게 된다 (서로다른놈이 됨)
b = a.copy()
b[2] = 99
print(a)
print(b) #* a와 b의 결과가 다름: b만 바뀜


#for문에서도 리스트의 값을 꺼내오면서 반복가능
for i in [23, 45, 67, 87, 53]:
    print(i, end=' ')

#enumerate()객체?를 이용하면 index값과 value를 값을 동시에 가져오면서
# 반복가능 index, value 변수로 받아서 사용

for index, value in enumerate(a):
    print(index, value)

#절취선
print("_" * 20)
#**start를 1로 주면 (인덱스는 0부터이지만)인덱스를 1부터 value와 매치시켜준다
for i, v in enumerate(a, start=1): 
    print(i,v)

