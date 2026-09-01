#include <stdio.h>
#include <string.h>
//문자열 기본 활용 함수들 
//** <string.h> 인크루드 해야함
int main() {
    char str[80];
    strcpy(str, "wine"); //카피: str에 wine을 복사해서 만듬
    strcat(str, "apple"); //결합 - 기존 str 뒤에 apple을 붙임
    strncpy(str, "pear", 1); //strncpy는 source 문자열(2번째 파라미터)에서 n만큼만 결합시킴
    
    printf("%s, %d\n", str, strlen(str)); //strlen() 문자열의 길이 반환


    char source[30] = "example";
    char destination[30]; //최종 바뀔 문자열 
    
    strncpy(destination, source + 0, 5); //? strncpy() 함수는 첫 번째 파라미터는 destination, 두 번째는 source, 세 번째는 size(길이)
    //** 2번째 파람 source + 0 자체는 첫번째 주소를 가리킴, 세 번째 파라미터는 2번째 소스에서 5자리까지 받아옴

    
    printf("strncpy()함수의 결과: %s", destination); //examp까지 표시하는 것을 확인!

    destination[strlen(destination)] = '\0'; //*널문자 넣어주기, 쓰레기값을 읽어오기 때문
    //** 배열에 문자열상수 "string"이런것을 넣는 것은 불가능하지만, 한글자 넣는 것은 가능 
    // 아마도 배열자체가 주소를 의미하고 있어서?
    destination[3] = 'H'; //문자 한캐릭터는 배열로 넣어주는 것은 가능
    destination[4] = 'I'; //문자 한캐릭터는 배열로 넣어주는 것은 가능
    printf("\n%s", destination);

    // 초기 문자열배열 변수 정의하면서 문자열을 넣어주거나(배열초기화) 
    // scanf등으로 입력을 받은 경우가 아닐 때는 쓰레기 값이 들어갈 수 있다고 함
    


}

