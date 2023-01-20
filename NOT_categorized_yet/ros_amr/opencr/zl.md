### 보낼 때

| Driver Address | Function Code | 내용                          |
| -------------- | ------------- | ----------------------------- |
| 01             | 03            | Read Register                 |
|                | 06            | Write Single register (16bit) |
|                |               |                               |
|                |               |                               |

이어서 
| High 8 bits of register start address | Low 8 bits of register start address | 내용                   |     |
| ------------------------------------- | ------------------------------------ | ---------------------- | --- |
| 20                                    | 0E                                   | Control word           |     |
| 20                                    | 0D                                   | control mode           |     |
| 20                                    | 80                                   | 액셀 타임(left)        |     |
| 20                                    | 81                                   | 액셀 타임(right)       |     |
| 20                                    | 82                                   | 감속 타임(left)        |     |
| 20                                    | 83                                   | 감속 타임(right)       |     |
| 20                                    | 88                                   | target velocity(left)  |     |
| 20                                    | 89                                   | target velocity(right) |     |
|                                       |                                      |                        |     |

control word 는 각 quick stop, clear fault, stop, enable 이 있다  
20 0E 00 05 quick stop
20 0E 00 06 clear fault
20 0E 00 07 stop
20 0E 00 08 enable

control mode 는 3 은 velocity mode
20 0D 00 03 velocity mode

이제 나머지 acceleraion time/ Deceleration time / Traget velcity 는 그 다음



> 아무래도 json 형식으로 표현하는게 더 나을 듯 하다;;; 아흐 복잡혀



이어서

| High 8 bits of register number | Low 8 bits of register number |
| ----------------------------- | ----------------------------- |
|                               |                               |

이어서

| High 8 bits of CRC check | Low 8 bits of CRC check |
| ------------------------ | ----------------------- |
|                          |                         |


위의 8개의 내용을 보내야함

합치면  예를 들어   
01 03 20 AB 00 02 BE 2B

16비트 CRC check 바로 전 데이터가 Low 16bit register number 이다 . 각각의 mode들임
| register number | 모드 (control mode) | 16bits |
| --------------- | ------------------- | ------ |
| 03              | Velocity mode       | 00 03  |
| 04              | Torque mode         | 00 04  |
| 05              | quick stop          | 00 05  |
| 06              | clear fault         | 00 06  |
| 07              | stop mode           | 00 07  |
| 08              | enable mode         | 00 08  |
|                 |                     |        |

mode 전에 control word랑 짝이 맞아야 한다




04 토크 모드는 따로 매뉴얼 참고



오류 코드  
