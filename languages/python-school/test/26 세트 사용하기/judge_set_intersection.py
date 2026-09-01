# 표준 입력으로 양의 정수 두 개가 입력됩니다. 
# 다음 소스 코드를 완성하여 두 숫자의 공약수를 
# 세트 형태로 구하도록 만드세요. 
# 단, 최종 결과는 공약수의 합으로 판단합니다.

in1, in2 = map(int, (input().split()))

#표현식으롤 set 정의해주기 
#대신에 range함수(1 부터 시작, 역시 끝수는 포함하지 않게 되므로 끝수는 +1)
#표현식 마지막에 if문을 넣어주고 약수를 구해준다.
#입력 받은 수를 0으로 나눈것이 0으로 떨어지게 되는 것
a = {i for i in range(1, in1+1) if in1 % i == 0}
b = {i for i in range(1, in2+1) if in2 % i == 0}

#print(a)
#print(b)
# 교집합 구하기
divisor = a & b
result = 0

if type(divisor) == set:
    #sum()함수를 이용해서 간단하게 set의 요소를 더해준다
    result = sum(divisor)

print(result)
