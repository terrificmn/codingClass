# Topics, Services, Actions
노드 간에 통신을 할 때 사용하는 방식에 대해서 알아보자~

<br>

## 먼저 Topics이다
Topics 는 Publisher와 Subscriber로 나눠지는 방식이다. 

Publisher는 어떤 Topic에 대해서 계속 통신을 하게 된다. 이 때에는 듣는 사람 상관없이 계속 보내기만 하게 된다

Subscriber는 Topic만 맞춰주면 Publisher가 보내는 내용을 받을 수 있게 된다. 하지만 topic을 맞추지 않는다면
내용을 받을 수가 없다.

> 예를 들어 라디오를 생각한다면,   
라디오는 계속 송출이 되고 있고 이는 publisher 처럼 보인다  
그러면 나는 어떤 라디오를 듣고 싶은지 정해서 주파수를 정해준다. 이는 topic이다  
나는 subscriber가 되고 그 topic를 통해 publisher의 통신을 들을 수 있다.
그리고 다른 사람이 또 같은 주파수를 통해 즉, topic을 같은 것으로 정해서 듣는다면  
하나의 publisher가 여러명의 subscriber에게 내용을 전달하게 되는 것도 가능해진다

다른 예로는 유투브가 있다. 구독을 하게 되면 구독자(subscriber)가 되고, 어떤 유부버가 (publisher)
계속 발행하는 내용을 볼 수 있다.

<img src=0>
<br>
<img src=1>
<br>
<img src=2>
<br>
<img src=3>

> 물론 유부트 추천 알고리즘과 구독 안해도 볼 수 있는 것은 감안하고 생각하자

<br>

## Services
services는 서버와 클라이언트를 생각하면 쉽다.  
말 그대로 클라이언트가 요청을 하면 서버가 응답을 해주는 방식이다

예를 들어 API-server의 활용을 생각해 볼 수 있고,   
좀 더 쉽게 생각하면 맥도날드 같은 패스트푸드점 될 수도 있다.

점원 즉, Server에게    
나 Client 가 햄버거를 주문을 해야지만 점원이 나에게 햄버거를 주게 되는 것과 같다.

<img src=4>
<br>
<img src=5>
<br>

여기에서는 클라이언트가 요청을 해야지만 서버가 응답을 한다.
내가 주문을 안하게 된다면 햄버거를 받을 수 없게 되는 것과 같다

service 방식은 서버에서는 요청을 하면 바로 응답을 해줘야하는 것이 특징이다.

ROS에서는 Sevrice를 요청하면 서버는 즉각 클라이언트에게 응답하는 것으로 되어 있다.

<br>

## 마지막으로는 Actions 이다
actions는 services와 비슷하지만 action server/ client 라고 부르며

클라이언트에서 요청을 하게 되면 서버에서 응답을 해주는 방식까지는 같지만
서버는 어떤 액션을 한 다음에 액션이 끝나게 되면 클라이언트에게 요청을 해주는 방식이다.

그래서 클라이언트에서는 요청을 하고 난 뒤에 바로 응답을 받는 것이 아니고 기다리게 된다.

액션 서버는 중간 중간 액션이 끝날 때 응답을 해주고, 최종 액션이 끝나게 되면 
액션 클라이언트에게 최종 응답을 해주게 된다.

예를 들어 청소 로봇이 있다고 하자~ 청소 로봇은 방 2개를 청소하는 프로그램이라고 가정을 하면

클라이언트가 로봇 청소기에게 청소를 요청을 한다

<img src=6>
<br>

그러면 로봇 청소기는 액션을 시작하고 청소를 하게 된다.

그리고 클라이언트는 응답은 못 받고 기다리고 있는 상태가 되고 

<img src=7>
<br>


중간마다 방 1 청소 끝 같은 응답을 받게 되고 
또 다른 액션인 방 2 청소 끝 으로 응답을 한다
<img src=8>
<br>
<img src=9>
<br>

최종적으로 청소가 끝나게 되면 청소 끝으로 클라이언트에게 응답을 하게 된다

<img src=10>
<br>








