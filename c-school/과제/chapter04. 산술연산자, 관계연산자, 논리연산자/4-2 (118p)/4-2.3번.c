#include <stdio.h>
int main() {
int hour, min, sec;
double time = 3.76;

hour = (int)time;
time -= hour;
time *= 60;
min = (int)time;
time -= min;
time *= 60;
sec = (int)time;

printf("%d�ð� %d�� %d�� �Դϴ�.", hour, min, sec);
return 0;
}