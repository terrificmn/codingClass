현재 windows에서는 다행히 base64 형식을 decode 해서 파일이 열리나  

리눅스 우분투에서는 파일의 header를 임의로 수정한 것은 열리지 않는다  
```
pnm loader expected to find an integer
```
에러가 발생하면 열 수가 없다.

좀 더 연구를 해봐야할 듯 하다 

[pnm파일 header관련 내용보기]([https://www.scratchapixel.com/lessons/digital-imaging/simple-image-manipulations)

[stackoverflow의 ppm관련 코드](https://stackoverflow.com/questions/2693631/read-ppm-file-and-store-it-in-an-array-coded-with-c)


