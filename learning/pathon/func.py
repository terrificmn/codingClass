def test(a):  # function 예
    if a > 10:
        return 'a is greater than 10'
    else:
        return 'a is smaller than 10'


print(test(15))

# lambda 함수로 한줄로 정의 하기 (이름없는 함수 쯤 되는 것 같다)
# 정확히는 리스트 내포, 조건부 표현식 등과 같이 여러 줄의 코드를 간결하게끔
# 새로운 함수 정의 방법 이라고 함
print((lambda a: 'a is greater than 10' if a > 10 else 'a is smaller than 10')(14))
# lambda a 매개변수: True실행될 코드 is조건 False실행될 코드 (넘겨줄숫자)
