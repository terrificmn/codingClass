#include <stdio.h>
#include <string.h>
int main()
{
    char str[30];
    char replacedStr[30]; //최종 바뀔 문자열 
    char star[20]; // * 문자열 넣어줄 변수
    int len;

    printf("입력하세요: ");
    scanf("%s", &str);
    getchar(); //버퍼 삭제

    len = strlen(str);
    //printf("원래문자열%d\t", len); //test
    if (len > 5 && len < 15) {
        strncpy(replacedStr, str + 0, 5);
        replacedStr[strlen(replacedStr)] = '\0'; //*널문자 넣어주기, 쓰레기값을 읽어오기 때문
            //printf("바뀐문자열 길이 %d\t", strlen(replacedStr)); //test
        strncpy(star, "********", len - 5);
        //printf("%d\t", strlen(star)); // 쓰레기 값도 같이 넣어지는 문제 쓰레기값이 몇개 인지 모름 //test
        //printf("%s ", star);  //값은 맞게 들어가는 데 쓰레기값도 같이 들어가는 문제 //test
        star[len - 5] = '\0'; //입력받은 길이에서 5를 빼고 그냥 null 셋팅
            //printf("%d\t", strlen(star)); // 맞게 나옴 //test
            //printf("%s ", star); //test
        strcat(replacedStr, star); //결합

    } else if (len >= 15) {
        strncpy(replacedStr, str + 0, 15); //15자로 제한
        strncpy(star, "********", len - 5);
        star[len - 5] = '\0'; //널 넣어주기
        strcat(replacedStr, star);

    } else { //단어수가 4자리 이하
        strcpy(replacedStr, str);
    }
    
    printf("입력한 단어: %s,  생략한 단어: %s", str, replacedStr);
    return 0;
}