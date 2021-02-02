#include <stdio.h>
void swap_dbPtr (char **ppa, char **ppb); 
//void swap_dbPtr (char **, char **) //함수정의 할 때는 파라미터 변수는 생략가능

int main() {
// int a = 10;
    // int *ptr = &a;
    // int **pptr = &ptr;
    // *pptr == ptr == &a  (주소)
    //. **pptr == *ptr == a (값)

    int a = 10, b = 20, c = 30;
    int * arr[3] = { &a, &b, &c};
    int **pptr; //더블포인터 선언 // arr의 배열 주소를 갖고 있는 포인트배열을 받는다
    pptr = arr;

    //** 암기가 편할 수도...
    // *arr[0] == *pptr[0] == a
    // *(arr + i) == *(pptr + i) == *arr[i]  

    printf("%d %d %d\n\n", *pptr[0], *arr[0], a); // 모두 같음, 

    char *pa = "success"; 
    char *pb = "failure";
    printf("%s   %s", pa, pb);
    swap_dbPtr(&pa, &pb); //문자열을 받은 주소값을 넘겨줘야 한다. 왜냐하면
    // 함수에서 포인터의 주소를 받는 것은 이중포인터이기 때문에 주소값을 넘겨준다
    // 헛갈리는것은 문자열로 받았지만(문자열이 주소값),
    // 일단 포인트 배열이 아니고, 일반 포인터이기 때문????
    // 함수의 인수(args)로 이중포인터에 주소값을 넘겨줘야하는 것이 중요!!

    return 0;
}

void swap_dbPtr (char **ppa, char **ppb) {
    char *tmp;
    tmp = *ppa;
    *ppa = *ppb;
    *ppb = tmp;
}
