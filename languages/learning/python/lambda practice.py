a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
# 서로 더하는 람다 함수
list1 = list(map(lambda x, y: x + y, a, b))
print(list1)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 람다 함수로 짝수만 리스트에 새로 생성하기
# map 함수로만 사용할 경우에는 if문을 사용하면 꼭 else를 넣어줘야한다. 아니면 에러발생
# todo: 원하는 짝수가 안나옴, 공부 필요!
list1 = list(map(lambda x: x if x % 2 == 0 else x, a))
print(list1)

# 입력을 받고 받은 수를 리스트로 만들면서 format메소드를 이용해서 변환시키기, 숫자는 3자리로 만들기
# 입력할 문자열 1.jpg 10.png 11.png 2.jpg 3.png
f = input('입력하세요: ').split()

print(list(map(lambda x: "{0:03d}.{1}".format(
    int(x.split('.')[0]), x.split('.')[1]), f)))
#list(map(lambda x: '{0:03d}.{1}'.format(int(x.split('.')[0]), x.split('.')[1]), files))
