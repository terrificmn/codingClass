'''
#연습문제
class Date:
    
    @staticmethod
    #staticmethod 파라미터는 self를 뺀다
    def is_date_valid(date):
        test = list(map(int, date.split('-')))
        if test[1] <= 12 and test[2] <= 31:
            return True
        else:
            return False

if Date.is_date_valid('2000-14-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')
'''

class Time:


    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second


    @classmethod
    def from_string(cls, time_string):
        #cls 키워드로 접근한 속성(프로퍼티)와 그냥 일반적으로 만들어진 속성(프로퍼티)는 다르다
        #**참고** 예 cls.hour 와 hour로 변수로 만들었을 때 서로 다른 결과가 나옴
        #! cls()의 의미는 자기자신 class 자체를 리턴할 수 있다. 즉, 클래스가 생성되는 효과
        #cls.hour, cls.minute, cls.second = map(int,time_string.split(':'))
        #return cls(cls.hour, cls.minute, cls.second)

        #여기에서는 메소드 내에서만 속성들을 사용할 것 이므로 변수로만 선언해서 사용 
        hour, minute, second = map(int,time_string.split(':'))
        return cls(hour, minute, second)

        #? 더 간단하게 하면 스태틱 메소드로 만들어진 변수 값을 통해 바로 cls()자신을 리턴해 줄 수도 있다
        #단, is_time_valid()메소드가 먼저 만들어 지지 않는다면 에러가 날 수 있다
        #return cls(Time.hour, Time.minute, Time.second)
    

    #? static으로 선언해서 클래스명으로 접근할 수 있게 한다
    #? static으로 만들어주면 class바깥에서는 클래스 이름으로 접근 예: Time.hour, Time.minute 이런식
    @staticmethod
    #* 스태택은 파라미터에 self를 넣지 않는다
    def is_time_valid(time_string):
        #각 변수에 입력받은 값을 split(":")으로 나눠서 넣어준다
        Time.hour, Time.minute, Time.second = map(int,time_string.split(':'))
        
        # 각각의 변수값이 조건에 맞을 때 true를 리턴할 수 있게 한다
        return Time.hour <= 24 and Time.minute <= 59 and Time.second <=60

        #hour, minute, second = map(int,time_string.split(':'))
        #return hour <= 24 and minute <= 59 and second <=60


time_string = input()

# static으로 선언된 메소드를 호출한다 
#* @staticmethod로 만들어진 메소드는 class명 .(점) 메소드이름 으로 접근할 수 있다 (아규먼트 인수로 입력받은 값을 넘겨준다)
if Time.is_time_valid(time_string):

    t = Time.from_string(time_string)
    # 조건이 맞으면 form_string 메소드를 호출하는데 객체가 생성되어 있지 않으므로 ,
    # classmethod 메소드 상태인 from_string 메소드를 호출한다
    # from_string 메소드에는 매개인수(arguments)로 넘어간 입력값을 나눠어서 각 변수에 넣어준 다음에 
    #** 클래스 cls()자체를 리턴해주는데 이러면 객체가 생성되는 효과가 난다. 
    # 즉, t변수는 객체가 된 것이고,
    print(t.hour, t.minute, t.second)
    # 여기 t변수 인스턴스가 생성이 되면서 바로 contructor 메소드가 실행이 되면서 (생성자)
    #각 인스턴스 변수들이 만들어진다 (그 시점은 from_string클래스 메소드가 리턴하는 시점에 
    # 매개인수로 이미 시간, 분, 초 데이터를 넘겨주므로 그 때 생성자 메소드에 의해 만들어지고 
    # 그래서 t변수는 객체로 사용이 되어서 t.hour, t.minute 처럼 속성을 (properties)에 접근할 수 있게 되는 것!
else:
    print('잘못된 시간 형식입니다.')
