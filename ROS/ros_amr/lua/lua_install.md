# lua devel 버전 설치
기본적으로 lua 5.4 버전이 설치되어 있기는 하나, 헤더 파일등이 없다.  
devel 버전으로 설치해준다. 아래에 빌드하는 방법도 있으나, 이 방법을 사용하자!  

## on fedora

```
sudo dnf install lua-devel
```
lua-devel-5.4.6-5.fc40.x86_64  설치된다.

```
usr/
    include/
        lauxlib.h
        lua.h
        lua.hpp
        luaconf-x86_64.h
        luaconf.h
        lualib.h
    lib64/
        liblua.so
        pkgconfig/
            lua.pc
```
요렿게 설치되는 듯 하다.

## on ubuntu 20.04
```
sudo apt install liblua5.3-dev
```
> fedora에서는 일단 5.4 버전이라 호환이 되는지 확인이 필요하다;; 

ubuntu 20 버전에서는 5.3 버전까지 있는 듯 하고, 우분투 22 에서는 5.4 가 가능
```
sudo apt install liblua5.4-dev
```
호환이 안되면 아래 직접 build 하기

## lua build & install
5.4.4 버전을 다운로드 후에 압축 풀고 빌드
```
curl -R -O http://www.lua.org/ftp/lua-5.4.4.tar.gz
tar xvf lua-5.4.4.tar.gz
cd lua-5.4.4
make all test
```

이렇게 까지 하면 빌드가 완료가 된다   

## installing Lua
설치하기
```
make all install
```

> 깃허브에서 받은 디렉토리 중에 doc도 있는데 여기에 들어가면 html파일들이 있고 내용을 브라우저로 볼 수가 있다   

/usr/local/ibn/lua/5.4   /usr/local/bin  /usr/local/lib 등에 설치가 됨   
여기 경로에 설치가 되는 듯 하다
```
cd src && mkdir -p /usr/local/bin /usr/local/include /usr/local/lib /usr/local/man/man1 /usr/local/share/lua/5.4 /usr/local/lib/lua/5.4
cd src && install -p -m 0755 lua luac /usr/local/bin
cd src && install -p -m 0644 lua.h luaconf.h lualib.h lauxlib.h lua.hpp /usr/local/include
cd src && install -p -m 0644 liblua.a /usr/local/lib
cd doc && install -p -m 0644 lua.1 luac.1 /usr/local/man/man1
```


## g++ 로 빌드 하기
c++ 프로그램 내에서 include 는 extern 으로 해준다 
```cpp
extern "C" {
    #include <lua.h>
    #include <lualib.h>
    #include <lauxlib.h>
}
```
> cpp 이기 때문에 C 라고 알려주는 기능이라고 함

빌드는 `-llua -ㅣdl` 을 포함시켜주면 된다
```
g++ -o test main.cpp -llua -ldl
```
