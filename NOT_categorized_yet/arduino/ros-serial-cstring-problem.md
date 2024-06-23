
cstring을 못찾는 경우 c++ 라이브러리를 사용하는데 없어서 그렇다고 함


msg.h 파일에서

처음 incldue 를  #include <cstring> 에서 #include <string.h> 로 변경


std::memcpy() 사용하는데 이를 memcpy() 함수로 변경, 2곳 있음
