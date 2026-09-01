# Mecanum Functions

각 모터마다 2개의 신호가 있음
| AI1 (BI1) | AI2 (BI2)   | Direction |
| --- | --- | --- | 
| LOW | LOW | OFF |
| HIGH | LOW | FORWAWRD |
| LOW | HIGH | REVERSE |
| HIGH | HIGH | BRAKE |

Front / Rear 휠로 각각 left/right 로 4개의 바퀴  

MF-L, MF-R, MR-L, MR-R

## straight

| Direction | MF-AI1 | MF-AI2 | MF-BI1 | MF-BI2 | MR-AI1 | MR-AI2 | MR-BI1 | MR-BI2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| straight forward | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| straight backward | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 비고 | MF-R | MF-R | MF-L | MF-L | MR-R | MR-R | MR-L | MR-L |


## sideways

| Direction | MF-AI1 | MF-AI2 | MF-BI1 | MF-BI2 | MR-AI1 | MR-AI2 | MR-BI1 | MR-BI2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sideways right | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| sideways left | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 |
| 비고 | MF-R | MF-R | MF-L | MF-L | MR-R | MR-R | MR-L | MR-L |

## Diagonal
| Direction | MF-AI1 | MF-AI2 | MF-BI1 | MF-BI2 | MR-AI1 | MR-AI2 | MR-BI1 | MR-BI2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 45 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| 135 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 225 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| 315 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| 비고 | MF-R | MF-R | MF-L | MF-L | MR-R | MR-R | MR-L | MR-L |

## Pivot
| Direction | MF-AI1 | MF-AI2 | MF-BI1 | MF-BI2 | MR-AI1 | MR-AI2 | MR-BI1 | MR-BI2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pivot right forward | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 |
| pivot right backward | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| pivot left forward | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| pivot left backward | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| 비고 | MF-R | MF-R | MF-L | MF-L | MR-R | MR-R | MR-L | MR-L |

## Rotate

| Direction | MF-AI1 | MF-AI2 | MF-BI1 | MF-BI2 | MR-AI1 | MR-AI2 | MR-BI1 | MR-BI2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| clockwise | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| counter-clockwise left | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| 비고 | MF-R | MF-R | MF-L | MF-L | MR-R | MR-R | MR-L | MR-L |

## Pivot SideWays
| Direction | MF-AI1 | MF-AI2 | MF-BI1 | MF-BI2 | MR-AI1 | MR-AI2 | MR-BI1 | MR-BI2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pivot sideways front right | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| pivot sideways front left | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| pivot sideways rear right | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| pivot sideways rear left | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| 비고 | MF-R | MF-R | MF-L | MF-L | MR-R | MR-R | MR-L | MR-L |


18 바이트가 필요하다. 현재까지 있는 움직임을 구동하려면 8비트씩 18개가 필요

예를 들어서.. byte로 선언하고 숫자의 B는 binary 넘버를 의미한다 
```cpp
const byte MEC_STRAIGHT_FORWARD = B10101010;
```


