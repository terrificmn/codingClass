# termios 이용해서 std::cin 입력 시
원래 입력을 한 후 엔터를 쳐야지 버퍼에 저장되었던 것이 처리가 되는데   
이를 한 자, 한 자, 키를 입력 받아서 사용하려면 I/O 에서 unbuffered 되게 처리 해야한다   

이를 termios.h 파일을 사용해서 구현할 수가 있다.  

셋팅을 할 변수를 2개를 만들고, 예전 설정과 현재 설정을 할 수 있게 하고   
모든 입력이 끝나고 프로그램이 종료되기 전에 다시 예전 설정을 돌아가게 하는 프로그램  

> 그렇게 안하면 프로그램이 종료된 후에 터미널 상에서 키를 입력할 때 마다 실행이 되는 불상사가 생김

예제
```c
#include <stdio.h>
#include <unistd.h>
#include <termios.h>

int main()
{
	struct termios old_tio, new_tio;
	unsigned char c;

	/* get the terminal settings for stdin */
	tcgetattr(STDIN_FILENO,&old_tio);

	/* we want to keep the old setting to restore them a the end */
	new_tio=old_tio;

	/* disable canonical mode (buffered i/o) and local echo */
	new_tio.c_lflag &=(~ICANON & ~ECHO);

	/* set the new settings immediately */
	tcsetattr(STDIN_FILENO,TCSANOW,&new_tio);

	do {
		 c=getchar();
		 printf("%d ",c);
	} while(c!='q');
	
	/* restore the former settings */
	tcsetattr(STDIN_FILENO,TCSANOW,&old_tio);

	return 0;
}
```

이제 getchar() 입력을 받을 때 엔터를 안 쳐도 키 하나를 누르면 하나씩 입력이 되어 진다.   


