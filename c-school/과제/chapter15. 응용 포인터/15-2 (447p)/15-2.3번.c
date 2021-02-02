#include <stdio.h>

int add(int a, int b) { return (a + b); }
int sub(int a, int b) { return (a - b); }
int mul(int a, int b) { return (a * b); }

int main() {
    //* 함수명은 함수 정의가 있는 메모리의 시작 위치!!
    // 함수포인터 선언은 type (*포인터변수) (파라미터 타입지정int, int)  예: int (*fp)(int, int);
    int (*pary[3])(int, int) = { add, sub, mul };   // 함수포인터 배열로  선언(파라미터는 int, int) ---배열에 add, sub, mul 넣는다
    
    int i, res = 0;

    for (i=0; i < 3; i++) {
        res += pary[i](2, 1);   //함수포인터를 호출하면서 배열에 들어있는 것들을 호출(args 2, 1을 넘김) 위에서 함수들이 호출되면서(add, sub, mul) 리턴함
        //리턴값 받은 것을 res 변수에 계속 더해줌
    }
    printf("%d\n", res);

    int ary[5] = { 10, 20, 30, 40, 50};
    
    //void 함수포인터 선언
    void *vp = ary;  //자료형이 다른 경우에 void 함수포인터를 사용 

    //printf("%d\n", ((int *)vp)[2]);  //형 변환 연산자는 우선순위가 배열연산자보다 낮음, 그래서 괄호를 묶어서 먼저 수행되도록 함
    //위의 코드는 vp를 int *형으로 변환하는 type 변환 작업, 그 다음에 괄호 앞에 * 넣어 간접 참조
    printf("%d\n", *((int *)vp + 2));  //같은 의미
    // vp[2] == *(vp + 2)
    return 0;
}


