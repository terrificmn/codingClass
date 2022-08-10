 클론
```
git clone https://github.com/staropram/cantcoap.git
```

먼저 dependencies  
```
sudo apt-get install libcunit1 libcunit1-dev
```


해당 디렉토리에 들어가면 Makefile이 있음~  
make 를 쳐준다 

그리고 test를 하려면 ./test 를 쳐보면 됨   

clang++ 없음

make: clang++: Command not found   
Makefile에 되어 있는 CXX=clang++ 부분이 에러가 발생하는 듯 하다 

clang부분을 주석처리하고  
CXX=g++ 를 주석해제 시키고 make 터미널에서 명령을 하면 잘 실행 된다 


cantcoap 훌륭한 예제 파일들 참고 

https://cpp.hotexamples.com/examples/-/CoapPDU/setPayload/cpp-coappdu-setpayload-method-examples.html