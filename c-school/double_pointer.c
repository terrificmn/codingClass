// 이중 포인터
#include <stdio.h>
void swap_ptr(char **ppa, char **ppb);

int main() {
    int a = 10;
    int *singleP = &a; //포인터에 a주소를 할당
    int **doubleP = &singleP; //이중포인터에 singleP의 주소를 할당 == a의 주소
    
    printf("변수\t|\t변수값\t|\t&연산\t|\t*연산\t|\t**연산\n");    
    printf("-----------------------------------------------------------------------\n");   
    printf("    a   |%13d  |%13u  |\n", a, &a);    
    printf("singleP |%13d  |%13u  |%10d    |\n", singleP, &singleP, *singleP);    
    printf("doubleP |%13d  |%13u  |%10d    |%10d    |\n", doubleP, &doubleP, *doubleP, **doubleP);    

    printf("\n");
    
    
    char *pa = "success"; //포인터 변수pa 문자열 상수 초기화
    char *pb = "failure"; //포인터 변수pb 문자열 상수 초기화

    printf("바꾸기 전: pa ---> %s, pb ---> %s\n", pa, pb); 

    swap_ptr(&pa, &pb); //swap_ptr()함수를 호출하면서 args로 주소값을 넘겨준다 (&pa, &pb) 
    
    printf("바꾼  후:  pa ---> %s, pb ---> %s\n", pa, pb); //바꾼 후

    return 0;
}

void swap_ptr(char **ppa, char **ppb) {  //* 파라미터는 douple pointer로 정의해서 받는다
    char *pTemp; //바꿔줄 임시 변수 (포인터 변수)

    // 바꾸기 (주소값을 참조해서 바꿔준다)
    pTemp = *ppa; //pTemp를 이용해서 바꿈
    *ppa = *ppb;  //더블포인터 ppa의 싱글포인터는 pa의 주소를 의미하는데, 여기에 pb의 주소를 넣어서 바꿈
    *ppb = pTemp; //더블포인터 ppb의 싱글포인터는 pb의 주소를 의미하는데, 바뀐 pTemp의 값이 넣어지면서 pa의 주소로 바뀜
}