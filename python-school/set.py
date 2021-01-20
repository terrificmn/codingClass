#set
#중복을 허용하지 않음
#시퀸스 객체가 아니다
#세트는 { }(중괄호) 안에 값을 저장하며 각 값은 ,(콤마)로 구분

#set 이용해서 만들기
x = set(range(5))
print(x)

#set은 {}중괄호로 묶어서 만들어 주면 됨
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

#set객체 이용해서 union()메소드를 사용하면 두개의 아규먼트를 넘겨주면 합집합을 만들어줌
#합집합에서는 중복요소가 있으면 한개만 처리한다
print(set.union(a, b))
#그냥 기호로 | 같은 합집합을 할 수 있음
print(a|b)

#차집합
#a집합에서 b집합을 빼버림, (겹치는 부분)
#set.difference(a, b)
print(a-b)

#교집합
# 중복된 것을 집합 (공통)
print(a&b)

#대칭차집합
print(a^b)

a = {1, 2, 3, 4}
#차집합으로 빼기
a |= {5}
print(a)
# 요소 삭제
a -= {3}
print(a)

#추가
a.add(5)
print(a)
#삭제
a.remove(4)
print(a)
#pop으로 지울 때는 리스트에서 사용할 때와는 다르게 랜덤으로 지워지는것에 유의
a.pop()
print(a)

a = {1, 2, 3, 4, 5} #set 만들어 주기
for i in a:
    print(i) #set 요소 출력
#표현식으로 set 만들기 {}중괄호로 묶고 처음 키워드는 입력될 데이터
#그 다음은 for문을 써주고 어떤것을 반복할 지 마지막에 써 주면 됨 (여기서는 "apple"문자열)
a = {i for i in "apple"}
print(a)
#! set이 만들어 지는데 셋은 중복을 허용하지 않으므로 (p가 2개) 
#! p는 한개만 넣어서 만들어지고, 순서는 없음, 랜덤으로 만들어진다

