#include <stdio.h>
void fruit (int count); //void 함수 (리턴값이 없을 때) 
int rec_func (int n);
int fac(int num);


int main() {

    //fruit(1);  //apple출력하는 기본 재귀함수
    printf("%d\n", rec_func (10)); //넘어간 인자의 범위안에서 개별로 더하기 
    printf("%d", fac (5)); //인수 만큼 곱하기
    
    return 0;
}

//재귀호출 
void fruit (int count) {
    printf("apple\n");
    if (count == 3) return; //! return으로 함수가 종료는 되지만 바로 함수를 호출했던 그 전으로 돌아간다. 리턴했다고 바로 종료되는 것이 아니다!
    fruit(count +1); 
    printf("jam\n");
    //*참고: 리턴이 한번 되면 그 아래 코드는 실행하지 않고, 다시 함수를 호출한 곳으로 돌아가는데, 함수가 실행한 만큼 함수가 복사되었다고 생각하면 좋다
    //현재 함수는 3번을 반복했으므로 2번째 함수를 호출한 부분을 다시 돌아가서 아래코드가 남아있어서 printf("jam")을 하게되고 (물론 함수는 호출하지 않는다)
    //함수2번째가 }를 만나서 끝나면 다시 함수를 호출했던 1번째 함수로 돌아가게 되서 다시한번 printf("jam")만나게 되고 또 출력 
    // }를 만나 함수가 끝나면 원래 처음 main함수에서 호출했던 부분으로 돌아가게 그 다음에 더 이상의 코드가 없고, return 0를 만나면서 프로그램이 종료
    // 그래서 재귀함수를 호출했고 끝났음에도 나머지 코드인 printf("jam")부분이 출력되게 되는 것임
}

int rec_func (int n){
    //int count=0;
    
    if (n == 0) {
        return 0;
    }
    //-1감소시켜서 함수 호출 그리고 받은 +n 값을 더해서 리턴함
    // 최종적으로 위의 if문에서 0이 되어 0을 리턴받으면 다시 그 전의 함수를 호출한 부분으로 돌아가서 
    // 리턴값과(-1) + 원래n값이 더해진 것이 리턴
    //todo: 정리가 좀 필요
    return rec_func(n -1) + n;  

    /* 위의 코드를 풀으면 이런식인듯..
    count = rec_func(n -1);
    count += n;
    return count;
    */
    
}

int fac(int num) {
    
    if (num == 1) {
        return 1;
    }
    
    return fac(num - 1) * num;

}
//todo: 복습!
//참고 사이트:
//https://dojang.io/mod/page/view.php?id=585 

