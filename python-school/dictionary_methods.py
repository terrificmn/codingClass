x = {'a':10, 'b':20, 'c':30, 'd':40}
print(x)
#update()메소드 해당 key의 value를 업데이트 해준다(수정)
#키값은 ''(따옴표)로 묶지 않는다 (''를 사용하면 에러 발생)
x.update(a = 90)
print(x)
#해당 키가 없다면 새로 만들어서 업데이트 해준다
x.update(a=900, f=60)
print(x)

y = {1: 'ONE', 2: 'two'}
#? 리스트 식으로 묶어서 2개로 넘겨주면, [대괄호]의 1요소는 key, 2요소는 value 처리되어 업데이트 됨
y.update([[2, 'TWO'], [4, 'FOUR']])
print(y)

#zip() 함수를 이용해서 리스트 방식으로 처리할 수 있음
#zip()함수는 update와 방식이 좀 다름
#? zip([1번째리스트의 value, value], [2번째리스트의 value, value]) 
#? 해주면 1번 리스트와 2번리스트를 매칭해서 첫번째가 키가 되고  2번째가 value로 넘어감
y.update(zip([1, 2],['one', 'two']))
print(y)

print('-------------')
#** associative array와 비슷한 듯 해서 여기서 인덱스로 접근하는 것이 아니고 
#** Key로 접근하는 것 
#? 여기서 [1] 인덱스가 아니고 key 임, y의 1 key의 내용을 바꿈
#? y[0]으로 이렇게 하게 되면 없기때문에 마지막에 추가된다
y[1] = 'Five'
print(y)

x = {'a':10, 'b':20, 'c':30, 'd':40}
#get함수는 키 값의 내용을 받아온다
print(x.get('a'))

#items(), keys(), values() 메소드는 각각 해당 딕셔너리의 데이터를 보여줌
#각각 아이템, key이름, value값
# 이 메소드들은 아규먼트 없음
print(x.items()) #해당 딕셔너리의 구성요소를 다 보여준다
print(x.keys()) #해당 딕셔너리의 keys만 보여줌
print(x.values())  #해당 딕셔너리의 values만 보여줌

#리스트와 튜플을 딕셔너리로 변경
keys = ['a', 'b', 'c', 'd'] #리스트 만들기

# **dict객체의 fromkeys()메소드에 keys라는 키워드를 주면 딕션러니로 만들어 준다
# * fromkeys(keys) 만 사용하면 value는 None으로 들어가 짐
x = dict.fromkeys(keys)
print(x)
#? keys, value)
x = dict.fromkeys(keys, 200)
print(x)

print("----------------------------")
#dictionary 생성
x = {'key1': 10, 'key2': 20, 'key3': 30, 'key4': 40} 

for i in x:
    print(i, end=' ')
print()
#for문으로 key, value 값만 받아와서 반복할 수 있음
for key, value in x.items():
    print(key, value)

# x 딕션너리에 values()메소드로 value값만 가져온다
for value in x.values():
    print(value)

# x 딕션너리에 keys()메소드로 key값만 가져온다
for key in x.keys():
    print(key)



keys = ['a', 'b', 'c', 'd']
#? 표현식 사용해서 한줄로 딕션너리로 변환 생성
x = {key:value for key, value in dict.fromkeys(keys).items()}
print(x)

'''
#! 반복문을 실행할 때는 딕션너리는 사이즈는 바뀌면 안됨!
#! for문상에서 아래처럼 del x[key]로 직접 삭제가 안됨
#! 이유는 for문 돌아갈 때 해당 value가 지워지면 논리적 오류가 생겨서 안됨
for key, value in x.items():
    if value == 20:
        del x[key] #해당 key에 value를 지우는 명령어지만 실제로는 수행되지 못함
print(x)
'''

x = {'a': 10, 'b': 20, 'c': 30, 'd':40}
#* for문으로 딕셔너리의 요소가 삭제가 안되므로 새로 x변수에 다시 구성으르 해서 
#* if문에서 20이 아니면 key:value를 그대로 생성해서 만들어주는 우회적인 방법
# 결과는 삭제한거 같은 효과
#? 방식은 처음은 key:value for문 x변수에 items()메소드 실행 마지막은 if문
# 방식은 외우기?
x = {key:value for key,value in x.items() if value != 20}
print(x)

# 딕셔너리 중첩구조로 만들기 
x = {'a':{'python': '2.7'}, 'b':{'python':'3.6'}}
print(x['a'])
# ** b key값의 value 바꾸기 2차원으로 접근해야한다
x['b']['python'] = '3.9'
print(x['b'])


'''
# 리스트를 이용해서 데이터를 입력받아서 딕셔너리 변수로 만들어 주는 프로그램
dict_list = []
while True:
    sel = int(input('1번은 딕셔너리 생성, 2번은 종료!'))
    if sel == 1:
        my_dict = {} #my_dict 딕셔너리 변수로 정의
        print('요소추가를 추가해주세요: ')
        while True:
            key = input('key입력해주세요: ')
            val = input('value입력해주세요: ')
            my_dict[key] = val
            con = int(input('1번은 딕셔너리 생성, 2번은 종료!'))
            if con == 2:
                print('입력 종료')
                break
        #요소 추가 시킴, my_dict 변수는 딕셔너리로 만들어 짐
        dict_list.append(my_dict) #리스트안에 my_dict딕셔너리가 추가되어 만들어짐
    elif sel == 2:
        print('2번 입력됨 종료')
        break
    else:
        break

print("결과 :", dict_list)
'''
