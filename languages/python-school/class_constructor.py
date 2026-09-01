#class: 객체를 표현하는 형식
#properties, methods
#properties는 class내의 선언된 속성이며 변수를 의미하고
#properties는 attribute라고도 한다
#methods는 기능을 담당하는 함수의 역활을 한다

#클래스 정의
# 클래스의 이름은 대문자로 시작하는게 좋다. (딱 봤을 때 클래스인지 알아보기 쉬움)
class Person:
    #함수의 메소드의 파라미터에는 self를 넣어준다 (class를 의미)
    def greeting(self):
        print('안녕하세요')

#클래스 생성 instanace (메모리 할당이 됨)
mike = Person()
#생성된 객체: 인스턴스의 메소드를 참조 접근하기위해서는 .(period)를 적어주고 접근한다
#객체.메소드()
mike.greeting()

#class constructor: 클래스를 이용 객체가 생성되었을 때 처음으로 실행이 됨
class MarkOne:
    age = 25
    #constructor 메소드 
    def __init__ (self):
        #property 생성
        #속성은 self를 키워드로 먼저 입력한 후에 . (점)으로 접근한다 
        #self은 자기자신 현재 PersonOne class를 의미
        self.hello = '안녕하세요'
        self.name = '둘리'

    def greeting(self):
        print(self.hello, self.name)

#object 생성 / 메모리의 어딘가에 위치한 PersonOne 클래스의 주소를 참조하게됨
john = MarkOne()
#단 메소드에 접근할 때는 아규먼트를 넘길 때 (self)를 적지않는다
john.greeting()
#클래스 속성에 접근
print(john.age)
print(john.hello)


#constructor 메소드에 파라미터(매개변수) 정의하기 
#** self 는 반드시 넣어준다
class MarkTwo:
    # 파라미터 정의 해주기 (self는 처음에 적어준다)
    # 실제 객체를 생성하면서 아규먼트로 넘어오면 생성자 메소드가 self.속성 값들을 정의해 주게된다
    def __init__ (self, name, age, address):
        #인스턴스 객체라고 함 (self.속성)
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print("{0}. 나는 {1} 입니다".format(self.hello, self.name))
    
    def introducing(self):
        print("나이는 {0}, {1}에 산다".format(self.age, self.address))

#obj인스턴스 생성
james = MarkTwo('제임스', 28, '인천')
james.greeting()
james.introducing()
print(james.name)
print(james.age)


class MarkThree:
    #클래스 변수 (일반적인 변수)
    bag = [] #list
    def put_bag(self, stuff):
        self.bag.append(stuff)

#객체 생성
robin = MarkThree()
robin.put_bag('열쇠')
#bag속성은 일반변수로 선언되었기 때문에 공통적으로 쓰이게 됨 
#__init__메소드로 할당해서 만들어준 변수가 아니기 때문에 조금 차이가 있다

#maria 객체를 만들었는데도 클래스변수로 선언이 되어 있는 bag을 쓰게되면
#공통으로 사용해서 위의 robin객체와 아래 maria객체가 bag 변수를 같이 쓰게 됨
maria = MarkThree()
maria.put_bag('책')
#서로 bag 속성을 불러오면 같은 값을 공유한 것을 알 수 있음
print(robin.bag)
print(maria.bag)

class MarkFour:
    #? 위의 MarkThree 클래스와는 다르게 여기에서는 생성자 메소드를 이용해서
    #? 생성해주게 되면은 객체의 각각 서로 다른 bag 변수를 사용할 수 있게 됨
    def __init__ (self):
        self.bag = []

    bag = [] #list
    def put_bag(self, stuff):
        self.bag.append(stuff)

robin2 = MarkFour()
maria2 = MarkFour()
robin2.put_bag('열쇠')
maria2.put_bag('책')

