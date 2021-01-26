#include <stdio.h>
int main() {

//3번 문제
    int kor, eng, mat;
    int credits;
    int res;
    double kscore, escore, mscore;
    double grade;

    kor = 3;
    eng = 5;
    mat = 4;
    credits = kor + eng + mat;

    kscore = 3.8;
    escore = 4.4;
    mscore = 3.9;
    grade = kscore + escore + mscore / 3.0; //실수형태로 구하기 위해 3.0으로 나눔
    
    //c언어는true,false가 없다고 함, 숫자로만 리턴됨: 참이면 1, 거짓이면 0
    res = grade >= 4.0 && credits >= 10;
    printf("%d", res);

    return 0;

}