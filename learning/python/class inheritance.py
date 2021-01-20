class A:
    # 아무것도 안할때는 pass를 써 줘야함 (파이썬에서는)
    pass


class B:
    def f(self):
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
