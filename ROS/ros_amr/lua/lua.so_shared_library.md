# lua shared library 실패
lua 이용해서 어떤 shared library 형태로 만들려고 하면

```
/usr/bin/ld: /usr/local/lib/liblua.a(lstate.o): relocation R_X86_64_PC32 against symbol `lua_newstate' can not be used when making a shared object; recompile with -fPIC
/usr/bin/ld: final link failed: bad value
```
이런 결과   
-fPIC로 shared 라이브러리로 만들어야 하는 것 같다.  아예 lua를. so 파일로 만들어야 하는 것 같은디...  

so파일이 없다..;; 
야매로 만들면 기존 원 소스 파일에서 a 파일을 통해서 만들 수 있다고 한다   (lua_install.md 참고)
```
gcc -shared -o liblua.so src/liblua.a 
```
잘 만들어진다.. 이를 CMakeLists.txt에서 사용하려면 다음과 같이..

```
find_package(Lua REQUIRED)

add_library(
    amr_model_publish SHARED 
    src/model_publish.cpp
)

set(LUA_SO_LIBRARIES /usr/local/lib/liblua.so)
target_link_libraries(amr_model_publish
    ${GAZEBO_LIBRARIES}
    ${LUA_SO_LIBRARIES}
)

set_target_properties(amr_model_publish PROPERTIES
    IMPORTED_LOCATION "/usr/local/lib/liblua.so"
)
```
기존에는 빌드를 하게 되면 아예 에러가 발생하지만, 위 방법처럼 하면 빌드는 빌드만 잘 된다,     
단, gazebo 플러그인에서 (so파일)이어서 할려고 했던 것인데  
안타깝게도 빌드는 이상 없으나, 실행시 gazebo쪽에서 lual_newstate 부터 인식을 못하는 것 같다..

```
gzserver: symbol lookup error: /home/sgtubunamr/catkin_ws/devel/lib/libamr_model_publish.so: undefined symbol: luaL_newstate
```

결국 실패 : 일단 포기

포기는 하지만.. 일단,  
gazebo 플러그인 상태에서만 인식을 못하는 것인지 아니면 일반 so파일 라이브러리에서도 그러한지 테스트를 해봐야겠다  





