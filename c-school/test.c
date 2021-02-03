#include <stdio.h>
#include <string.h>
/*
int get_num(void);

int main() {
    int result;
    result = get_num();
    printf("반환 값: %d\n", result);
    return 0;
}

int get_num(void) {
    int num;
    printf("양수 입력: ");
    scanf("%d", &num);

    return num;
*/


/*
void print_char(char ch, int count);
int main(void) {
    print_char('@', 5);
    return 0;

}

void print_char(char ch, int count) {
    int i;

    for (i=0; i < count; i++) {
        printf("%c", ch);

    }
    return;
}
*/
void print_str(char **pps, int cnt);

int main() {
/*
    int ch;

    //getchar()와 putchar()
    printf("문자 입력: ");
    ch = getchar(); // getchar()는 integer형태로 아스키코드로 받음
    putchar(ch);    //putchar(문자열변수) 로 getchar로 받은 입력값을 출력할 수 있음
    printf("%d", ch); // integer이기때문에 출력하면 숫자가 나오는데 바로 아스키코드이다
*/

/*
    char str[80];
    char str1[80];
    // printf("입력 공백 포함: ");
    // fgets(str, sizeof(str), stdin); // 마지막에 \n 이 추가됨
    // printf("%s\n", str);
*/
    
/*
    scanf("%s", str);
    printf("또 입력: ");
    scanf("%*c");  //버퍼 삭제시 
    gets(str1);
    
    printf("%s\n", str1);
*/

/*
//포인터 변수 활용 연습
    int num1 = 10, num2 = 20;
    int *ptr1, *ptr2; 
    ptr1 = &num1;
    ptr2 = &num2;

    printf("%d\t%d\n", *ptr1, *ptr2);
    *ptr1 += 10;
    *ptr2 -= 10;

    printf("%d\t%d\n", num1, num2);
    
    int *temp; //temp를 포인터변수로 선언하면 ptr1의 주소값을 바로 할당해 주는게 가능 //?(즉, 포인터의 주소값만 교환! 값은 안 바뀜)
    temp = ptr1; 
    ptr1 = ptr2;
    ptr2 = temp;
    printf("%d\t%d\n", *ptr1, *ptr2);

    int tmp; //만약 tmp를 일반변수로 선언하면, 포인트변수가 아니어서 주소를 받을 수 없음, 값의 참조
    // 대신 포인터값을 참조해서 //? 변수의 값을 직접 바꿔버릴 수 있음 (주소는 못 바꿈, 대신 값을 바꿈)
    tmp = *ptr1; //tmp를 일반 변수일 경우
    *ptr1 = *ptr2;
    *ptr2 = tmp;
    printf("%d\t%d\n", *ptr1, *ptr2);
*/

/*
    //포인터를 이용해서 뒤집기 
    int arr[6] = {1,2,3,4,5,6};
    printf("%d\n", arr[0]);
    int *fp = &arr[0];  //포인터에 주소값을 넣어준다, 
    //** (배열명이 주소를 의미하지만, 인덱스가 아닌 배열명이여야 한다) 하지만 여기에서 값이 아닌 주소값을 넣어준다, 인덱스 방식
    // int *fp = arr; 문제가 없는 코드
    // int *fp = arr[0]; 이렇게 하면 에러가 남, 배열명은 주소값을 찾지만 arr[0]번째는 알 수 없으므로 에러
    int *lp = &arr[5];  
    int temp, i;
    
    for(i=0; i< 3; i++) {
        temp = *fp;
        *fp = *lp;
        *lp = temp;
        fp += 1;
        lp -= 1;
    }

    for(i=0; i< 6; i++) {
        printf("%d ", arr[i]); //출력
    }
*/
    char *ptr_ary[] = {"eagle", "tiger", "lion", "squirrel"};
    int count;

    count = sizeoff(ptr_ary) / sizeof(ptr_ary[0]);
    print_str(ptr_ary, count);  //ptr_ary가 포인터 변수래서 주소값을 넘길 수 있음
    
    return 0;
}

void print_str(char **pps, int cnt) {
    int i;
    for (i=0; i < cnt; i++) {
        printf("%s\n", pps[i]);
    }
}

