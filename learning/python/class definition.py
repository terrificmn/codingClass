# class 정의
class MyClass:
    # methods
    # self 키워드는 클래스 자신을 의미
    def class_set(self, v):
        # 파라미터로 패스해서 받은 값을 value로 넣어줌
        self.value = v

    def class_get(self):
        return self.value


# 인스턴스 객체 생성  (클래스로 오브젝트 생성을 인스턴스라고 한다고 함)
obj = MyClass()
# 클래스의 메소드 호출
obj.class_set('5')
# class_get()메소드 호출
print(obj.class_get())

# 직접 클래스 접근을 해서 obj 인스턴스를 넘겨주면서 할 수도 있다
MyClass.class_set(obj, '10')
print(MyClass.class_get(obj))
# 결과가 5가 아닌 10으로 다시 set 된 것을 알 수 있다

# 생성자 constructor, 와 소멸자 destructor
# 인스턴스 (객체)가 생성될 때 자동으로 호출되는 method


class Myclass2:
    # constructor __init__
    def __init__(self):
        self.name = "Class"
        print('클래스가 생성되었습니다.', self.name)

    # 소멸자는 __del__
    def __del__(self):
        print('클래스가 소멸되었습니다.')


c = Myclass2()
