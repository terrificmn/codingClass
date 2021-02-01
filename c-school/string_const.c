#include <stdio.h>
//https://blog.naver.com/tipsware/221018307213 참고

void checkStrAmend(char *my_string);
void checkStrDirect(char *p_my_string); //보통 5번의 경우
void checkStrDirectConst(const char *p_my_string); //보통 5번의 경우

int main() {
//1. 배열로 선언, 배열문자열 초기화
char str[12]; 
char data[12] = {'h', 'a', 'p', 'p', 'y', 0}; //직접 초기화 할 때는 문자열 끝에 NULL문자 (ASCII값 0)을 넣어주면됨
// 널까지 6개의 배열 문자
// 스택 메모리에 배열을 위한 공간이 마련됨 1byte씩  6번 데이터가 들어가짐
printf("%s\n", data); 

//2. 문자열 상수를 배열초기화에 사용
char data_const[] = "happy"; //배열 항목수를 생략하고 data_const[]변수의 선언
printf("%s\n", data_const);  //결과는 같으나 항목은 6개만 만들어짐

//3. pointer이용
char *pString = "happytime";
printf("%s\n", pString);

//** 포인터 초기값이랑 문자열 상수로 하는 것의 차이점
char data1[] = "happytime";
data1[5] = 0;  // 문자열을 수정할 수 있음 //중간에 0 끝 널값을 넣어주는 것이 가능함
printf("%s\n", data1 ); // 문자열 NULL이 수정이 되면서 happy만 출력됨

//* 위의 3번 경우처럼 포인터를 이용시 문자열 상수를 넣었다면.. (차이점!!) 예: char *pString = "Happytime"; 이렇게 하고
// 뭔가 문자열을 바꾸려고 하면 
// *(pString +4) = 0;  //포인터로 문자열 상수를 지정했다면 컴파일 시는 에러가 안남, 하지만 실행시 오류
// 문자열 상수가 저장된 메모리 주소를 포인터가 직접 사용, 포인터로 문자열 변경하려고 하면 
// 쓰기 접근 위반 오류가 발생
// 하지만 2번 경우처럼 배열에 먼저 문자열 상수를 초기화하면서 할당해주면 변경이 가능

//4. 매개변수로 문자열 전달 하는 경우
char my_string[] = "happytime"; //배열 초기화
checkStrAmend(my_string); // 문자열 배열로 초기화해서 문자열 상수를 넣었을 경우에 함수에 args로 넘긴다면
//! 매개 변수로 전달된 문자열이 변경되거나 변경될 가능성이 있다면 함수의 파라미터를 포인터로 받게 한다 예: (char *p_mysting)
//** 변경가능성(변경해야한다면)이 있으면 문자열[배열]로 선언하고 초기화를 한 후에 함수등에서 포인터로 사용이 좋은 방법인 듯
// 즉, my_string의 주소를 함수로 전달

//5. 매개변수에 직접 문자열을 전달할 경우, 포인터로 받을 수 있음
// 주의할 점은 직접 문자열 상수를 전달했으므로 바꾸면 에러가 난다 (바꾸지 않으면 됨, 예: 출력만)
checkStrDirect("happytime");

//6. 매개변수를 const로 지정한 경우
//** 좋은점은 뭔가 에러가 나면 컴파일 단계에서 에러가 난다. 문자열상수를 직접 변경할 때 등
//참고: 5번 같은 경우에서는 만약에 문자열을 고치려다가 에러가 나면 컴파일에서는 에러가 안나기 때문에 찾기가 어려울 수 있다고 함
checkStrDirectConst("happytime");

return 0;

}

/////////////////////////////사용자 함수 부분//////////////////////////

void checkStrAmend(char *p_mystring) { //?단, 문자열 (문자열 자체가 주소)를 배열 초기화한 변수를 받아야 함
    *(p_mystring + 5) = 0; // 4번 처럼, 초기 문자열 배열 초기화 한것을 전달해 받으면 오류가 발생하지 않음
    printf("%s\n", p_mystring);
}


void checkStrDirect(char *p_my_string) { // 5번 경우 처럼 단순히 문자열 상수를 직접 보내도 수정을 안하면 상관없음
    printf("%s\n", p_my_string); //  //작동 잘 됨
} 


/* 5번 경우 문자열 상수를 직접 받고 수정할 경우
void checkStrDirect(char *p_my_string) { // 5번경우, 문자열 상수를 직접 받았다면 수정하면 에러가 나기때문에
    printf("%s\n", p_my_string); //
    // 에러 발생
    // *(p_my_string + 4) = 0; // 이러면 직접 문자열 상수를 받았기 때문에 에러가 발생
    // 포인터로 받았기 때문에 안심하고 변경하려고 하면
    // 컴파일 시는 문제없으나 실행 시 에러!
    
    // 추후 어디에서 문제가 있었는지 찾기가 어려워 질 수 있음, 그래서 
    // 함수 파라미터를 선언할 때 const를 넣어서 선언해주면 보기에 좋고 상수이니깐 변경안된다고 선언해서 
    // 미리 알기 쉬워진다
} 
*/

void checkStrDirectConst(const char *p_my_string) { // 6번경우, 문자열 상수를 직접 받았다면 const로 선언하기
    printf("%s\n", p_my_string); //
    
    // 이 경우는 문자열 상수를 이용해서 변경될 가능성이 없을 경우 사용한다고 함 const 정의
    // 5번경우의 문자열 상수를 직접 입력하는 경우와 같지만 const로 선언했기 때문에 
    // 애초에 아래처럼 포인터변수로 p_my_string으로 받은 것을 직접 변경하려고 하면
    //* 컴파일 단계에서 에러가 나기 때문에 미리 쉽게 알 수 있게 된다! (중요한 차이)
    //error: assignment of read-only location 이런식의 에러 발생
    // const는 변경안되는 상수라는 의미이니 이런 경우 잘 사용하면 될 듯

    *(p_my_string + 4) = 0; // 이러면 직접 문자열 상수를 받았기 때문에 에러가 발생
    

} 
