


#### vector의 인덱스를 알아보는 함수
vector를 만들고 그 안에 특정 요소 (문자열)을 찾을려고 하면 인덱스를 리턴한다
```cpp
int getIndexOfVec(std::vector<std::string> vecs, std::string find_str);

int main(){
	std::vector<std::string> vecs {"Find", "String", "Vector", "Index"};
	int result = getIndexOfVec(vecs, "Index");
	std::cout << index << std::endl;
}
```

함수 내용
```cpp
int getIndexOfVec(std::vector<std::string> vecs, std::string find_str) {

	auto it = std::find(vec.begin(), vec.end(), find_str);
	if (it != vec.end()) {
		int index = std::distance(vec.begin(), it);
		std::cout << find_str <<"'s index: " << index << std::endl;
	}
return index;
}
```



이건 그냥 벡터에 있는 내용 출력하고 싶을 때
```cpp

std::vector<std::string> vec = {"hello", "world", "yes", "cpp"};
for(auto aa: vec) {
	std::cout << aa << std::endl;
}
```