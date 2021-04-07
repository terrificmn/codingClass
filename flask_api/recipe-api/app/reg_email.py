import re

def validation(email):
    regex = '^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$'
    
    # 공백 제거
    email = email.strip(' ')
    
    if not re.match(regex, email) :
        print('password wrong')
        return False

