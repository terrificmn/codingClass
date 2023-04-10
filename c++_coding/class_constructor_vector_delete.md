class 초기화 
생성자에서 

원래 
Time(int h, int m) {
    hour = h;
    minute = m;
}

c++14 부터는 

Time(int h, int m) : hour {h}, minite {m} {
}

이렇게 가능하다고 한다  
initializer list 라고함- 익숙해지면 편하고, 실행도 효율적이라고 함   

> : hour (h), minite(m)  방식으로도 가능 (조금 예저 방식)




## vector
일반 배열은 정적 배열: 컴파일 시간에 배열의 크기 결정됨

그래서 나온게 실행시간에서도 크기 변경이 가능한 dynamic array 이 나오는데 vector 라이브러리를 이용한다

단, 성능이 중요한  app  작성 시엔느 생성/소멸에 있어서 상당한(?) 시간이 소요

그래서 나온게 c++11에서  std::array가 나옴

std::array<int, 3> list { 1, 2, 3}; 
이런식으로 사용한다 

> vector의 장점과 기존 배열의 성능을 동시에..할 수 있으나 최대 단점은 동적으로 크기를 변경할 수는 없다



동적 메모리 (dynaic memory allocation) 프로그램 실행 중 동적으로 메모리를 할당

히프(heap) 에서 아직 사용하지 않은 메모리 공간을 관리
그래서 히프에서 할당받게 된다 

new, delete

int* ptr;
ptr = new int[5];

5개의 배열을 가지는 동적메모리 할당

삭제 
delete [] ptr;

> 배열로 할당을 했을 경우에는 위 처럼 배열도 해제를 해줘야 한다. 배열로 만든 경우가 아니면  
delete ptr; 하면 된다 

