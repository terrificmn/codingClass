# lud if else 
루아 파일 심플 사용

변수에 빈값을 넣을 때는 `nil`,

if 로 시작해서 then 을 넣고, 중간 else, 끝에는 end
```lua
if temp == nil then
    print("test")
else
    print("test2")
    temp = 1
end
```

## 환경 변수에서 받기 

```lua
os.getenv("ns_robot1")
```

c++의 getenv() 함수와 비슷하다. 실제 환경변수를 받아올 수도 있을 것 같은데 ~~테스트는 못해봄~~  
된다.. ㅋㅋ
```lua
print(os.getenv("PATH"))
```

## ros launch 에서 env 받기  환경변수
이를 ros launch file을 이용해서 런치파일 실행하면서 환경 변수로 만들면 이를 받아서 사용할 수 있다   
```xml
<env name="my_robot_path" value="/home/user/robot_path">
```




