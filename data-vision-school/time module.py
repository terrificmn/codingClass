#날짜와 시간 모듈
from datetime import date 
today = date(2021, 2, 4)
print(today)

today.weekday() #요일 반환, 해당 요일에 맞는 숫자 리턴
# 0: mon, 1: tue, 2: wed, 3:thu, 4: fri, 5: sat, 6: sun

today.isoformat() #전세계 표준형식 지정
#'2021-02-04' 으로 출력

today.strftime('%Y/%m/%d') # 원하는 형식으로 바꿈
'''
%Y 앞의 빈자리 0으로 채우는 4자리 연도 숫자
%m 앞의 빈자리 0으로 채우는 2자리 월 숫자
%d 앞의 빈자리 0으로 채우는 2자리 일 숫자
%H 앞의 빈자리 0으로 24시간 형식 2자리 시간 숫자
%M 앞의 빈자리를 0으로 채우는 2자리 분 숫자
%S 앞의 빈자리를 0으로 채우는 2자리 초 숫자
%A 영어로 된 요일 문자열
%B 영어로 된 월 문자열
'''

from datetime import time #datetime 모듈에서 time 사용
today = time(15, 23, 11)
today.isoformat()

#속성 hour, minute, second 속성으로 접근
print(today.minute)  
print(today.hour)
print(today.second)

#또는 isoformat() , strftime(%y) 의 메소드 사용


from datetime import datetime
today = datetime.today()
print(today)
today.weekday() #weekday()메소드
#속성
today.year
today.month


#시각 다루기
import time

# UTC 시간 가져오기
print(time.gmtime()) #영국 그린위치 천문대 기준의 시간을 가져옴

#local시각 가져오기
print(time.localtime())

# 문자열의 날"짜를 파이썬이 계산할 수 있는 모듈

#from dateutil.parser import parse 
day = '2021-02-04' #일반 문자열 데이터
p_day = parse(day) #parse()함수로 날짜타입으로 변환

print(p_day)



