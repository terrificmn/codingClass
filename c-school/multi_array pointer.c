#include <stdio.h>
void print_ary(int (*)[4]); //(괄호에는 배열포인터의 변수명 생략 가능)

int main () {
    int ary[3][4] = {
        {1,2,3,4},
        {5,6,7,8},
        {9,10,11,12}
    };
    print_ary(ary);
    return 0;
}


void print_ary(int (*pa)[4]) { //()괄호로 감싼 배열 포인터를 받는다. [4]는 col의 개수 // 1차원 배열의 4개짜리 int형을 가리킴
    int i, j;

    for (i=0; i < 3; i++) {
        for(j=0; j < 4; j++) {
            //printf("%5d", pa[i][j]);  //배열 포인터는 2차원 배열 처럼 사용
            /* //*433 페이지 참고
                ptr + 0 == arr
                ptr + 1 == arr[1]
                *(ptr + 1) == arr[1]  //역 참조할 때 사용법
                *(*(ptr + 0) + 1) == arr[0][1]  //역 참조할 때 사용법

                *(ptr + 1) + 2 == arr[2]  // arr[1]에서 +2 를 한 값  //2차원 배열에서는 row의 주소값
                (ptr + 1) +2 == ptr +3 //  위의 것과 다름
            */
           
        }
        printf("\n");
    }
    printf("%5d\n", *(pa + 0) +2); //주소값
    printf("%5d\n", (pa + 0) +2); //주소값
    printf("%5d", *(*(pa + 1) +1)); //주소값
    printf("%5d", *(*(pa + 2) +3)); //주소값

    //TODO: 공부 필요;;
}