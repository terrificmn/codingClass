#include <stdio.h>
int main() {
    /*
    switch (값) { //여기에서 값은 정수만 가능함
        case 비교값1: 실행문;
            break;   //break는 생략할 수는 있으나 다음코드까지 실행될 수 있음에 유의
        case 비교값2: 실행문;
            break;
        case 비교값3: 실행문;
            break;
        case 비교값4: 실행문;
            break;
        case 비교값5: 실행문;
            break;
        default: 실행문; //기본적으로 
    }
    */
    int rank = 2, m =0;

    switch (rank) {
        case 1:
            m = 300;
            break;
        case 2:
            m = 200;
            break; //break 생략이 가능하나, 만약 생략을 하면 원하는 결과가 안나온다. 아래코드인 case3까지 진행이 되어서 m =100이 됨
        case 3:
            m = 100;
            break;
        default:
            m = 10;
            break;
    }
    printf("switch문 결과 m : %d\n", m);

    // if문으로 전환
    if (rank == 1) {
        m = 100;
    } else if (rank == 2) {
        m = 200;
    } else if (rank == 3) {
        m = 100;
    } else {
        m = 10;
    }
    printf("if문 결과 m: %d", m);

    return 0;
}