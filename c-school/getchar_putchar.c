#include <stdio.h>
/*
//?getchar()와 putchar()
int main() {

    int ch;

    printf("문자 입력: ");
    ch = getchar(); // getchar()는 integer형태로 아스키코드로 받음
    putchar(ch);    //putchar(문자열변수) 로 getchar로 받은 입력값을 출력할 수 있음
    printf("%d", ch); // integer이기때문에 출력하면 숫자가 나오는데 바로 아스키코드이다

    return 0;
}
*/

/*
//?버퍼 삭제하기
int main() {
    int num, grade;

    printf("학번 입력: ");
    scanf("%d", &num); //scanf 로 입력을 받으면 입력 받은 값 (예: 123엔터) 하면 123\n으로 버퍼에 저장되고 123만 int로 바뀌어 num에 할당됨
    // 버퍼에는 아직'\n'값이 남아있게 되는데, 버퍼에 남아있는 채로 
    //getchar()를 받게 되면 버퍼에 남아있는 \n 값이 입력이 되어짐, 결국 원하는 결과 값을 얻지 못함
    //scanf()도 마찬가지 임, (다시 scanf를 써도 버퍼값에 들어있는 값을 읽어옴)
    //scanf("%d", &grade);

    getchar(); //getchar()를 해주면 버퍼에 있는 값을 읽어옴 (버퍼에 남아있는 '\n' 삭제와 같은 효과)
    
    printf("학점 입력: ");
    grade = getchar(); //이후 다시 getchar()를 실행하면 원하는 결과가 나옴
    printf("학번: %d, 학점: %c", num, grade);

    return 0;
}
*/


//? 함수로 getchar()를 반복하여 배열변수에 넣어주기 (파라미터로 포인터로 받음)
void my_gets(char *str, int size);

int main() {
    char str[7];

    my_gets(str, sizeof(str)); //문자열배열 크기도 넘겨줌  //사용자 함수
    printf("입력한 문자열: %s\n", str); 
    

    return 0;
}

// 반복문으로 버퍼에서 문자를 받아서 
void my_gets(char *str, int size) {
    int ch, i = 0;

    printf("입력하세요: ");
    ch = getchar(); //getchar도 버퍼를 사용하는 문자 입력 함수 (scanf도 버퍼사용)
    
    while ((ch != '\n') && (i < size -1)) { 
        // \n은 엔터를 의미하므로 엔터친게 아니면 계속 반복 , size를 -1은 마지막에 \0을 넣어야하기 때문
        str[i] = ch;
        i++;
        ch = getchar();
    }
    str[i] = '\0'; //마지막에 끝 문자 넣어주기

}
