#include <stdio.h>
//! 함수 정의시에 중요한 점은 리턴할 값이 어떤 type인가에 따라 함수의 type을 정의해줘야한다
// 예를 함수를 들어 아래의 centi_to_meter()함수는 doublt형 실수를 리턴하게 되는데 여기에서 
// int centi_to_meter()이런식으로 정의하게 되면 값이 소수점은 짤려서 리턴되게 되어, 원하는 결과값이 나오지 않을 수 있다.
// 추가로 리턴할 값이 없는 함수는 void function_name() 으로 정의한다
// 파라미터도 type도 맞게 정의하면 됨
double centi_to_meter(int cm);

int main() {
    double res;
    res = centi_to_meter(187);
    printf("%.2lfm\n", res);
    return 0;
}

double centi_to_meter(int cm) {
    double temp;
    temp = (double)cm / 100.0;
    return temp;

}