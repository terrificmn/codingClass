# 클래스로 점 구현
import math  # math 모듈을 이용하면 루트를 구할 수 있다 sqrt (SQuare RooT) 제곱근


class Point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point2d(x=30, y=20)
p2 = Point2d(x=60, y=50)

print('p1: {} {}'.format(p1.x, p1.y))
print('p2: {} {}'.format(p2.x, p2.y))

# 피타고라스의 정리로 두 점의 거리 구하기
# 임의의 직각삼각형에서 빗변을 한 변으로 하는 정사각형의 넓이는
# 다른 두 변을 각각 한 변으로 하는 정사각형의 넓이의 합과 같다
# a제곱 + b제곱 = c제곱

# y

# 60
#                                p2
# 50                          /|
#                           /  |
# 40                   c  /    |
#                       /      |  b
# 30                  /        |
#                   /          |
# 20           p1 /____________|
#                        a
# 10
#
# 0  10   20   30   40   50   60   x

a = p2.x - p1.x  # 선 a의 길이
b = p2.y - p1.y  # 선 b의 길이


c = math.sqrt((a * a) + (b * b))  # a*a, b*b 의 제곱근을 구함
print(c)

# 거듭제곱 (power)를 구하는 pow()함수를 사용해도 가능
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
print(c)

# 또는 파이썬 ** 거듭제곱 연산자 사용 가능
c = math.sqrt((a ** 2) + (b ** 2))
print(c)
