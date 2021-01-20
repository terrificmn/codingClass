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
