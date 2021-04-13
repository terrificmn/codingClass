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
