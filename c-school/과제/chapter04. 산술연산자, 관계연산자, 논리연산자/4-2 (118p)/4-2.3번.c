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

printf("%d시간 %d분 %d초 입니다.", hour, min, sec);
return 0;
}