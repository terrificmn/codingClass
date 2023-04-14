# memset
memory에 특정 값으로 넣어주는 함수

파라미터에는 메모리 주소, x (값), n (byte 수) 이렇게 3개

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[20] = "Hello world";
    printf("---plain str print: %s", str);

    memset(str + 13, '.', 8*sizeof(char));
    printf("---after memset: %s", str);
    return 0;
}
```

