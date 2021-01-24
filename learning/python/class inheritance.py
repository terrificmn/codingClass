class A:
    # 아무것도 안할때는 pass를 써 줘야함 (파이썬에서는)
    pass


class B:
    def f(self):  # method의 파라미터에는 꼭 self를 넣어준다.
        pass


# 상속을 해줄 떄는 자식 클래스명 (부모클래스명)으로 함
class C(B):
    pass


# 오브젝트 생성
obj = A()

# isinstance(비교인스턴스, 클래스) instnace 인지 확인 True, False 리턴
print(isinstance(obj, A))

# 자식 클래스 인지 확인 (첫번째파라미터가 두번째파라미터의 subclass인지 확인)
print(issubclass(A, B))  # A class는 B class의 자식클래스 아님
print(issubclass(C, B))  # C class는 B class의 자식클래스 임


class Asia():
    def __init__(self, name):
        self.name = name

    def show(self):
        return "해당 국가는 아시아에 있습니다."


class Korea(Asia):
    def __init__(self, name, population, capital):
        # Asia 클래스한테 inheritance를 받아서 Asia 클래스의 contructor 메소드를 실행해준다
        # 즉 상속받았으므로 (속성, 메소드) 부모 클래스의 메소드에 접근 가능
        Asia.__init__(self, name)
        self.population = population
        self.capital = capital

    def show_name(self):
        return "국가 이름은 : ", self.name


# 오브젝트 생성
nation = Korea('대한민국', '5천만', 'seoul')
# Korea클래스로 생성된 nation에서 메소드에 접근할 떄는 .메소드()
# 부모 class를 상속 받았으므로 부모 클래스의 메소드도 사용할 수 있다 nation.show() 메소드()
print(nation.show_name(), nation.show())


class Person:
    def greeting(self):
        print('안녕하세요')


class Student(Person):  # 상속 받기
    def study(self):
        print('공부하기')


mike = Student()  # 객체 생성, Studend는 Person클래스를 상속받았음
mike.study()
mike.greeting()  # 부모클래스(Person)의 메소드인 greeting()을 호출할 수 있다

# 포함 관계 (상속을 하지않고 속성으로 관리, 여기에서는 person_List 속성)


class PersonList:
    def __init__(self):
        self.person_list = []

    def append_person(self, person):
        self.person_list.append(person)


# 위에 처럼 사람-학생이 아니고 사람-사람 이라면 포함관계라고 함
# 상속개념이 아닌 포함 관계라고 부르고, 사람 목록은 사람을 가지고 있다. has-a 관계(PersonList has a Person) 이런 관계라고 함
jack = PersonList()  # 학생이 아닐 경우, 클래스를 Student()으로 생성하지 않고, PersonList()로 인스턴스 만든다
jack.append_person('jack')  # apeend_person()메소드를 이용해서 속성만 추가해준다
print(jack.person_list)
# 이런것을 포함관계라고 함

# super() 기반클래스 부모클래스 초기화
# 상속을 받았다고 해도, 기반클래스(부모클래스)가 __init__ 또는 생성이 안되서 자체의 속성(properties) 가 생성이 안되었다면
# 부모클래스의 속성을 사용할 수가 없음
# 이때 super() 사용할 수 있다고 함


class Person1:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요'


class Student1(Person1):
    def __init__(self):
        print('Studen class __init__ has been initiatived')
        super().__init__()
        self.school = '학생 입니다'


alice = Student1()
print(alice.school)
print(alice.hello)
# 여기에서 Person1 클래스의 hello property는 Person1 자체가 생성이 된 적이 없어서 에러가 나야하지만
# Student1 클래스에서 super().__init__() 으로 인해서 즉, 기반클래스(부모)를 초기화되어서 속성이 만들어 짐
# 단, 파생(자식)클래스에서 pass로만 되어 있으면,(__init__ 메소드가 없다면..)
# 기반클래스의 __init__은 자동 호출된다고 함
