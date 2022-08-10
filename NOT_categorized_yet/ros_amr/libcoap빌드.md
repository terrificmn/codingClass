먼저 configure을 해줘야하는데  
그냥 기본 설정으로 한다면  

```
./configure --help 
```
를 해서 enable이 어떤 것들이 default가 되어 있는지 확인할 수 있고 뺄 수도 있다  


그냥 configure를 했는데 아래와 같은 에러라면  
```
checking for a2x... no
configure: WARNING: ==> You want to build the manpages, but a2x was not found!
configure: error: ==> Install the package that contains a2x (mostly asciidoc) or disable the build of the manpages using '--disable-manpages'.
```
이런 메세지가 나오는데 위 처럼 ./configure --disable-manpages 을 해서 하거나  

a2x관련 패키지를 설치해준다 
```
sudo apt install asciidoc-base
```

```
./configure --disable-documentation
```
그리고 make 끝나면 make install
```
make 
make install
```

client 예제를 실행했을 때 아래 같은 에러이면  

./client: error while loading shared libraries: libcoap-3-openssl.so.3: cannot open shared object file: No such file or directory

libcoap-3-openssl.so.3를 심볼릭 링크를 걸어줘야 한다 
/usr/local/lib 디렉토리에 libcoap-3e-openssl.so.3로 심볼릭 링크를 만들어서 libcoap-3-openssl.so.3.0.0 을 가리켜준다  

먼저 이동
```
cd /usr/local/lib
```
```
sudo ln -s libcoap-3-openssl.so.3.0.0 libcoap-3.so.3
```

> 항상 헷깔리는게 ln -s 는 {원본파일target} {심복링링크파일명}

아니면
```
sudo ldconfig
```
를 해주면 아무런 메세지도 안 나오지만 심복릭 링크를 만들어 주는 듯 하다



minimal coap 예제   
https://github.com/obgm/libcoap-minimal

libcoap-3가 있어야 하고 간단한 예제지만,, 실패;; 그냥 참고만 하자 어렵다 ㅠ

cantcoap cpp 용으로 사용하자 

