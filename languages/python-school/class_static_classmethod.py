#클래스 정적 메소드
class Calc:
    #static 으로 선언하기
    #? 키워드는 @staticmethod 를 붙여준다,
    #* 단, 파라미터에서 self를 사용하지 않는다
    # 정적으로 생성하면 이 자체로 메모리에 입력이 되서 
    # 객체를 생성하지 않고 바로 메소드를 호출해서 사용할 수 있다

    # @staticmethod는 객체를 생성안하고 접근할 수 있게 할려고 할 때 만듬
    @staticmethod
    def add(a, b):
        print(a+b)
    
    @staticmethod
    def mul(a, b):
        print(a*b)

#일반적은 클래스 사용은 객체를 생성한 후 사용을 하지만, static 메소드는 메모리에 올라가져있기 때문에 
#바로 access를 해서 사용 가능함, 단 클래스 이름은 적어줘야함
Calc.add(10, 5)
Calc.mul(10, 5)

class Person:
    #클래스 변수
    count = 0
    def __init__ (self):
        #* 일반 클래스안에서 정의된 변수는 클래스 자체를 참조 여기에서는 Person.count
        #여기에서는 공통으로 사용할 count변수에 계속 +1을 해주면
        Person.count += 1
    
    #* 클래스 메소드를 사용하려면 키워드 @classmethod 를 적어준다
    #* 메소드의 파라미터는 self가 아닌 cls 로 사용한다
    # cls는 class 자체를 의미 (self와 같은 의미이지만.. 여기서는 cls사용)
    # properties에 접근하려면 cls 로 하면 됨
    @classmethod
    def print_count(cls):
        print('{0}'.format(cls.count))

    # classmethod 선언, 파라미터는 cls로 받고
    # classmethod는 어떤 기능을 공유해서 사용할 때 사용한다 
    @classmethod
    def create(cls):
        # p변수에 자기자신을 준다, 즉 객체 생성 p = Person() 과 같은 의미가 된다
        p = cls()
        # 리턴을 해준다. 리턴을 받는 입장(변수)에서는 객체생성이 되게 된다
        return p 


james = Person()
maria = Person()

#? @classmethod를 이용해서 바로 object를 통하지 않고 바로 메소드를 접근하기
# 바로 class명을 적고 .(점)으로 접근해서 메소드명()을 입력
Person.print_count()

# classmathod를 사용할 때는 객체를 직접하지 않고 class에 직접 접근해서 사용한다
park = Person.create()

