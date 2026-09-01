#key:value 로 이루어짐
#{'key':value} 형태로 이루어 짐
#associative array 생각해도 될 듯
#중복되는 키는 저장되지 않음
#중복되는 키는 가장 뒤에 있는 값만 사용
di = {'health':490, 'mana':334, 'melee':550, 'armor':18.72}
print(type(di)) #<class 'dict'
print(di)

#키와 값의 type이 여러 방식으로도 가능
di2 = {100:'text', False:0, 3.4:[2,3]}
print(di2)

#x변수에 {} (dictionary로 정의 (빈 딕션너리)
x = {}
print(x)

#******dict()함수로도 정의 가능 다양하게 정의가 가능
x2 = dict()
#dict()에서는 {}중괄호로 감싸서 key:value 써 준다
x2 = dict({'key': 'value'})
#절취선
print("_" * 80)
#[]대괄호로 묶어서 [(key, value), (key, value)] 도 가능
# tuple형식으로 만든 것을 리스트로  만듬
x2 = dict([('key1', 10), ('key2', 20)])
print(x2)
#dict()함수에 그냥 (key=value, key=value) 로 정의도 가능
#단, key가 문자열일때에도 '(signle qutation)을 빼준다. 예: dict(key1=10)
x2 = dict(key1=10, key2=20)
print(x2)

#key 는 중복을 허용하지 않는다 (컬럼명이 중복이 될 수 없다고 생각하면 될 듯)
di = dict({'health': 400, 'health': 500, 'mana': 334, 'melee':550, 'armor': 18.72})
#같은 키가 있다면 뒤에 오는 key 의 value를 사용함
print("중복은 뒤에꺼만 사용", di)
#value는 중복을 허용


#절취선
print("_" * 80)
#튜플형태로 만들기 딕션너리 만들기
di3 = dict(health=400, mana=334, melee=550, armor=18.72)
print((type(di3)))
print(di3)

#zip()함수를 이용해서 각각 []리스트로 [key-리스트], [value-리스트]로 만들어 딕셔너리로 만듬
#zip()함수는 리스트를 결합? 해줌
di3 = dict(zip(['health','mana','melee','armor'], [400, 332, 550, 18.72]))
print(di3)

#리스트형태로 []로 묶어서 딕셔너리 만들기
di4 = dict([('health',400),('mana',334),('melee',550),('armor',18.72)])
print(di4)

#오리지널 방법 {}중괄호 사용
di5 = dict({'health': 400, 'mana': 334, 'melee':550, 'armor': 18.72})
print(di5)


#절취선
print("_" * 80)
#key로 접근해서 value 받아옴 (associative array와 유사)
print(di5['health'])
#각각의 키들에는 int value가 있으므로 + 연산 가능
print(di5['health'] + di5['mana'])

di5['health'] = 2021
print(di5['health'])

#새로운 key와 value를 추가할 수 있다 (기존에 없다면 새로 추가함(마지막에 추가됨))
di5['mana_regen'] = 3.25 
print(di5)


#연습문제
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}

print(camille['health'])
print(camille['movement_speed'])


