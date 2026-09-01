# tar 압축 시에 --transform 사용
보통 `tar cvfp my_compressed.tar my-install` 이런식으로 사용하게 되면 my-install 디렉토리를 압축하게 된다.  

현재 압축해야할 my-install 이라는 디렉토리에 source 파일 등이 있거나   
다시 압축을 풀 경우에 같은 이름으로 my-install 로 풀리기 때문에 덮어 씌어지거나 할 수 있는데  
이때 --transform 을 사용할 수가 있다.   

물론 쉽게 `cp -r my-install my-install-test` 이렇게도 할 수 있겠지만...   

어쨋든 --transform 은 sed-sytle subsitituion regex 를 사용하는데
```
's/^원래내용/바꿀내용/'
```
^ 은 스트링에서 처음 시작 나오는 것만 매칭을 한다. 그래서 top directory 만 지정될 수 있게 함  

실제로는 
`--transform='s/^my-install/my-install-test/'`

그래서 이런식으로 사용하면 좋다   
```
tar Jcvfp my_compressed.tar --transform='s/^my-install/my-install-test/' my-install
```

이제 압축된 파일을 풀어보면 my-install-test 디렉토리 이름으로 풀어진다.  

## 압축 형태
-J  .tar.xz   xa 알고리즘,  속도는 느림,  Best Compression   
-z  .tar.gz   gzip 알고리즘,   속도 빠름, Medium Compression,  Very widely supported  
--zstd  .tar.zst  Zstandard   속도 빠름 & modern  Close to xz , 최신 (기본으로 사용은 안될 수도 있다)

