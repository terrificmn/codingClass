#표준 입력으로 문자열 여러 개와 숫자(실수) 여러 개가 두 줄로 입력됩니다. 
# 입력된 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 
# 생성한 뒤 딕셔너리를 출력하는 프로그램을 만드세요. 
# input().split()의 결과를 변수 한 개에 저장하면 리스트로 저장됩니다.

#입력1-1
#health health_regen mana mana_regen
#입력1-2
# 575.6 1.7 338.8 1.63

#입력2-1
# health mana melee attack_speed magic_resistance
# 입력2-2
# 573.6 308.8 600 0.625 35.7

d1 = input().split()
d2 = list(map(float, input().split()))
d3 = dict(zip(d1, d2))
print(d3)

#list로 결합을 하기 위해서 list()로 만들어 줘야한다
#map()으로 해도 실행은 됨 
# (객체로 넘어오기 때문에 리스트로 해주는 것이 좋다고 함)