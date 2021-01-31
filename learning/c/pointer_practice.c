#include <stdio.h>
//이중 포인터를 사용한 포인터 교환
/*
void swap_ptr(char **ppa, char **ppb);

int main() {
    char *pa = "success";
    char *pb = "failure";

    printf("pa -> %s, pb -> %s\n", pa, pb);
    swap_ptr(&pa, &pb); //? 값이 바뀐것이 아니고 포인터의 주소값이 바뀌어서 문자열이 바뀐것 같은 효과
    printf("pa -> %s, pb -> %s\n", pa, pb);
    return 0;
}

void swap_ptr(char **ppa, char **ppb) {
    char *ptemp;

    ptemp = *ppa; //주소 값을 참조하겠다, 싱글포인터로 사용
    *ppa = *ppb;
    *ppb = ptemp;
}
*/
