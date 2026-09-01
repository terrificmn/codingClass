# is number
lua와 연결한 cpp 함수에 내용을 받을 때   

특히  
 `lua_isstring(L, 5)` 숫자를 넣던, 스트링이 넘어 오든 스트링 구분은 제대로 하지 못한다.   

 그래서 스트링인지 비교하려면  
```lua
if(lua_type(L, i+1) == LUA_TSTRING)
```

위와 같은 방식으로 사용하면 잘 구분 한다 

> +1 해준 것은 lua에서 넘어 온 값은 기본적으로 1부터 시작됨


그외 `lua_isnumber(L, i)`, `lua_isinteger(L, i)` 식으로 사용할 수 가 있는데   
숫자 구분은 잘 해준다, 스트링 들어가면 false를 반환



