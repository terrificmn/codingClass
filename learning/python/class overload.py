class A():
    def __init__(self, i):
        self.i = i

    def __str__(self):
        return str(self.i)

    def __add__(self, other):
        # 클래스 자신 말고, 다른 파라미터가 들어왔을 때 +를 연산을 시키면
        # 리턴은 자신과 - 2번쨰 파라미터 값을 해서 리턴해서 결과는 -결과 값이 됨
        return self.i - other


# 인스턴스 생성
a = A(10)
# a 변수에는 contructor 로 인해 파라미터 값이 들어가지고
# 더하기 5를 했지만 __add__ overload에 의해서 -연산이 되게 됨
print(a + 5)

# * 오버 라이딩 overriding


class Skynet:
    def greeting(self):
        print('안녕하세요 스카이넷 입니다')


class Robot (Skynet):
    def greeting(self):
        print('안녕하세요 로봇 입니다')


ai = Robot()  # 인스턴스 생성 (Robot은 Skynet을 상속받았음)
ai.greeting()  # greeting메소드를 호출하지만 부모의 greeting메소드가 아닌 Robot class의 메소드 호출이 됨
# override는 상속받은 기반 클래스의 메소드를 무시하고 새로운 메서드를 만듬

# 같은 메서드 이름으로 계속 사용되어야 할 경우 사용한다고 함
print('--------------------------')


class Skynet1:
    def greeting(self):
        print('안녕하세요')
        # Skynet1, Robot1의 오버라이딩한 greeting의 기능이 '안녕하세요' 이 부분이 같다고 하면
        # 중복되는 부분을 파생 클래스에서 만들지 않고, 기반 클래스(현재 Skynet1 클래스)의 기능을 살리면서 하면되는데
        # 자식클래스에서 super().메소드명()을 하면 오버라이딩한 메소드를 호출했을 때 부모클래스의 메소드로 사용할 수 있게 만들 수 있음


class Robot1 (Skynet1):
    def greeting(self):
        # 예를 들어, 여기에서 중복되는 안녕하세요는 빼고 super()를 이용해서 부모클래스의 메서드를 호출해준다
        super().greeting()
        # print('안녕하세요 로봇 입니다')   #중복기능 제거
        print('로봇 입니다.')


ai1 = Robot1()
ai1.greeting()
# 그래서 오버라이딩은 원래 기능을 유지하면서 새로운 기능을 덧붙일 때 사용함
