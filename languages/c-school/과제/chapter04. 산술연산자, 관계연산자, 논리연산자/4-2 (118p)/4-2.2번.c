#include <stdio.h>
int main() {
int seats = 70;
int audience = 65;
double rate;
rate = (double)audience / (double)seats;
rate = rate * 100;
printf("ÀÔÀå·ü : %.1lf%%", rate);
return 0;
}