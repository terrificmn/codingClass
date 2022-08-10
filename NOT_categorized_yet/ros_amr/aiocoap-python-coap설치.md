https://aiocoap.readthedocs.io/en/latest/guidedtour.html

설치는 먼저 깃 허브 클론  
```
git clone https://github.com/chrysn/aiocoap
cd aiocoap
```

aiocaop 디렉토리에서 pip3로 인스톨하기.
```
pip3 install --upgrade ".[all,docs]"
```


## Learning asyncio: "coroutine was never awaited" warning error
파이썬 coap은 사용하기도 쉽고 잘 되는 듯 하다  

단,   
Learning asyncio: "coroutine was never awaited" warning error 에러가 발생한다  

async def 함수를 사용을 해야해서 생소하다  
asyncio을 사용할 떄 다른 함수에서 loop이 돌아간다면 사용이 제대로 안된다 


ros에서 spin()으로 돌아갈 때 어떤 식으로 호환을 시키는지 모르겠다 ㅋㅋ
그래서 패스 . 다시 cpp로 



기본 참고   
https://www.geeksforgeeks.org/how-to-run-two-async-functions-forever-python/