#include <stdio.h>
int main() {
//file open 기본
/*
    FILE *fp; //FILE 라이브러리를 이용해서 포인터 선언
    fp = fopen("a.txt", "r");
    if (fp == NULL) {
        printf("파일이 열리지 않았습니다.\n");
        return 1;  //리턴하고 끝냄
    }
    printf("파일이 열렸습니다.\n");
    fclose(fp);
*/

    FILE *fp1; //다시 정의
    int ch;

    fp1 = fopen("C:\\Users\\5-20\\Desktop\\a.txt", "r");  // 디렉토리 구분은 \\ 역슬래쉬를 2번씩 사용
    if (fp1 == NULL) { 
        printf("파일이 열리지 않았습니다.");
        return 1;
    }

    while (1) {
        ch = fgetc(fp1);  //fp1 포인터로 연결된 파일에 읽어와서 반환해서 ch변수에 할당 //** 더 이상 읽을것이 없은 EOF 반환
        // *참고: -1을 직접 사용할 수도 있지만 시스템에 따라 EOF정의가 다를 수 있어서 호환성을 위해 EOF 상수를 사용하는게 좋음
        if (ch == EOF) {  //EOF End Of File로 상수값 -1이 미리 정의되어 있다. 파일의 끝에 도달하면 -1을 반환한다고 함
            break;  
        }
        putchar(ch);  //받은 값 출력
    }
    fclose(fp1);  //파일을 오픈 후에는 꼭 fclose를 해야한다. 메모리에서 제거

    return 0;
}