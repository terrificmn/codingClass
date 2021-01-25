#include <stdio.h>
#include <string.h>  // <string.h> 라이브러리는 문자열 배열로 선언된 문자열을 바꿔줄 때 사용

int main() {
	char fruit[20] = "strawberry"; //char 문자열 변수에 값을 넣으려면 변수[배열]을 적어줘야하고 인덱스는 문자열크기 +1 되어야한다 //자동으로 마지막에 \0인 null문자가 들어간다
	printf("딸기: %s\n", fruit);
	printf("딸기쨈: %s %s\n", fruit, "jam");
	
	//fruit = "banana"; //문자열 배열에는 직접 할당할 수가 없다. 처음에 선언할 때만 가능(c언어 특징) 
	//에러 발생함
	//include <string.h> 를 불러와서 strcpy()함수를 사용하면 변수에 문자열을 할당가능

	strcpy(fruit, "banana");  //strcpy()함수로 새로운 값을 넣어줄 수 있음
	printf("%s\n", fruit);
	printf("과일");


//상수와 데이터 입력
    printf("%d을 %d로 나누면 %lf입니다.", 1, 2, 0.5);
    
    printf("\n");
    
    printf("Be\rHappy!\nBaby");

	//정수는  %d, 문자열 %s, 문자(캐릭터) %c로 포맷팅해서 출력
    printf("학번: %d\n", 32165);
    printf("이름: %s\n", "홍길동");
    printf("학점: %c", 'A');

    int age;
    double height;
    char name[20];  //원래 크기 보다 +1해서 배열을 선언한다. 마지막는 문자의 끝을 표시하는 \0이 들어가므로 +1 크게 잡아줘야함

    printf("나이와 키를 입력하세요: ");
    scanf("%d%lf", &age, &height); //* scanf로 입력을 받을 때는 %d%lf를 붙여서 사용해야함. 변수 연결은 &변수
    printf("나이는 %d살, 키는 %.1lfcm입니다.\n", age, height);

    printf("이름 입력: ");
    scanf("%s", name);  //* 원래 scanf()에서는 변수를 할당할 때 &를 써야하는데 문자열 배열 입력을 받을 때는 &를 붙이지 않는다.
    printf("%s 입니다.\n", name);

    return 0;
}