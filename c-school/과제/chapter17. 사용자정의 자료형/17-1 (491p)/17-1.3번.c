#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct profile {
    int num;
    char name[20];
    char *skill; // 포인터는 사용하려면 동적할당을 해줘야함
};

struct sports {
    char *event;
    struct profile player;  //sports 구조체 안에 profile 구조체 변수를 정의 (player)
};

int main() {
    struct sports a; //구조체 변수 선언
    a.event = (char *)malloc(10 * sizeof(char)); //#include <stdlib.h> 선언 해줘야함, 그 이후 malloc()함수로 동적영역 메모리 할당을 해준다
    //strcpy(a.event, "figure skating"); //틀린 예//event가 포인터이므로 동적할당을 먼저해야함 //
    a.event = "soccer game";

    //a.player.name = "Yuni Seo"; //틀린 예 //name[]배열명으로 되어있어 문자상수 입력 불가, strcpy()사용해야함
    strcpy(a.player.name, "Yuni Seo"); //먼저 <string.h> 헤더파일을 포함시켜야 함
    
    //a.player = 19; //틀린 예   //player가 profile 구조체를 정의한 변수이므로 a.player.num 으로 지정해야한다
    a.player.num = 19;

    a.player.skill = (char *)malloc(10 * sizeof(char)); // 그냥 malloc(80) 해도 됨
    //scanf("%s", a.player.skill); //틀린 예: 위의 코드 없잉 동적 할당 없이 scanf 할 경우
    //skill이 포인터이므로 동적할당을 먼저 해준다
    printf("스킬을 입력하세요: ");
    scanf("%s", a.player.skill);

    printf("a구조체의.event: %s\n", a.event);
    printf("a구조체의.player(profile구조체).name: %s\n", a.player.name);
    printf("a구조체의.player(profile구조체).num: %d번\n", a.player.num);
    printf("a구조체의.player(profile구조체).num: %s\n", a.player.skill);
    
    return 0;
}