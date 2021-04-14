import re

# 비밀번호 특수기호 포함시키기
def val_pass_char(password):
    regex = '[`!@#$%^&*()_+|]'
    if re.search(regex, password) is None:
        print('특수기호 없음')
        return False


# 비밀번호 길이 체크
def passwd_length(password) :
    if len(password) < 4 or len(password) >= 16 :
        return False


# 빈 문자열 검사
def val_empty(requestedData):
    strippedData = requestedData.strip(' ')
    if strippedData == ""  :
        print('one of requested data is null')
        return False


def val_number(number):
    regex = '^[0-9]+$'
    # 원래 json으로 숫자만 보내야하지만, 문자열 상태로 요청했을 때도 처리
    #숫자일경우 변환
    number = str(number)
    # 공백 제거
    number = number.strip(' ')
    if re.search(regex, number) is None :
        #print('only number')
        return False
