[여기https://www.softwaretestinghelp.com/regex-in-cpp/](https://www.softwaretestinghelp.com/regex-in-cpp/)

[여기도 참고](https://linuxhint.com/regular-expression-basics-cpp/)

```cpp
#include <regex>

// create payload data
	std::string data = "{\"MacAddress\": \"04-7C-16-05-E9-1A\", \"x\": \"$x\", \"y\": \"$y\"}";

	// regex 후 replace 변환, double은 string으로 
	data = std::regex_replace(data, std::regex("\\$x"), std::to_string(robot_x));
	data = std::regex_replace(data, std::regex("\\$y"), std::to_string(robot_y));
```

~~정규식은 \패턴\ 방식을 많이 사용하는데 cpp는 일단 \\ \\ (더블 백슬래쉬)로 이스케이프만 하고 시작하는듯  
$x 로 한 것은 $x만 잡아낼려고 혹시 x가 있을 수도 있으니 ~~

더블 백슬래쉬는 이스케이프를 할 때 사용하는데, 다른 언어에서는 \\ 한번만 사용하지만  
c++에서는 두 번을 사용해야한다  

> 운이 좋아서 실행이 되었는지?? ㅋㅋ 잘 못 알고 있었다;;;

다른 언어와 마찬가지로 [ ] 안에서 regex를 사용하면 되겠다  

자주 사용하는 함수는 std::regex_replace(), std::regex_search() 등이 있다 



origin: [-28.126819, -27.423724, 0.000000]
여기 스트링에서 찾아보기



```cpp
void openFile(std::string file_path) {
	std::fstream yamlFile;
	std::string line;
	yamlFile.open(file_path, std::ios::in);
	if (yamlFile.is_open()) {
		int counter_=0;
		while(getline(yamlFile, line)) {

			if(counter_ == 2) {
				ROS_INFO("%s", line.c_str());
				std::string test_string = "01234 abcd";
				std::regex reg("[ 0-9.,-]+");  /////space is problem
				std::smatch mat;
				if (std::regex_search(line, mat, reg)) {
					std::cout << "ok found it" << std::endl;
					for(auto x: mat) {
						std::cout << x << " \n";
					}
				}

			}

			counter_++;

		}
```