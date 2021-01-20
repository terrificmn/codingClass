# time 모듈
import time
# 현재시간 함수 ctime()
print(time.ctime())
# sleep() 파라미터 만큼 멈춤 예: 3은 3초
time.sleep(3)
print(time.ctime())


class Life:
    # __는 예약된 키워드라는 것을 의미함, 즉 생성자는 __init__ 키워드로만 사용
    def __init__(self):
        # self 키워드는 현재 클래스 의미 .birth는 property인 듯 하다
        self.birth = time.ctime()
        print("시작", self.birth)

    # __는 예약된 키워라는 것을 의미함, 즉 소멸자는 __del__ 키워드로만 사용
    def __del__(self):
        print("끝", time.ctime())


def time_test():
    # 인스턴스 생성
    l = Life()
    time.sleep(3)


time_test()
