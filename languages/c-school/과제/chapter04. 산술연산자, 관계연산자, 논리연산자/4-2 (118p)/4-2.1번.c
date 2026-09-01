#include <stdio.h>

int main() {
    int res;
	res = sizeof(short) > sizeof(long);
	printf("%s\n«—±€", res ? "short" : "long");

} 

