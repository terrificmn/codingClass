# encoding 후 파일 만들기

> converting_base64 pkg를 이용해서 base64.cpp 파일을 include해서 사용할 때   

img 파일을 열어서 처리를 할 때 2가지 방법이 있음 

1. 파일을 연 후에 char 로 읽어서 하나의 string 배열을 넣어주는 방법이 있다    
이 방법이 다른 시스템, 언어(windows, C#) 와 호환성이 좋았고 문제가 없었음  
```cpp
char c;
std::string string_c;

std::ifstream input("dicrectory/img-file", std::ios::in | std::ios::binary);

if(input.is_open()) {
	while(input.get(c)) {
		string_c.push_back(c);
	}

	std::string encoded = base64_encode(reinterpret_cast<const unsigned char*>(string_c.c_str()), string_c.length());

/// 이후 결과 str을 만들어서 encoded를 넣어주면 된다
	input.close();
}
```

2.  파일을 연 후에 line by line으로 읽어서 처리하는 방법. 같은 base64 (c++) decode했을 때 잘 복원이 된다 
```cpp
std::ifstream input("dicrectory/img-file", std::ios::in | std::ios::binary);
std::string line;
std::ofstream output("directory/output-decoded-filename");

while(getline(input, line)) {
	std::string encoded = base64_encode(reinterpret_cast<const unsigned char*>(line.c_str()), line.length());
	std::string decoded = base64_decode(encoded);

	if (decoded != line) {
		std::cout << "decoded != input line" << std::endl;
		all_tests_passed = false;
	}
	
	//write file
	output << encoded;
		
	//write decoded_img 사용하려면 위에 객체 만들어 줘야함
	output_pgm << decoded_str + "\n"; //add linebreak
}
```

대충 이런식이 된다. 다시 decode를 할 때에는 함수만 사용하면 만들어진다  
단, output 파일로 내보낼 때에는 끝에 "\\n"을 넣어줘야 제대로 된 image 파일이 다시 만들어진다  
그래서 실행이 가능해 진다  

> 윈도우와 리눅스 사이에 엔터 처리가 달라서 windows에서나 다른언어로 했을 때 호환이 잘 안되는 문제가 있었다. 이 부분을 해결하면 원할하게 될 듯도 하다  

대충 line 사이에 = 기호가 들어가는데 이 부분을 수정하면 될 듯 하지만, 참고로 windows 에서 base64로 인코딩 한 것과 비교를 해보면 windows에서는 = 로 처리를 안 하는 듯 하다 
> include 한 base64.cpp 파일의 trailing_char 변수를 확인하고 처리하는 부분에 (if문) 에서 ret.push_back() 부분을 수정하면 될 듯도 하다. 연구가 필요!
 

```cpp
while (pos < in_len) {
	ret.push_back(base64_chars_[(bytes_to_encode[pos + 0] & 0xfc) >> 2]);

	if (pos+1 < in_len) {
	... 생략
	}
	else {
	  ret.push_back(base64_chars_[(bytes_to_encode[pos + 1] & 0x0f) << 2]);
	  ret.push_back(trailing_char);
```

대충 요 부분임

