#include <stdio.h>
//* c언어의 특징: 메모리에 할당되는 시점에 따라 함수를 인식하므로 호출받는 함수는 항상 위쪽에 코딩해야한다
//* 단, main()함수 위에 함수를 정의 하면 문제 없이 사용할 수 있다

/* void add() {  // 리턴할 값이 없을 때는 void로 함수를 만든다
    }
*/
int sum(int x, int y); //함수를 정의함 , 함수 자체가 main()함수 아래에 있다면 인식을 못하나,
// 함수 정의가 안되어있다면, warning: implicit declaration of function 'sum' 워닝 싸인이 나오나, 실제 실행은 가능함
// 위 처럼 함수 정의를 하면 main()함수에서 함수 인식을 한다

//! 함수 정의시에 중요한 점은 리턴할 값이 어떤 type인가에 따라 함수의 type을 정의해줘야한다
// 예를 함수를 들어 아래의 centi_to_meter()함수는 doublt형 실수를 리턴하게 되는데 여기에서 
// int centi_to_meter()이런식으로 정의하게 되면 값이 소수점은 짤려서 리턴되게 되어, 원하는 결과값이 나오지 않을 수 있다.
// 추가로 리턴할 값이 없는 함수는 void function_name() 으로 정의한다
// 파라미터도 type도 맞게 정의하면 됨
double centi_to_meter(int cm);


int main () {
    int a = 10, b =30;
    int result;

    result = sum(a, b);
    printf("result : %d\n", result);

    /// centi_to_meter() 사용 예제: 187cm에서 m로 변환하는 사용자 함수 *함수 type에 유의
    double res;
    res = centi_to_meter(187);
    printf("%.2lfm\n", res);

    return 0;
}

int sum(int x, int y) {
    //int temp;
    //temp = x + y;
    //return temp;
    return x+y;
}

double centi_to_meter(int cm) { //반환되는 값과 같은 type로 함수를 선언해 준다. (return이 더블형으로 되면, 함수도 double로 선언)
    double temp;
    temp = (double)cm / 100.0;
    return temp;
}