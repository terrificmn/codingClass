# fopen 

매개변수 종류  
| argment | explaination |
| --- | --- |
| r or rb | Open file for reading. |
| w or wb | Truncate to zero length or create file for writing. |  
| a or ab | Append; open or create file for writing at end-of-file. |
| r+ or rb+ or r+b | Open file for update (reading and writing). | 
| w+ or wb+ or w+b | Truncate to zero length or create file for update. |
| a+ or ab+ or a+b | Append; open or create file for update, writing at end-of-file.|



```c
#include <stdio.h>
FILE *fp;
fp = fopen("a_file", "wb");

// 또는 
fp = fopen("a_file", "rb");
```


리눅스, UNIX 에서는 r, rb 가 같다.(별 상관이 없다)   
그러나 Windows에서는 newlines을 할 때 하나의 케릭터로 사용되는데,, '\n' 이다   
이것을 읽고 쓰고 할 때 문제가 될 수가 있다  

파일을 읽을 때에는 r/rb, 쓸때는 w/wb 상관이 없지만,   
binary 파일은 rb, wb 로 해야지.. newline 관련해서 문제가 없다고 한다.   

어쨌든 그냥 rb, wb, ab 로 사용하면 될 듯 하다 

