```c
find_package(Lua REQUIRED)


target_link_libraries(타켓라이브러리
    ${LUA_LIBRARIES}
)
```

이 정도만 넣으면 작동함  
