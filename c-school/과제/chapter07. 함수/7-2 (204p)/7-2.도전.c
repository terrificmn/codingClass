#include <stdio.h>
int rec_func (int n);
int fac(int num);

int main() {

    printf("%d\n", rec_func (10));
    printf("%d", fac (5));
    return 0;
}

int rec_func (int n){
    int count=0;
    
    if (n == 0) {
        return 0;
    }
    //-1감소시켜서 함수 호출 ..그리고 또 반복
    // 최종적으로 위의 if문에서 0이 되어 0을 리턴받으면 다시 그 전의 함수를 호출한 부분으로 돌아가서 
    // 리턴값과(-1된 값) + 원래n값이 더해진 것이 리턴
    count = rec_func(n -1);
    count += n;
    return count;
    
    //위의 코드를 한번에 구현
    //return rec_func(n -1) + n;  
}


int fac(int num) {
    
    if (num == 1) {
        return 1;
    }
    
    return fac(num - 1) * num;

}
//todo: 복습!