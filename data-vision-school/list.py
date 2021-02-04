#리스트 만들기 
# []로 묶거나 list() 함수 사용

names = ["sara", "chanel", "mike", "ryan", "holy", "alex", "rob"]

#각 이름의 맨 앞자를 대문자로 다시 names 리스트로 만들기
count = 0
for i in names:
    names[count] = i.title()
    count += 1

# 좀 더 쉬운 방법
names_newList = [] #리스트 변수 하나 만들기
for item in names:
    names_newList.append(item.title())  #단순히 item변수에 저장된 값들을 .title()메소드로 앞글자만 대문자로
    # names_newList 에 바로 추가

# 좀 더더 쉬운 방법 (코드 한줄)
#item.title() for item in names # names리스트 변수에서 item.title()으로 대문자로 바꾼 후 item에 하나씩 넣어주고 

print(names[1]) #두번째 항목 인덱스 접근
print(names[-1]) #마지막 인덱스에 접근하는 가장 편한 방법 -1

#인덱싱 
print(names[1:4])  #2번째 숫자의 마지막은 적용안됨 (-1)

#리스트 안에 리스트로 되어 있을 때
my_list = ["Mitch", ["sara", "sally", "joe"], "peter", "aly"]

#풀이법 
#리스트에 하나씩 접근해본다
#[1]의 요소에는 2차원으로 구성 []한번더 접근
print(my_list[3], my_list[1][1], my_list[2:] )

length = len(my_list) #마지막 요소 인덱스를 알아낸 뒤
my_list.insert(length, "Insert_NAME")

#리스트의 오름차순 정렬  sort()메소드의 기본값으로 사용
my_list.sort()

#리스트의 내림차순 정렬
my_list.sort(reverse=True)

#리스트안에 리스트에서 맨 마지막의 항목만 뽑아서, 새로운 리스트 만들기
grocery_list = [['chips','jelly','chocolate'],['sweet potatoes','potatoes'],['peanuts','protein bar']]

newlists = []
for alist in grocery_list:
    #print(alist)
    i = len(alist) -1 #정확한 마지막 수를 맞추기 위해서 -1함
    newlists.append(alist[i])
    
# 가장 쉬운방법은 [-1] #인덱스 마지막을 가져온다
#newlists.append(alist[-1])
    
# 한줄
# data[-1] for data in grocery_list

#문자열에 공백 제거
essay = "She had a lot of money. She was a generous woman."
essay_list = essay.split()  #split()은 리스트로 만들어 줌

# count() 해당문자열 개수를 리턴
essay.count('to')  #문자열에서는 '찾는문자열' 이 포함된 모든것을 카운트
essay_list.count('to') #리스트 내에서는 'to' 단어가 to인것만 찾음 (찾는 문자열)

