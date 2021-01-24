class Person:
    def greeting(self):
        print('안녕하세요')


class University:
    def manage_credit(self):
        print('학점 관리')

# 다중 상속은 ,콤마로 구분해서 기반 클래스를 넣어주면 됨


class Undergraduate(Person, University):
    def study(self):
        print('공부하기')


mark = Undergraduate()  # 인스턴스 생성 #2개의 기반 클래스를 상속받음
mark.greeting()  # Person 클래스의 메소드 콜
mark.manage_credit()  # University 클래스의 메소드 콜
mark.study()  # 물론 자기 클래스의 메소드도 콜
