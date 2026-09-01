coap을 사용하다가 보면 한번 연결을 하고 나서 다시 한번 바로 연결을 하려고 하면  
이미 ip address를 사용하고 있는 중이라고 나오면서 연결이 되지를 않는 현상이 있는데  

socket에서는 connection 이 끝나는데 socket은 TIME_WAIT에 들어간다고 한다  
이유는 데이타가 모두 잘 전송이 될 수 있게 하기 위해서  

그래서 setsockop()함수를 사용해서 socket을 설정할 수가 있다  

관련 페이지   (sys/socket.h) 파일을 참조한다  


옵션이 이러하다.. 대표적으로 ..  
https://linux.die.net/man/3/setsockopt  

SO_DEBUG   
    Turns on recording of debugging information. This option enables or   
    disables debugging in the underlying protocol modules. This option takes an int value.  
    This is a Boolean option.   

SO_BROADCAST  
    Permits sending of broadcast messages, if this is supported by the protocol.  
    This option takes an int value. This is a Boolean option.   

SO_REUSEADDR  
    Specifies that the rules used in validating addresses supplied to bind() should allow reuse of local addresses,  
    if this is supported by the protocol. This option takes an int value. This is a Boolean option.   

SO_KEEPALIVE  
    Keeps connections active by enabling the periodic transmission of messages,   
    if this is supported by the protocol. This option takes an int value.  




socket을 바로 사용할 수 있게 하려면 SO_REUSEADDR 상수를 사용해야 한다  

예제는 이렇다  
```cpp
int sockfd;
int option = 1;
sockfd = socket(AF_INET, SOCK_STREAM, 0);
setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &option, sizeof(option));
```


