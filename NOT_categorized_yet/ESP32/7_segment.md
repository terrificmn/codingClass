# 7 segment

연결이 꽤 복잡하다(?)  

## Cathode type

핀이 위에 5개, 아래 5개씩 배치되어 있는데, 위의 핀 중 가운데 3번째 핀에 저항을 연결한 다음에   
ESP32, 또는 아두이노의 GND 에 연결해준다.   
그리고 위쪽의 오른쪽 끝의 핀을 보드의 핀에(D21, RX0, TX0 등) 연결을 해주게 되면  
오른쪽 끝 막대가 불이 켜지면 Cathode 방식이라고 한다    

> +(신호), GND가 연결이 되어서 불이 들어오는 것을 확인하는 것 같다

핀 순서는 

g f 저항 a b  (위쪽)
| |  |  | |


| |  |  |  |
e d 저항 c (생략) (아래)


ESP32에서 성공했던 핀들과 매칭을 해보면  

| 순서 | cathode abc..핀 | ESP32 핀 |
| --- | --- | --- |
| 1 | a | 25 |
| 2 | b | 26 |
| 3 | c | 18 |
| 4 | d | 19 |
| 5 | e | 21 |
| 6 | f | 33 |
| 7 | g | 32 |

> 위에서 그림으로 표현하지는 못했지만.. 실제 abc..핀의 위치가 순서대로 되어 있지 않으므로  
헷깔릴 수 있다. esp핀도 순서대로 해주면 좋겠지만, 다 붙어있는 것은 아니라서   
위 처럼 순번을 정해서 기억을 해놓아도 될 듯 하다   



