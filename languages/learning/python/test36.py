# 연습문제
# list를 상속받는 AdvancedList 클래스를 만들고 특정 데이터를 받아 특정 데이터로 바꾸는 메소드를 만들기
# list 도 클래스여서 바로 상속받는게 가능
class AdvancedList(list):
    def replace(self, findN, replaceN):
        while findN in self:
            self[self.index(findN)] = replaceN
# 리스트에서 특정 요소가 있는 지 확인할 때는 in 연산자를 사용,
# 리스트에서 요소를 계속 바꾸다가 바꿀 값이 없으면 반복을 끝냄
# 반복을 while self.count(findN) != 0: 이것도 가능하다고 함


x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)


# 다중 상속
class Animal:
    def eat(self):
        print('먹다')


class Wing:
    def flap(self):
        print('파닥거리다')


class Bird (Animal, Wing):
    def fly(self):
        print('날다')


b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))
