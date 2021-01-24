#import abc
# abc 모듈은 Abstract Base Class 의 약자
# import abc만 한다면
# 참고로 추상클래스를 만들 때 모듈이름을 적어주고 사용하게 된다
# 예: 추상클래스 만들때
# class PersonBase(metaclass=abc.ABCMeta):


from abc import *
# abc 모듈의 모든 것을 다 가져오면 모듈이름은 생략한다
'''
class StudentBase (metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass


class Student(StudentBase):
    def study(self):
        print('공부하기')


james = Student()
james.study()
'''
# 위의 코드를 실행하면 타입에러가 발생한다
# TypeError: Can't instantiate abstract class Student with abstract method go_to_school
# 추상클래스는 @abstractmethod로 메소드 위에 정의해 주는데
# 상속 받은 자식클래스에서는 추상메서드로 모두 구현해야한다


class StudentBase (metaclass=ABCMeta):  # 추상클래스로 정의하려면 파라미터에 metaclass=ABCMeta 라고 정의한다
    @abstractmethod  # 추상클래스의 추상 메소드에는 @abstractmethod를 적어준다
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass


class Student(StudentBase):  # 상속받기 (추상클래스 상속)
    def study(self):
        print('공부하기')

    def go_to_school(self):  # **상속받은 파생클래스에서는 상속받은 모든 추상 메소드를 구현해야한다
        print('학교가기')


# 이렇게 하면 맨 위의 예제와는 다르게 에러 없이 잘 실행 됨
james = Student()
james.study()
james.go_to_school()

# ** 추상 클래스는 인스턴스화 할 수 없다.
# alice = StudentBase()  #인스턴스하면 아래처럼 에러가 발생
# TypeError: Can't instantiate abstract class StudentBase with abstract methods go_to_school, study
# 그래서 추상클래스의 추상메서드는 pass를 넣어 빈 메서드로 만들고
# @absractmethod
# def study(self):
#   pass
# 상속받은 파생 클래스나 자식클래스에서 해당 메소드를 구현해줘야 함
