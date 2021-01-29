//local (지역변수) 중에 static (정적 지역변수)
//static은 메모리에 할당되어서 {}중괄호 블럭을 벗어나도 사라지지 않고 상관없이 사용할 수 있다 
//(전역변수처럼, 단, 지역에서만 사용가능 {}벗어나도 없어지지는 않지만 지역변수이므로 사용은 안됨)

#include <stdio.h>
void auto_func();
void static_func();

int main() {
    int i;

    printf("일반 지역 변수(auto)를 사용한 함수..\n");

    for(i=0; i < 3; i++) {
        auto_func();
    }

    printf("정적 static 지역 변수를 사용한 함수..\n");
    
    for(i=0; i < 3; i++) {
        static_func();
    }
    return 0;
}

void auto_func() {
    auto int a = 0; //auto 는 local 변수이며 생략 가능하다, 
    //* a변수가 지역변수로 0으로 초기화 되었지만 계속 유지되는 것이 아니라 함수가 끝날때 제거됨, 
    //* 다시 호출되었을 때 새롭게 할당된 후 0으로 초기화 된다. 
    a++;    // 함수가 종료된 것과 동시에 a변수는 메모리에서 더 이상 유지되지 않는다.
    printf("%d\n", a);

}

void static_func() {
    static int a; //초기화를 안해도 0으로 자동초기화 됨 (static)
    a++;
    printf("%d\n", a);  //*함수가 종료되면 static으로 선언한 a변수는 메모리에 남아 프로그램이 실행되는 동안 유지
                //* 이것이 같은 지역변수지만 static이 아닌 지역변수와의 차이점
    //함수가 다시 호출되었을 때 +1이 되어진다
    //void함수로 값을 안 넘길 때 a변수의 값을 계속 유지할 수 있음

}
