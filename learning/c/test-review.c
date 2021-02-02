//int f;
    //int a = -4, b=3, c= -5, d=2;
    //f = a*b % c /d;
    //printf("%d", f);

    // int a=2, b=3, c=4, d=5;
    // a = ++c + c++ + ++c + c++;
    // printf("%d", c);

/* ////////////////13번
#include <stdio.h>

struct point {
        int xpos;
        int ypos;
    };
void OrgSymTrans(struct point * ptr) {
    //printf("%d ", ptr[0]); //변경 전 테스트
    //printf("%d \n", (ptr+0)->ypos); //변경 전 테스트

    if ((ptr+0)->xpos > 0) {
        (ptr+0)->xpos -= 14;  //음수 전환
    } else if ((ptr+0)->xpos < 0) {
        (ptr+0)->xpos += 14;  //양수 전환
    }  

    if ((ptr+0)->ypos < 0) {
        (ptr+0)->ypos += 10;  //양수 전환
    } else if ((ptr+0)->ypos > 0) {
        (ptr+0)->ypos -= 10;  //음수 전환
    }
    //printf("%d ", ptr[0]);  //변경 후 테스트
    //printf("%d \n", (ptr+0)->ypos); //변경 후 테스트
}
void ShowPosition(struct point pos) {
    printf("[%d, %d]\n", pos.xpos, pos.ypos);
}

int main() {
    struct point pos={7, -5};
    OrgSymTrans(&pos);
    ShowPosition(pos);
    OrgSymTrans(&pos);
    ShowPosition(pos);
    return 0;

    
}
*/

#include <stdio.h>
void ShowArr(int (*arr)[4]);
void RotateArr(int (*arr)[4]);

int main(void) {
    int i = 0;
    int arr[4][4] = {
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12},
                {13, 14, 15, 16}
    };

    for(i=0; i<4; i++) {
        ShowArr(arr);
        RotateArr(arr);
    }

    return 0;
}

void ShowArr(int (*arr)[4]) {
    int i, j;
    printf("----Show Array----\n");

    for(i=0; i<4; i++) {
        for(j=0; j<4; j++) {
            printf("%5d", arr[i][j]);
            //문제 오타printf("\n");
        }
        printf("\n");
        
    }
}

void RotateArr(int (*arr)[4]) {
    int i, j;
    int count = 1; 
    static int func_count = 0;
    func_count += 1;  //함수 호출 될 때마다 카운트 해주기
    //printf("%d", func_count); //test

    switch (func_count) {
        case 1: 
            for(i=0; i<4; i++) {
                for(j=3; j >= 0; j--) {
                    arr[i][j] = count;
                    count += 4;
                }
                count = i + 1; //초기화 //i==0일때 +1해서 1로 초기화
                count += 1; // i번째가 넘어가서 1차원 배열 반복이 일어날 때 원하는 숫자가 나오게 설정
            }
            break;
        
        case 2:
            for(i=3; i >=0; i--) {  //거꾸로
                for(j=3; j >= 0; j--) {  //거꾸로
                    arr[i][j] = count++;  //그냥 단순히 거꾸로 출력한다, count는 단순히 +1씩
                }
            }
            break;
        
        case 3:
            for(i=3; i>=0; i--) {
                for(j=0; j < 4; j++) {
                    arr[i][j] = count;
                    count += 4;
                }
                count = j-i; //초기화 //j는 항상 4로 끝나고 4- (i)인셈, i는 3, 2, 1, 0 이 됨
                count += 1; //위 코드 결과에 따라 +1을 시켜서 카운트가 i번째 시작할 때 원하는 숫자가 되게 함
            }
            break;

        default: 
            break;
    }
}

/*
    // 세 번째 로테이션 성공
    for(i=3; i>=0; i--) {
        for(j=0; j < 4; j++) {
            arr[i][j] = count;
            count += 4;
        }
        count = j-i; //초기화 //j는 항상 4로 끝나고 4- (i)인셈, i는 3, 2, 1, 0 이 됨
        count += 1; //위 코드 결과에 따라 +1을 시켜서 카운트가 i번째 시작할 때 원하는 숫자가 되게 함
    }
*/

/*  
    // 두 번째 로테이션 성공
    for(i=3; i >=0; i--) {  //거꾸로
        for(j=3; j >= 0; j--) {  //거꾸로
            arr[i][j] = count++;  //그냥 단순히 거꾸로 출력한다, count는 단순히 +1씩
        }
    }
*/

/*
    //첫 번째 로테이션 성공
    for(i=0; i<4; i++) {
        for(j=3; j >= 0; j--) {
            arr[i][j] = count;
            count += 4;
        }
        count = i + 1; //초기화 //i==0일때 +1해서 1로 초기화
        count += 1; // i번째가 넘어가서 1차원 배열 반복이 일어날 때 원하는 숫자가 나오게 설정
    }
*/



