# http

TCP 로 소켓 통신을 해서 포트를 8080 등으로 해서 웹 브라우저에서 볼 수가 있는데   

이때 HTTP 관련 헤더를 만들어 줘야하는데  
일단 windows 경우는 문자열의 끝에서는 즉, 줄바꿈을 할 때 CR, LF가 들어가야한다 `\r\n` 이 된다   

하지만 리눅스는 LF만 사용을 하는데, 리눅스에서는 LF 즉 `\n`만 사용해도 작동에는 문제가 없었다

> CR: Carriage Return, LF: Line Feed   
리눅스도 무조건 사용해야하는지는 모르겠지만, `\n`으로도 일단 ok이다


HTTP/1.1 에 관한 프로토콜이 RFC 2616 이라고 하는데, 시간이 나면 읽어보는 것도 좋겠지만  
너무 많은 내용인 듯 하다   

[MDN 사이트를 이용하는게 좋을 듯 하다](https://developer.mozilla.org/en-US/docs/Web/HTTP)



