#include <stdio.h>
/* //함수에서 배열로 넘기고 받기
//함수에서 배열로 넘기고 받기
void add (int *par) {  //함수에서는 *포인터 변수로 받으면 배열 주소를 받을 수 있다
    int i;
    for (i=0; i < 5; i++) {
        printf("%-3d", par[i]); //par[i]번째는 arr[]의 주소값을 가지고 arr[]의 데이터를 출력할 수 있음
        //printf("%-3d", *(par +i)); // == 같은 결과를 볼 수 있음 (*par로 주소를 +1하면 배열[0]과 같은 의미)
    }
}

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    add(arr); //!배열명은 주소값을 가지고 있으므로 add()함수에 args로 &없이 넘긴다

    return 0;

}
*/

//
void print_ary (int *par, int size) {  //함수에서는 *포인터 변수로 받으면 배열 주소를 받을 수 있다
    int i;
    for (i=0; i < size; i++) {
        printf("%-3d", par[i]); //par[i]번째는 arr[]의 주소값을 가지고 arr[]의 데이터를 출력할 수 있음
        //printf("%-3d", *(par +i)); //? == 같은 결과를 볼 수 있음 (*par로 주소를 +1하면 배열[0]과 같은 의미) == par[i]
    }
}

int main() {
    int arr1[5] = {1, 2, 3, 4, 5};
    int arr2[7] = {1, 2, 3, 4, 5, 6, 7};
    
    // 배열의 크기를 넘김( 배열자체(주소), 길이)
    //print_ary(arr1, 5);
    print_ary(arr1, sizeof(arr1) / sizeof(arr1[0]));   //바로 위의 코드와 일치, sizeof()함수를 이용해서 size값을 넘겨줄 수 있음
    // **1차원배열: 전체배열의 크기 나누기(/) 배열한개의 사이즈 로 하면 크기가 나옴 
    // [  ][  ][  ][  ][  ] (전체arr1)     /나누기       [ 0 ] (arr1중 배열1개)
    // 전체사이즈 20 / int는 4 바이트 , 5개 배열 크기

    printf("\n");
    //print_ary(arr2, 7);
    print_ary(arr2, sizeof(arr2) / sizeof(arr2[0])); //위의 코드와 같은 결과 값
    
    return 0;

}



