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


## 기본 example
```py
class PoseRosRelated():
    def __init__(self):
        self.odomSub = rospy.Subscriber('/odom', Odometry, self.odomCb)
        self.posePub = rospy.Publisher('/send_pose', PoseStamped, queue_size=10)

    def UserFunc():
        pass


async def coapSend(x, y): 
    context = await Context.create_client_context()
    await asyncio.sleep(1)

    payload = b'{\'Name\': \'hello\', \'x\': \'100\', \'y\': \'100\'}'

    request = Message(code=POST, payload=payload, uri="coap://192.168.10.100/endpoint")  #192.168.10.28

    response  = await context.request(request).response

    print('Result: %s\n%r'%(response.code, response.payload))


async def main():
    rospy.init_node('pose_send_node')

    sendPoseObj = SendPose()

    rospy.spin()


if __name__ == '__main__':
    asyncio.run(main())

```
대충 이런식이다. aiocoap 패키지에 example이 있으므로 참고하자  



## Learning asyncio: "coroutine was never awaited" warning error
파이썬 coap은 사용하기도 쉽고 잘 되는 듯 하다  

하지만   
Learning asyncio: "coroutine was never awaited" warning error 에러가 발생한다  

async def 함수를 사용을 해야해서 생소하다  
asyncio을 사용할 때 다른 함수에서 loop이 돌아간다면 사용이 제대로 안된다   

ros에서 spin()으로 돌아갈 때 어떤 식으로 호환을 시키는지 모르겠다 ㅋㅋ
그래서 패스 . 다시 cpp로 (추후 시간이 나면 연구를..)


기본 참고   
https://www.geeksforgeeks.org/how-to-run-two-async-functions-forever-python/