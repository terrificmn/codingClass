# lua install
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

빌드는 `-llua -ㅣdl` 을 포함시켜주면 된다
```
g++ -o test main.cpp -llua -ldl
```
