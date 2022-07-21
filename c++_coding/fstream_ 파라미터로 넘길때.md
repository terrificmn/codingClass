ofstream을 이용해서 파일을 연 것을 함수의 argument로 보낼려면  

```cpp
    std::ofstream myFile;

    myFile.open("test.txt", std::ios::app);

    myFile << "test";

    fileFunction(myFile);
    myFile.close();


void fileFunction(std::ofstream& myFile) {
    if (myFile.is_open()) {
        std::cout << "a file is existed." << std::endl;
        
    }
```

reference로 해줘야 함 &

