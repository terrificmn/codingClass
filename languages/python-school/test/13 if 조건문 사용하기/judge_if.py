''' 퀴즈:
표준 입력으로 가격(정수)과 쿠폰 이름이 각 줄에 입력됩니다. 
Cash3000 쿠폰은 3,000원, Cash5000 쿠폰은 5,000원을 할인합니다. 
쿠폰에 따라 할인된 가격을 출력하는 프로그램을 만드세요
(input에서 안내 문자열은 출력하지 않아야 합니다).
'''
money = int(input())
coupon = input()

if coupon == "Cash3000" or coupon == "Cash5000": #둘 중에 하나일 때
    print(money - int(coupon[4:])) #coupon으로 받은 변수에서 4번째 이후부터만  (0부터시작)사용해서 int로 계산


