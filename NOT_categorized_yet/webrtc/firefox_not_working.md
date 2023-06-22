# firefox 에서 webrtc가 안 되는 문제
firefox에서 동영상 스트리밍 화면이 나오지는 않는다. WebRTC 크롬 기반이라서 그런가 했는데,  
좀 더 자세히 찾아보니 이런, 크롬, 사파리, 파이어폭스, 엣지, 오페라 등등 최신 버전은 다 지원이 된다   

> 물론 IE 빼고  

파이어폭스에서 안 되는 이유에는 Websocket 에서 upgrade request 를 하면 HTTP/1.0 기반으로   
응답을 하게 되어 있는데  

파이어폭스는 HTTP/1.1 이어야 한다고 한다  

그래서 async_web_server_cpp 패키지 (webrtc_ros 의 의존성 패키지 중 하나)의 http_reply.cpp 파일을 수정해준다   

src/http_reply.cpp
```cpp
// 생략..
namespace status_strings
{
// 네임스페이스가 시작되고 22번째 줄의 string 값을 변경
const std::string switching_protocols =
//   "HTTP/1.0 101 Switching Protocols\r\n"; // 1.0을 삭제하고 1.1로 변경
    "HTTP/1.1 101 Switching Protocols\r\n";
// 생략
}
```

이제 `async_web_server_cpp` 를 빌드해주고 다시 webrtc_ros 를 실행하면 파이어폭스에서도 영상이 잘 나오게 된다  
```
cd ~/webrtc_ws
catkin build async_web_server_cpp
```

[레퍼런스 (under "The WebSocket handshake")](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_servers)

