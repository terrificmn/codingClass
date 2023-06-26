# amr development

stm32 을 사용할 때 관련 프로그램을 빌드하려면 
gcc-arm-none-eabi gcc 등의 Arm GNU Toolchanin 이라고 불리는 프로그램이 필요  

## 설치
Arm GNU Toolchain 을 다운로드 받는다  
[GNU Arm Embedded Tollchain Download](https://developer.arm.com/downloads/-/gnu-rm)
 

> stm32 MCU 에 obj code를 만들어준다 (micro-controllers / microprocessor 전용)   

압축을 풀어준다 
```
tar xvf gcc-arm-none-eabi-10.3-2021.10-x86_64-linux.tar.bz2 
```

해당 gcc-arm-none-eabi-버전 으로 디렉토리가 생긴다. 이제 이를 

이동 시켜준다
```
mv gcc-arm-none-eabi-10.3-2021.10/ /usr/share
```

그리고 각각의 gcc, g++ 등을 사용하기 위해서 심링크를 걸어준다

```
sudo mv gcc-arm-none-eabi-10.3-2021.10 /usr/share
sudo ln -s /usr/share/gcc-arm-none-eabi-10.3-2021.10/bin/arm-none-eabi-gcc /usr/bin/arm-none-eabi-gcc
sudo ln -s /usr/share/gcc-arm-none-eabi-10.3-2021.10/bin/arm-none-eabi-g++ /usr/bin/arm-none-eabi-g++
sudo ln -s /usr/share/gcc-arm-none-eabi-10.3-2021.10/bin/arm-none-eabi-gdb /usr/bin/arm-none-eabi-gdb
sudo ln -s /usr/share/gcc-arm-none-eabi-10.3-2021.10/bin/arm-none-eabi-size /usr/bin/arm-none-eabi-size
sudo ln -s /usr/share/gcc-arm-none-eabi-10.3-2021.10/bin/arm-none-eabi-objcopy /usr/bin/arm-none-eabi-objcopy
```

의존성 패키지 추가 설치1
```
sudo apt install libncurses-dev libncurses5
```

명령어 잘 되는 지 확인 
````
arm-none-eabi-gcc --version
```


