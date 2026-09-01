//1 정수형의 크기가 5인 배열을 정의한다
//2 배열에 값을 5개 입력 받는다.
//3 배열에 있는 숫자 중에서 최대값과 최소값을 각각 출력.

#include <stdio.h>
int main () {
    int nbr[4];
    int i, max, min; 
    
    for(i=0; i < 5; i++) {
        //printf("입력하세요 (총 %d 중에 %d5 남음): ", )
        printf("입력하세요: ");
        scanf("%d", &nbr[i]);
    }

    max = nbr[0], min = nbr[0]; // 입력 받은 다음에 max, min변수에 할당해준다 
    //* 0번째 데이터를 넣어주면서 기준값으로 for문으로 돌리면서 if문으로 구현할 수 있음

    for(i=0; i < 5; i++) {
        
        if (max < nbr[i]) { // 크면 max변수에 할당
            max = nbr[i];   
        } 
        
        if (min > nbr[i]) {    //작으면 min변수에 할당
            min = nbr[i];   
        }
        
    }
    printf("배열의 가장   큰 수는 %d 입니다.\n", max);
    printf("배열의 가장 작은 수는 %d 입니다.\n", min);
}
