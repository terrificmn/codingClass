# AMR Labs Modbus Protocol
범퍼, 트레이, e스탑, 휠 락커, 레드 라이트, 네오픽셀, 배터리, 무선 조종기   
(* 모터 드라이브 / 배터리는 (요청) 예외로 한다.)  

프로토콜 정의.

## 프로토콜 설명
- 싱글 기능을 이용할 경우에 아래와 같은 형식으로 보내게 된다.

```
장치명,  
Function Code (싱글 펑션),  
주소 (1byte high) - 편의상 시작 주소  
주소 (1byte low) - 편의상 끝 주소  
데이터 (1byte high)    
데이터 (1byte low)  
crc (1byte high)    
crc (1byte low)  
```

- 멀티 기능 코드를 이용할 경우에는 아래와 같은 형식으로 보내게 된다.  
예를 들어서 3개의 프로토콜로 보내는 경우   

```
장치명,  
Function Code(멀티 펑션),   
주소 (1byte high) - 편의상 시작 주소  
주소 (1byte low) - 편의상 끝 주소  
주소 (1byte low) - 편의상 끝 주소  (주소는 사용할 만큼 사용되게 된다.)
주소 (1byte low) - 편의상 끝 주소  (주소는 사용할 만큼 사용되게 된다.)
프로토콜 갯수 (1byte high)   (0x00 으로 해준다.)   
프로토콜 갯수 (1byte low)  - 실질상 low 쪽에 입력   
프로토콜 바이트 (1byte)  - 위의 프로토콜 갯수에 2 곱하기 (프르토콜당 데이터는 2byte가 필요)   
데이터 (1byte high)  
데이터 (1byte low)  
데이터 (1byte high)  
데이터 (1byte low)  
데이터 (1byte high)   
데이터 (1byte low)  
crc (1byte high)    
crc (1byte low)  
```


## 네오픽셀
| 이름      | 내용 |
| -------- | ---- |
| device id | 0x01  |
| function code | 0x06 |
| address |  0x40 |
| address | 0xA0  |
| data |  0xFF |
| data |  0xFF |
| crc  |  계산된 crc값 |
| crc  |  계산된 crc값 |

low address : A0, A1, A2, A3,  
| 이름      | 내용 | 설명 |
| --- | --- | --- | 
| address (low) | 0xA0  | 샤시 color R |
| address (low) | 0xA1  | 샤시 color G |
| address (low) | 0xA2  | 샤시 color B |
| address (low) | 0xA3  | 샤시 blink time |
| --- | --- | --- | 
| address (low) | 0xA4  | 트레이 color R |
| address (low) | 0xA5  | 트레이 color G |
| address (low) | 0xA6  | 트레이 color B |
| address (low) | 0xA7  | 트레이 blink time |

(최대 AF까지)

## 레드 라이트
| 이름      | 내용 |
| -------- | ---- |
| device id | 0x01  |
| function code | 0x06 |
| address |  0x41 |
| address | 0xB0  |
| data |  0xFF |
| data |  0xFF |
| crc  |  계산된 crc값 |
| crc  |  계산된 crc값 |

시간만 주기
low address : B0, 
| 이름      | 내용 | 설명 |
| --- | --- | --- | 
| address (low) | 0xB0  | 주기 시간 |

(* 최대 B7) 


## 배터리
| 이름      | 내용 |
| -------- | ---- |
| device id | 0x01  |
| function code | 0x03 |
| address |  0x42 |
| address | 0xBA  |
| data |  0xFF |
| data |  0xFF |
| crc  |  계산된 crc값 |
| crc  |  계산된 crc값 |

low address : BA, BB
| 이름      | 내용 | 설명 |
| --- | --- | --- | 
| address (low) | 0xBA  | 배터리 남은 용량(퍼센트) |
| address (low) | 0xBB  | 배터리 V |

최대 BF


## 범퍼
한영 hy200 에 추가된 기능

| 이름 | 내용 |
| --- | --- |
| device id | 0x01  |
| function code | 0x03 |
| address |  0x43 |
| address | 0xC0  |
| data |  0xFF |
| data |  0xFF |
| crc  |  계산된 crc값 |
| crc  |  계산된 crc값 |

low address : C0, C1  
| 이름      | 내용 | 설명 |
| --- | --- | --- | 
| address (low) | 0xC0  | front hit 여부 |
| address (low) | 0xC1  | rear hit 여부 |

최대 C7

> 데이터 true 는 0xFF, 0xFF 처리   
false 는 0x00, 0x00 으로 한다. 


## 트레이
| 이름      | 내용 |
| -------- | ---- |
| device id | 0x01  |
| function code | 0x03 |
| address |  0x44 |
| address | 0xC8  |
| data |  0x00 |
| data |  0xFF |
| crc  |  계산된 crc값 |
| crc  |  계산된 crc값 |

low address : C8, C9, CA
| 이름      | 내용 | 설명 |
| --- | --- | --- | 
| address (low) | 0xC8  | bottom tray 점유 여부 |
| address (low) | 0xC9  | middle tray 점유 여부 |
| address (low) | 0xCA  | top tray 점유 여부 |

최대 CF

> 데이터 true 는 0xFF, 0xFF 처리   
false 는 0x00, 0x00 으로 한다. 


## e스탑
| 이름      | 내용 |
| -------- | ---- |
| device id | 0x01  |
| function code | 0x03 |
| address |  0x45 |
| address | 0xD0  |
| data |  0x00 |
| data |  0xFF |
| crc  |  계산된 crc값 |
| crc  |  계산된 crc값 |

low address : D0,
| 이름      | 내용 | 설명 |
| --- | --- | --- | 
| address (low) | 0xD0  | e stop push 여부 |

최대 D3

> 데이터 true 는 0xFF, 0xFF 처리   
false 는 0x00, 0x00 으로 한다. 


## 휠 락커
| 이름      | 내용 |
| -------- | ---- |
| device id | 0x01  |
| function code | 0x03 |
| address |  0x46 |
| address | 0xD4  |
| data |  0x00 |
| data |  0xFF |
| crc  |  계산된 crc값 |
| crc  |  계산된 crc값 |

low address : D4,
| 이름      | 내용 | 설명 |
| --- | --- | --- | 
| address (low) | 0xD4  | 바퀴 락 여부 |

최대 D7

> 데이터 true 는 0xFF, 0xFF 처리   
false 는 0x00, 0x00 으로 한다. 


## 컨베이어 는 추후 정리;;;

이미 적용 되어 있으나, 추후 정리하기






