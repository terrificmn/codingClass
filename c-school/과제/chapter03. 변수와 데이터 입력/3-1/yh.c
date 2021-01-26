#include <stdio.h> 

int main() {
	int a = 0;
	a = a + 1;
	a = a + 2;
	a = a + 3;
	printf("a : %d\n", a);

	int kor = 70, eng = 80, math = 90;
	int sum;

	sum = kor + eng + math;
	printf("국어 : %d, 영어 : %d, 수학: %d\n", kor, eng, math);
	printf("총점: %d\n", sum);
	return 0;
}