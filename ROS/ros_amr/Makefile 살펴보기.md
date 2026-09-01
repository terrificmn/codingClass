
```
LIB_INSTALL=$(HOME)/lib
INCLUDE_INSTALL=$(HOME)/include

INCLUDE= -I../../

CXX=g++
#CXX=clang++
CXXFLAGS=-Wall -DDEBUG -std=c++11 $(INCLUDE)

CC=gcc
#CC=clang
CFLAGS=-Wall -std=c99 -DDEBUG

default: server client

server: ../../libcantcoap.a ../../nethelper.o server.cpp

client: ../../libcantcoap.a ../../nethelper.o client.cpp

clean:
	rm server; rm client;

install:
	install libcantcoap.a $(LIB_INSTALL)/
	install cantcoap.h $(INCLUDE_INSTALL)/
```
여기에서 볼 것은 CXX, CC 에서 설정

default, server, client, clean 등은 명령어로 사용이 가능

예
make clean, 
설정된 것 처럼 rm 명령어 사용해서 지움  

make install  
.a 파일 (static 파일), 설정된 것 처럼 만들어 줌  
단 LIB_INSTALL 등의 변수에 설정된 디렉토리가 없다면 못 만듬  



