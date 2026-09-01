coap으로 전송을 계속 하다가  coap서버가 꺼져 있거나 응답이 없을 경우에  
client 쪽이 먹통이 되어버리는데  

특히 recv() 함수를 호출했을 때 응답을 받지 못하고 멈추는 것을 확인  

recv() 함수의 파라미터 중 마지막 파라미터를 __flags (int) 파라미터를   
MSG_DONTWAIT 로 넣어서 넘겨준다   

대충  
Enables nonblocking operation; if the operation would   
    block, the call fails with the error EAGAIN or   
    EWOULDBLOCK.   


참고 

https://man7.org/linux/man-pages/man2/recv.2.html   


이렇게 하면 중간에 메세지가 안 들어오게 되면 멈추지 않고 에러메세지를 출력해준다  

