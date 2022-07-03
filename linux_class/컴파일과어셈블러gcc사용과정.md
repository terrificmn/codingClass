## 설치
우분투 기준   
sudo apt-get install gcc  
를 먼저 설치해준다  

그래도 안되면 build-essential 을 설치

간단한 c 언어 작성한 후 program.c  
(nano로 작성해보기)

전처리기 까지만 생성해보기 (-E 옵션) : 전처리결과 파일이 만들어 진다  
```
gcc -E program.c -o program_preprocessed.i
```

전처리결과 부터 파일을 기계어 가깝게 어셈블러로 만들기 (-S 옵션)  
```
gcc -S program_preprocessed.i -o program_compiled.s
```

이제 바이너리 파일이어서 볼 수가 없고 vim으로 읽으면 이상한 기호만 보인다  
그래서 hexdump라는 명령어로 볼 수 있다 . 16진수로 보여줌  
어셈블리어   
```
$hexdump program_assembled.o 
```
**참고로 뭔가 파일이 안열리거나 했을 때 hexdump파일로 열어보면 실행파일인지 구별할 수 있다고 함  


어셈블러 결과로 부터 링커까지만 진행해서 링커 결과 파일 만들기
```
$ gcc program_assembled.o -o program_linked.exe
```
실행이 가능한 exe파일이 만들어진다. 

