def div(x):
    return 10 / x

print(div(2)) #이상없이 실행됨
#print(div(0)) #0을 넘기면, ZeroDivisionError 오류가 발생

'''
#예외 처리 : 사용자가 직접 에러메세지를 보는 난감한 상황을 처리하기 위해서 예외를 처리
try:
    x = int(input('숫자 입력하세요: '))
    y = 10 / x
    print(y)
except:
    print('0으로 정수를 나누지 마세요.')
'''

'''
y = [10, 20, 30]
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 2개 입력하세요').split())
    print(y[index] / x)

#에러Type은 이미 정의가 되어 있음. 검색해서 사용하면 된다
# 에러 Type만 써주고 따로 print()으로 메세지를 출력하면 됨
# 미리정의된 에러메세지를 사용하려면 as e 라고 쓰고, 변수처럼 사용도 가능
except ZeroDivisionError as e:
    print('숫자를 0으로 나눌 수 없습니다.', e)
except IndexError as e:
    print('잘못된 인덱스 번호 입니다.', e)
#예외가 발생하지 않는 경우에 else 이후가 실행 됨
else:
    print('예외가 발생 하지 않음')

#예외가 발생하든지 안 하든지의 상관없이 최종적으로 처리 
finally:
    print('예외의 발생 유무와 상관 없이')

'''

'''
#고의로 예외 처리 발생 시키기
try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:
        #? 강제로 예외를 발생시키기 
        #강제로 발생시키는 키워드는 raise
        raise Exception('3의 배수가 아닙니다.')

# 원래 예외가 아닌, 문제는 없지만 일부러 예외로 만들어야 하
#? Exception type은 따로 정의되어있지 않는 예외에 대해서 키워드로 사용
except Exception as e:
    print('예외가 발생.', e)

'''

'''
#예외 타입 만들기 / 상속을 받아야 함 
# 상속 정의는 클래스명 뒤에 ()안에 상속받을 부모 클래스를 넣어준다
class NotThreeMulError(Exception):
    def __init__ (self):
        #아래는 정형화 되어 있는 코드
        super().__init__('3의 배수가 아닙니다.')

def mul():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:
            #강제로 예외를 발생시키기, 만들어 놓은 NotThreeMulError 클래스 사용
            #미리 정의가 된 클래스가 실행되며 
            raise NotThreeMulError
        #예외가 아닐 경우 아래 실행
        print(x)
        
    except NotThreeMulError as e:
        print('예외가 발생하였습니다: ', e)

mul()
'''
