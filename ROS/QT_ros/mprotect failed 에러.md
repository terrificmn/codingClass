#
qt qml 을 이용한 프로그램을 사용할 때 나오는 워닝   
현재까지는 워닝 수준으로 보이고 프로그램에 영향은 없는 듯 하다   
```
mprotect failed in ExecutableAllocator::makeExecutable: Permission denied
mprotect failed in ExecutableAllocator::makeExecutable: Permission denied
mprotect failed in ExecutableAllocator::makeExecutable: Permission denied
```

환경 변수를 셋팅해주면 더 이상 메세지가 출력되지 않는다. 
```
export QV4_FORCE_INTERPRETER=1
```
자바스크립트, JIT 과 관련된 것 같다. JIT을 중단하는 

> Setting this environment variable disables the JIT and runs all functions through the interpreter, no matter how often they are called.

> JIT: Just-In-Time compilation   
즉 컴파일 방식에는 정적 컴파일과 인터프리터 방식이 있음. 실행하기전 기계어로 컴파일하는 것이 정적 컴파일,  
인터프리터는 실행 중에 프로그램을 읽으면서 실행하는 차이점이 있다고 함   
JIT 은 위 2가지 기능을 합친(?) 방식, 인터프리터 방식으로 프로그램이 가동 중에 기계어로 변환,   
코드들을 캐싱을 하여서 같은 함수를 또 사용하면 매번 기계어로 다시 컴파일되는 것을 방지해준다고 한다    

그래서 interpreter 방식으로 QML을 돌리는 것 같다. 테스트 해보고 괜찮으면 bashrc에 넣어준다 

