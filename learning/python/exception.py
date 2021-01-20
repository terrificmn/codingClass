a = input("정수 입력: ")

# try except 일반오류 제어
try:
    a = float(a)
    print("반지름: ", a)
    print("둘레: ", 2 * 3.14 * a)
    print("넓이: ", 3.14 * a * a)

except:
    print("error")

# 예외를 그냥 넘어가고 싶은 경우 pass 키워드 사용
# 프로그램 실행에 치명적이 않는 오류이나 프로그램 진행 하고 싶을 경우
num = ["3", '안녕하세요', '4', 2.67, 'python']
digit_num = []

for i in num:
    try:
        # int값만 넣어 주고 싶을 떄 , int가 아니면 에러가 나지만
        digit_num.append(int(i))
    # 그냥 넘어가고 싶을 때는 pass
    except:
        pass
# 이렇게 하면 결과는 [3, 4, 2]로 되서 나오게 된다
print(digit_num)

# try: 실행할 코드(에러 없을때), except: 예외코드, else: 그 밖에 경우 코드
# try, except, else, finally: (else와 finally는 예외 발생 유무에 관계 없이 실행되는 코드작성 가능)

# 예외 객체와 예외 구분
# num 변수는 위에 정의 됨(참고)
try:
    a = input("정수를 입력 해주세요: ")
    a = int(a)
    print(a, "번째 요소는 : ", num[a], '입니다.')
# 문자를 입력했을 때
except ValueError:
    print("정수를 입력해 주세요")
# index범위를 초과했을 때: 현재 num변수의 index는 5개
except IndexError:
    print("리스트의 범위를 벗어났습니다.")


# 구구단 예외 처리
# try, except으로 처리하고
# try에서 실행되는 코드도 if문으로 제어, elif, else

nbr = input("2~9사이의 숫자를 입력하세요: ")
try:
    if(nbr.isdigit()):
        # 입력받으면 숫자여도 str 로 되기 때문에 변환해줌
        nbr = int(nbr)

    if(nbr > 9):
        nbr = 9
    elif (nbr < 2):
        nbr = 2
    else:
        nbr = nbr

    for i in range(1, 10):
        print("{} x {} = {}" .format(nbr, i, nbr*i))

# 미리 정의된?(예외객체) 키워드로 msg변수에 할당해서 print처리
except Exception as msg:
    print("예외 발생 :", msg)

# 참고
# 숫자를 0으로 나눌때 예외는 ZeroDivisionError
# 예외를 강제로 발생시키는 키워드는 raise
