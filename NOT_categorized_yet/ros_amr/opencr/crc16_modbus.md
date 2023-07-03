# crc
주로 시리얼 통신을 할 때 데이터를 주고 받을 때, 데이터가 맞는지 체크를 해주는 것   
데이터의 오류 검출을 위해서 만들어진 것이고, 데이터를 신뢰할 수 있게 계산을 통해서 맞춰보는 과정이라고 할 수 있다  

실 데이터와, crc로 변환된 값 2개를 같이 보내주게되고,   
받는 쪽에서 crc 체크를 다시 한번 해서 맞는 값인지 체크를 하게 된다   

> 암호화와 복호화 같은 과정 처럼 똑같은 알고리즘에 대입을 해서 계산을 하게 되는 것   


[참고 유투브1](https://www.youtube.com/watch?v=69bQ9PF0g0g)   


1. crc 코드를 16bits 로 셋팅 FFFF   

initial crc
1111 1111   ---> 0xFF

input data
1100 0001

2. 여기에서 initial crc와 input data 를 XOR 해준다 

 1 1 1 1 1 1 1 1
^
 1 1 0 0 0 0 0 1
 

3. 맨앞의 bit가 0이면 left shift를 해준다. 연산자는 <<  . 그리고 마지막은 0으로 채운다 (bit 수 맞춤)
crc << 1

맨앞의 bit가 1이어도 left shft를 해준다. 단, 그리고 나서 Poly XOR 연산을 해준다. 

나온 결과로 위의 작업을 반복한다   

총 8개의 bit이므로 left shift를 8번하게 되면 끝이 나게 된다.   


## crc 의 미리 구한 상수
코드 중에 crc_table 구하기
```cpp
for(int i=0; i < data.size(); i++) {
    //생략//

    for(int j=0; j < 8; j++) {
        CY = CRC & 1;
        CRC = CRC / 2;   // C = C >> 1 과 동일
        if(CY == 1) {
            CRC = CRC ^ CRC_POLY_16;
        }
    }

}

```
> 코드는 위 처럼 작동하고 CY 등의 상수는 libcrc 참고할 것

위 처럼 이중 for문으로 구해져있는 부분이 CRC의 값들을 뽑아내는 것인데  위의 값들 처리하게 되면   
1 byte: 0 부터 255의 경우의 수를 구하게 되고 결과로 255개의 값들이 나오게 된다   

libcrc 에서는 그 때 그때 마다 함수를 호출해서 그 값을 만들어 내는데, 위의 j 에 해당하는 for문을 해보면   
그에 해당하는 값들을 미리 변수에 지정해 놓을 수가 있다   
즉, 이제 crc_table이 만들어진 것을 미리 변수에 저장해서 사용을 하게 되는데   

> libcrc 에서는 위의 테이블을 최초 한번만 구할 수 있게 되어 있고, table 자체를 변수로 만들어져 있지는 않다  
만들어져있지 않으면 위의 함수를 호출해서 한번만 구하고 사용하게 된다   

## crc 체크
위의 테이블이 있다고 가정하고  crc_table 을 통해서 데이터를 넣어 주면 이를 함수로 구현하게 되면 아래 처럼 된다   
```cpp
std::vector<uint8_t> data {10, 20, 30, 40};
uinit16_t crc = 0xFFFF;

for(int i=0; i<data.size(); i++) {
    crcUpdateMod16(crc, data.at(i));
}

void crcUpdateMod16(uint16_t* crc, uint8_t data_i) {
    uint16_t tmp;
    uint16_t short_c;

    short_c = 0x00FF & (uint16_t)data_i;   // origin 은 short_c = 0x00FF & (uint16_t)data_i;  == 같은 uint8_t를 uint16_t에 넣어주면 같은 효과
    // short_c = (uint16_t)data_i;   // 같음

    // // calculate crc
    tmp = *crc ^ short_c;
    *crc = (*crc >> 8) ^ CRC_table[tmp & 0xFF]; // CRC_table, 0-255까지의 경우의 수가 이미 구해져 있는 배열 상수
}
```

> modbus crc_table 은 검색을 하면 나옴









[libcrc 오픈소스 다운로드](https://www.libcrc.org/download/)   
오픈소스를 참고해보자  

여기도 참고 오제이 튜브   
https://www.youtube.com/watch?v=_KnqwGczUjE
