# libcrc 빌드 에러 시 


빌드시 에러 `'ignoring return value of fgets' in C` 이라면  

unsed 되었다고 에러가 발생하는 것이라고 한다. 그냥 워닝에서 그치는 것이 아니라 아예 에러처리 되는 듯 하다   
null pointer 리턴 받게 되거나 할 때 (또는 EOF 일 경우) 에러가 발생  

tstcrc.c 파일의 약 100번째 줄을 수정

```c
if ( do_ascii  ||  do_hex ) {
    printf( "Input: " );
    if(fgets( input_string, MAX_STRING_SIZE-1, stdin ) == NULL) {
        // 여기에 에러처리 해준다. 그냥 빌드를 위한 거라면 비워둬도 상관 없음 (libcrc 경우)
    }
}
```
위 처럼 수정하고 다시 빌드   

빌드는 Makefile 파일이 있는 경로에서 실행
```
make all
```

## libcrc 사용 방법

실행 
```
./tstcrc -x
```

> -x 옵션은 HEX 코드 넣어주는 것

실행 입력 예 (띄어쓰기로 구분)
```
10 20 30 40
```

이 중 결과의 CRC16 (Modbus) 를 참고해주면 된다.  
**결과는 뒤 바뀌어서 나오게 되어 있다** 뒤의 2자리가 앞의 앞2자리 이다  
```
Input: 10 20 30 40
"" :
CRC16              = 0xFA10      /  64016
CRC16 (Modbus)     = 0xDE10      /  56848
CRC16 (Sick)       = 0x2030      /  8240
CRC-CCITT (0x0000) = 0xD030      /  53296
CRC-CCITT (0xffff) = 0x54F0      /  21744
CRC-CCITT (0x1d0f) = 0xDE20      /  56864
CRC-CCITT (Kermit) = 0x3C34      /  15412
CRC-DNP            = 0x0CC7      /  3271
CRC32              = 0xE08AB900  /  3767187712
```

즉, 10 DE 가 crc 체크된 값

