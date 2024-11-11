# protoc 버전

빌드할 때 "google/protobuf/runtime_version.h" 파일을 찾지 못한다.  
아마도 protoc를 아예 빌드를 했었는데 이게 영향을 줬을 수도 있다. 어쨋든 버전이 안 맞는 경우 인 듯 하다.



쉡 스크립트로 설치하지 않는다. --> cartographer 디렉토리 안에 있는 scrtipts 에 보면 `install_proto3.sh`  이걸로 설치하지 않는다.   

아예 지웠다가 다시 설치해준다.
```
sudo apt purge libprotoc-dev
sudo apt install libprotoc-dev
```

이후 `catkin clean` 으로 한번 지워준 후에 다시 빌드를 진행 한다.  

```
protoc --version
``` 
으로 확인해보면 3.6.1 이다.

