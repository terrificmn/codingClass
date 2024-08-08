# websocket 설치

```
sudo apt install libwebsocketpp-dev
```

인쿠루드는 
```cpp
#include <websocketpp/client.hpp>
#include <websocketpp/config/asio_no_tls_client.hpp>
```

다행히 `/usr/include/websocketpp` 이하에 설치가 되어서 header 파일 인쿠르드 하는데 크게 문제는 없다.

> websocket 이후 pp 가 붙는 것에 주의 ㅋ



### example
[exampel github](https://github.com/zaphoyd/websocketpp/blob/master/examples/)
