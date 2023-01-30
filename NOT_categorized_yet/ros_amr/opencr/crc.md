참고
https://www.youtube.com/watch?v=69bQ9PF0g0g


initial crc
1111 1111   ---> 0xFF

input data
1100 0001

여기에서 initial crc와 input data 를 XOR 해준다 

 1 1 1 1 1 1 1 1
^
 1 1 0 0 0 0 0 1
 

맨앞의 bit가 0이면 left shift를 해준다. 연산자는 <<  . 그리고 마지막은 0으로 채운다 (bit 수 맞춤)
crc << 1

맨앞의 bit가 1이어도 left shft를 해준다. 단, 그리고 나서 Poly XOR 연산을 해준다. 

나온 결과로 위의 작업을 반복한다   

총 8개의 bit이므로 left shift를 8번하게 되면 끝이 나게 된다.   


libcrc.org/download   
오픈소스를 참고해보자  

여기도 참고 오제이 튜브   
https://www.youtube.com/watch?v=_KnqwGczUjE
