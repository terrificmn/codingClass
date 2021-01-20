'''
#연습문제 평균 구하기
maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
average = sum(maria.values()) / len(maria)
print(average)
'''

#표준 입력으로 문자열 여러 개와 숫자 여러 개가 두 줄로 입력되고, 
# 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성합니다. 
# 다음 코드를 완성하여 딕셔너리에서 키가 'delta'인 키-값 
# 쌍과 값이 30인 키-값 쌍을 삭제하도록 만드세요.

keys = input().split()
values = map(int, input().split())
# x를 dict()이용해서 zip()함수로 묶어서 만들어 준다
x = dict(zip(keys, values))

x = {key:value for key, value in x.items() if key != 'delta' and value != 30}
print(x)

# x변수를 다시 딕셔너리로 다시 {}로 딕셔너리로 다시 정의
# key:value 값을 넣어주는데 기존 x딕셔너리를 for문으로 반복해 주고,
# 이어서 if문이 마지막에 오는데 key가 delta가 아니고 and value가 30이 아닐 때만 수행될 수 있게 한다
# 그래서 결과적으로 키 값이 delta가 아니면서 동시에 value가 30인 것을 제외하고 
# 처음의 key:value로 딕셔너리 상태로 만들어 지게 된다
