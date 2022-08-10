```cpp
// create payload data
	std::string data = "{\"MacAddress\": \"04-7C-16-05-E9-1A\", \"x\": \"$x\", \"y\": \"$y\"}";

	// regex 후 replace 변환, double은 string으로 
	data = std::regex_replace(data, std::regex("\\$x"), std::to_string(robot_x));
	data = std::regex_replace(data, std::regex("\\$y"), std::to_string(robot_y));
```

정규식은 \패턴\ 방식을 많이 사용하는데 cpp는 일단 \\로 이스케이프만 하고 시작하는듯  

$x 로 한 것은 $x만 잡아낼려고 혹시 x가 있을 수도 있으니 

