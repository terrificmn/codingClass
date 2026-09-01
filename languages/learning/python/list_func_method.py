a = [10, 20, 30]
'''
print(a)
a.append(500)  # append()메소드 마지막에 요소 추가
print(a)
'''

'''
a.append([500, 600])  # 중첩 리스트
print(a)
print(len(a))  # len()을 하면 4로 나옴
print(a[3])  # 마지막 배열; 리스트의 마지막 요소(중첩 리스트)
print(a[3][0])  # 중첩된 것의 첫번째 요소
'''
'''
#insert(인덱스, 요소)
a.insert(2, 500)  # 2번째 요소에, 500값 삽입
print(a)
'''
'''
# pop() 마지막 요소/특정인덱스 값 삭제
print(a.pop())  # 마지막 값 삭제 후 마지막 요소 반환
print(a)

a.pop(1)  # 인덱스 1 삭제
# del a[1] #같은 결과: a[인덱스1] 삭제
print(a)
'''
'''
# remove() 특정 값 삭제
a = [10, 20, 30, 20]
print(a)
a.remove(20)  # 특정 값 찾아서 삭제. 단, 처음에 찾은 것만 삭제
print(a)
'''

# index() 특정 요소 value를 찾아서 인덱스 반환
a = [10, 20, 30, 15, 20, 40]
print(a.index(20))  # index() 리스트에 20은 [1]인덱스, 1 반환
print(a.count(20))  # count() 리스트의 값의 개수 확인, 2개가 있으므로 2 반환

# reverse() 리스트의 순서 반대로
# sort() 또는 sort(reverse=False) 오름차순으로 정렬
# sort(reverse=True) 내림차순 (큰 값 부터 내림차순으로 정렬)
